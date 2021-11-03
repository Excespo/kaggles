# <center> Something to know in this proj


## *Pandas*
---
### <center> pd.Series & pd.DataFrame

[pd.Series](https://pandas.pydata.org/docs/reference/api/pandas.Series.html?highlight=series#pandas.Series)

index: 1-dim array-like (list/ dict/ ...)

[pd.DataFrame](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html?highlight=datafram)

additional param: `columns`

__ATTENTION!__ index is always at position 0

---
### <center> `@property` in source code

To modify private variables for a class

---
### <center> `df.__dir__()`

First look:

    - df.describe()
    - df.columns()
    - df.shape/ df.size
    - df.unique()/ df.nunique()
    - df.values()

Statistic:
    
    - df.corr()/ df.cov()
    - df.median(), df.mode()
    - df.select_type(include=List)
    - df.isnull()
    - df.fillna()
    - df.drop()
    - df.sort_value(by, axis=0, ascending=True, inplace=False,...)
    - df.value_counts()

usual(& __important__) params:
- `axis = 0 or 1` down or across (Matrix-like)
- `inplace: bool`

df.groupby():
`df.groupby(by, axis=0, level=None,)

### df.groupby & transform/ agg/ apply

## *Seaborn & Matplotlib.pyplot*

---
### sns.FacetGrid

---
### sns.distplot 

include: hist, kde, rug

---
### sns.probplot

## *scipy & sklearn*

---
### scipy.norm(.fit)

---
### prepocessing.LabelEncoder

---
### stats.skew & stats.norm

