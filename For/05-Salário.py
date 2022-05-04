# Um funcionário de uma empresa recebe, anualmente, aumento salárial. Sabe-se que: 
# Esse funcionário foi contratado em 2005, com salário inicial de R$1.000,00. 
# Em 2006, ele recebeu um aumento de 1,5% sobre seu salário inicial. 
# A partir de 2007, os aumentos salariais sempre corresponderam ao dobro do percentual do ano anterior. 
# Faça um programa que determine o salário atual desse funcionário

salario = 1000
x = 1.5

print("_" * 70)
for ano in range(2005, 2023):
    print(f"Ano %.0f: Salário = %.2f" % (ano, salario))
    salario += salario * (x/100)
    x *= 2
print("_" * 70)
