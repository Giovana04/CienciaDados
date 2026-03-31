import requests
from bs4 import BeautifulSoup

def extrair_titulos_h2(url):
    try:
        resposta = requests.get(url, timeout=10)
        
        resposta.raise_for_status()
        
        soup = BeautifulSoup(resposta.text, 'html.parser')
        
        titulos = soup.find_all('div')
        
        if not titulos:
            print(f"Nenhum <div> encontrado em {url}")
            return

        print(f"{'Contagem':<5} | {'Texto do Título'}")
        print("-" * 40)
        
        for i, div in enumerate(titulos, 1):
            texto = div.get_text(strip=True)
            print(f"{i:<8} | {texto}")
            
    except requests.exceptions.RequestException as e:
        print(f"Erro na requisição: {e}")
    except Exception as e:
        print(f"Erro inesperado: {e}")

extrair_titulos_h2("https://dados.gov.br/")