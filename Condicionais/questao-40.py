num = int(input("Insira um número inteiro: "))

if num == 0:
    print("O número inserido é igual a zero!")
else:
    if num > 0:
        print("Seu número é positivo")
    else:
        print("Seu número é negativo")
    if num%2 == 0:
        print("Seu número é par")
    else:
        print("Seu número é impar")