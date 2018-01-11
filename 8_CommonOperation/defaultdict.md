```python
import collections
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

# defaultdict
d = collections.defaultdict(list)
for k, v in s:
    d[k].append(v)

# Use dict and setdefault    
g = {}
for k, v in s:
    g.setdefault(k, []).append(v)

# Use dict
e = {}
for k, v in s:
    e[k] = v
```
---
## 字典计数
```python
hmm_model = {i:Counter() for i in 'sbme'}
# {'b': Counter(), 'e': Counter(), 'm': Counter(), 's': Counter()}
hmm_model['s']['xxxx']=10
# {'b': Counter(), 'e': Counter(), 'm': Counter(), 's': Counter({'xxxx': 10})}
```
