import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


class DataLoader():
    def __init__(self, path: str, name: str):
        self.path = path
        self.data = self.read_data(path)
        self.name = name
        self.shape = self.data.shape

        print("Data loaded.")

    def __str__(self):
        return "Dataset named: " + self.name + ", under path: " + self.path

    def read_data(self, path: str) -> pd.DataFrame:
        data_pdframe = pd.read_csv(path)
        return data_pdframe

    def analyse_data(self) -> str:
        '''J'ai wrote a piece of merde ici.
        '''
        data_info = os.path.dirname(__file__) + '/' + self.name + '_info.txt'
        assert not os.path.exists(data_info), "Info file exists."
        di = open(data_info, 'w')
        _data_rows, _data_columns = self.data.shape
        di.write("Data of shape: (" + str(_data_rows) + ', ' +
                 str(_data_columns) + ')\n')
        # _data_descrip = self.data.describe()
        # _data_descrip.to_csv(data_info,sep = ' ')


class DataProcessor():
    def __init__(self, data):
        self.data = data
        assert type(data)==pd.DataFrame, 'Data not a pandas DataFrame'

    def remove_outliers(self):
        '''seems that the data processing doesnt need a functonal programming as it is not as repeatable as other tasks
        '''
        self.data.drop(self.data[(self.data['OverallQual']<5) & (self.data['SalePrice']>200000)].index,inplace=True)
        self.data.drop(self.data[(self.data['YearBuilt']<1900) & (self.data['SalePrice']>300000)].index,inplace=True)
        self.data.drop(self.data[(self.data['YearBuilt']<1980) & (self.data['SalePrice']>650000)].index,inplace=True)
        self.data.drop(self.data[(self.data['TotalBsmtSF']>5000) & (self.data['SalePrice']>200000)].index,inplace=True)
        self.data.drop(self.data[(self.data['GrLivArea']>4000) & (self.data['SalePrice']<200000)].index,inplace=True)

        pass

    def fit(self,):
        pass



if __name__ == "__main__":

    # read data, check shape
    train_path = "/home/yijie/kaggles/data/house_price/" + 'train.csv'
    train_data = DataLoader(train_path, 'train')
    assert train_data.shape==(1460,81),'az'
    # train_data.analyse_data()

    # process data