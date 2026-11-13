'''
2- Faça um programa em Py que leia um vetor de seis elementos numéricos inteiros, calcule e mostre: 
a) A quantidade de números pares 
b) Quais os números pares 
c) A quantidade de números ímpares 
d) Quais os números ímpares
'''
qtd = 6
numeros = []
pares = []
impares = []
qtd_pares = 0
qtd_impares = 0

for i in range(qtd):
    numeros.append(int(input("Insira um número inteiro: ")))
    if numeros[i]%2 == 0:
        pares.append(numeros[i])
        qtd_pares += 1
    else:
        impares.append(numeros[i])
        qtd_impares += 1

print(f"\nQuantidade de números pares: {qtd_pares}\nPares inseridos: ", end="")
for i in range(qtd_pares):
    print(f"{pares[i]} ", end="")

print(f"\n\nQuantidade de números impares: {qtd_impares}\nImpares inseridos: ", end="")
for i in range(qtd_impares):
    print(f"{impares[i]} ", end="")