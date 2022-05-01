print("_" * 70)
numero = int(input("Digite um número para saber o fatorial: "))
fatorial = 1

if numero < 0:
    print("Fatorial negativo não existe.")
else:
    while numero > 0:
        fatorial *= numero
        numero -= 1
    print(f"Fatorial: {fatorial}")
print("_" * 70)
