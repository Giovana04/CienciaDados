import firebase_admin
from firebase_admin import credentials, auth, firestore, storage, messaging

cred = credentials.Certificate("cienc.json")
firebase_admin.initialize_app(cred)

print("")