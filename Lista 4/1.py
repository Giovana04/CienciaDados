import re
from collections import Counter

def contar_palavras(caminho_arquivo):
    try:
        with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().lower()
            
            palavras = re.findall(r'\b\w+\b', conteudo)
            
            contagem = Counter(palavras).most_common(10)
            
            print(f"{'Palavra':<15} | {'Frequência'}")
            print("-" * 30)
            for palavra, freq in contagem:
                print(f"{palavra:<15} | {freq}")
                
    except FileNotFoundError:
        print("arquivo não foi encontrado")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")