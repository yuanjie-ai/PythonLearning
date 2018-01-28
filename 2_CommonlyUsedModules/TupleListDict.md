- Tuple
```python
from collections import namedtuple
vector= namedtuple("Dimensiton", 'x,y,z')
# vector= namedtuple("Dimensiton", ['x', 'y', 'z'])
vec = vector(1,2,3)
print(vec.x, vec.y, vec.z)
```
