valor = 1
negativos = 0
while valor != 0:
    valor = int(input("Insira um valor: "))
    if valor < 0:
        negativos += 1
print(negativos, "dos valores digitados são negativos!")