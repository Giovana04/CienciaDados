import pandas as pd

e = pd.read_csv(r"C:\Users\giova\OneDrive\Documentos\GitHub\CienciaDados\Lista 3\notas.csv", sep=",", decimal=".")
print(e)
print(e.describe())
#        matematica  portugues  historia
#mean     7.750000   7.250000  7.750000
