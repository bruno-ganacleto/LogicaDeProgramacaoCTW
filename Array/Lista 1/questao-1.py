'''
1- Faça um programa em Py que receba o total das vendas de cada vendedor e armazenadas em um vetor.
Receba também o percentual de comissão de cada vendedor e armazene-os em outro vetor.
Receba os nomes desses vendedores e armazene ­os em um terceiro vetor.
Existem apenas dez vendedores. Calcule e mostre: 
a) Um relatório com os nomes dos vendedores e os valores a receber; 
b) O total das vendas de todos os vendedores; 
c) O maior valor a receber e quem o receberá; 
d) O menor valor a receber e quem o receberá.
'''

qtd = 10 #numero de vendedores
total_vendas = []
percentual_comissao = []
comissao = []
nomes = []
pos_menor = 0
pos_maior = 0
total = 0

for i in range(qtd):
    print(f"\n{i+1}º Vendedor")
    nomes.append(input("Nome: "))
    total_vendas.append(float(input("Total das vendas: ")))
    percentual_comissao.append(float(input("Percentual de comissão: ")))
    comissao.append(total_vendas[i]*(percentual_comissao[i]/100))
    total += total_vendas[i]

    if comissao[i] < comissao[0]:
        pos_menor = i
    if comissao[i] > comissao[0]:
            pos_maior = i

print("\n---------------------------------")
print(f"\nTOTAL DE VENDAS --> R${total:.2f}")
print(f"MENOR COMISSÃO --> {nomes[pos_menor]} - R${comissao[pos_menor]:.2f}")
print(f"MAIOR COMISSÃO --> {nomes[pos_maior]} - R${comissao[pos_maior]:.2f}")

print("\n\n---- VALORES A RECEBER ----\n")
for i in range(qtd):
    print(nomes[i], "-->", (f"R${comissao[i]:.2f}"))

