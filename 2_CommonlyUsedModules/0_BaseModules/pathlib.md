# 创建Path对象
```
from pathlib import Path
p = Path(_path)
print(p) 
```
```
/algor/yuanjie/Competitions/1_糖尿病/DataCache
```

# p的父路径
```
p.as_uri() # 'file:///algor/yuanjie/Competitions/1_%E7%B3%96%E5%B0%BF%E7%97%85/DataCache'
p.parent # p.parents[0]
list(p.parents)
```
```
PosixPath('/algor/yuanjie/Competitions/1_糖尿病')
Out[72]:
[PosixPath('/algor/yuanjie/Competitions/1_糖尿病'),
 PosixPath('/algor/yuanjie/Competitions'),
 PosixPath('/algor/yuanjie'),
 PosixPath('/algor'),
 PosixPath('/')]
```

# p目录下的所有文件
```
list(p.iterdir()) # list(p.glob('*'))
```
```
[PosixPath('/algor/yuanjie/Competitions/1_糖尿病/DataCache/.ipynb_checkpoints'),
 PosixPath('/algor/yuanjie/Competitions/1_糖尿病/DataCache/f_sample_20180204.csv'),
 PosixPath('/algor/yuanjie/Competitions/1_糖尿病/DataCache/f_test_a_20180204.csv'),
 PosixPath('/algor/yuanjie/Competitions/1_糖尿病/DataCache/f_train_20180204.csv')]
```

# 判断
```
p.is_dir() # 判断p是不是目录
p.is_file() # 判断p是不是文件
p.is_absolute() # 判断p是不是绝对路径

p.match('/algor/yuanjie/Competitions/1_糖尿病/*') # 判断p是否符合某一模式
list(p.glob('*.csv')) # 在p下搜索符合某一模式文件
list(p.rglob('*.csv'))

# 利用relative_to获取当前目录\文件名 
p.relative_to(p.parent)

# 当p不是目录时，将其创建为目录
p.mkdir()
# 当p是空目录时，移除p
p.rmdir()
```
