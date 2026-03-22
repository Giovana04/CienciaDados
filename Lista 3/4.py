from os import read

import pandas as pd

e = pd.read_csv(r"C:\Users\giova\OneDrive\Documentos\GitHub\CienciaDados\Lista 3\estoque.csv", sep=";", decimal=",")
print(e)
print(e.dtypes)