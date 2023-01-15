import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import random
random.seed(42)

class Modelo:

    # construtor
    def __init__(self, df):

        self.df = df

        self.__bla = "a" # variável privada

    def splitar(self, perc_test):
        '''
        test_size: tamanho percentual da amostra de teste
        '''

        y = self.df['y']
        X = self.df.drop('y', axis = 1)

        # atribuindo novos objetos ao self
        self.X_train, self.X_test, self.y_train, self.y_test = train_test_split(X, y, test_size = perc_test)

    def fitPred(self):
        
        lr = LogisticRegression()
        
        lr.fit(self.X_train,self.y_train)
        
        y_pred = lr.predict(self.X_test)

        return accuracy_score(self.y_test, y_pred)


if __name__ == '__main__':

    df = pd.read_csv('data.csv')

    modelo = Modelo(df = df)

    print(modelo)