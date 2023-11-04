def fib(n):
    anteriores=[0,1]
    retorno=0
    for i in range(n):
        retorno=sum(anteriores)
        anteriores = [anteriores[1],retorno]
    return anteriores[1]

if __name__=="__main__":
    #exemplo de como utilizar   
    print(fib(9))
