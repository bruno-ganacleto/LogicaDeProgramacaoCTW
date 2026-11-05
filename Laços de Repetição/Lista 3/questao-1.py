contador = 0

for _ in range(80):
    numero = int(input("Insira um número: "))
    if numero >= 10 and numero <= 150:
        contador += 1
print(contador, " números estão entre 10 e 150.")