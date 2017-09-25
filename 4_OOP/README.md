> 类的方法与普通的函数只有一个特别的区别——它们必须有一个额外的第一个参数名称, 按照惯例它的名称是 self。

> 在类地内部，使用def关键字可以为类定义一个方法，与一般函数定义不同，类方法必须包含参数self,且为第一个参数:

## 类定义
```
class people:
    #定义基本属性
    name = ''
    age = 0
    #定义私有属性,私有属性在类外部无法直接进行访问
    __weight = 0
    #类参数
    def __init__(self,n,a,w):
        self.name = n
        self.age = a
        self.__weight = w
    #定义构造方法
    def speak(self):
        print("%s 说: 我 %d 岁。" %(self.name,self.age))
```

## 实例化类
```
p = people('runoob',10,30)
p.speak()
```

## 单继承示例
```
class student(people):
    grade = ''
    def __init__(self,n,a,w,g):
        #调用父类的构函
        people.__init__(self,n,a,w)
        self.grade = g
    #覆写父类的方法
    def speak(self):
        print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
```

## 多重继承(继承多个类)
- 未绑定方法
```
class speaker():
    topic = ''
    name = ''
    def __init__(self,n,t):
        self.name = n
        self.topic = t
    def speak(self):
        print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
        
class sample(speaker,student):
    a =''
    def __init__(self,n,a,w,g,t):
        student.__init__(self,n,a,w,g)
        speaker.__init__(self,n,t)
```
```
test = sample("Tim",25,80,4,"Python")
test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法
```
- 绑定方法
```
class Base(object):
    def __init__(self,a=1,b=11):
        self.a = a
        self.b = b
 
# 绑定（推荐）
class B(Base):
    def __init__(self, a, b, c):
        super().__init__(a, b)  # super(B, self).__init__(a, b)
        self.c = c
 # 未绑定
class BB(Base):
    def __init__(self, a, b, c):
        Base.__init__(self, a=a, b=1000)
```
```
B(1,2,3).a, B(1,2,3).b, B(1,2,3).c
BB(1,2,3).a, BB(1,2,3).b, BB(1,2,3).c

(1, 2, 3)
(1, 1000, 3)
```
```
　　1. super并不是一个函数，是一个类名，形如super(B, self)事实上调用了super类的初始化函数，
       产生了一个super对象；
　　2. super类的初始化函数并没有做什么特殊的操作，只是简单记录了类类型和具体实例；
　　3. super(B, self).func的调用并不是用于调用当前类的父类的func函数；
　　4. Python的多继承类是通过mro的方式来保证各个父类的函数被逐一调用，而且保证每个父类函数
       只调用一次（如果每个类都使用super）；
　　5. 混用super类和非绑定的函数是一个危险行为，这可能导致应该调用的父类函数没有调用或者一
       个父类函数被调用多次。
```
## 装饰器
- @classmethod: 不需要self参数，但第一个参数需要是表示自身类的cls参数
> @classmethod意味着：当调用此方法时，我们将该类作为第一个参数传递，而不是该类的实例（正如我们通常使用的方法）。 这意味着您可以使用该方法中的类及其属性，而不是特定的实例

- @staticmethod: 不需要表示自身对象的self和自身类的cls参数，就跟使用函数一样
> @staticmethod意味着：当调用此方法时，我们不会将类的实例传递给它（正如我们通常使用的方法）。 这意味着你可以在一个类中放置一个函数，但是你无法访问该类的实例（当你的方法不使用实例时这很实用）

```
class A(object):  
    bar = 1  
    def foo(self):  
        print 'foo'  
 
    @staticmethod  
    def static_foo():  
        print 'static_foo'  
        print A.bar  
 
    @classmethod  
    def class_foo(cls):  
        print 'class_foo'  
        print cls.bar  
        cls().foo()
        
A.static_foo()  
A.class_foo()
```
```
static_foo
1

class_foo
1
foo
```
