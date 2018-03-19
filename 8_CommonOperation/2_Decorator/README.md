<h1 align = "center">:rocket: 装饰器 :facepunch:</h1>

---
```python
@property
@staticmethod
@classmethod
```
- `wrapt`
- `from decorator import decorate`
```
import wrapt

# without argument in decorator
@wrapt.decorator
def logging(func, instance, args, kwargs):  # instance is must
    print ("[DEBUG]: enter {}()".format(func.__name__))
    return func(*args, **kwargs)

from decorator import decorator
@decorator
def _logging(func, *args, **kwargs):
    print ("[DEBUG]: enter {}()".format(func.__name__))
    return func(*args, **kwargs)

@logging
def say(): 
    pass

@_logging
def _say():
    pass
```
---
## 自定义装饰器
### 1. 普通装饰器

- 无参数
```python
import functools

def decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        print('call %s():' % func.__name__)  # 主体
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

### 2. 类装饰器

- 无参数
```python
class tracer:
    def __init__(self, func):
        self.calls = 0
        self.func = func

    def __call__(self, *args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)

@tracer
def spam(a, b, c):
    print(a + b + c)

spam(1, 2, 3)
```

- 带参数
```python
class tracer:
    def __init__(self, *args):
        self.calls = 0

        self.args = args

    def __call__(self, func):
        self.func = func

        def realfunc(*args):
            self.calls += 1

            print('call %s to %s' % (self.calls, self.func.__name__))

            self.func(*args)

        return realfunc


@tracer("xxxx")
def spam(a, b, c):
    print(a + b + c)


spam(1, 2, 3)

```

```python
def decorator(text=11):
    def _wrapper(func):

        def wrapper(x=text, *args, **kw):
            print('text = %s' % text)  # 主体
            return func(x, *args, **kw)

        return wrapper

    return _wrapper

@decorator(99999999999999)
def f(x=1, y=2):
    print(x+y)
```

