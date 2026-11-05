num = int(input("Insira um número inteiro: "))
col = 0

for i in range(num):
    col += 1
    lin = 0
    for i in range(col):
        lin += 1
        print(lin, "", end="")
    print()