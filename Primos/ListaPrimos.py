primos=[2,3] 
def retornar_primos(valor_teto):
    
    global primos
    for i in primos:
        yield i
    identador=primos[-1]+2
    
    #bloco para encontrar os primos até o valor_teto
    while identador<=valor_teto:                   
        for x in range(3,identador,2):      
            if(identador%x==0):  #verificacao se é um divisor
                laco_concluido=False  #laço não concluido
                break  #quebra de laço quando encontra o primeiro divisor
        else:
            yield identador
            primos.append(identador)
        identador+=2  #incrementação de 2 em 2 para pular os pares
