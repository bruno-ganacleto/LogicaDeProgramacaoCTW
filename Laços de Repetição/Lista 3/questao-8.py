valor = float(input("Insira o valor da dívida: "))
valorJuros = 0
qtdParcelas = 1

print("Valor da Dívida - Valor dos Juros - Qtd de Parcelas - Valor da Parcela")

for i in range(5):
    valorParcela = (valor+(valor*(valorJuros/100)))/qtdParcelas
    print(f"R${valor}","              ", valorJuros,"                 ", qtdParcelas,"         ", f"R${valorParcela:.2f}")

    if i == 1:
        valorJuros += 10
        qtdParcelas += 2
    else:
        valorJuros += 5
        qtdParcelas += 3
