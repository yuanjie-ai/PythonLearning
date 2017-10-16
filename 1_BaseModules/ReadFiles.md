---
- DataFrame2libsvm
```python
from sklearn.datasets import dump_svmlight_file
df = pd.DataFrame()
df['a'] = np.random.rand(10,)
df['b'] = np.random.rand(10,)
df['label'] = list(map(lambda x: -1 if x < 0.5 else 1, np.random.rand(10,)))
X = df[['x1', 'x2']]
y = df.label
dump_svmlight_file(X,y,'smvlight.dat',zero_based=True,multilabel=False)

1 0:0.468403855472003 1:0.4666512988598032
-1 0:0.8517423694470649 1:0.4327355266019312
1 0:0.9917465382398956 1:0.7157050909216627
-1 0:0.2641384684398076 1:0.6669819018417372
-1 0:0.1935762008016808 1:0.1663854560933703
-1 0:0.5022230367312078 1:0.3667819344196961
1 0:0.4594241453460095 1:0.692500446551131
1 0:0.2379311735370921 1:0.9509205138927085
1 0:0.2221779411574195 1:0.916799481115229
1 0:0.01015918812655936 1:0.5159480732646645
```

---
- libsvm
```python
from sklearn.datasets import load_svmlight_file, load_svmlight_files
from svmloader import load_svmfile, load_svmfiles
X, y = load_svmlight_file('./smvlight.dat')
X, y = load_svmfile('./smvlight.dat')
```
---
