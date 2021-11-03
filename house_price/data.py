import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os


class DataLoader():
    def __init__(self, path: str, name: str):
        self.path = path
        self.data = self.read_data(path)
        self.name = name
        print("Data loaded.")

    def __str__(self):
        return "Dataset named: " + self.name + ", under path: " + self.path

    def read_data(self, path: str) -> pd.DataFrame:
        data_pdframe = pd.read_csv(path)
        return data_pdframe

    def analyse_data(self) -> str:
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


def main():

    train_path = "/home/yijie/kaggles/data/house_price/" + 'train.csv'
    train_data = DataLoader(train_path, 'train')
    train_data.analyse_data()


if __name__ == "__main__":
    main()