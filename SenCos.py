
#lista com todos os fatoriais já calculados
f={1:1,}


def fat(n):
    if n < 1:
        return None 
    
    global f
    
    temp=n
    r=1
    
    #laço até descobrir o fatorial de n ou número menor que ele, 
    #que já tenha sido calculado
    while temp > 1:
        if f.get(temp) != None:
            r=f[temp]
            break
        temp-=1
    
    #continua o cálculo até o valor desejado           
    for i in range(temp+1,n+1):
        r*=i
    
    #guarda e retorna o valor
    f[n]=r
    return f[n]
            
def cos(x,precisao=16):
    precisao=16 if precisao < 16 else precisao
    cos=1
    s=-1
    p=base=x**2
    f=fat(2)
    #fórmula de cos 1-(x^2/2!)+(x^4/4!)...
    #reaproveita x^2 e apenas multiplica por x^2 para não recalcular tudo a todo
    #momento, e o mesmo vale pra fatorial
    for i in range(2,precisao,2):
        cos+=s*(p/f)
        s*=-1
        p*=base
        f*=(i+1)*(i+2)
        
    return cos
    
def sen(x,precisao=17):
    
    precisao=17 if precisao < 17 else precisao
    sen=1
    s=-1
    p=x**3
    base=x**2
    f=fat(3)
    
    #fórmula de sen 1-(x^3/3!)+(x^5/5!)...
    #reaproveita x^3 e apenas multiplica por x^2 para não recalcular tudo a todo
    #momento, e o mesmo vale pra fatorial
    for i in range(3,precisao,2):
        sen+=s*(p/f)
        s*=-1
        p*=base
        f*=(i+1)*(i+2)
        
    return sen
    
if __name__=="__main__":
  print(cos(2))
  print(cos(6))
