import time

numMaquina = ((int(time.time()*1001))%50)+1
print(numMaquina)

tentativas = 5

while tentativas > 0:
    print("\nTentativas restantes: ", tentativas)
    numUsuario = int(input("Insira um número: "))

    if numUsuario == numMaquina:
        print("Parabéns! Você acertou o número!")
        break
    elif numUsuario < numMaquina:
        print("O número sorteado é maior que", numUsuario)
    elif numUsuario > numMaquina:
        print("O número sorteado é menor que", numUsuario)
    tentativas -= 1

    if tentativas == 0:
        print("\nVocê perdeu! O número era: ", numMaquina)