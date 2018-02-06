# :rocket: 临时笔记 :facepunch:
---
- 对象转字符串
```
a = 1000
repr(a)

'1000'
```
- Jaccard相关系数
```
jaccard = lambda a, b: len(set(a).intersection(b))/(len(set(a).union(b))+0.)
```
- class
```
class p:
    e = None
    def __init__(self, a):
        p.e = self
        self.a = a
    def f(self):
        print(self.a)
        
<__main__.p instance at 0x7f052c3390e0>
不知道什么场景        
```

- 目录树
```
from pathlib import Path
import sys

def lst_tree(p, n):
    if p.is_file():    #判断是否是文件
        print('|' + '\t|' * n + '-' * 4 +  p.name)
    elif p.is_dir():    # 判断是否是目录
        print('|' + '\t|' * n + '-' * 4 +  str(p.relative_to(p.parent)) + '\\')
        for pt in p.iterdir():
            lst_tree(pt, n + 1)   # 递归

if __name__ == "__main__":
        # 对命令行参数进行判断
    if len(sys.argv) != 1 and Path(sys.argv[1]).exists():
        lst_tree(Path(sys.argv[1]), 0)
    else:
        lst_tree(Path('.'), 0)
```
