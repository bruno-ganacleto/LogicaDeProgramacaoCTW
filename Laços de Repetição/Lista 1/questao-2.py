num = int(input("Informe o número que a tabuada será calculada: "))
lim = int(input("Informe qual número será o limite da tabuada: "))
contador = 1

#while contador*num < lim:
#    print(contador*num)
#    contador += 1

for contador in range(1, lim+1):
    print(num," * ",contador," = ",num*contador)