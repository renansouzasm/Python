# Programa que calcula a média aritimética de cinco notas digitadas pelo usuário;

media = 0
x = 1
print("_" * 70)
while x <= 5:
    nota = float(input(f"Entre com sua {x}° nota: "))
    media += nota
    x += 1

media /= 5
if media >= 7:
    print("\n Média Final: %.1f APROVADO(a)" % media)
elif media < 4:
    print("\n Média Final: %.1f REPROVADO(a)" % media)
else:
    print("\n Média Final: %.1f EXAME" % media)
    nota_exame = 7 - media
    print("A nota que você precisa tirar para passar é: %.1f" % nota_exame)
print("_" * 70)
