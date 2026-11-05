num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
num3 = int(input("Digite o terceiro número: ")) #fica a dica

maiorNum = num1
menorNum = num1

if maiorNum < num2:
    maiorNum = num2
if maiorNum < num3:
    maiorNum = num3
if menorNum > num2:
    menorNum = num2
if menorNum > num3:
    menorNum = num3
if num1 != maiorNum and num1 != menorNum:
    medNum = num1
if num2 != maiorNum and num2 != menorNum:
    medNum = num2
if num3 != maiorNum and num3 != menorNum:
    medNum = num3

print("Ordem crescente: ", menorNum, medNum, maiorNum)