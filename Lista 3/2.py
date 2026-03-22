import pandas as pd

t = pd.read_csv(r"C:\Users\giova\OneDrive\Documentos\GitHub\CienciaDados\Lista 3\temperaturas.csv", sep=";", usecols=["Data", "Temp. Ins. (C)", "Umi. Ins. (%)"])
t['Data'] = pd.to_datetime(t['Data'])
t.set_index('Data', inplace=True)

print(t.info())
print(t.head())