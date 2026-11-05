capitalInicial = int(input("Insira o valor do capital inicial: "))
taxaDeJuros = int(input("Insira a porcentagem da taxa de juros mensal: "))
tempoDeAplicação = int(input("Insira o tempo de aplicação: "))

valorFinal = capitalInicial * (1+taxaDeJuros/100)**tempoDeAplicação
print("Montante final: ", valorFinal)