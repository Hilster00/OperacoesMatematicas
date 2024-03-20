def ackermann(m, n):
    if m == 0:
        return n + 1
    elif n == 0:
        return ackermann(m - 1, 1)
    else:
        return ackermann(m - 1, ackermann(m, n - 1))

# Testando a função
resultado = ackermann(3, 4)
print("O resultado da função de Ackermann para m=3 e n=4 é:", resultado)
