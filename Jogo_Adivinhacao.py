import random

print("°°°°°°°°°°°°°°°°°")
print("Bem-Vindo ao Jogo\n")
print("Acerte o número para ganhar!\n")
print("°°°°°°°°°°°°°°°°°")

numero_secreto = round(random.randrange(50,80))
total_tentativas = 5
pontos = 100

print(numero_secreto)

print("Qual é o nível de dificuldade desejado?\n")
print("(1) Fácil (2) Moderado (3) Difícil\n")

nivel = int(input("Digite o nível desejado:\n "))

if(nivel == 1):
    total_tentativas = 20
elif(nivel == 2):
    total_tentativas = 10
else:
    total_tentativas = 5

for rodadas in range (1, total_tentativas + 1):
    print(f"Tentativa {rodadas} de {total_tentativas}\n")
    chute = int(input("Digite um número entre 50 e 80: \n"))
    

    if(chute < 50 or chute > 80):
        print("Você deve digitar um número entre 50 e 80!")
        continue 

    acertou = numero_secreto == chute
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto

    print(f"Você digitou {chute}\n")

    if(acertou):
        print(f"Você acertou! Sua pontuação foi {pontos} pontos\n")
        print("°°°°°°°°°°°")
        print("Parabéns! Fim de Jogo")
        print("°°°°°°°°°°°")
        break
    else:
        pontos_perdidos = abs(numero_secreto - chute)
        pontos -= pontos_perdidos

        if pontos < 0:
            pontos = 0

        if(chute_maior):
            print("Humm... Seu chute foi maior que o número surpresa. Tente novamente!\n")
        elif(chute_menor):
            print("Humm... Seu chute foi menor que o número surpresa. Tente novamente!\n")

        print(f"Você perdeu {pontos_perdidos} pontos. Pontuação restante: {pontos}\n")

if pontos > 0:
    print("Fim de jogo. Essa foi sua pontuação:", pontos)
else:
    print("Fim de jogo. Você não pontuou.")
