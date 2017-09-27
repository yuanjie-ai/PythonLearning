
---
```python
def runTime(func):
    def wrapper(*args,**kwargs):
        import time
        t1 = time.time()
        func(*args,**kwargs)
        t2 = time.time()
        print ("%s run time: %.5f s" %(func.__name__,t2-t1))
    return wrapper
```

```
@runTime
def bubbleSort(a):
    length = len(a)
    for i in range(length):
        for j in range(0,length-1-i):
            if a[j] > a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
```

```
a = [5,8,6,3,7,8,5,2,8,6,4]*100
bubbleSort(a)
```
```
bubbleSort run time: 0.14201 s
```
