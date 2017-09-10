# -*- coding: utf-8 -*-

import re
import time
import itertools
import numpy as np
import pandas as pd
from scipy import stats

import pyspark.sql.functions as F

from pyspark.sql import *
from pyspark.sql.types import *
from pyspark.sql.functions import *
from pyspark.ml.feature import *
from pyspark.ml.classification import *
from pyspark.ml.evaluation import *
from pyspark.ml.tuning import *
# from pyspark.ml.recommendation import *
from pyspark.mllib.recommendation import *
from pyspark.ml.linalg import Vectors,VectorUDT
# f = udf(lambda x:Vectors.dense([i[1] for i in x]),VectorUDT())
# f = udf(lambda x:[i[1] for i in x],ArrayType(StringType()))
#http://stackoverflow.com/questions/42216891/pyspark-use-one-column-to-index-another-udf-of-two-columns

spark = SparkSession.builder \
    .appName("Yuanjie_Test") \
    .config('log4j.rootCategory',"WARN") \
    .enableHiveSupport() \
    .getOrCreate()
spark.conf.set("spark.executor.memory", '16g')
spark.conf.set('spark.executor.cores', '50')
spark.conf.set('spark.cores.max', '5')


sc = spark.sparkContext



spark.table('')

# time datetime
t_0 = time.strftime("%Y-%m-%d",time.localtime(time.time()))


#
arrayToVector = udf(lambda x: Vectors.dense(x), VectorUDT())
vectorToArray = udf(lambda x: [float(i) for i in x], ArrayType(FloatType()))


# dfToList
def dfToList(df, axis=0, head_n=1):
    '''
    a列转换：dfToList(df.select('a'),axis=1)
    '''
    if axis:
        ls = np.array(df.agg(collect_list(*df.columns)).head())[0]
    else:
        ls = np.array(df.select(array(df.columns)).head(head_n))[0][0]        
    return ls

# 子查询
# df1.id不在df2.id 子查询：【在与不在】[df1.select('id').subtract(df2.select('id')).]join(df1,'id')
# "select * from test1 where id in (select id from test2)"


# F.litList：df.select(array([lit(i) for i in range(5)]).name('a')).show()
def litArray(ls=[]):
    return(array([lit(i) for i in ls]))#=

# topList
def topList(df, topN=1, subset=[]):
    if subset:
        df = df.select(subset)
    return map(lambda x:x[0], np.array(df.head(topN)).tolist())

# ALS推荐列表
def resALS(df,params,topk=5,implicit=True):
    '''
    params = dict(rank=10,
              iterations=20,
              lambda_=0.01,
              alpha=0.01,
              blocks=-1,
              nonnegative=False,
              seed=0)
    '''
    colname = ['user','product','rating']
    df = df.toDF(*colname)
    '''
    encoding
    '''
    df = stringIndexed(df,stringcol=['user','product'])
    indexed_user = df.select('user','indexed_user').distinct()
    indexed_item = df.select('product','indexed_product').distinct()
    traindata = df.select('indexed_user','indexed_product','rating')
    traindata.cache()

    if implicit:
        model = ALS.trainImplicit(traindata,**params)
    else:
        params.pop('alpha')
        model = ALS.train(traindata,**params)

    toList = udf(lambda x:[i[1] for i in x],ArrayType(StringType()))
    rec = model.recommendProductsForUsers(topk).toDF(['indexed_user','indexed_product'])
    rec = rec.withColumn('indexed_product',explode(toList('indexed_product'))) \
             .withColumn('indexed_product',col('indexed_product').astype(LongType()))
    res = rec.join(broadcast(indexed_user),'indexed_user') \
             .join(broadcast(indexed_item),'indexed_product') \
             .select('user','product') \
             .groupby('user') \
             .agg(collect_list('product').name('product'))
    return(res)

# 字符串列数值化
def stringIndexed(df,stringcol=[] ):
    for i in stringcol:
        df = StringIndexer(inputCol=i,outputCol='indexed_'+i).fit(df).transform(df).withColumn('indexed_'+i,col('indexed_'+i).astype(LongType()))
    return(df)

# a-b保持顺序不变
diffList = lambda a,b: [a[i] for i in np.where([i not in b for i in a])[0]]

