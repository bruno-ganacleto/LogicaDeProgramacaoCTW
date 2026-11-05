dia = int(input("Informe o dia da semana ( 1 para Domingo... 7 para Sábado ): "))

match dia:
    case 1:
        print("\nSem Trabalho")
    case 7:
        print("\nTurno Reduzido")
    case 2|3|4|5|6:
        print("Turno Normal")
    case _:
        print("Valor inválido")