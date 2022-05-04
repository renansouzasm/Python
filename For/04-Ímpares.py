# Escreva um programa que mostre os números de um até o número digitado pelo usuário, 
# mas, apenas os númers ímpares;

print("_" * 70)
numero = int(input("Digite qualquer número ímpar: "))
for x in range(1, (numero + 2), 2):
    print(x)
print("_" * 70)
