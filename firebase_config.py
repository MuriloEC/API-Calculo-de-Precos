import firebase_admin
import json
from firebase_admin import credentials, firestore

# Esconder a chave antes de hospedar
cred = credentials.Certificate("SUA_CHAVE.json")
firebase_admin.initialize_app(cred)

db = firestore.client()