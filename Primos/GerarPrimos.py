import os

#printa os primos assim que os encontra e não os guarda, sendo mais rápido
def printar_primos(quantidade):
    if quantidade >= 1:

        #recebimento de valor inicial para polpar tempo
        primos=1
        identador=3  #variavel que será verificado se é primo

        #mensagens para diferentes quantidades
        msg= "O primeiro número primo é: 2" if quantidade==1 else f"Os {quantidade} primeiros primos são: 2,"
        
        print(f"{msg}",end=" ")
        if quantidade != 1:    
            #bloco para encontrar os 'n' primeiros primos
            while True:
                

                #laçao para verificar os primos
                for x in range(3,identador,2):      
                    if(identador%x==0):  #verificacao se é um divisor
                        laco_concluido=False  #laço não concluido
                        break  #quebra de laço quando encontra o primeiro divisor

                #printa o número primo caso tenha concluido o laço
                else:
                    print(f"{identador}",end="")
                    primos+=1
                    
                    #bloco que verifica se ainda tem primos a serem encontrados
                    if(primos ==quantidade):
                        break
                    else:
                        #coloca ',' ao final da linha caso ainda tenha mais primos para serem encontrados
                        print(", ",end="")
                identador+=2  #incrementação de 2 em 2 para pular os pares

    else:
        print(f"Valor {quantidade} não é um valor válido!")


#função que retorna lista com os 'n' primeiros primos e os retorna
def retornar_primos_Y(quantidade):
    
    if quantidade >= 1:        
        #recebimento de valor inicial para polpar tempo
        primos=[2]
        identador=3  #variavel que será verificado se é primo

        #bloco para encontrar os 'n' primeiros primos
        while len(primos)!=quantidade:                   
            for x in range(3,identador,2):      
                if(identador%x==0):  #verificacao se é um divisor
                    laco_concluido=False  #laço não concluido
                    break  #quebra de laço quando encontra o primeiro divisor
            else:
                yield identador
                primos.append(identador)
            identador+=2  #incrementação de 2 em 2 para pular os pares

    else:
        print(f"Quantidade {quantidade} invalida!")
        return 0 #retorno para a funcao não dar erro
      
def retornar_primos(quantidade):
  
    if quantidade >= 1:        
        #recebimento de valor inicial para polpar tempo
        primos=[2]
        identador=3  #variavel que será verificado se é primo

        #bloco para encontrar os 'n' primeiros primos
        while len(primos)!=quantidade:                   
            for x in range(3,identador,2):      
                if(identador%x==0):  #verificacao se é um divisor
                    laco_concluido=False  #laço não concluido
                    break  #quebra de laço quando encontra o primeiro divisor
            else:
                primos.append(identador)
            identador+=2  #incrementação de 2 em 2 para pular os pares

        return primos
    else:
        print(f"Quantidade {quantidade} invalida!")
        return 0 #retorno para a funcao não dar erro
