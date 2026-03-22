import pandas as pd

dados_lista = []
for i in range(1, 51):
    temp = 20 + (i % 10) + (i * 0.1)
    if i % 7 == 0:
        temp = "NA"
    elif i % 10 == 0:
        temp = "-"
    dados_lista.append(f"S{i},{temp},{1000 + i},OK")
    
cabecalho = "sensor_id,temperatura,pressao,status\n"
conteudo_final = cabecalho + "\n".join(dados_lista)
with open('dados_sensor_gigante.csv', 'w', encoding='utf-8') as f:
    f.write(conteudo_final)
    
df_iterador = pd.read_csv('dados_sensor_gigante.csv', na_values=['NA', '-'], chunksize=10, engine='python')

print(f"{'Bloco':<10} | {'Temp Média':<12} | {'Valores Ausentes (Temp)':<20}")
print("----------------------------------------------------------")
for i, bloco in enumerate(df_iterador):
    media_temp = bloco['temperatura'].mean()
    ausentes = bloco['temperatura'].isna().sum()
    
    print(f"Bloco {i+1:<5} | {media_temp:<12.2f} | {ausentes:<20}")