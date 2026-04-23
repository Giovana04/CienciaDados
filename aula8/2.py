import firebase_admin
from firebase_admin import credentials, auth, firestore, storage, messaging
from networkx import display
from pymsgbox import password

cred = credentials.Certificate("cienc.json")
firebase_admin.initialize_app(cred)

user = auth.create_user(
    email="g@mail.com",
    email_verified=False,
    password="123456",
    display_name="bah"
)

print(user.uid)