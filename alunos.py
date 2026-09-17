from validacoes import notas_validas, validar_idade
from banco import inserir_aluno, nome_ja_cadastrado_banco, listar_alunos_banco, converter_alunos, remover_aluno_banco, atualizar_aluno_banco, atualizar_nota_banco

def obter_nota(aluno):
    return float(aluno.get('nota', 0))


def nome_ja_cadastrado(alunos, nome):
    nome_normalizado = " ".join(nome.split()).casefold()
    return any(
        " ".join(aluno["nome"].split()).casefold() == nome_normalizado
        for aluno in alunos
    )
def cadastrar_alunos(alunos):
    while True:
        nome = input("Digite o nome completo do aluno: ").strip()
        if not nome:
            print("O nome não pode ficar vazio.")
        elif nome_ja_cadastrado_banco(nome):
            print("Este aluno já está cadastrado.")
        else:
            break
    idade = validar_idade("Digite a idade do aluno: ")  # Inicializa a idade chamando a função de validação
    nota = notas_validas("Digite a nota do aluno: ")

    inserir_aluno(nome, idade, nota)
    print(f"Aluno {nome} cadastrado com sucesso.")
    alunos= listar_alunos_banco()
    alunos = converter_alunos(alunos)
    return alunos


def remover_aluno(alunos):
    nome = input("Digite o nome do aluno que deseja remover: ")
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            resultado = remover_aluno_banco(aluno['id'])
            if resultado>0:
                print(f"Aluno {nome} removido com sucesso.")
            else:
                print("Aluno não encontrado no banco de dados.")
            alunos = listar_alunos_banco()
            alunos = converter_alunos(alunos)
            return alunos
    print("Aluno não encontrado.")
    return alunos
    
def atualizar_aluno(alunos):
    nome = input("Digite o nome completo do aluno que deseja atualizar: ")

    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            novo_nome = input("Digite o novo nome completo do aluno: ")
            nova_idade = validar_idade("Digite a nova idade do aluno: ")

            resultado = atualizar_aluno_banco(aluno['id'], novo_nome, nova_idade)
            if resultado>0:
                print(f"Aluno {nome} atualizado com sucesso.")
            else:
                print("Aluno não encontrado no banco de dados.")

            alunos = listar_alunos_banco()
            alunos = converter_alunos(alunos)
            return alunos

    print("Aluno não encontrado.")
    return alunos
def verificar_situacao(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"
def calcular_media(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    soma = 0
    for aluno in alunos:
        soma += obter_nota(aluno)
    media = soma / len(alunos)
    print(f"A média das notas dos alunos é: {media}\n")



def atualizar_nota(alunos):
    nome = input("Digite o nome do aluno que deseja atualizar a nota: ")

    for aluno in alunos:
        if aluno["nome"].lower() == nome.lower():
            nota = notas_validas("Digite a nova nota (0 a 10): ")
            resultado = atualizar_nota_banco(aluno['id'], nota)
            if resultado>0:
                print(f"Nota do aluno {nome} atualizada com sucesso.")
            else:
                print("Aluno não encontrado no banco de dados.")

            alunos = listar_alunos_banco()
            alunos = converter_alunos(alunos)
            return alunos

    print("Aluno não encontrado.")
    return alunos
def consultar_situacao(alunos):
    nome = input("Digite o nome do aluno para consultar a situação: ")
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            nota = obter_nota(aluno)
            situacao = verificar_situacao(nota)
            print(f"A situação do aluno {nome} é: {situacao}")
            return
    print("Aluno não encontrado.")

