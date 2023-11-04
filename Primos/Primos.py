import os
import GerarPrimos
#laco para tratamento de erro
while True:
    #trata valores válidos
    try:
            
    #recebimento e cast de valores
        quantidade=input("Digite a quantidade de números primos desejados:")
        quantidade=int(float(quantidade))

        #verificação se o valor corresponde a uma quantidade válida
        if quantidade >= 1:
            break
        else:
            print(f"Valor {quantidade} não está no intervalo valido")
    #bloco para valores não numericos
    except:
        os.system("cls")
        print(f"Valor {quantidade} não é um número valido")

                       
#função propria para printar os números primos, printa eles de forma rápida
#GerarPrimos.printar_primos(quantidade)

print("\n")
print("_"*10)

#função propria para retornar uma lista com os 'n' primeiros primos, quando usado para printar acaba sendo mais lendo
primos=GerarPrimos.retornar_primos_Y(quantidade)
print(f"Os numeros primos são:")
for numero in primos:
    print(f"{numero}",end=", ")
    
print("\n")
print("_"*10)

#função propria para retornar uma lista com os 'n' primeiros primos, quando usado para printar acaba sendo mais lendo
primos=GerarPrimos.retornar_primos(quantidade)
print(f"Os numeros primos são:")
for numero in primos:
    print(f"{numero}",end=", ")
