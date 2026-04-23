import firebase_admin
from firebase_admin import credentials, messaging

# Inicialização padrão (se já não estiver inicializado)
if not firebase_admin._apps:
    cred = credentials.Certificate("cienc.json")
    firebase_admin.initialize_app(cred)

def enviar_por_token(registration_token):
    message = messaging.Message(
        notification=messaging.Notification(
            title='Promo',
            body='promo',
        ),
        token=registration_token,
    )

    try:
        response = messaging.send(message)
        print('Notificação enviada com sucesso:', response)
    except Exception as e:
        print('erro', e)

def enviar_por_topico(topico):
    message = messaging.Message(
        notification=messaging.Notification(
            title='Aviso Geral',
            body='novo',
        ),
        topic=topico,
    )

    response = messaging.send(message)
    print('Notificação enviada para o tópico:', response)

token = '**********' 
enviar_por_token(token)

enviar_por_topico('ofertas')