print("_" * 70)
numero = int(input("Digite um número para saber o fatorial: "))
fatorial = 1

for x in range(numero):
    fatorial *= numero
    numero -= 1
print(f"Fatorial: {fatorial}")
print("_" * 70)
