from validacoes import notas_validas, validar_idade

from banco import (
    inserir_aluno,
    nome_ja_cadastrado_banco,
    pesquisar_aluno_banco,
    listar_alunos_banco,
    remover_aluno_banco,
    atualizar_aluno_banco,
    atualizar_nota_banco,
)


def cadastrar_aluno():
    while True:
        nome = input("Digite o nome completo do aluno: ").strip()

        if not nome:
            print("O nome não pode ficar vazio.")

        elif nome_ja_cadastrado_banco(nome):
            print("Este aluno já está cadastrado.")

        else:
            break

    idade = validar_idade("Digite a idade do aluno: ")
    nota = notas_validas("Digite a nota do aluno: ")

    inserir_aluno(nome, idade, nota)

    print(f"Aluno {nome} cadastrado com sucesso.")


def remover_aluno():
    nome = input("Digite o nome do aluno que deseja remover: ")

    aluno = pesquisar_aluno_banco(nome)

    if not aluno:
        print("Aluno não encontrado no banco de dados.")
        return

    resultado = remover_aluno_banco(aluno[0][0])

    if resultado == "possui_disciplina":
        print("O aluno possui disciplinas associadas.")
        print("Remova as disciplinas associadas antes de tentar remover o aluno.")

    elif resultado > 0:
        print(f"Aluno {nome} removido com sucesso.")

    else:
        print("Aluno não encontrado no banco de dados.")


def atualizar_aluno():
    nome = input("Digite o nome completo do aluno que deseja atualizar: ")

    aluno = pesquisar_aluno_banco(nome)

    if not aluno:
        print("Aluno não encontrado no banco de dados.")
        return

    novo_nome = input("Digite o novo nome completo do aluno: ")
    nova_idade = validar_idade("Digite a nova idade do aluno: ")

    resultado = atualizar_aluno_banco(
        aluno[0][0],
        novo_nome,
        nova_idade
    )

    if resultado > 0:
        print(f"Aluno {nome} atualizado com sucesso.")

    else:
        print("Aluno não encontrado no banco de dados.")


def verificar_situacao(nota):
    if nota >= 7:
        return "Aprovado"

    elif nota >= 5:
        return "Recuperação"

    else:
        return "Reprovado"


def calcular_media():
    alunos = listar_alunos_banco()

    if not alunos:
        print("Nenhum aluno cadastrado.")
        return

    soma = 0

    for aluno in alunos:
        soma += aluno[3]

    media = soma / len(alunos)

    print(f"A média das notas dos alunos é: {media}\n")

    return media


def atualizar_nota():
    print("Digite o nome do aluno que deseja atualizar a nota.")

    nome = input("Nome do aluno: ")

    aluno = pesquisar_aluno_banco(nome)

    if not aluno:
        print("Aluno não encontrado.")
        return

    nova_nota = notas_validas("Digite a nova nota (0 a 10): ")

    resultado = atualizar_nota_banco(
        aluno[0][0],
        nova_nota
    )

    if resultado > 0:
        print(f"Nota do aluno {nome} atualizada com sucesso.")

    else:
        print("Aluno não encontrado no banco de dados.")


def consultar_situacao():
    nome = input("Digite o nome do aluno para consultar a situação: ")

    aluno = pesquisar_aluno_banco(nome)

    if not aluno:
        print("Aluno não encontrado.")
        return

    nota = aluno[0][3]

    situacao = verificar_situacao(nota)

    print(f"A situação do aluno {nome} é: {situacao}")
    