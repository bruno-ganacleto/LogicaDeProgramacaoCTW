cod = 1
qtdNP = 0
qtdP = 0
qtdV = 0
qtdHP = 0
qtdLUD = 0

while cod != 0:
    cod = int(input("Informe o código do produto: "))

    if cod == 0:
        print("Quantidade de produtos cadastrados:")
        print("Não-Perecíveis:", qtdNP)
        print("Perecíveis:", qtdP)
        print("Vestuário:", qtdV)
        print("Higiene Pessoal:", qtdHP)
        print("Limpeza e Utensílios:", qtdLUD)
        break

    if cod == 1:
        print("Alimento Não-Perecível\n")
        qtdP += 1
    elif cod >=2 and cod <=4 :
        print("Alimento Perecível\n")
        qtdNP += 1
    elif cod == 5 or cod == 6 :
        print("Vestuário\n")
        qtdV += 1
    elif cod == 7:
        print("Higiene Pessoal\n")
        qtdHP += 1
    elif cod >=8 and cod <=15 :
        print("Limpeza e Utensílios Domésticos\n")
        qtdLUD += 1
    else:
        print("Código Inválido\n")