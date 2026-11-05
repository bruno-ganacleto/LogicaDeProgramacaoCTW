qtdRegular = 0
qtdBom = 0
idadeOtimo = 0
qtdOtimo = 0

for _ in range(15):
    idade = int(input("Informe a idade: "))
    nota = int(input("Informe a opinião do filme (3 - Ótimo / 2 - Bom / 1 - Regular): "))

    if nota == 3:
        idadeOtimo += idade
        qtdOtimo += 1
    
    if nota == 1:
        qtdRegular += 1
    
    if nota == 2:
        qtdBom += 1

mediaOtimo = idadeOtimo/qtdOtimo
qtdTotal = qtdOtimo + qtdBom + qtdRegular
porcentagemBom = (qtdBom/15)*100

print("Idade média das pessoas que avaliaram como Ótimo:", mediaOtimo)
print("Quantidade de pessoas que avaliaram como Regular:", qtdRegular)
print(f"Porcentagem de pessoas que avaliaram como Bom: {porcentagemBom:.2f}")
