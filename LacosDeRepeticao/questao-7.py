total = 0
num = 0
qtd = 0

while num >= 0:
    num = int(input("Insira um número: "))
    total += num
    qtd += 1

media = total/qtd

print("Média: ", media)