import pandas as pd

e = pd.read_csv(r"C:\Users\giova\OneDrive\Documentos\GitHub\CienciaDados\Lista 3\vendas.csv", sep=";", decimal=".", chunksize=20)
for i, bloco in enumerate(e):
    print(f"Bloco {i + 1}:")
    print(f"Número de linhas neste bloco: {len(bloco)}")
    print("Primeiras 3 linhas do bloco:")
    print(bloco.head(3))
    print("-" * 30)