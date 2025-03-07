print("°°°°°°°°°°°°°°°°°")
print("Bem-Vindo ao Jogo\n")
print("Acerte o número para ganhar!\n")
print("Dica: É divisível por 7 e maior que 4 multiplicando 10.\n")
print("°°°°°°°°°°°°°°°°°")

numero_secreto = 77
total_tentativas = 9

for rodadas in range (1,total_tentativas):
    print(f"Tentativa {rodadas} de 8")
    chute = int(input("Digite o seu número: \n"))

    acertou = numero_secreto == chute
    chute_maior = chute > numero_secreto
    chute_menor = chute < numero_secreto
    chute_proximo = chute 

    print(f"Você digitou {chute}\n")

    total_tentativas = total_tentativas - 1

    if(acertou):
        print("Você acertou!\n")
        print("°°°°°°°°°°°")
        print("Parabéns! Fim de Jogo")
        print("°°°°°°°°°°°")
        break

    else:
        if(chute_maior):
            print("Humm... Seu chute foi maior que o número surpresa. Tente novamente!\n")
        elif(chute_menor):
            print("Humm... Seu chute foi menor que o número surpresa. Tente novamente!\n")