operacao = input("Selecione a operação desejada ( + - / * ): ")
num1 = float(input("Insira o primeiro valor: "))
num2 = float(input("Insira o segundo valor: "))

match operacao:
    case "*":
        resul = num1*num2
        print("Resultado: ", resul)
    case "/":
        resul = num1/num2
        print("Resultado: ", resul)
    case "+":
        resul = num1+num2
        print("Resultado: ", resul)
    case "-":
        resul = num1-num2
        print("Resultado: ", resul)