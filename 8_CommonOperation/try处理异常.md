```python
try:
    print("正常的操作")
except <名字>:
    print("发生异常，执行这块代码")
    print("如果在try部份引发了'name'异常")
except <名字>，<数据>:
    print("如果引发了'name'异常，获得附加的数据")
else:
    print("如果没有异常执行这块代码")
finally:
    print("最后总会执行")
```
