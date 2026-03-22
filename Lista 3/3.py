import pandas as pd
df = pd.read_csv(r"C:\Users\giova\OneDrive\Documentos\GitHub\CienciaDados\Lista 3\log_sistema.csv", sep=None, engine='python', nrows=2, comment='#')
print(df)