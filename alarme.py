from fastapi import FastAPI
from pydantic import BaseModel


class Dado(BaseModel):
    dado: float


app = FastAPI()

dadoA:Dado = {"dado": 0}

@app.post('/postdistancia/')
async def post_distancia(dado: Dado):
    """
    Envia a distância do objeto detectado pelo sensor ultrassom.

    Args:
        distancia: A distância do objeto detectado.

    Returns:
        Uma mensagem de sucesso.
    """
    try:
        global dadoA
        dadoA = dado
    except:
        return {401:'Bad Request'}
    else:
        return {200:'OK'}

@app.get('/getdistancia/')
async def get_distancia():
    """
    Obtem a distância do objeto detectado pelo sensor ultrassom.

    Args:
        distancia: A distância do objeto detectado.

    Returns:
        Uma mensagem de sucesso.
    """
    try:
        return dadoA
    except:
        return {401:'Bad Request'}

@app.get('/')
async def home():
    """
    Apenas a pagina inicial da API
    """
    return {'Bem-Vindo à ': 'AlarmeAPI'}