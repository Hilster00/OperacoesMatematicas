def fat(n):
    retorno=1
    for i in range(1,n+1):
        retorno*=i
    return retorno
    
if __name__=="__main__":
    #exemplo de como utilizar   
    print(fat(5))
