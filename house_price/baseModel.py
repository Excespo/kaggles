import numpy as np
import sklearn
from sklearn.model_selection import GridSearchCV

class Grid():
    def __init__(self,model):
        self.model = model
    
    def fit(self,X,y,param_grid):
        grid_search = GridSearchCV(self.model,param_grid,cv=5,scoring='neg_mean_squared_error')

