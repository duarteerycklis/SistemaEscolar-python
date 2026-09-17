from alunos import salvar_alunos, verificar_situacao
from validacoes import notas_validas, disciplinas_validas

def adicionar_disciplinas(alunos, aluno):
    aluno["disciplinas"] = aluno.get("disciplinas", {})
    while True:
        disciplina = disciplinas_validas("Digite o nome da disciplina: ").strip()
        if disciplina in aluno["disciplinas"]:
            print("Disciplina já cadastrada.")
        else:
            break
    nota = notas_validas("Digite a nota da disciplina: ")
    aluno["disciplinas"][disciplina] = nota
    salvar_alunos(alunos)

def adicionar_disciplina_aluno(alunos):
    nome = input("Digite o nome completo do aluno que deseja adicionar uma disciplina: ").strip()
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            adicionar_disciplinas(alunos, aluno)
            return
    print("Aluno não encontrado.")
def listar_disciplinas(disciplinas):
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
    else:
        for disciplina, nota in disciplinas.items():
            print(f"- {disciplina}: {nota}")
def calcular_media_disciplinas(aluno):
    disciplinas = aluno.get("disciplinas", {})

    if not disciplinas:
        return 0

    return round(sum(disciplinas.values()) / len(disciplinas), 2)
def atualizar_nota_disciplina(alunos):
    nome = input("Digite o nome completo do aluno que deseja atualizar a nota de uma disciplina: ").strip()
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            if not aluno.get("disciplinas"):
                print("O aluno não possui disciplinas cadastradas.")
                return
            listar_disciplinas(aluno["disciplinas"])
            disciplina = input("Digite o nome da disciplina que deseja atualizar a nota: ").strip()
            if disciplina not in aluno["disciplinas"]:
                print("Disciplina não encontrada.")
                return
            nova_nota = notas_validas("Digite a nova nota da disciplina: ")
            aluno["disciplinas"][disciplina] = nova_nota
            salvar_alunos(alunos)
            print("Nota atualizada com sucesso.")
            return
    print("Aluno não encontrado.")
def remover_disciplina_aluno(alunos):
    nome = input("Digite o nome completo do aluno que deseja remover uma disciplina: ").strip()
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            if not aluno.get("disciplinas"):
                print("O aluno não possui disciplinas cadastradas.")
                return
            listar_disciplinas(aluno["disciplinas"])
            disciplina = input("Digite o nome da disciplina que deseja remover: ").strip()
            if disciplina not in aluno["disciplinas"]:
                print("Disciplina não encontrada.")
                return
            del aluno["disciplinas"][disciplina]
            salvar_alunos(alunos)
            print("Disciplina removida com sucesso.")
            return
    print("Aluno não encontrado.")

def consultar_nota_disciplina(aluno, disciplina):
    disciplinas = aluno.get("disciplinas", {})
    return disciplinas.get(disciplina, None)
def consultar_nota_disciplina_aluno(alunos):
    nome = input("Digite o nome completo do aluno que deseja consultar a nota de uma disciplina: ").strip()
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            if not aluno.get("disciplinas"):
                print("O aluno não possui disciplinas cadastradas.")
                return
            listar_disciplinas(aluno["disciplinas"])
            disciplina = input("Digite o nome da disciplina que deseja consultar a nota: ").strip()
            if disciplina not in aluno["disciplinas"]:
                print("Disciplina não encontrada.")
                return
            nota = consultar_nota_disciplina(aluno, disciplina)
            print(f"Nota da disciplina {disciplina}: {nota}")
            return
    print("Aluno não encontrado.")
def situacao_disciplina(aluno, disciplina):
    nota = consultar_nota_disciplina(aluno, disciplina)
    if nota is None:
        return "Disciplina não encontrada."
    return verificar_situacao(nota)
def exibir_situacao_disciplinas(aluno):
    disciplinas = aluno.get("disciplinas", {})
    if not disciplinas:
        print("O aluno não possui disciplinas cadastradas.")
        return
    for disciplina in disciplinas:
        situacao = situacao_disciplina(aluno, disciplina)
        print(f"Disciplina: {disciplina}, Situação: {situacao}")
def consultar_situacao_disciplinas(alunos):
    nome = input("Digite o nome completo do aluno que deseja consultar a situação das disciplinas: ").strip()
    for aluno in alunos:
        if aluno['nome'].lower() == nome.lower():
            exibir_situacao_disciplinas(aluno)
            return
    print("Aluno não encontrado.")

