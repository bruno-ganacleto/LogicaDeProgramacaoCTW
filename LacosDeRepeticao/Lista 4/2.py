temp = float(input("Informe a temperatura do forno: "))
contador = 0

while temp < 1000:
    contador += 1
    if temp < 800: temp += 50
    elif temp >= 800: temp += 20

print(f"\nCiclos necessários: {contador}     Temperatura final: {temp}")