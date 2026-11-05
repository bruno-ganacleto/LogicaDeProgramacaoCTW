valor = int(input("Insira o valor do veículo: "))
combustivel = int(input("Digite 1 para Álcool, 2 para Gasolina ou 3 para Diesel: "))

match combustivel:
    case 1:
        valorFinal = valor*0.75
        print("Valor final: ", valorFinal)
    case 2:
        valorFinal = valor*0.79
        print("Valor final: ", valorFinal)
    case 3:
        valorFinal = valor*0.86
        print("\nValor final: ", valorFinal)