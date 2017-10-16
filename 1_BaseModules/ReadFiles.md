
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

0 0:0.5962697164566368 1:0.9392180357148177
1 0:0.9547540606261182 1:0.484083746521063
0 0:0.6975938462755731 1:0.5302397020723172
1 0:0.6521080262021213 1:0.7397087084980414
1 0:0.9842921591804101 1:0.6113926776050588
1 0:0.6473347661802823 1:0.5186862522875021
0 0:0.6803983736436738 1:0.224082922556595
0 0:0.8023152733681855 1:0.752657665609176
0 0:0.3906487370086729 1:0.09713638970088423
1 0:0.4407321395463357 1:0.9165169287262472
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
