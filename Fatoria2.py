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

if __name__=="__main__":
  print(fat(6))
  print(f)
  print(fat(5))
  print(f)
  print(fat(7))
  print(f)
