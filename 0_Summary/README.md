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

|member_id|linajia_community_org|lianjia_address|col4_disc|level|
|:--:|:--:|:--:|:--:|:--:|
|     6001|                 明湖雅居|       莫愁湖东路12号|address_demp|           1|
|     6002|                 新旺花苑|        江宁区秣陵街道|address_demp|           0|
|     6003|                 华庭北园|           华庭北园|address_demp|           2|
|     6004|                  童卫路|            童卫路|address_demp|           2|
|     6005|                  新安里|            新安里|address_demp|           3|
|     6006|                 和睦北园|          天目山路9号|address_demp|           2|
