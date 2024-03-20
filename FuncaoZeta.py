import sympy

def zeta_function(s, terms=100):
    # Definindo a variável 'n'
    n = sympy.symbols('n')

    # Definindo a soma da série para a função Zeta de Riemann
    series_sum = sympy.Sum(1 / (n ** s), (n, 1, sympy.oo))

    # Avaliando a série com um número finito de termos
    series_evaluated = series_sum.doit().evalf(n=terms)

    return series_evaluated

# Testando a função
s_value = 2  # Valor de s
terms_count = 100  # Número de termos na série
resultado_zeta = zeta_function(s_value, terms_count)
print("O valor da função Zeta de Riemann para s =", s_value, "com", terms_count, "termos é:", resultado_zeta)
