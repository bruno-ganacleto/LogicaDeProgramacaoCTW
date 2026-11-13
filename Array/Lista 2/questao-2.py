'''
2- Utilizando vetores, crie um programa que organize uma quantidade qualquer de números
inteiros fornecidos pelo usuário da seguinte forma: primeiro os números pares em ordem
crescente e depois os números ímpares em ordem decrescente. 
'''

numeros = []
pares = []
impares = []

while True:
    res = (input("Digite um número ou aperte enter para finalizar: "))
    if res == "":
        break
    else:
        res = int(res)
        if res%2 == 0: pares.append(res)
        else: impares.append(res)
        numeros.append(res)

resposta = []
while pares != []:    
    for i in range(len(pares)):
        if pares[i] == min(pares):
            resposta.append(pares[i])
            pares.remove(pares[i])
            break

while impares != []:        
    for i in range(len(impares)):
        if impares[i] == max(impares):
            resposta.append(impares[i])
            impares.remove(impares[i])
            break

print(resposta)