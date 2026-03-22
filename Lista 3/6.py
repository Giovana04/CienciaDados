from os import read

import pandas as pd

e = pd.read_csv(r"C:\Users\giova\OneDrive\Documentos\GitHub\CienciaDados\Lista 3\sensores.csv", sep=",", na_values=['NA', '-'])
print(e)
print(e.info())