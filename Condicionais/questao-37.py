valor = int(input("Insira o valor que deseja sacar: "))

if valor == 0:
    print("Nada a receber.")

else:

    resto = valor

    notas100 = (valor-(valor%100))/100
    resto -= notas100*100
    notas50 = (resto-(resto%50))/50
    resto -= notas50*50
    notas20 = (resto-(resto%20))/20
    resto -= notas20*20
    notas10 = (resto-(resto%10))/10
    resto -= notas10*10
    notas5 = (resto-(resto%5))/5
    resto -= notas5*5

    print("Cédulas recebidas: ")

    if notas100 > 0:
        print(int(notas100), " notas de 100.")
    if notas50 > 0:
        print(int(notas50), " notas de 50.")
    if notas20 > 0:
        print(int(notas20), " notas de 20.")
    if notas10 > 0:
        print(int(notas10), " notas de 10.")
    if notas5 > 0:
        print(int(notas5),  " notas de 5.")