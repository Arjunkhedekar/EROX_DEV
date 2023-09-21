import os
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase Admin SDK with your credentials
cred = credentials.Certificate("path/to/your/credentials.json")
firebase_admin.initialize_app(cred, {'storageBucket': ' '})

local_directory = " "

bucket = storage.bucket()
blobs = bucket.list_blobs()
for blob in blobs:
    if blob.name.endswith(".pdf"): 
        local_file_path = os.path.join(local_directory, blob.name)
        blob.download_to_filename(local_file_path)
        print(f"PDF file downloaded to: {local_file_path}")
