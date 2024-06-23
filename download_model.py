import firebase_admin
from firebase_admin import credentials, storage
from google.oauth2 import service_account
from google.cloud import storage
from tempfile import gettempdir
from os.path import exists
from os import mkdir

def download():
    temp = gettempdir()
    folder_path = f'{temp}/models'
    if not exists(f'{temp}/models'):
        mkdir(f'{temp}/models')
    cred = credentials.Certificate(".keys/key.json")
    firebase_admin.initialize_app(cred,{'storageBucket': 'asd-model.appspot.com'})

    cred_var = service_account.Credentials.from_service_account_file(".keys/key.json")
    storage.Client(credentials=cred_var).bucket(firebase_admin.storage.bucket().name).blob('svc_new.joblib').download_to_filename(f'{folder_path}/svc_new.joblib')
    return f'{folder_path}/svc_new.joblib'