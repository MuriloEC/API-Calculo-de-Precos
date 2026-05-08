import firebase_admin
from firebase_admin import credentials, firestore

# Esconder a chave antes de hospedar
cred = credentials.Certificate("SUA_CREDENCIAL_AQUI.json")
firebase_admin.initialize_app(cred)

db = firestore.client()


