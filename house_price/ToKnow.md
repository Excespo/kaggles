# <center> Something to know in this HousePrice prediciton proj


## *Pandas*


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


### sns.FacetGrid

---
### sns.distplot 

include: hist, kde, rug



## *scipy & sklearn*


### scipy.norm(.fit)

---
### preprocessing.Imputer
`Imputer(missing_values=’NaN’, strategy=’mean’, axis=0, verbose=0, copy=True)` 

[`Imputer.SimpleImputer`](https://scikit-learn.org/stable/modules/generated/sklearn.impute.SimpleImputer.html#sklearn.impute.SimpleImputer)

---
### preprocessing.RobustScaler
[Doc](https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html)

Methods:
 - fit
 - transform
---
### preprocessing.LabelEncoder

---
### stats.skew & stats.norm

---
### stats.probplot

__Quantial__: For a distribution $X$, the quantile is a fonction $Z = Z\left( \alpha \right)$ in the formula , $$\mathbb P \left(X \leq Z(\alpha) \right) = \alpha$$

__probplot__: __Q-Q__ graph, with X quantiles and Y quantiles as respectively horizonal axis and vertical axis. __Therefore 2 variables with identical distribution should show a line on Q-Q graph.__
[details](https://zhuanlan.zhihu.com/p/53124278)

[`stats.probplot(x:array_like,...)`](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.probplot.html?highlight=probplot#scipy.stats.probplot)

---
### XGBoost
