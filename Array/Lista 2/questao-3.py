'''
3- Faça um programa que leia e monte dois vetores de números inteiros com 20 números cada.
Depois de montados, gere um terceiro vetor formado pela diferença dos dois vetores lidos, um quarto vetor
formado pela soma dos dois vetores lidos e por último um quinto vetor formado pela multiplicação dos dois vetores lidos.
'''
qtd = 2
primeiro = []
segundo = []
terceiro = []
quarto = []
quinto = []

print("LISTA UM")
for i in range(qtd):
    primeiro.append(int(input(f"Informe o {i+1}° número: ")))

print("\nLISTA DOIS")
for i in range(qtd):
    segundo.append(int(input(f"Informe o {i+1}° número: ")))

for i in range(qtd):
    terceiro.append(primeiro[i]-segundo[i])
    quarto.append(primeiro[i]+segundo[i])
    quinto.append(primeiro[i]*segundo[i])

print("Subtração das listas:",*terceiro)
print("Soma das listas:",*quarto)
print("Multiplicação das listas:",*quinto)