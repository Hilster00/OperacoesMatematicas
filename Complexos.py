while True:
    a=int(input("Digite um número:"))
    if a == 0 :
        break
    print(f"{a}^2 == {a*a}")
    print(f"{a}^(1/2) == {abs(a)**0.5}",end="")
    if a < 0:
        print("i",end="")
    print()
