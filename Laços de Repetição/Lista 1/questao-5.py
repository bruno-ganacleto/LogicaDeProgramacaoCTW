total = 0
qtd = 0
num = 1

while num!=0:
    num = int(input("Insira um número: "))
    if num%2 == 0 and num != 0:
        total += num
        qtd += 1

media = total/qtd
print("Media dos números pares: ", media)