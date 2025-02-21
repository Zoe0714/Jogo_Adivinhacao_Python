print("*****************")
print("Bem-Vindo ao Jogo\n")
print("Acerte o número para ganhar!\n")
print("Dica: É divisível por 7.\n")
print("*****************")

chute = int(input("Digite o seu número: \n"))

print(f"Você digitou {chute}\n")

numero_secreto = 77
acertou = numero_secreto == chute
chute_maior = chute > numero_secreto
chute_menor = chute < numero_secreto

if(acertou):
    print("Você acertou!\n")
    print("***********")
    print("Parabéns! Fim de Jogo")
    print("***********")
else:
    if(chute_maior):
        print("Humm... Seu chute foi maior que o número surpresa. Tente novamente!\n")
    elif(chute_menor):
        print("Humm... Seu chute foi menor que o número surpresa. Tente novamente!\n")
  