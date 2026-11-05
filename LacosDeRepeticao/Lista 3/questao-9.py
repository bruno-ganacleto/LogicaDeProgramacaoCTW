totalAdm = 0; qtdAdm = 0
totalOp = 0; qtdOp = 0
total = 0

for _ in range(10):
    setor = int(input("Informe o setor (1 para admnistrativo / 2 para operacional): "))
    salario = float(input("Insira o salário: "))

    if setor == 1:
        total += salario
        totalAdm += salario
        qtdAdm += 1
    
    if setor == 2:
        total += salario
        totalOp += salario
        qtdOp += 1

mediaAdm = totalAdm/qtdAdm
mediaOp = totalOp/qtdOp

print("\n---------- Setor Administrativo ----------")
print("Quantidade de Funcionários:", qtdAdm)
print("Média Salarial:", mediaAdm)

print("\n----------   Setor Operacional   ----------")
print("Quantidade de Funcionários:", qtdOp)
print("Média Salarial:", mediaOp)