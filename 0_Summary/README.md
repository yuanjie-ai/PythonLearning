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
- h5
```
# complevel: 压缩级别（1-9，0是无压缩，默认值）, blosc提供非常快的压缩
df.to_hdf(path, 'w', complib='blosc', complevel=5)
```
