preco100 = 1.2
preco101 = 1.3
preco102 = 1.5
preco103 = 1.2
preco104 = 1.3
preco105 = 1
precoPedido = 0

while True:
    pedido = int(input("Insira o código do pedido (Digite 0 para encerrar): "))
    if pedido == 0:
        print(f"Preço total: R${precoPedido:.2f}")
        break
    qtd = int(input("Insira a quantidade: "))

    match pedido:
        case 100:
            precoPedido += qtd*1.2
            print(f"Cachorro Quente - Preço do Pedido: R${qtd*1.2:.2f}")
            print()
        case 101:
            precoPedido += qtd*1.3
            print(f"Bauru Simples - Preço do Pedido: R${qtd*1.3:.2f}")
            print()
        case 102:
            precoPedido += qtd*1.5
            print(f"Bauru com Ovo - Preço do Pedido: R${qtd*1.5:.2f}")
            print()
        case 103:
            precoPedido += qtd*1.2
            print(f"Hambúrguer - Preço do Pedido: R${qtd*1.2:.2f}")
            print()
        case 104:
            precoPedido += qtd*1.3
            print(f"Cheeseburguer - Preço do Pedido: R${qtd*1.3:.2f}")
            print()
        case 105:
            precoPedido += qtd
            print(f"Refrigerante - Preço do Pedido: R${qtd:.2f}")
            print()
        case _:
            print("Código Inválido")