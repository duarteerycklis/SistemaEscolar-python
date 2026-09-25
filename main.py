from banco import criar_tabelas

from alunos import (
    cadastrar_aluno,
    atualizar_aluno,
    remover_aluno,
    atualizar_nota,
    consultar_situacao,
    calcular_media,
)

from disciplinas import (
    adicionar_disciplina,
    adicionar_disciplina_aluno,
    listar_disciplinas_aluno,
    pesquisar_disciplina,
    atualizar_disciplina,
    remover_disciplina,
    atualizar_nota_disciplina,
    remover_disciplina_aluno,
    consultar_disciplina_aluno,
    verificar_situacao_disciplina,
    exibir_disciplina_aluno,
    estatisticas_disciplina,
)

from exibicao import (
    listar_alunos,
    alunos_cadastrados,
    pesquisar_aluno,
)

from estatisticas import (
    estatisticas_da_disciplina,
    estatistica_de_todas_disciplinas,
    estatisticas_turma,
    consultar_alunos_por_situacao,
    ordenar_alunos,
)


criar_tabelas()


while True:

    print("\n======== MENU ========")
    print("1. Cadastrar aluno")
    print("2. Listar alunos")
    print("3. Pesquisar aluno")
    print("4. Remover aluno")
    print("5. Atualizar aluno")
    print("6. Atualizar nota")
    print("7. Calcular média")
    print("8. Consultar situação do aluno")
    print("9. Estatísticas da turma")
    print("10. Ordenar alunos")
    print("11. Consultar alunos por situação")
    print("12. Cadastrar disciplina")
    print("13. Adicionar disciplina a um aluno")
    print("14. Atualizar nota de uma disciplina")
    print("15. Remover disciplina de um aluno")
    print("16. Consultar nota de uma disciplina")
    print("17. Consultar situação das disciplinas de um aluno")
    print("18. Estatísticas da disciplina")
    print("19. Estatísticas de todas as disciplinas")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")


    if opcao == "1":
        cadastrar_aluno()


    elif opcao == "2":
        listar_alunos()


    elif opcao == "3":
        pesquisar_aluno()


    elif opcao == "4":
        remover_aluno()


    elif opcao == "5":
        atualizar_aluno()


    elif opcao == "6":
        atualizar_nota()


    elif opcao == "7":
        calcular_media()


    elif opcao == "8":
        consultar_situacao()


    elif opcao == "9":
        estatisticas_turma()


    elif opcao == "10":
        ordenar_alunos()


    elif opcao == "11":
        consultar_alunos_por_situacao()

    elif opcao == "12":
        disciplina = input("Digite o nome da disciplina que deseja cadastrar")
        adicionar_disciplina = disciplina


    elif opcao == "13":
        print("Digite o Nome do aluno e o Nome da disciplina")

        aluno_nome = input("Nome do aluno: ")
        disciplina_nome = input("Nome da disciplina: ")

        adicionar_disciplina_aluno(
            aluno_nome,
            disciplina_nome
        )


    elif opcao == "14":
        print("Digite o Nome do aluno e o Nome da disciplina")

        aluno_nome = input("Nome do aluno: ")
        disciplina_nome = input("Nome da disciplina: ")

        atualizar_nota_disciplina(
            aluno_nome,
            disciplina_nome
        )


    elif opcao == "15":
        print("Digite o Nome do aluno e o Nome da disciplina")

        aluno_nome = input("Nome do aluno: ")
        disciplina_nome = input("Nome da disciplina: ")

        remover_disciplina_aluno(
            aluno_nome,
            disciplina_nome
        )


    elif opcao == "16":
        print("Digite o Nome do aluno e o Nome da disciplina")

        aluno_nome = input("Nome do aluno: ")
        disciplina_nome = input("Nome da disciplina: ")

        exibir_disciplina_aluno(
            aluno_nome,
            disciplina_nome
        )


    elif opcao == "17":
        print("Digite o Nome do aluno e o Nome da disciplina")

        aluno_nome = input("Nome do aluno: ")
        disciplina_nome = input("Nome da disciplina: ")

        situacao = verificar_situacao_disciplina(
            aluno_nome,
            disciplina_nome
        )

        print(f"Situação da disciplina: {situacao}")


    elif opcao == "18":
        print("Digite o Nome da disciplina")

        disciplina_nome = input("Nome da disciplina: ")

        estatisticas_da_disciplina(disciplina_nome)


    elif opcao == "19":
        estatistica_de_todas_disciplinas()


    elif opcao == "0":
        print("Saindo do sistema...")
        break


    else:
        print("Opção inválida. Tente novamente.")