class numero:
    
    #lista que define todos os caracteres usados nos numeros
    __lista=[str(i) for i in range(10)]
    for i in range(ord("A"),ord("Z")+1):
        __lista.append(chr(i))
        
    
    def __init__(self,valor=None,base=10):
        
        if 1 < base < 37:
            self.__base=base
            if valor == None:
                self.valor="0"
            else:
                self.valor=str(valor).upper()
        else:
            raise ValueError(f"Base {base} invalida")
    
    @property
    def base(self):
        return self.__base
      
    #conversor de base  
    @base.setter
    def base(self,nbase):
        if(1 < nbase < 37):
            valor=self.decimal(self.valor,self.base)
            temp=[]
            while valor != 0:
                temp.append(valor%nbase)
                valor=valor//nbase
            valor=temp[::-1]
            self.valor=self.__conversao_base(valor)
            self.__base=nbase
        else:
            raise ValueError(f"Base {nbase} invalida")
        
    @classmethod    
    def __conversao_base(cls,valor):
        return ''.join([cls.__lista[i] for i in valor])
        
        
    @classmethod
    def lista_posicao(cls,i):
        return cls.__lista[i]    
        
    @property
    def valor(self):
        return self.__valor
    
    @valor.setter
    def valor(self,valor):
        self.__valor=[i for i in str(valor)]

    @classmethod
    def __decimal(cls,valor,base):
        d=0
        for i,va in enumerate(valor[::-1]):
            d+=cls.__lista.index(va)*(base**i)
        return d
        
    #conversão de valor do objeto ou usando a classe
    def decimal(self,valor=None):
        if isinstance(self, numero):
            valor = self.valor if valor is None else valor
            return self.__decimal(valor,self.__base)
        return numero.__decimal(str(self).upper(),valor)

        
    def __str__(self):
        
        return "{"+f"valor:{''.join(self.__valor)},  base:{self.__base}"+"}"
    
 
if __name__=='__main__':       
    a=numero(11)
    print(a.decimal())
    print(a)
    
    print('Conversão de Base')
    a.base=2
    print(a.decimal())
    print(a)
    
    b=numero('a',36)
    print(b.decimal())
    print(numero.decimal(10,36))
    print(numero.decimal('0w',36))
