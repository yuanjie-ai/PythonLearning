## 根据AUC推算正负样本
```python
from numba import jit
@jit
def f(auc):
    auc = auc
    pred_n1 = sum(pred)
    r = pd.Series(pred).rank().unique()
    r1 = r.max()
    r2 = r.min()
    n = len(pred)
    for n1 in range(1, n):
        for k1 in range(n1+1):
            n0 = n - n1
            k2 = n1-k1
            x = auc*n1*n0 + 0.5*n1*(n1+1) - k1*r1 - k2*r2
            print(n1, n0, k1, k2, n1/n0)
             if x == 0 and n1/n0 < 1:
                 print(n1, n0, k1, k2, n1/n0)
```
