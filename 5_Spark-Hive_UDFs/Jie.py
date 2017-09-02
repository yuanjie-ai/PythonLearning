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

spark = SparkSession.builder \
                    .appName("Yuanjie_Test") \
                    .config('log4j.rootCategory',"WARN") \
                    .enableHiveSupport() \
                    .getOrCreate()
spark.conf.set("spark.executor.memory", '16g')
spark.conf.set('spark.executor.cores', '50')
spark.conf.set('spark.cores.max', '5')

sc = spark.sparkContext

# List(spark array)
class SparkArray(object):
    def __init__(self):
        pass

    @staticmethod
    def listUnique(x):
        listUnique = lambda x: sorted(list(set(x)), key=x.index)
        return listUnique(x)

    @staticmethod
    def listSub(a, b):
        listSub = lambda a, b: [a[i] for i in np.where([i not in b for i in a])[0]]
        return listSub(a, b)

    @staticmethod
    def listExplode(df, colname='name'):
        n = len(df.select(colname).first()[0])
        names = df.columns + [col(colname)[i].name(colname + str(i)) for i in range(n)]
        return df.select(names)

    @staticmethod
    def litArray(ls=[]):
        return (array([lit(i) for i in ls]))

# colToList
class SparkCol(object):
    def __init__(self):
        pass

    @staticmethod
    def takeN(df, n=5):
        return np.array(df.take(n)).flatten().tolist()

    @classmethod
    def colToList(cls, df):
        return cls.takeN(df.select(collect_list(df.columns[0])), 1)


# DataFrame
class SparkDF(object):
    def __init__(self):
        pass   
    
    @staticmethod
    def createEmptyDF(floatcol=[], stringcol=[]):
        ls = zip(Floatcol, [FloatType()] * len(floatcol)) + zip(Stringcol, [StringType()] * len(stringcol))
        schema = StructType([StructField(*i) for i in ls])
        df = spark.createDataFrame([], schema=schema)
        return df
    

    
    
    
    
    
    
    
    
    
    
if __name__ == '__main__':
    print('It is main!!!')
else:
    print('Sucessful Import Jie!!!')
