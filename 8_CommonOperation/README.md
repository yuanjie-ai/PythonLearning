<h1 align = "center">:rocket: 常用操作 :facepunch:</h1>

---
- 取整数各位置数
```python
f = lambda x: np.floor(x / np.array([10**i for i in range(len(str(x)))])) % 10
f(123456789)

array([ 9.,  8.,  7.,  6.,  5.,  4.,  3.,  2.,  1.])
```
- exec 被当成一个函数 ，可以通过以下的方法来进行将字符串变成变量的名字进行赋值
```python
x='myVar'
exec("%s = %s" % (x, [1,2,3]))
print(myVar)

[1, 2, 3]
```
- 生成器保存的是算法(yield)
```
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]
        
for char in reverse('golf'):
    print(char)
```

- print(value, ..., sep=' ', end='\n', file=sys.stdout)
    - file默认打印到终端
    ```python
    print(value, ..., sep=' ', end='\n', file=sys.stdout)
    ```
    - file打印到指定文件
