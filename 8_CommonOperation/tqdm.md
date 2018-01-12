```python
from tqdm import tqdm
for char in tqdm(["a", "b", "c", "d"], desc='%s' % char):
    print(char)
```
