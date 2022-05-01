# Programa que conta os pontos de acordo com a resposta;

pontos = 0
questao = 1
print("_" * 70)
while questao <= 3:
    resposta = input(f"Resposta da questão {questao}: ")
    if questao == 1 and resposta == "a":
        pontos += 1
    elif questao == 2 and resposta == "b":
        pontos += 1
    elif questao == 3 and resposta == "c":
        pontos += 1
    questao += 1
print(f"\nO aluno fez {pontos} ponto(s)")
print("_" * 70)
