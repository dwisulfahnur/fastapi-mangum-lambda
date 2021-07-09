import os
from fastapi import FastAPI
from mangum import Mangum

STAGE = os.environ.get('STAGE')
root_path = '/' if not STAGE else f'/{STAGE}'

app = FastAPI(title="FastAPI x AWS Lambda", root_path=root_path)


@app.get('/hello')
def hello_api(name: str = 'World'):
    return {"hello": name}


# Mangum Handler, this is so important
handler = Mangum(app)
