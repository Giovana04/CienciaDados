import firebase_admin
from firebase_admin import credentials, auth, firestore, storage, messaging
from networkx import display
from pymsgbox import password

cred = credentials.Certificate("cienc.json")
firebase_admin.initialize_app(cred)

def atualizaProduto(id, preco):
    db = firestore.client()
    doc_ref = db.collection('produtos').document(id)
    doc_ref.update({'preco': preco})

db = firestore.client()

ref = db.collection('produtos').document('produto_id')
ref.set({
    'nome': 'p1',
    'preco': 10.0
})

idproduto = db.collection('produtos').add({'nome': 'Produto B', 'preco': 20.0})[1].id

atualizaProduto(idproduto, 200.0)

pega = db.collection('produtos').document(idproduto).get()

print(pega.to_dict())


