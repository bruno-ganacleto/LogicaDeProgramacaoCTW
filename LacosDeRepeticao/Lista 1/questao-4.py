salario = 0
filhos = 0
filhosTotal = 0
salariosTotal = 0
salario100 = -1
maiorSalario = 0
contador = -1

while salario >= 0:
    contador += 1
    salariosTotal += salario
    filhosTotal += filhos
    if salario <= 100:
        salario100 += 1
    if salario > maiorSalario:
        maiorSalario = salario
    salario = float(input("Insira o salário: "))
    if not salario <0:
        filhos = int(input("Quantidade de filhos: "))

mediaSalario = salariosTotal/contador
mediaFilhos = filhosTotal/contador
percentualSalarios100 = (salario100*100)/contador

print("\nMédia salarial da população: ", mediaSalario)
print("Média de filhos: ", mediaFilhos)
print("Maior salário: ", maiorSalario)
print("Percentual de pessoas com o salário até R$100: ", percentualSalarios100)