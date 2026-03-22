import pandas as pd

e = pd.read_csv(r"C:\Users\giova\OneDrive\Documentos\GitHub\CienciaDados\Lista 3\transacoes.csv", sep=",", thousands=".", decimal=".")
print(e)
print(e.dtypes)