num = int(input("Escreva um valor: "))

match num:
    case 7 | 1:
        print("Final de Semana")
    case 2 | 3 | 4 | 5 | 6:
        print("Dia de Semana")
    case _:
        print("Opção Inválida")