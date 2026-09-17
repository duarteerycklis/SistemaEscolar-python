from alunos import (
    carregar_alunos,
    cadastrar_alunos,
    remover_aluno,
    atualizar_aluno,
    atualizar_nota,
    calcular_media,
    consultar_situacao,
    obter_nota
)
from banco import inserir_aluno, listar_alunos_banco, pesquisar_aluno_banco, converter_alunos
from disciplinas import (
    adicionar_disciplina_aluno,
    atualizar_nota_disciplina,
    remover_disciplina_aluno,
    consultar_nota_disciplina_aluno,
    consultar_situacao_disciplinas,
    
)
from validacoes import*
from exibicao import listar_alunos, pesquisar_aluno
from estatisticas import (
    estatisticas_turma,
    ordenar_alunos,
    consultar_alunos_por_situacao,
    estatisticas_da_disciplina,
    estatistica_de_todas_disciplinas
)
from banco import criar_tabelas
criar_tabelas()

alunos = listar_alunos_banco()
alunos = converter_alunos(alunos)


while True:
    print("\n========Menu========")
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
    print("12. Adicionar disciplina a um aluno")
    print("13. Atualizar nota de uma disciplina")
    print("14. Remover disciplina de um aluno")
    print("15. Consultar nota de uma disciplina")
    print("16. Consultar situação das disciplinas de um aluno")
    print("17. Estatísticas da disciplina")
    print("18. Estatísticas de todas as disciplinas")
    print("0. Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        alunos = cadastrar_alunos(alunos)
    elif opcao == "2":
        listar_alunos()
    elif opcao == "3":
        pesquisar_aluno()
    elif opcao == "4":
        alunos = remover_aluno(alunos)
    elif opcao == "5":
        alunos = atualizar_aluno(alunos)
    elif opcao == "6":
        alunos = atualizar_nota(alunos)
    elif opcao == "7":
        calcular_media(alunos)
    elif opcao == "8":
        consultar_situacao(alunos)
    elif opcao == "9":
        estatisticas_turma(alunos)
    elif opcao == "10":
        ordenar_alunos(alunos)
    elif opcao == "11":
        consultar_alunos_por_situacao(alunos)
    elif opcao == "12":
        adicionar_disciplina_aluno(alunos)
    elif opcao == "13":
        atualizar_nota_disciplina(alunos)
    elif opcao == "14":
        remover_disciplina_aluno(alunos)
    elif opcao == "15":
        consultar_nota_disciplina_aluno(alunos)
    elif opcao == "16":
        consultar_situacao_disciplinas(alunos)
    elif opcao == "17":
        estatisticas_da_disciplina(alunos)
    elif opcao == "18":
        estatistica_de_todas_disciplinas(alunos)
    elif opcao == "0":
        break
    else:
        print("Opção inválida.")


