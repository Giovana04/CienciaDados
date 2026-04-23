import firebase_admin
from firebase_admin import credentials, firestore, exceptions

if not firebase_admin._apps:
    try:
        cred = credentials.Certificate("cienc.json")
        firebase_admin.initialize_app(cred)
    except Exception as e:
        print(f"Nem começou e já deu erro na credencial. Boa sorte: {e}")
        exit()

db = firestore.client()

def buscar(valor):
    try:
        print(f"Tentando buscar produtos acima de R$ {valor}...")
        
        query = db.collection('produtos_mysql').where('preco', '>', valor).stream()

        encontrou = False
        for doc in query:
            encontrou = True
            p = doc.to_dict()
            print(f"Produto: {p.get('nome')} - R$ {p.get('preco')}")

        if not encontrou:
            print("Vazio.")

    except exceptions.NotFoundError:
        print("não encontrado")
    
    except exceptions.PermissionDeniedError:
        print("não tem permissão")
    
    except exceptions.InvalidArgumentError as e:
        print(f"argumento invalido: {e}")

    except exceptions.FirebaseError as e:
        print(f"erro generico: {e}")

    except Exception as e:
        print(f"erro inesperado: {e}")

    finally:
        print("feito")

buscar(15.0)