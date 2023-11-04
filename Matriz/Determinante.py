def determinante(matriz=[1]):
    tamanho=len(matriz)
    if tamanho == 1:
        return matriz[0][0]
    det=0
    for i in range(tamanho-1):
        psm,psb = i,(tamanho-1)-i
        det_soma=det_sub=1
        for j in range(tamanho):
            det_soma*=matriz[j][psm]#produto diagonais positivas
            det_sub*=matriz[j][psb]#produto diagonais negativas
            psm+=1
            psb-=1
            if psm == tamanho:
                psm=0
            if psb == -1:
                psb=tamanho-1
        det+=(det_soma-det_sub)
    return det

if __name__=="__main__":
    matriz=[
        [1,2,3],
        [3,2,1],
        [3,0,3]
    ]
    #exemplo de como utilizar
    print(determinante(matriz))
