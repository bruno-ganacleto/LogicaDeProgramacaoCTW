totalTurma = 0
alunosAprovados = 0

for _ in range(20):
    nome = input("Informe o nome: ")
    nota = float(input("Informe a nota: "))

    totalTurma += nota
    if nota > 7: alunosAprovados += 1
    
print("Média da Turma:", totalTurma/20)
print("Alunos com nota maior que 7:", alunosAprovados)