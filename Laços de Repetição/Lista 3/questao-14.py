temperatura = 0
tempMedias = 0
tempDiv5 = 0
tempDiv10 = 0
while temperatura != 999:
    temperatura = float(input("Informe a temperatura: "))

    if temperatura > 20 and temperatura < 80:
        tempMedias += 1
    
    if temperatura%5 == 0:
        tempDiv5 += 1

    if temperatura%10 != 0:
        tempDiv10 += 1

print("Temperaturas registradas entre 20 e 80:", tempMedias)
print("Temperaturas registradas multiplas de 5:", tempDiv5)
print("Temperaturas registradas que não são multiplas de 10:", tempDiv10)