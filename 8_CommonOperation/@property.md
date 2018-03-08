<h1 align = "center">:rocket: @property :facepunch:</h1>

---
> Python内置的@property装饰器就是负责把一个方法变成属性调用的，但是有时候setter/deleter也是需要的。

- @property: 可读
- @xx.setter: 可写
- @xx.deleter: 可删除

```python
class Student(object):
    def __init__(self):
        self._age = None

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        if isinstance(age, int):
            self._age = age
            return
        if isinstance(age, str) and age.isdigit():
            age = int(age)
            self._age = age
        else:
            raise ValueError("age is illegal")

    @age.deleter
    def age(self):
        del self._age


student = Student()
student.age = 20
print student.age

del student.age
```
