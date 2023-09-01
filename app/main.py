from typing import Union
from fastapi import FastAPI
import socket
import os

app = FastAPI()


@app.get('/')
def hello_cloudru():
    return "Hello, cloudru!"

@app.get('/hostname')
def get_hostname():
    return socket.gethostname()

@app.get('/author')
def get_author():
    return os.getenv("AUTHOR")

@app.get('/id')
def get_id():
    return os.getenv("UUID")