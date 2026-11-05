multTres = 0
somaPares = 0

for _ in range(50):
    numero = int(input("Digite um número: "))

    if numero%3 == 0:
        multTres += 1
    if numero%2 == 0:
        somaPares += numero

print("Quantidade de números múltiplos de três:", multTres)
print("Soma dos valores pares:", somaPares)

