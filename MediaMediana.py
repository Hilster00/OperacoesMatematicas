entrada =[ float(i) for i in input("Digite uma sequência de números separados por uma vírgula:").split(",")]
entrada.sort()
quantidade = len(entrada)
mediana = entrada[quantidade//2] if quantidade%2 == 1 else (entrada[quantidade//2] + entrada[quantidade//2-1])/2
print(f"Média: {sum(entrada)/quantidade:.1f}")
print(f"Mediana: {mediana}")

