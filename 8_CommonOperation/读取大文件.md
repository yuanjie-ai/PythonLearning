```python
from tqdm import tqdm

def iterRead(file='/opt/yuanjie_data/wiki.txt'):
    with open(file) as myfile:
        for line in tqdm(myfile, desc='iterRead'):
            yield line
```

```python
import fileinput
for line in fileinput.input('myfile'):
    do_something(line)
```
