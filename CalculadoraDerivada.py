import os

def printar_expressao(expressao):
    
    q=0
    for i in expressao:
        
        #verifica se eh uma constante ou se esta vazaio
        if i['a'] == 0 or i["a"] == None:
            continue
        
        #verifica se eh o primero termo da expressao ou se o termo eh negativo
        if q != 0 and i["a"] > 0:
            print('+',end='')
        q+=1
        
        
        #verifica se a constante que acompanha x eh 1
        temp=f'{i["a"]}' if i['a'] != 1 else ''
        print(f'{temp}',end='')
        
        #verifica se eh uma constante ou se esta vazaio
        if i['b'] == 0 and i["b"] != None:
            continue
        print(f'X',end='')    
        
        #verifica se a potencia e a raiz se cancelam
        if i["b"] != i["c"]:
            
            print(f"^({i['b']}",end='')
            
            #printa a raiz caso ela nao seja nula e precise ser expressa
            if i["c"] != None and i["c"] != 1:
                print(f'/{i["c"]}',end='')
            print(')',end='')
            
    
    
def derivada(expressao):
    for i in range(len(expressao)):
        
        if expressao[i]['b'] != 0:
            #derivada
            expressao[i]['a']*=(expressao[i]['b']/expressao[i]['c'])
            expressao[i]['b']=(expressao[i]['b']/expressao[i]['c'])-1
            expressao[i]['c']=1
       
        else:
            #derivada de constante
            expressao[i]['a']*=0
            expressao[i]['b']=1
            expressao[i]['c']=1
            
    return expressao
def derivada_mult(expressao1,expressao2):
    
    d1=derivada(expressao1)
    d2=derivada(expressao2)
    
    print(f'((',end='')
    printar_expressao(d1)
    print(')*(',end='')
    printar_expressao(expressao2)
    print('))+((',end='')
    printar_expressao(expressao1)
    print(')*(',end='')
    printar_expressao(d2)
    print('))')
    
while True:
    
    tipo=input('Digite o tipo de operacao (+,*):')
    q=1
    if tipo == '*':
        q=2

    for t in range(q):   
        expressao=[]
        entrada=''
        
        quantidade=int(input("Digite a quantidade de termos na operacao:"))
        for i in range(quantidade):
            
            temp={'a':None,
                'b':None,
                'c':None
            }
            
            expressao.append(temp)
            
            for v,j in enumerate([['a','{A}X'],['b','X^{B}'],['c','X^(1/{c})']]):
                
                os.system("clear")
                printar_expressao(expressao)
                print()
                entrada=input(f"Digite {j[1]}:")
                entrada=float(entrada) if '.' in entrada else int(entrada)
            
                if entrada == 0:
                    if v == 0:
                        expressao.remove(temp)
                        temp['a']=0
                    if v == 1:
                        temp['b']=0
                    temp['c']=1
                    break
                temp[j[0]]=entrada
            if temp['a'] == 0:
                break
            
        expressao1=expressao        
        if tipo == '*' and t == 0:
            expressao2=expressao
    if tipo == '*':
        derivada_mult(expressao1,expressao2)
    else:
        
        os.system("clear")
        print(f'f(x)=',end='')
        printar_expressao(expressao)
        print(f"f(x)'=",end='')
        printar_expressao(derivada(expressao))    

