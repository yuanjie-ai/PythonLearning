# :rocket: Numpy :facepunch:
---
- reshape：一列
```
a = np.arange(10)
a[:, np.newaxis]
a.reshape((-1,1))
```
```
array([[0],
       [1],
       [2],
       [3],
       [4],
       [5],
       [6],
       [7],
       [8],
       [9]])
```

