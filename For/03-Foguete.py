# Faça um programa para escrever a contagem regressiva do lançamento de um foguete.
# O programa deve imprimir 10, 9, 8, ....1, 0 e Fogo! na tela;

a = 10
print("_" * 70)

for x in range(11):
    print(a)
    a -= 1
print("Fogo!")
print("_" * 70)
