import os
from json import loads
from dotenv import load_dotenv
from binascii import unhexlify
from hashlib import pbkdf2_hmac
from firebase_admin import credentials, firestore, initialize_app

# Initialize Firebase
load_dotenv()
credStr = os.environ.get('FIREBASE_KEY')
credJson = loads(credStr)
cred = credentials.Certificate(credJson)
initialize_app(cred)
db = firestore.client()

def verifyLogin(email, password):
    try:
        doc = db.collection('users').document(email).get()
        if doc.exists:
            hashPassHex = doc.get('passwordHash')
            saltHex = doc.get('salt')
            
            hashPass = unhexlify(hashPassHex)
            salt = unhexlify(saltHex)
            
            inputPass = pbkdf2_hmac(
                'sha256',
                password.encode('utf-8'),
                salt,
                100000
            )
            
            return hashPass == inputPass
        else:
            return False
    except Exception as e:
        print(f"Error verifying login: {e}")
        return False
