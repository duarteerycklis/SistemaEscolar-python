from alunos import verificar_situacao
from disciplinas import listar_disciplinas_aluno
from banco import pesquisar_aluno_banco, listar_alunos_banco


def exibir_aluno(aluno):
    print(
        f"\nNome: {aluno[1]}"
        f"\nIdade: {aluno[2]}"
        f"\nNota: {aluno[3]}"
        f"\nSituação: {verificar_situacao(aluno[3])}"
    )

    disciplinas = listar_disciplinas_aluno(aluno[0])

    if disciplinas:
        print("Disciplinas do aluno:")

        for disciplina in disciplinas:
            print(f"- {disciplina[1]}")
    else:
        print("O aluno não possui disciplinas cadastradas.")


def listar_alunos():
    resultados = listar_alunos_banco()

    if not resultados:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in resultados:
        exibir_aluno(aluno)


def alunos_cadastrados():
    resultados = listar_alunos_banco()

    if not resultados:
        print("Nenhum aluno cadastrado.")
        return

    for aluno in resultados:
        exibir_aluno(aluno)


def pesquisar_aluno():
    nome = input(
        "Digite o nome do Aluno que deseja Pesquisar: "
    ).strip()

    resultados = pesquisar_aluno_banco(nome)

    if resultados:
        for aluno in resultados:
            exibir_aluno(aluno)
    else:
        print("Aluno não encontrado.")