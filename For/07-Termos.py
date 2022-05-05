# Programa que apresenta o número de termos que o usuário solicitar;

print("_" * 70)
numero = int(input("Solicite o número de termos que devem ser apresentados: "))
termo2 = 2
termo3 = 7
termo4 = 3

for x in range(numero):
    print(termo2)
    termo2 *= 2
    print(termo3)
    termo3 *= 3
    print(termo4)
    termo4 *= 4
print("_" * 70)
