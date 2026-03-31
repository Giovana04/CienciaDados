import pandas as pd

def calcular_media_categoria(caminho_arquivo, categoria_alvo):
    try:
        df = pd.read_csv(caminho_arquivo, sep=';', decimal=',')
    
        produtos_filtrados = df[df['item'] == categoria_alvo]
        
        if not produtos_filtrados.empty:
            media_preco = produtos_filtrados['valor_unitario'].mean()
            
            print(f"Itens encontrados: '{categoria_alvo}':")
            print(produtos_filtrados[['item', 'valor_unitario']])
            print(f"\nPreço Médio: R$ {media_preco:.2f}")
        else:
            print(f"Nenhum item encontrado para: {categoria_alvo}")
            
    except FileNotFoundError:
        print("arquivo não existe")
    except KeyError as e:
        print(f"coluna não encontrada no CSV: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

calcular_media_categoria('Lista 3\estoque.csv', 'maca')
