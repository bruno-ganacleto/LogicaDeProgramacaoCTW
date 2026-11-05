votos1 = int(input("Insira o número de votos do primeiro candidato: "))
votos2 = int(input("Insira o número de votos do segundo candidato: "))
votos3 = int(input("Insira o número de votos do terceiro candidato: "))


if votos1 > votos2 and votos1 > votos3:
    print("O primeiro candidato venceu!")
elif votos2 > votos1 and votos2> votos3:
    print("O segundo candidato venceu!")
elif votos3 > votos1 and votos3> votos2:
    print("O terceiro candidato venceu!")
elif votos1 == votos2 and votos1 == votos3:
    print("Empate! Todos os candidatos tem o mesmo número de votos.")
elif votos1 == votos2:
    print("Empate! O primeiro e o segundo candidato tem o mesmo número de votos.")
elif votos1 == votos3:
    print("Empate! O primeiro e o terceiro candidato tem o mesmo número de votos.")
else:
    print("Empate! O segundo e o terceiro candidato tem o mesmo número de votos.")
