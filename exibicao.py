from alunos import obter_nota, verificar_situacao
from disciplinas import listar_disciplinas, calcular_media_disciplinas
from banco import pesquisar_aluno_banco, listar_alunos_banco, converter_alunos

def exibir_aluno(aluno):
    nota = aluno.get('nota', 'N/A')
    situacao = verificar_situacao(obter_nota(aluno))
    print(
        f"\n Nome: {aluno['nome']}"
        f"\n Idade: {aluno['idade']}"
        f"\n Nota: {nota}"
        f"\n Situação: {situacao}"
    )
    if aluno.get("disciplinas"):
        print("Disciplinas do aluno:")
        listar_disciplinas(aluno["disciplinas"])
        media = calcular_media_disciplinas(aluno)
        print(f"Média das disciplinas: {media}")
    else:
        print("O aluno não possui disciplinas cadastradas.")
def listar_alunos(alunos):
    resultados = listar_alunos_banco()
    resultados = converter_alunos(resultados)
    if resultados:
        for aluno in resultados:
            exibir_aluno(aluno)
    else:
        print("Nenhum aluno cadastrado.")
        
def alunos_cadastrados():
    resultados = listar_alunos_banco()
    resultados = converter_alunos(resultados)
    if not resultados:
        print("Nenhum aluno cadastrado.")
        return
    for aluno in resultados:
        exibir_aluno(aluno)
def pesquisar_aluno():
    nome = input("Digite o nome do Aluno que deseja Pesquisar: ").strip()
    resultados = pesquisar_aluno_banco(nome)
    resultados = converter_alunos(resultados)
    if resultados:
        for aluno in resultados:
            exibir_aluno(aluno)
    else:
        print("Aluno não encontrado.")
