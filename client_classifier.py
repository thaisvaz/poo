# from novoClassifier import splitar, fitPred
import pandas as pd

from novoClassifier import Modelo

df = pd.read_csv('data.csv')


modelo = Modelo(df = df)

# print(modelo)