from fastapi import FastAPI

app = FastAPI()

dadoA = 0

@app.post('/postdistancia/')
async def post_distancia(dado: float):
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

@app.get('/getdistancia')
def get_distancia():
    """
    Obtem a distância do objeto detectado pelo sensor ultrassom.

    Args:
        distancia: A distância do objeto detectado.

    Returns:
        Uma mensagem de sucesso.
    """
    try:
        return {"Sucesso": dadoA}
    except:
        return {401:'Bad Request'}
