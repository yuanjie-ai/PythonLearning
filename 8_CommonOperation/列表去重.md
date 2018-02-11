```python
l = [3, 1,2,2,1]
# 无序
set(l)
# 有序
list(OrderedDict.fromkeys(l))

order_set = lambda x: list(OrderedDict.fromkeys(x))
```
