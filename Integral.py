from scipy.integrate import quad

# Função que queremos integrar
def f(x):
    return x**2

# Limites de integração
a = 0
b = 1

# Calculando a integral definida de f(x) de a até b
resultado, erro = quad(f, a, b)

print("O resultado da integral é:", resultado)
print("O erro estimado é:", erro)
