<h1 align = "center">:rocket: 装饰器 :facepunch:</h1>

---
```python
@property
@staticmethod
@classmethod
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

