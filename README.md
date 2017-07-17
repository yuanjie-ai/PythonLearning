# SpecialModule
:kissing_closed_eyes:
---
# pip
- Online: 镜像源加速
```
pip install --upgrade tensorflow -i https://pypi.tuna.tsinghua.edu.cn/simple
```

- 默认配置
    - linux: linux的文件在~/.pip/pip.conf
    - windows: windows在%HOMEPATH%\pip\pip.ini（新建）
```
[global]
trusted-host =  pypi.tuna.tsinghua.edu.cn
index-url = https://pypi.tuna.tsinghua.edu.cn/simple
```

- Offline
```
which pip
sudo /home/bigdata/software/anaconda/bin/pip install sklearn_pandas-1.4.0-py2.py3-none-any.whl
```
---

# jupyter
- 多输出交互
```
echo 'c = get_config()
# Run all nodes interactively
c.InteractiveShell.ast_node_interactivity = "all"' >> .ipython/profile_default/ipython_config.py
```

# 算法框架
```
xgboost
lightgbm
keras
tensorflow
```
---

# 预处理
```
sklearn_pandas
```
---

# 评估指标
```
ml_metrics
```
---

# 数据库
- ORM
```
sqlalchemy
```

- Hive
> sqlalchemy中hive的url形式: hive://localhost:port/database?auth=XX
```
pyhive
thrift
future
sasl
thrift_sasl
thriftpy
ply
sqlalchemy
```

- MySql
```
pymysql
```

