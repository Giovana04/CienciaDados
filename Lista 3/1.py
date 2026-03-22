import kagglehub
import pandas as pd
import os

path = kagglehub.dataset_download("anuchhetry/product-sales")
print("Path to dataset files:", path)

arquivos = os.listdir(path)
print(f"Arquivos encontrados: {arquivos}")
arquivo_excel = None
for f in arquivos:
    if f.endswith('.xlsx'):
        arquivo_excel = os.path.join(path, f)
        break

df = pd.read_excel(arquivo_excel) 
print(df.head())