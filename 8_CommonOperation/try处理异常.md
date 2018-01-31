- try
```python
try:
    print("正常的操作")
except <名字>:
    print("发生异常，执行这块代码")
    print("如果在try部份引发了'name'异常")
except <名字>, <数据>:
    print("如果引发了'name'异常，获得附加的数据")
else:
    print("如果没有异常执行这块代码")
finally:
    print("最后总会执行")
```

```
try:
    """
    需要判断是否会抛出异常的代码，如果没有异常处理，python会直接停止执行程序
    """
except:
    """
    这里会捕捉到上面代码中的异常，并根据异常抛出异常处理信息
    """
# except ExceptionName, args:
#     """
#     同时也可以接受异常名称和参数，针对不同形式的异常做处理
#     """
#     
else:
    """
    如果没有异常则执行else
    """
finally:
    """
    退出try语句块总会执行的程序
    """

# 函数中做异常检测
def try_exception(num):
  try:
    return int(num)
  except ValueError,arg:
    print(arg,"is not a number")
  else:
    print("this is a number inputs")


try_exception('xxx')
#输出异常值
Invalide literal for int() with base 10: 'xxx' is not a number
```