# 列表去重顺序不变
def uniqueList(x):
    l = list(set(x))
    l.sort(key=x.index)
    return l

# 列裂
def creatCols(df,colname='name',strType=True):
    n = len(df.select(colname).first()[0])
    '''
    VectorUDT()
    Array()
    '''
    if strType:
        for i in range(n):
            f = udf(lambda x:x[i])
            df = df.withColumn(colname+str(i),f(colname))
    else:
        for i in range(n):
            f = udf(lambda x:float(x[i]),FloatType())
            df = df.withColumn(colname+str(i),f(colname))        
    return(df)

# emptyDF：初始化数据类型
def emptyDF(Stringcol=[],Floatcol=[]):
    ls = zip(Floatcol, [FloatType()]*len(Floatcol)) + zip(Stringcol, [StringType()]*len(Stringcol))
    schema = StructType([StructField(*i) for i in ls])
    df = spark.createDataFrame([], schema)
    return df

# freqItem
def freqItem(df,user_id=[],product_catalog=[]):
    '''
    推荐规则：商品目录主次顺序取众数
    '''
    p = product_catalog
    for i in range(len(p)):
        df = df.join(df.groupBy(user_id+p[:i]).agg(modeString(collect_list(p[i])).name(p[i])),user_id+p[:(i+1)])
    df = df.select(user_id+product_catalog)
    return(df.distinct())

# head
def head(df,n=5):
    sql = 'select * from df limit ' + str(n)
    df.registerTempTable('tab')
    df = spark.sql(sql)
    spark.catalog.dropTempView('tab')
    return(df)

#时间序列：pd.date_range(start='2016-06-01',end='2017-01-01',freq='D').map(lambda x:str(x)[:10])
# slidingWindow：尽量转换成时间戳
# 观察变量时间窗口宽度：observation_window = [start_time,start_time + 86400*m]
# 响应变量时间窗口宽度：response_window = [observation_window[1],observation_window[1] + 86400*n]
def slidingWindow(df,_id='id',time_col='time',label='label',observation_window=[],response_window=[]):
    observation = df.filter(col(time_col) >= observation_window[0]).filter(col(time_col) < observation_window[1]).drop(label)
    response = df.filter(col(time_col) >= response_window[0]).filter(col(time_col) < response_window[1]).select(_id,label)
    df = observation.join(response,_id).distinct()
    return(df)

# n_na
def n_na(df,isNull = True,axis = 0):
    '''
    axis:0按行统计,每列缺失值数
    只有axis=0才有null与nan
    '''
    if axis == 0:
        SUM = udf(lambda x:float(np.sum(x)),FloatType())
        if isNull:
            df = df.agg(*[SUM(collect_list(isnull(i))).name(i) for i in df.columns])
            return df
        else:
            df = df.agg(*[SUM(collect_list(isnan(i))).name(i) for i in df.columns])
            return df
    else:
        SUM = udf(lambda x:float(np.sum([i is None for i in x])),FloatType())
        if isNull:
            df = df.withColumn('n_null',SUM(array(df.columns)))
            return df
        else:
            df = df.withColumn('n_nan',SUM(array(df.columns)))
            return df
        
# mode
modeNumber = udf(lambda x:float(stats.mode(x)[0]),FloatType())
modeString = udf(lambda x:str(stats.mode(x)[0][0]),StringType())

# median
median = udf(lambda x:float(np.median(x)),FloatType())

# 组内众数（sql方式）
def spark_mode(df,colnames):
    gr_count = pp.groupBy(colnames).count()
    mode = gr_count.join(gr_count.groupBy(colnames[0]).agg(F.max(F.col('count')).alias('count')),on=[colnames[0],'count'])#.drop('count')
    mode.show(5)
    return mode

# Shape
def dim(df):
    shape = (df.count(),len(df.columns))
    print shape
    return(shape)

# 加索引
def addIndex(df,gr = lit(0)):
    w = F.row_number().over(Window.partitionBy(gr).orderBy(F.lit(0)))
    return(df.withColumn('_index', w))

# Cbind
def cbind(df1,df2,how='inner',_index=False):
    """
    One of `inner`, `outer`, `left_outer`, `right_outer`, `leftsemi`
    """
    if _index:
        df = addIndex(df1).join(addIndex(df2),on='_index',how=how)
    else:
        df = addIndex(df1).join(addIndex(df2),on='_index',how=how).drop('_index')
    return(df)

