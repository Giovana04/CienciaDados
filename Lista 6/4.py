import pandas as pd
#1
df = pd.read_csv('vendas.csv', header=None, index_col=0, na_values=['ND'])

#2
relatorio_anual = df  
relatorio_anual.to_excel('relatorio.xlsx', sheet_name='Resultados')
df_brutos = pd.read_excel('arquivo_existente.xlsx', sheet_name='Dados Brutos')

#3
import requests
resposta = requests.get('https://api.portaldatransparencia.gov.br/api-de-dados/servidores/por-orgao?pagina=1')
df_orgao = pd.DataFrame([resposta.json()])

#4
from sqlalchemy import create_engine
engine = create_engine('sqlite:///meu_banco.db')
df_orgao.to_sql('produtos', con=engine, index=False, if_exists='replace')
df_produtos = pd.read_sql_table('produtos', con=engine)