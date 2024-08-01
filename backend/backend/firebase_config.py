import firebase_admin
from firebase_admin import credentials, firestore

# Initialize Firebase Admin SDK
cred = credentials.Certificate('/Users/martinlacsamana/Documents/project-guardian/backend/backend/project-guardian-c0841-d156975d131c.json')  # Ensure the filename is correct
firebase_admin.initialize_app(cred)

# Initialize Firestore
db = firestore.client()