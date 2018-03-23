- https://github.com/looking-for-a-job/self.py
```python
class CLS:
	@self
	def method(self):
		print("test")

	@self
	def method2(self):
		print("test")

CLS().method().method2() # jQuery like chain
```

- Pipe

- [tqdm][2]
```python
from tqdm import tqdm
for char in tqdm(["a", "b", "c", "d"], desc='%s' % char):
    print(char)
```
---
[2]: https://lorexxar.cn/2016/07/21/python-tqdm/
