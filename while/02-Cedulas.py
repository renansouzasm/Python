# Programa que le um valor e imprime a quantidade de cédulas para pagar o valor. 
# Para simplificar, vamos trabalhar apenas com valores inteiros 
# e com cédulas de R$50, R$20, R$10, R$5 e R$1;

print("_" * 70)
valor = int(input("Digite o valor a pagar: R$"))
cedulas = 0
atual = 50

while True:
    if valor >= atual:
        valor -= atual
        cedulas += 1
    else:
        if cedulas != 0:
            print(f"{cedulas} Cédula(s) de R${atual}")
        if valor == 0:
            break
        if atual == 50:
            atual = 20
        elif atual == 20:
            atual = 10
        elif atual == 10:
            atual = 5
        elif atual == 5:
            atual = 1
        cedulas = 0
print("_" * 70)
