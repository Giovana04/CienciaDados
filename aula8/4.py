import firebase_admin
from firebase_admin import credentials, firestore

if not firebase_admin._apps:
    cred = credentials.Certificate("cienc.json")
    firebase_admin.initialize_app(cred)

db = firestore.client()

def buscar_produtos_caros(valor_limite):
    print(f"Procurando produtos que custam mais que R$ {valor_limite}...")
    
    query = db.collection('produtos_mysql').where('preco', '>', valor_limite).stream()

    encontrou = False
    for doc in query:
        encontrou = True
        p = doc.to_dict()
        print(f"Nome: {p.get('nome')} | Preço: R$ {p.get('preco'):.2f}")
    
    if not encontrou:
        print("Nenhum produto encontrado")

buscar_produtos_caros(15.0)