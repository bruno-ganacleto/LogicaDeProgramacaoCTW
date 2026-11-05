num = int(input("Informe o número inicial: "))
intervalo = int(input("Informe o intervalo: "))
atual = num+intervalo

while atual > 0:
    atual -= intervalo
    if atual > 0:
        print(atual)
    else:
        print(0)
        break