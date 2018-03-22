```python
def apply_parallel(df, func, n_jobs=16):
    from joblib import Parallel, delayed
    df_grouped = df.groupby(df.reset_index(drop=True).index)
    results = Parallel(n_jobs)(delayed(func)(group) for _, group in df_grouped) # map
    return pd.concat(results) # reduce

def tmp_func(df):
    df['xx'] = df['x'].apply(complexFunction)
    return df
```
