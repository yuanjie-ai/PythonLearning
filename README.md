# :rocket: Learning :facepunch:

---
## 工具类
- [Linux][0]
    - [RPM][5]
- [Cygwin][8]
- [IntelPython][1]
- [Anaconda][2]
- [WinWheel][3]
- [Jetbrians注册码][6]
- [Everything][9]
- [Matools][13]
- [Convert Excel sheet to MarkDown Table][15]
- Notepad++
    - Notepad++ ->"运行"菜单->"运行"按钮
    ```
    cmd /k python "$(FULL_CURRENT_PATH)" & ECHO. & PAUSE & EXIT
    ```
---

# 资源类
- [最新emoji][16]
- [emoji速查][17]
- [最流行数据集][12]
- [美团技术博客][4]

---
## Git
- [git push][7]
- [git branch][14]
```
# 检验线上线下一致性
git add/rm ...
git checkout
```
- Git常用命令速查
![Git常用命令速查][11]

---
## Pip
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

## [Jupyter][10]: A simple way to share Jupyter Notebooks
- IpynbShow: nbviewer.jupyter.org/github/Jie-Yuan+项目
- 多输出交互
```
echo 'c = get_config()
# Run all nodes interactively
c.InteractiveShell.ast_node_interactivity = "all"' >> .ipython/profile_default/ipython_config.py
```
---
## 算法框架
```
xgboost
lightgbm
keras
tensorflow
```
---

## 预处理
```
sklearn_pandas
```

## Json
```
json-transporter
```
---

## 评估指标
```
ml_metrics
```
---

## 数据库
---
### Sql
- ORM
```
sqlalchemy
```
- MySql
```
pymysql
```
---
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
---
### NoSql
---
- HBase
```
happybase
```



---
[0]: https://jaywcjlove.github.io/linux-command/
[1]: https://registrationcenter.intel.com/en/products/postregistration/?sn=CTGC-JS77PNXP&EmailID=313303303%40qq.com&Sequence=2053363&dnld=t
[2]: https://mirrors.tuna.tsinghua.edu.cn/anaconda/archive/
[3]: http://www.lfd.uci.edu/~gohlke/pythonlibs/
[4]: https://tech.meituan.com/
[5]: http://rpmfind.net/linux/rpm2html/search.php
[6]: http://xidea.online
[7]: http://www.cnblogs.com/qianqiannian/p/6008140.html
[8]: http://www.cygwin.com/
[9]: http://www.voidtools.com/
[10]: http://nbviewer.jupyter.org/
[11]: http://chuantu.biz/t5/162/1502091545x1884350018.jpg
[12]: http://archive.ics.uci.edu/ml/index.php
[13]: http://www.matools.com/
[14]: http://blog.csdn.net/arkblue/article/details/9568249/
[15]: https://github.com/fanfeilong/exceltk
[16]: https://emojipedia.org/
[17]: https://www.webpagefx.com/tools/emoji-cheat-sheet/
