'''
4- Faça um programa em Py que alimente um vetor, com um número de posições definidas pelo usuário.
Este vetor deverá armazenar um conjunto de nomes em diferentes posições.
Crie um mecanismo para alimentar elementos no vetor e pesquisar por um valor existente.
 ======== MENU ======== 
1) Cadastrar nome 
2) Pesquisar nome 
3) Listar todos os nome 
0) Sair do programa 
——————– 
Digite sua escolha:
'''

nomes = []
escolha = None
''
while True:
    print("========== MENU ==========")
    print("1) Cadastrar nome")
    print("2) Pesquisar nome")
    print("3) Listar todos os nomes")
    print("0) Sair do programa")
    print("—————————————————————")
    escolha = int(input("Digite sua escolha: "))

    match escolha:
        case 0:
            break
        case 1:
            nomes.append(input("Digite um nome: "))
            print("")
        case 2:
            pesquisa = input("Digite um nome: ")
            if pesquisa in nomes:
                print(f"Nome encontrado na posição {nomes.index(pesquisa)} da lista.\n")
            else:
                print("Nome não encontrado\n")
        case 3:
            print("Lista de nomes:\n", nomes,"\n")