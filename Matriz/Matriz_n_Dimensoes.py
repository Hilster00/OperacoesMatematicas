def matriz(tamanho=1,camada=None):
    if camada == None:
        camada=tamanho
    if camada > 1:
        return [matriz(tamanho,(camada-1)) for i in range(tamanho)]
    else:
        return [i for i in range(tamanho)]
