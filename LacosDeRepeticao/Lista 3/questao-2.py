totalM = 0
totalH = 0

for _ in range(56):
    nome = input("Informe o nome: ")
    sexo = int(input("Insira 1 para Homem ou 2 para Mulher: "))

    if sexo == 1:
        print("\nNome:", nome, "\nSexo: Homem\n")
        totalH += 1

    if sexo == 2:
        print("\nNome:", nome, "\nSexo: Mulher\n")
        totalM += 1

print("Total de homens:", totalH, "\nTotal de mulheres:", totalM)