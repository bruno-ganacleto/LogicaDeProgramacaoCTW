qtdExc = 0; qtdPes = 0; idadeExc = 0; qtdBom = 0; qtdReg = 0

for _ in range(40):
    idade = int(input("Informe a idade: "))
    nota = int(input("Informe a opinião do filme (1 - Péssimo / 2 - Regular / 3 - Bom / 4 - Excelente): "))

    if nota == 1:
        qtdPes += 1
    
    elif nota == 2:
        qtdReg += 1
    
    elif nota == 3:
        qtdBom += 1

    elif nota == 4:
        qtdExc += 1
        idadeExc += idade

if qtdExc == 0:
    mediaExc = None
    print("Não houve nenhuma avaliação excelente.")
else:
    mediaExc = idadeExc/qtdExc
    print("Idade média das pessoas que avaliaram como Excelente:", mediaExc)

qtdTotal = qtdPes + qtdReg + qtdBom + qtdExc
porcentagemBom = (qtdBom/40)*100


print("Quantidade de pessoas que avaliaram como Péssimo:", qtdPes)
print(f"Porcentagem de pessoas que avaliaram como Bom: {porcentagemBom:.2f}")