from banco import listar_alunos_banco
from alunos import verificar_situacao
from disciplinas import listar_disciplinas_aluno


def estatisticas_da_disciplina(disciplina=None):
    if disciplina is None:
        disciplina = input(
            "Digite o nome da disciplina para ver as estatísticas: "
        ).strip()

    aprovados = 0
    reprovados = 0
    recuperacao = 0
    soma_notas = 0
    total = 0

    alunos = listar_alunos_banco()

    for aluno in alunos:
        nota = None

        disciplinas_aluno = listar_disciplinas_aluno(aluno[0])

        for d in disciplinas_aluno:
            if d[1] == disciplina:
                nota = d[2]
                break

        if nota is not None:
            if nota >= 7:
                aprovados += 1
            elif nota >= 5:
                recuperacao += 1
            else:
                reprovados += 1

            soma_notas += nota
            total += 1

    if total == 0:
        print("Nenhum aluno possui esta disciplina cadastrada.")
    else:
        media = soma_notas / total

        print(
            f"Total de alunos com a disciplina {disciplina}: {total}"
        )
        print(f"Aprovados: {aprovados}")
        print(f"Reprovados: {reprovados}")
        print(f"Recuperação: {recuperacao}")
        print(f"Média das notas: {media:.2f}")


def estatistica_de_todas_disciplinas():
    disciplinas = set()

    alunos = listar_alunos_banco()

    for aluno in alunos:
        disciplinas_aluno = listar_disciplinas_aluno(aluno[0])

        for disciplina in disciplinas_aluno:
            disciplinas.add(disciplina[1])

    for disciplina in disciplinas:
        print(f"\nEstatísticas da disciplina: {disciplina}")
        estatisticas_da_disciplina(disciplina)

    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")


def estatisticas_turma():
    alunos = listar_alunos_banco()

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    total_alunos = len(alunos)

    aprovados = sum(
        1
        for aluno in alunos
        if verificar_situacao(aluno[3]) == "Aprovado"
    )

    recuperacao = sum(
        1
        for aluno in alunos
        if verificar_situacao(aluno[3]) == "Recuperação"
    )

    reprovados = sum(
        1
        for aluno in alunos
        if verificar_situacao(aluno[3]) == "Reprovado"
    )

    print("========== Estatísticas da turma ==========\n")

    print(f"\nTotal de alunos: {total_alunos}")
    print(f"\nAprovados: {aprovados}")
    print(f"\nRecuperação: {recuperacao}")
    print(f"\nReprovados: {reprovados}")

    print(
        f"\nMaior nota: "
        f"{max(aluno[3] for aluno in alunos)}"
    )

    print(
        f"\nMenor nota: "
        f"{min(aluno[3] for aluno in alunos)}"
    )

    print(
        f"\nMédia da turma: "
        f"{sum(aluno[3] for aluno in alunos) / len(alunos)}"
    )


def alunos_por_situacao(situacao_desejada):
    alunos = listar_alunos_banco()

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    alunos_filtrados = [
        aluno
        for aluno in alunos
        if verificar_situacao(aluno[3]) == situacao_desejada
    ]

    if not alunos_filtrados:
        print(
            f"Nenhum aluno com situação "
            f"'{situacao_desejada}'."
        )
        return

    for aluno in alunos_filtrados:
        print(
            f"Nome: {aluno[1]}, "
            f"Nota: {aluno[3]}\n"
        )

    print(
        f"Total de alunos com situação "
        f"'{situacao_desejada}': {len(alunos_filtrados)}"
    )

    print("==========================================")


def consultar_alunos_por_situacao():
    while True:
        print("Escolha a situação desejada:")
        print("1. Aprovado")
        print("2. Recuperação")
        print("3. Reprovado")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            alunos_por_situacao("Aprovado")

        elif opcao == "2":
            alunos_por_situacao("Recuperação")

        elif opcao == "3":
            alunos_por_situacao("Reprovado")

        elif opcao == "0":
            return

        else:
            print("Opção inválida.")


def ordenar_alunos():
    alunos = listar_alunos_banco()

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    while True:
        print("Escolha o critério de ordenação:")
        print("1. Maior nota")
        print("2. Menor nota")
        print("3. Ordem alfabética A-Z")
        print("4. Ordem alfabética Z-A")
        print("0. Voltar")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            print("Ordenando alunos por Maior nota\n")

            alunos_ordenado = sorted(
                alunos,
                key=lambda aluno: aluno[3],
                reverse=True
            )

            for aluno in alunos_ordenado:
                print(
                    f"Nome: {aluno[1]}, "
                    f"Nota: {aluno[3]}\n"
                )

        elif opcao == "2":
            print("Ordenando alunos por Menor nota\n")

            alunos_ordenado = sorted(
                alunos,
                key=lambda aluno: aluno[3],
                reverse=False
            )

            for aluno in alunos_ordenado:
                print(
                    f"Nome: {aluno[1]}, "
                    f"Nota: {aluno[3]}\n"
                )

        elif opcao == "3":
            print(
                "Ordenando alunos por ordem alfabética A-Z\n"
            )

            alunos_ordenado = sorted(
                alunos,
                key=lambda aluno: aluno[1]
            )

            for aluno in alunos_ordenado:
                print(
                    f"Nome: {aluno[1]}, "
                    f"Nota: {aluno[3]}\n"
                )

        elif opcao == "4":
            print(
                "Ordenando alunos por ordem alfabética Z-A\n"
            )

            alunos_ordenado = sorted(
                alunos,
                key=lambda aluno: aluno[1],
                reverse=True
            )

            for aluno in alunos_ordenado:
                print(
                    f"Nome: {aluno[1]}, "
                    f"Nota: {aluno[3]}\n"
                )

        elif opcao == "0":
            break

        else:
            print("Opção inválida. Tente novamente.")