# metric
def confusionMatrix(pred):
    return(pred.crosstab('label','prediction').sort(F.col('label_prediction')))
    
# 特征名
def featureDate(df):
    feature_date = list((set(df.columns) & set(spark.table('fbidm.yuanjie_feature_date').select(F.collect_list('col_name')).first()[0])))
    return feature_date
def featureString(df):
    feature_string = list(set(df.columns) & set(spark.table('fbidm.yuanjie_feature_string').select(F.collect_list('col_name')).first()[0]))
    return feature_string
def featureNames(df,feature_string=[],feature_number=[],other=['acct_no','label']):
    if feature_string:
        feature_number = list(set(df.columns)- set(feature_string+other))
        return([feature_string,feature_number])
    if feature_number:
        feature_string = list(set(df.columns)- set(feature_number+other))
        return([feature_string,feature_number])

# 缺失值
def imputer(df,feature_string=[],feature_number=[]):
    for i in [i[0] for i in df.select(feature_string).dtypes if i[1] !='string']:
        df = df.withColumn(i,df[i].astype(LongType()))
    for i in feature_string:
        df = df.withColumn(i,df[i].astype(StringType()))  
    for i in feature_number:
        df = df.withColumn(i,df[i].astype(FloatType()))
    df = df.fillna(dict(zip(feature_string,['88888888']*len(feature_string)) + zip(feature_number,[0]*len(feature_number))))
    return(df)

# OneHot
## label为数值型，id为字符型
def preprocessing(df,_id='acct_no',feature_string=[],feature_number=[],model_Data='fbidm.df',isTrainData=True):
    indexed_Data = model_Data+'_indexed_Data'
    scaled_Data = model_Data+'_scaled_Data'
    df = df.withColumnRenamed(_id,'_id').withColumn('_id',col('_id').astype(StringType()))
    if 'label' in df.columns:
        df = df.withColumn('label',col('label').astype(IntegerType()))
    for i in [i[0] for i in df.select(feature_string).dtypes if i[1] !='string']:
        df = df.withColumn(i,df[i].astype(LongType()))    
    for i in feature_number:
        df = df.withColumn(i,col(i).astype(FloatType()))
    for i in feature_string:
        df = df.withColumn(i,col(i).astype(StringType()))
    print "Sucessful Data Astype:===================>10%"
    
    df = df.fillna(dict(zip(feature_string,['88888888']*len(feature_string)) + zip(feature_number,[0]*len(feature_number))))
    print "Sucessful Data Imputer:==================>20%"
    
    if feature_string:
        if isTrainData:
            DataFrameWriter(df.select(feature_string)).saveAsTable(indexed_Data,mode='overwrite')
            indexed_Data = spark.table(indexed_Data)
        else:
            indexed_Data = spark.table(indexed_Data)
            """
            在新数据集df上每类加上类别值，避免新数据各类别值变少
            """
