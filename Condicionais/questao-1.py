preco = int(input("Insira o preço do produto: "))
desconto = preco * 0.9
parcelaSemJuros = preco/5
parcelaComJuros = (preco*1.2)/10

print("Valor à vista: ", desconto)
print("Valor da prestação 5x sem juros: ", parcelaSemJuros)
print("Valor da prestação 10x com juros: ", parcelaComJuros)