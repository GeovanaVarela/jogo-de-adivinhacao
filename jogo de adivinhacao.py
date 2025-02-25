print("**********")
print("Bem vindo ao jogo de adivinhação!")
print("**********")
numero_secreto=24
total_de_tentativas =3
rodada = 1

while(rodada<= total_de_tentativas):
    print("tentativa {} de {}". format(rodada, total_de_tentativas))

chute_str = input ("Digite o seu número:")
print("Voce digitou:", chute_str)
chute = int (chute_str)

acertou = chute == numero_secreto
maior = chute > numero_secreto
menor = chute < numero_secreto

    if (acertou):
       print("Parabéns voce acertou!")
    else:
        if(maior):
       print   ("O  seu chute é maior que o número secreto!")
        elif(menor):
        print ("O seu chute é menor que o número secreto!")

    rodada = rodada + 1

    print("Fim de jogo!")

