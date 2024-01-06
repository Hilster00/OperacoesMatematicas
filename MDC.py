from functools import reduce

primos=[2,3] 
def mdc(n,m):
    lista_mdc=[]
    for i in retornar_primos(n if n>m else m):
        while (n%i == 0) or (m%i == 0):
            if (n%i == 0) and (m%i == 0):
                lista_mdc.append(i)
            n=n if n%i != 0 else n/i
            m=m if m%i != 0 else m/i
    return  reduce( lambda prod, i: i*prod, lista_mdc, 1)
    
