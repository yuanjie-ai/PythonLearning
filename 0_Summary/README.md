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
