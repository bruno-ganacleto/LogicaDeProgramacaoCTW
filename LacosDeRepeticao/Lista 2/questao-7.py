canal4 = 0
canal5 = 0
canal7 = 0
canal12 = 0
numPessoas = 0

while True:
    pes = int(input("Insira o número de pessoas na casa: "))
    canal = int(input("Insira o número do canal: "))

    if canal != 0:

        match canal:
            case 4: canal4 += pes
            case 5: canal5 += pes
            case 7: canal7 += pes
            case 12: canal12 += pes

    else:
        total = canal4 + canal5 + canal7 + canal12
        break

porcentagem4 = (canal4/total)*100
porcentagem5 = (canal5/total)*100
porcentagem7 = (canal7/total)*100
porcentagem12 = (canal12/total)*100

print(f"Canal 4: {porcentagem4:.2f}% da audiência.")
print(f"Canal 5: {porcentagem5:.2f}% da audiência.")
print(f"Canal 7: {porcentagem7:.2f}% da audiência.")
print(f"Canal 12: {porcentagem12:.2f}% da audiência.")