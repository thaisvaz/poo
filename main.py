# from novoClassifier import splitar, fitPred
import pandas as pd

from novoClassifier import Modelo

df = pd.read_csv('data.csv')

modelo = Modelo(df = df)

# modelo.splitar(perc_test=0.3)

print(modelo.__bla)

# print(modelo.y_train.shape)

# print(modelo.df.shape)
