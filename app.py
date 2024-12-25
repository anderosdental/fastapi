from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from Encryptors.Sha512 import SHA512

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # O puedes usar "*" para permitir todas las URLs
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP
    allow_headers=["*"],  # Permitir todos los encabezados
)

@app.get('/')
async def index():
    return {'message': 'Hello world'}


@app.post('/encrypted')
async def encrypted(request: Request):
    data = await request.json()
    password = SHA512.hash_password(data.get('password'))
    return {'response': password}

@app.post('/verify')
async def verify(request: Request):
    data = await request.json()
    password_verify = 'test123*'
    if SHA512.verify_password(data.get('password'), password_verify):
        return {'message': 'Password do match'}

    return {'message': 'Password doesnt match'}