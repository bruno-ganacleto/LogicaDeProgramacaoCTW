preco = float(input("Insira o valor do carro: "))
parcelas = int(input("Selecione a quantidade de parcelas (6, 12, 18, 24, 30, 36, 42, 48, 54, 60 ou 0 para pagamento à vista): "))
precoFinal = 0

match parcelas:
    case 0: precoFinal = preco*0.8
    case 6: precoFinal = preco*1.03
    case 12: precoFinal = preco*1.06
    case 18: precoFinal = preco*1.09
    case 24: precoFinal = preco*1.12
    case 30: precoFinal = preco*1.15
    case 36: precoFinal = preco*1.18
    case 42: precoFinal = preco*1.21
    case 48: precoFinal = preco*1.24
    case 54: precoFinal = preco*1.27
    case 60: precoFinal = preco*1.3

precoParcela = precoFinal/parcelas

print(f"Preço final: R${precoFinal:.2f}")
if parcelas != 0:
    print("Quantidade de Parcelas: ", parcelas)
    print(f"Valor da parcela: R${precoParcela:.2f}")  