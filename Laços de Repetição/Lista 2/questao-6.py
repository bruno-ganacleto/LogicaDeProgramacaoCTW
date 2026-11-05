listaPares = ""
listaImpares = ""
somaPositivos = 0
somaNegativos = 0
somaTotal = 0

while True:
    resposta = int(input("Insira um número: "))
    if resposta != 0:
        
        if resposta >0:
            somaPositivos += resposta
        else:
            somaNegativos += resposta
        
        if resposta%2 == 0:
            listaPares += str(resposta)
            listaPares += " "
        else:
            listaImpares += str(resposta)
            listaImpares += " "
    
    else:
        somaTotal = somaNegativos + somaPositivos
        break

print("Lista de números pares:", listaPares)
print("Lista de números ímpares:", listaImpares)
print("Soma dos números positivos:", somaPositivos)
print("Soma dos números negativos:", somaNegativos)
print("Soma total:", somaTotal)