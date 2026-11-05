totalPrazo = 0
totalAVista = 0
totalCompras = 0
prestacao = 0

for _ in range(15):
    codigo = int(input("Insira o código (1 à vista / 2 à prazo): "))
    valor = float(input("\nInsira o valor da transação: "))
    print()

    totalCompras += valor
    if codigo == 1:
        totalAVista += valor

    if codigo == 2:
        totalPrazo += valor
        prestacao = totalPrazo/3
    
print("Valor total das compras à vista:", totalAVista)
print("Valor total das compras à prazo:", totalPrazo)
print(f"Valor da primeira prestação das compras à prazo: R${prestacao:.2f}")