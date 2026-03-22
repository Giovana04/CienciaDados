import pandas as pd

e = pd.read_csv(r"C:\Users\giova\OneDrive\Documentos\GitHub\CienciaDados\Lista 3\bigDataSimulado.csv", sep=",", thousands=".", decimal=".")
print(e.info())
# memory usage: 462.0+ bytes