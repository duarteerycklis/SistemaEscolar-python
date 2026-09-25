from validacoes import notas_validas

from banco import (
    criar_disciplina_banco,
    disciplina_ja_cadastrada,
    listar_disciplina_banco,
    pesquisar_disciplina_banco,
    pesquisar_aluno_banco,
    atualizar_disciplina_banco,
    remover_disciplina_banco,
    adicionar_disciplina_aluno_banco,
    listar_disciplinas_aluno_banco,
    atualizar_nota_disciplina_banco,
    remover_disciplina_aluno_banco
)


def adicionar_disciplina(disciplina):
    if disciplina_ja_cadastrada(disciplina):
        print("Disciplina já cadastrada.")
        return

    resultado = criar_disciplina_banco(disciplina)

    if resultado:
        print("Disciplina criada com sucesso.")
    else:
        print("Erro ao criar disciplina.")


def adicionar_disciplina_aluno(aluno_nome, disciplina_nome):
    aluno_info = pesquisar_aluno_banco(aluno_nome)

    if not aluno_info:
        print("Aluno não encontrado.")
        return

    aluno_id = aluno_info[0][0]

    disciplina_info = pesquisar_disciplina_banco(disciplina_nome)

    if not disciplina_info:
        print("Disciplina não encontrada.")
        return

    disciplina_id = disciplina_info[0]

    nota = notas_validas("Digite a nota da disciplina: ")

    resultado = adicionar_disciplina_aluno_banco(
        aluno_id,
        disciplina_id,
        nota
    )

    if resultado:
        print("Disciplina adicionada ao aluno com sucesso.")
    else:
        print("Erro ao adicionar disciplina ao aluno.")


def listar_disciplinas():
    return listar_disciplina_banco()


def pesquisar_disciplina(nome):
    return pesquisar_disciplina_banco(nome)


def atualizar_disciplina(id, nome):
    return atualizar_disciplina_banco(id, nome)


def remover_disciplina(id):
    return remover_disciplina_banco(id)


def listar_disciplinas_aluno(aluno_id):
    return listar_disciplinas_aluno_banco(aluno_id)


def atualizar_nota_disciplina(aluno_nome, disciplina_nome):
    aluno_info = pesquisar_aluno_banco(aluno_nome)

    if not aluno_info:
        print("Aluno não encontrado.")
        return

    aluno_id = aluno_info[0][0]

    disciplina_info = pesquisar_disciplina_banco(disciplina_nome)

    if not disciplina_info:
        print("Disciplina não encontrada.")
        return

    disciplina_id = disciplina_info[0]

    nota = notas_validas("Digite a nova nota da disciplina: ")

    resultado = atualizar_nota_disciplina_banco(
        aluno_id,
        disciplina_id,
        nota
    )

    if resultado:
        print("Nota da disciplina atualizada com sucesso.")
    else:
        print("Erro ao atualizar nota da disciplina.")

    return resultado


def remover_disciplina_aluno(aluno_nome, disciplina_nome):
    aluno_info = pesquisar_aluno_banco(aluno_nome)

    if not aluno_info:
        print("Aluno não encontrado.")
        return

    aluno_id = aluno_info[0][0]

    disciplina_info = pesquisar_disciplina_banco(disciplina_nome)

    if not disciplina_info:
        print("Disciplina não encontrada.")
        return

    disciplina_id = disciplina_info[0]

    resultado = remover_disciplina_aluno_banco(
        aluno_id,
        disciplina_id
    )

    if resultado:
        print("Disciplina removida do aluno com sucesso.")
    else:
        print("Erro ao remover disciplina do aluno.")

    return resultado


def consultar_disciplina_aluno(aluno_nome, disciplina_nome):
    aluno_info = pesquisar_aluno_banco(aluno_nome)

    if not aluno_info:
        return None

    aluno_id = aluno_info[0][0]

    disciplina_info = pesquisar_disciplina_banco(disciplina_nome)

    if not disciplina_info:
        return None

    disciplina_id = disciplina_info[0]

    disciplinas = listar_disciplinas_aluno_banco(aluno_id)

    for disciplina in disciplinas:
        if disciplina[0] == disciplina_id:
            return disciplina

    return None


def verificar_situacao_disciplina(aluno_nome, disciplina_nome):
    disciplina = consultar_disciplina_aluno(
        aluno_nome,
        disciplina_nome
    )

    if disciplina is None:
        return "Disciplina não encontrada para o aluno."

    nota = disciplina[2]

    if nota is None:
        return "Disciplina cursada, mas sem nota registrada."

    elif nota >= 7:
        return "Aprovado"

    elif nota >= 5:
        return "Recuperação"

    else:
        return "Reprovado"


def exibir_disciplina_aluno(aluno_nome, disciplina_nome):
    disciplina = consultar_disciplina_aluno(
        aluno_nome,
        disciplina_nome
    )

    if disciplina is None:
        print("Disciplina não encontrada para o aluno.")
    else:
        situacao = verificar_situacao_disciplina(
            aluno_nome,
            disciplina_nome
        )

        print(
            f"Disciplina: {disciplina[1]}, "
            f"Nota: {disciplina[2]}, "
            f"Situação: {situacao}"
        )


def estatisticas_disciplina(aluno_id):
    disciplinas = listar_disciplinas_aluno_banco(aluno_id)

    total_disciplinas = len(disciplinas)

    aprovadas = sum(
        1 for d in disciplinas
        if d[2] is not None and d[2] >= 7
    )

    recuperacao = sum(
        1 for d in disciplinas
        if d[2] is not None and 5 <= d[2] < 7
    )

    reprovadas = sum(
        1 for d in disciplinas
        if d[2] is not None and d[2] < 5
    )

    sem_nota = sum(
        1 for d in disciplinas
        if d[2] is None
    )

    notas = [
        d[2]
        for d in disciplinas
        if d[2] is not None
    ]

    if notas:
        media = sum(notas) / len(notas)
    else:
        media = "N/A"

    print(f"Total de disciplinas: {total_disciplinas}")
    print(f"Aprovadas: {aprovadas}")
    print(f"Recuperação: {recuperacao}")
    print(f"Reprovadas: {reprovadas}")
    print(f"Sem nota: {sem_nota}")

    if isinstance(media, str):
        print(f"Média das notas: {media}")
    else:
        print(f"Média das notas: {media:.2f}")