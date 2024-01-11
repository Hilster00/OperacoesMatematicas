from functools import reduce

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


def mdc(n,m):
    lista_mdc=[]
    for i in retornar_primos(n if n>m else m):
        while (n%i == 0) or (m%i == 0):
            if (n%i == 0) and (m%i == 0):
                lista_mdc.append(i)
            n=n if n%i != 0 else n/i
            m=m if m%i != 0 else m/i
    return  reduce( lambda prod, i: i*prod, lista_mdc, 1)

def mmc(n,m):
    lista_mmc=[]
    for i in retornar_primos(n if n>m else m):
        while (n%i==0) or (m%i==0):
            lista_mmc.append(i)
            n=n if n%i != 0 else n/i
            m=m if m%i != 0 else m/i
     return  reduce( lambda prod, i: i*prod, lista_mmc, 1)

    
