import pandas as pd

e = pd.read_csv(r"C:\Users\giova\OneDrive\Documentos\GitHub\CienciaDados\Lista 3\experimento.csv", sep=",")
print(e.head())
print(e.tail())
print(e.describe())