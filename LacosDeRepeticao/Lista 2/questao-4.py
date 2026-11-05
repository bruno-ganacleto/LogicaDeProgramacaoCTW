pontosP1 = 0
pontosP2 = 0

while True:
    res = int(input("Quem marcou o ponto? (1 para o jogador 1 / 2 para o jogador 2): "))
    
    if res == 1:
        pontosP1+=1
    if res == 2:
        pontosP2+=1

    if pontosP1 >= 21 and pontosP1 - pontosP2 >= 2:
        print("Jogador 1 venceu!")
        break
    
    if pontosP2 >= 21 and pontosP2 - pontosP1 >= 2:
        print("Jogador 2 venceu!")
        break

    print("Pontos do Jogador 1: ", pontosP1)
    print("Pontos do Jogador 2: ", pontosP2)
    print()