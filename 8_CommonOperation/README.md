# :rocket: 常用操作 :facepunch:
---
- 取整数个位置数值
```python
f = lambda x: np.floor(x / np.array([10**i for i in range(len(str(x)))])) % 10
f(123456789)

array([ 9.,  8.,  7.,  6.,  5.,  4.,  3.,  2.,  1.])
```
