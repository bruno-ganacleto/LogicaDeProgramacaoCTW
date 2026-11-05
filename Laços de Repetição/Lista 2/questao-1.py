maiorIndice = 0
menorIndice = 0
cMenorIndice = 0
cMaiorIndice = 0
totalVeicSC = 0
totalVeicPR = 0
totalVeicRS = 0
totalAciSC = 0
totalAciPR = 0
totalAciRS = 0

for i in range(12):
    codCidade = int(input("Informe o código da cidade: "))
    numVeiculos = int(input("Informe o número de veículos de passeio: "))
    numAcidentes = int(input("Informe o número de acidentes: "))

    if codCidade < 20:
        totalVeicSC += numVeiculos
        totalAciSC += numAcidentes

    elif codCidade < 30:
        totalVeicRS += numVeiculos
        totalAciRS += numAcidentes

    else:
        totalVeicPR += numVeiculos
        totalAciPR += numAcidentes

    if i == 0:
        menorIndice = numAcidentes
        maiorIndice = numAcidentes
        cMenorIndice = codCidade
        cMaiorIndice = codCidade
    
    if menorIndice > numAcidentes:
        menorIndice = numAcidentes
        cMenorIndice = codCidade

    if maiorIndice < numAcidentes:
        maiorIndice = numAcidentes
        cMaiorIndice = codCidade

print("CIDADE COM MAIOR NÚMERO DE ACIDENTES: ", cMaiorIndice)
print("CIDADE COM MENOR NÚMERO DE ACIDENTES: ", cMenorIndice)
print("\nMÉDIA DE VEICULOS POR CIDADE EM SC: ", totalVeicSC/4)
print("MÉDIA DE VEICULOS POR CIDADE EM RS: ", totalVeicRS/4)
print("MÉDIA DE VEICULOS POR CIDADE EM PR: ", totalVeicPR/4)
print("\nMÉDIA DE ACIDENTES COM VÍTIMAS EM SC: ", totalAciSC/4)
print("MÉDIA DE ACIDENTES COM VÍTIMAS EM RS: ", totalAciRS/4)
print("MÉDIA DE ACIDENTES COM VÍTIMAS EM PR: ", totalAciPR/4)