from datetime import timedelta
from minio import Minio
from dotenv import load_dotenv
import os

load_dotenv()

ACCESS_KEY = os.environ.get('ACCESS_KEY')
SECRET_KEY = os.environ.get('SECRET_KEY')
MINIO_API_HOST = os.environ.get('MINIO_API_HOST')
BUCKET = os.environ.get('BUCKET')

MINIO_CLIENT = Minio(MINIO_API_HOST, access_key=ACCESS_KEY, secret_key=SECRET_KEY, secure=False)

def get_url(nome_arquivo: str):

    url = MINIO_CLIENT.get_presigned_url( "GET", BUCKET, nome_arquivo, expires=timedelta(days=1), ) 
    print(url)

    return url