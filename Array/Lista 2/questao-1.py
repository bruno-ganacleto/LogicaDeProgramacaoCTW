'''
1- Faça um algoritmo que leia a nota de 10 alunos de uma turma e guarde-as em um vetor. No final, mostre:
a) Qual é a média da turma
b) Quantos alunos estão acima da média da turma 
c) Qual foi a maior nota digitada
d) Em que posições a maior nota aparece
'''

alunos = 10
notas = []
total = 0
acima_media = 0

for i in range(alunos):
    notas.append(float(input(f"Digite a {i+1}° nota: ")))
    total += notas[i]
    if notas[i] >= 7:
        acima_media += 1
    
maior_nota = []
media = total/alunos

for i in range(len(notas)):
    if notas[i] == max(notas):
        maior_nota.append(i)

print("A média da turma é", media)
print(acima_media, "alunos estão acima da média")
print("A maior nota atingida foi", max(notas))
print("A maior nota apareceu nas posições", end=" ")
print(*maior_nota)