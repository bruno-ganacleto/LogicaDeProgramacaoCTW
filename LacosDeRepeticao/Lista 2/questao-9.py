for _ in range(150):
    nome = input("Insira o nome do cliente: ")
    total = int(input("Informe o valor gasto em compras: "))
    if total < 500000:
        bonus = total*1.1
    else:
        bonus = total*1.15

    print("Cliente:", nome, f"\nBonus: R${bonus:.2f}")