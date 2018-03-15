<h1 align = "center">:rocket: Python编码规范 :facepunch:</h1>

---
## 1. 主动遵循
![主要][1]
Refer:
- http://blog.csdn.net/qq_27657429/article/details/65449283
- http://blog.csdn.net/s1070/article/details/73529570
- http://www.imooc.com/article/19184?block_id=tuijian_wz#child_5_1
- http://www.runoob.com/w3cnote/google-python-styleguide.html

## 2. 被动接受（工具）
- IntelliJ IDEA 和 PyCharm 的格式化代码功能: `ctrl + l`
- Google 开源的 Python 文件格式化工具: `pip install yapf`
```python
from yapf.yapflib.yapf_api import FormatCode  # reformat a string of code
code = "def g():\n  return True"
print(FormatCode(code, style_config='pep8')[0])

def g():
    return True
```








---
[1]: https://dn-mhke0kuv.qbox.me/a542abfa2efe1fefd95e.png
