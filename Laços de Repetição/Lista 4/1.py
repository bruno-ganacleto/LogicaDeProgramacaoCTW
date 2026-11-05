producao_total = 0; estacao_falha = 0; pecas_2 = 0; pecas_3 = 0; pecas_4 = 0; pecas_5 = 0
contador1 = 0; contador2 = 0; contador3 = 0; contador4 = 0; contador5 = 0
contador = 0

meta = int(input("Informe a meta diária: "))
pecas_1 = int(input("Informe a quantidade de peças recebidas: "))
print("")
processamento_1 = int(input("Informe o processamento da primeira estação: "))
processamento_2 = int(input("Informe o processamento da segunda estação: "))
processamento_3 = int(input("Informe o processamento da terceira estação: "))
processamento_4 = int(input("Informe o processamento da quarta estação: "))
processamento_5 = int(input("Informe o processamento da quinta estação: "))
print("")

while producao_total < meta:
    contador += 1

    # Processamento Máquina 1
    if pecas_1 > 0:

        # Capacidade de Processamento
        if pecas_1 > processamento_1 * 0.9:
            contador1 += 1
        else:
            contador1 = 0
        
        if contador1 == 5:
            estacao_falha = 1
            break
        
        if pecas_1 - processamento_1 >= 0:    
            pecas_2 += pecas_1 - (pecas_1 - processamento_1)
            pecas_1 -= processamento_1
        else:
            pecas_2 += pecas_1
            pecas_1 -= processamento_1 + (pecas_1 - processamento_1)


    # Processamento Máquina 2
    if pecas_2 > 0 and contador > 1:

        # Capacidade de Processamento
        if pecas_2 > processamento_2 * 0.9:
            contador2 += 1
        else:
            contador2 = 0
        
        if contador2 == 5:
            estacao_falha = 2
            break

        if pecas_2 - processamento_2 >= 0:    
            pecas_3 += pecas_2 - (pecas_2 - processamento_2)
            pecas_2 -= processamento_2
        else:
            pecas_3 += pecas_2
            pecas_2 -= processamento_2 + (pecas_2 - processamento_2)


    # Processamento Máquina 3
    if pecas_3 > 0 and contador > 2:

        # Capacidade de Processamento
        if pecas_3 > processamento_3 * 0.9:
            contador3 += 1
        else:
            contador3 = 0
        
        if contador3 == 5:
            estacao_falha = 3
            break

        if pecas_3 - processamento_3 >= 0:    
            pecas_4 += pecas_3 - (pecas_3 - processamento_3)
            pecas_3 -= processamento_3
        else:
            pecas_4 += pecas_3
            pecas_3 -= processamento_3 + (pecas_3 - processamento_3)
    

    # Processamento Máquina 4
    if pecas_4 > 0 and contador > 3:

        # Capacidade de Processamento
        if pecas_4 > processamento_4 * 0.9:
            contador4 += 1
        else:
            contador4 = 0
        
        if contador4 == 5:
            estacao_falha = 4
            break

        if pecas_4 - processamento_4 >= 0:    
            pecas_5 += pecas_4 - (pecas_4 - processamento_4)
            pecas_4 -= processamento_4
        else:
            pecas_5 += pecas_4
            pecas_4 -= processamento_4 + (pecas_4 - processamento_4)
    

    # Processamento Máquina 5
    if pecas_5 > 0 and contador > 4:

        # Capacidade de Processamento
        if pecas_5 > processamento_5 * 0.9:
            contador5 += 1
        else:
            contador5 = 0
        
        if contador5 == 5:
            estacao_falha = 5
            break
        
        if pecas_5 - processamento_5 >= 0:    
            producao_total += pecas_5 - (pecas_5 - processamento_5)
            pecas_5 -= processamento_5
        else:
            producao_total += pecas_5
            pecas_5 -= processamento_5 + (pecas_5 - processamento_5)

    print("Ciclo:", contador)
    print("Peças restantes na primeira máquina:", pecas_1)
    print("Peças restantes na segunda máquina:", pecas_2)
    print("Peças restantes na terceira máquina:", pecas_3)
    print("Peças restantes na quarta máquina:", pecas_4)
    print("Peças restantes na quinta máquina:", pecas_5)
    print("Peças finalizadas:", producao_total)
    print("")
        
match estacao_falha:
    case 1: print(f"Processamento Interrompido! Estação Quebrada: 1\nProdução Total: {producao_total}          Ciclos Executados: {contador}")
    case 2: print(f"Processamento Interrompido! Estação Quebrada: 2\nProdução Total: {producao_total}          Ciclos Executados: {contador}")
    case 3: print(f"Processamento Interrompido! Estação Quebrada: 3\nProdução Total: {producao_total}          Ciclos Executados: {contador}")
    case 4: print(f"Processamento Interrompido! Estação Quebrada: 4\nProdução Total: {producao_total}          Ciclos Executados: {contador}")
    case 5: print(f"Processamento Interrompido! Estação Quebrada: 5\nProdução Total: {producao_total}          Ciclos Executados: {contador}")
    case _: print(f"Processamento Concluído!\nProdução Total: {producao_total}          Ciclos Executados: {contador}")