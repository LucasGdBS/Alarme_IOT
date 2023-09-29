from fastapi import FastAPI

app = FastAPI()

dado = 0

@app.post('/postdistancia')
def post_distancia(dado: float):
    """
    Envia a distância do objeto detectado pelo sensor ultrassom.

    Args:
        distancia: A distância do objeto detectado.

    Returns:
        Uma mensagem de sucesso.
    """
    try:
        dado = 0
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
        return {"Sucesso": dado}
    except:
        return {401:'Bad Request'}