#           nrow = np.max([len(indexed_Data.select(i).rdd.countByKey()) for i in feature_string])
            nrow = np.max(df.select([countDistinct(i) for i in feature_string]).head())
            df0 = spark.range(1,nrow)
            for i in feature_string:
                df0 = cbind(df0,indexed_Data.select(i).distinct(),how='outer')
            df0 = df0.drop('id')
            df0 = df0.fillna(dict(zip(feature_string,list(df0.first()))))
            for i in df.drop(*(feature_string)).columns:
                df0 = df0.withColumn(i,lit(0))
            df0 = df0.withColumn('_id',lit('new_id')).select(df.columns)
            df = df.union(df0)
            print "Sucessful Data kinds:====================>30%"

    print "Sucessful Data Indexed:==================>40%"

    for i in feature_string:
        inputCol=i
        outputCol='indexed_'+i
        indexer = StringIndexer(inputCol=inputCol,outputCol=outputCol,handleInvalid='skip').fit(indexed_Data)###model
        df = indexer.transform(df).withColumn(i,col(outputCol)).drop(outputCol)
    print "Sucessful Data Indexing:=================>50%" 

    for i in feature_string:
        inputCol=i
        outputCol='encoded_'+i
        encoder =  OneHotEncoder(dropLast=False,inputCol=inputCol,outputCol=outputCol)
        df = encoder.transform(df).withColumn(i,col(outputCol)).drop(outputCol)
    print "Sucessful Data OneHot:===================>60%"

    vecAssembler = VectorAssembler(inputCols=feature_string+feature_number,outputCol='features')
    df = vecAssembler.transform(df)
    print "Sucessful Data VectorAssembler:==========>70%"

    if 'label' in df.columns:
        df = df.select('_id','label','features')
    else:
        df = df.select('_id','features')
    if isTrainData:
        DataFrameWriter(df).saveAsTable(scaled_Data,mode='overwrite')
        scaled_Data = spark.table(scaled_Data)
    else:
        df = df.filter(col('_id') != 'new_id')
        scaled_Data = spark.table(scaled_Data)
    print "Sucessful Data Scaled:===================>80%"

    standardScaler = StandardScaler(withMean=True, withStd=True,inputCol='features', outputCol='scaled').fit(scaled_Data)###model
    df = standardScaler.transform(df).withColumn('features',col('scaled')).drop('scaled')
    print "Sucessful Data Scaling:==================>99%"
    return(df)

