num = int(input("Digite um número inteiro positivo: "))
if num%2 != 0:
    num -= 1
    
for contador in range(num):
    if (num - (contador*2)) >= 0:
        print(num - (contador*2))