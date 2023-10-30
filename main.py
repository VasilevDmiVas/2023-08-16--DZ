from fastapi import FastAPI
import psycopg2
from dotenv import dotenv_values
from pydantic import BaseModel

config = dotenv_values('.env')
connect = psycopg2.connect(
    host = config['HOST'],
    port = config['PORT'],
    user = config['USER_ID'],
    password = config['USER_PD'],
    database = config['DB_NAME'],
)

app = FastAPI()
@app.get('/')
def root():
    return {'Всем привет'}