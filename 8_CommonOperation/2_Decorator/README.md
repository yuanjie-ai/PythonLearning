<h1 align = "center">:rocket: 装饰器 :facepunch:</h1>

---
```python
@property
@staticmethod
@classmethod
```

---
## 自定义装饰器
- 不带参数
```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)
        return func(*args, **kw)

    return wrapper 
```

- 带参数
```python
import functools

def decorator(text):
    def _wrapper(func):
        @functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))  # 主体
            return func(*args, **kw)

        return wrapper

    return _wrapper
```
