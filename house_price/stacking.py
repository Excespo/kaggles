import numpy as np
import yaml

def train_base():
    pass

class Stacking():
    """
    Procedure of stacking:
    -inputs->
    -lower models->
    -middle outputs->
    -higher model->
    -final output
    """
    def __init__(self,config_file:str=None,train=None,test=None):
        self.config(config_file)
        assert train and test is not None, 'Empty data input!'
        self.test = test
        self.train = self.k_folded(train)

        # self.base_models = []
        # self.high_model = models.pop()
        # self.k_folds = len(models)
        # for model in models:
        #     self.low_models.append(model)

    def config(self,config_file):
        if not config_file:
            raise Exception('Configuration loading failed.')
        else:
            with open(config_file,'r',encoding='utf-8') as y:
                cfg = yaml.load(y.read(), Loader=yaml.FullLoader)
            self.base_models = cfg['base_models']
            self.k_folds = cfg['k_folds']
            self.high_model = cfg['high_model']
            print("Configuration loading succeeded.")

    @property
    def k_folded(self,k):
        pass

    def train(self):
        pass

    def predict(self):
        pass

    def show_eff(self):
        pass

if __name__ == '__main__':
    cfgf = r"/home/yijie/kaggles/house_price/config.yaml"
    model = Stacking(cfgf)
    print(model.k_folds)
    print(model.high_model)