#-------------------------------------------------------------------
important_feature = \
[['acct_no',
  'member_id',
  'sex',
  'actv_lvl',
  'adsl_chrg_lvl',
  'age_type',
  'asset_st',
  'bank_tran_lvl',
  'buy_cpy',
  'chn_love',
  'chp_tml_love',
  'commute_vst_lvl',
  'crdt_crd_tran_lvl',
  'debt_st',
  'ele_chrg_lvl',
  'epp_bag_actv_lvl',
  'epp_byscan_actv_lvl',
  'epp_lifecycle',
  'epp_pg_staytm_lvl',
  'epp_scan_actv_lvl',
  'epp_tran_lvl',
  'epp_vst_bounce_lvl',
  'epp_vst_cnt_lvl',
  'epp_vst_pg_lvl',
  'epp_vst_staytm_lvl',
  'fin_lifecycle',
  'gas_chrg_lvl',
  'gas_crd_lvl',
  'income',
  'inv_risk_love',
  'inv_term_love',
  'is_bill_fin_user',
  'is_chp_lotto_user',
  'is_chp_pay_user',
  'lifecycle',
  'loyal_lvl',
  'mbl_bill_lvl',
  'mbl_fill_lvl',
  'mgt_region',
  'night_vst_lvl',
  'rest_tm_vst_lvl',
  'sch_crd_lvl',
  'tel_chrg_lvl',
  'tv_chrg_lvl',
  'value_lvl',
  'water_chrg_lvl',
  'weekend_vst_lvl',
  'work_dt_vst_lvl',
  'work_tm_vst_lvl'],
 ['acct_no',
  'acct_type',
  'age',
  'auth_type',
  'blood_type',
  'channel_online',
  'chnel_cnt',
  'chnel_lvl',
  'college_user_type',
  'constellation',
  'education',
  'info_full_stat',
  'is_common_cust',
  'is_drumbt',
  'is_email_verify',
  'is_enterprise',
  'is_fzn',
  'is_govt',
  'is_inr_emp',
  'is_inr_emp_his',
  'is_laox',
  'is_mall',
  'is_media',
  'is_offline',
  'is_online',
  'is_partner',
  'is_phone_verify',
  'is_pptv_trans',
  'is_redbaby_store',
  'is_redbaby_trans',
  'is_sch_cust',
  'is_schl_surrgt',
  'is_scs_supplier',
  'is_scs_supplier_sub',
  'is_supplier_admin',
  'is_supplier_sub',
  'is_union_cust',
  'is_vip',
  'is_vipsnow',
  'mgt_area',
  'mgt_prov_cd',
  'mrge_st',
  'mthly_income',
  'pupsec_status',
  'rgst_tml',
  'trade_type'],
 ['acct_no',
  'first_epp_pay_dt',
  'first_fast_pay_dt',
  'first_order_dt',
  'first_order_online_dt',
  'last_epp_pay_dt',
  'last_fast_pay_dt',
  'last_order_dt',
  'last_order_online_dt',
  'mob_first_login_online',
  'mob_last_login_online',
  'online_dt'],
 ['acct_no', 'is_7d_bil_fail', 'is_7d_bof_fail', 'is_7d_fnd_fail'],
 ['acct_no',
  'buy_amt_12m',
  'buy_amt_avg_12m',
  'buy_amt_avg_online_12m',
  'buy_amt_max_12m',
  'buy_amt_online_12m',
  'buy_cnt_12m',
  'buy_cnt_offline_12m',
  'buy_cnt_online_12m',
  'buy_gds_cnt_12m',
  'buy_gds_cnt_online',
  'ord_addr_cnt_12m',
  'ord_city_cnt_12m',
  'pay_amt_12m',
  'pay_amt_gds_12m',
  'pay_amt_his',
  'pay_amt_online',
  'pay_cnt_12m',
  'pay_cnt_crdt_12m',
  'pay_cnt_gds_12m',
  'pay_cnt_his',
  'pay_cnt_online',
  'rjct_cnt_12m',
  'rjct_cnt_online',
  'sale_amt_online'],
 ['acct_no',
  'vst_avg_tm_12m',
  'vst_avg_tm_3m',
  'vst_avg_tm_6m',
  'vst_cnt_12m',
  'vst_cnt_1m',
  'vst_cnt_3m',
  'vst_cnt_6m',
  'vst_fnc_cnt_0_5_3m',
  'vst_fnc_cnt_11_12_3m',
  'vst_fnc_cnt_12m',
  'vst_fnc_cnt_13_14_3m',
  'vst_fnc_cnt_15_18_3m',
  'vst_fnc_cnt_19_20_3m',
  'vst_fnc_cnt_1m',
  'vst_fnc_cnt_21_23_3m',
  'vst_fnc_cnt_3m',
  'vst_fnc_cnt_6_8_3m',
  'vst_fnc_cnt_6m',
  'vst_fnc_cnt_9_10_3m',
  'vst_fnc_cnt_otw_3m',
  'vst_fnc_cnt_wkdy_3m',
  'vst_tm_12m',
  'vst_tm_1m',
  'vst_tm_3m',
  'vst_tm_6m',
  'vstr_pv_12m',
  'vstr_pv_1m',
  'vstr_pv_3m',
  'vstr_pv_6m'],
 ['acct_no',
  'actv_rfr_off',
  'actv_rfr_on',
  'actv_type',
  'app_hold',
  'auth_days',
  'coupon',
  'eg_mem_lvl',
  'eqmt_num',
  'is_1yuan_user',
  'is_3c_buyer',
  'is_4g',
  'is_adsl_chrg',
  'is_apple_fan',
  'is_bank_tran',
  'is_bil_vip',
  'is_bill_cash_user',
  'is_bill_prch',
  'is_bind_card',
  'is_bof_user',
  'is_bof_zero_hold',
  'is_by_scan',
  'is_cash_on_deli',
  'is_ccr_user',
  'is_cfc_user',
  'is_chp_focus_user',
  'is_chp_user',
  'is_crdt_crd_tran',
  'is_cur_bind_card',
  'is_djd_buyer',
  'is_ele_chrg',
  'is_epp_bag_user',
  'is_epp_tran',
  'is_fin_user',
  'is_fnd_prch',
  'is_fnd_user',
  'is_fnd_vip',
  'is_gas_chrg',
  'is_gas_crd_user',
  'is_huwei_fan',
  'is_ins_user',
  'is_lenovo_fan',
  'is_mbl_bill_user',
  'is_mbl_fill',
  'is_mi_fan',
  'is_myhz_buyer',
  'is_nokia_fan',
  'is_oppo_fan',
  'is_other_buyer',
  'is_quick_pay',
  'is_samsung_fan',
  'is_scan',
  'is_sch_crd_user',
  'is_sony_fan',
  'is_tel_chrg',
  'is_tv_chrg',
  'is_use_coupon',
  'is_water_chrg',
  'is_xjd_buyer',
  'is_zte_fan',
  'loyalty_level',
  'rgst_days',
  'score',
  'sply_days']]
#-------------------------------------------------------------------














if __name__ == '__main__':
    print('I IS MAIN!!!!!')
else:
    print('Sucessful Import Me!!!!!')
