'''
4-Em uma classe há n alunos, cada um dos quais realizou k provas com pesos distintos.
Dados n , k, os pesos das k provas e as notas de cada aluno, calcular a média ponderada das provas
para cada aluno e a média aritmética da classe em cada uma das provas
'''
alunos = int(input("Digite a quantidade de alunos: "))
provas = int(input("Digite a quantidade de provas feitas por cada aluno: "))
medias = []
media_classe = None

for i in range(alunos):
    notas = []
    pesos = []
    soma_pesos = 0
    somatorio_notas = 0
    somatorio_pesos = 0
    soma_medias = 0

    for prova in range(provas):
        notas.append(float(input(f"Digite a nota da {prova+1}° prova: ")))
        pesos.append(float(input(f"Digite o peso da {prova+1}° prova: ")))
        print()
        soma_pesos += pesos[prova]

    for x in range(alunos):
        somatorio_notas += notas[x]*pesos[x]
        somatorio_pesos += pesos[x]

    medias.append(somatorio_notas/somatorio_pesos)
    soma_medias += medias[i]

media_classe = soma_medias/alunos

print(f"Média dos alunos:* {medias:.2f}")
print(f"Média da classe: {media_classe:.2f}")
