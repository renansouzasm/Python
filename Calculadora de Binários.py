print("_" * 70)
try:
    N1 = str(input("Insira o valor do primeiro Binário: "))
    N2 = str(input("Insira o valor do segundo Binário: "))

    soma = bin(int(N1, 2) + int(N2, 2))
    sub = bin(int(N1, 2) - int(N2, 2))
    mult = bin(int(N1, 2) * int(N2, 2))
    div = bin(int(N1, 2) // int(N2, 2))

    print("""(1) Soma
    (2) Subtração
    (3) Multiplicação
    (4) Divisão""")
    opção = int(input("Escolha a operação desejada de 1 a 4: "))

    if opção == 1:
        print(soma[2:])
    elif opção == 2:
        print(sub[2:])
    elif opção == 3:
        print(mult[2:])
    elif (N1 != 0 and N2 !=0) and (opção == 4):
        print(div[2:])
    else:
        print("Digite um número de 1 a 4: ")

except ZeroDivisionError:
    print("ERROR TENTE NOVAMENTE")
print("_" * 70)
