from alunos import obter_nota, verificar_situacao
from disciplinas import consultar_nota_disciplina, situacao_disciplina
from exibicao import alunos_cadastrados
def estatisticas_da_disciplina(alunos, disciplina=None):
    if disciplina is None:
        disciplina = input("Digite o nome da disciplina para ver as estatísticas: ").strip()
    aprovados = 0
    reprovados = 0
    recuperacao = 0
    total = 0
    count = 0
    for aluno in alunos:
        nota = consultar_nota_disciplina(aluno, disciplina)
        if nota is not None:
            situacao = situacao_disciplina(aluno, disciplina)
            if situacao == "Aprovado":
                aprovados += 1
            elif situacao == "Reprovado":
                reprovados += 1
            elif situacao == "Recuperação":
                recuperacao += 1
            total += nota
            count += 1
    if count == 0:
        print("Nenhum aluno possui esta disciplina cadastrada.")
    else:
        media = total / count
        print(f"Média da disciplina {disciplina}: {media:.2f}")
        print(f"Aprovados: {aprovados}")
        print(f"Reprovados: {reprovados}")
        print(f"Recuperação: {recuperacao}")
        print(f"Total de alunos com a disciplina: {count}")
def estatistica_de_todas_disciplinas(alunos):
    disciplinas = set()
    for aluno in alunos:
        for disciplina in aluno.get("disciplinas", {}):
            disciplinas.add(disciplina)
    for disciplina in disciplinas:
        print(f"\nEstatísticas da disciplina: {disciplina}")
        estatisticas_da_disciplina(alunos, disciplina)
    if not disciplinas:
        print("Nenhuma disciplina cadastrada.")
def estatisticas_turma(alunos):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    total_alunos = len(alunos)
    aprovados = sum(1 for aluno in alunos if verificar_situacao(obter_nota(aluno)) == "Aprovado")
    recuperacao = sum(1 for aluno in alunos if verificar_situacao(obter_nota(aluno)) == "Recuperação")
    reprovados = sum(1 for aluno in alunos if verificar_situacao(obter_nota(aluno)) == "Reprovado")

    print("========== Estatísticas da turma ==========\n")
    print(f"\n Total de alunos: {total_alunos}")
    print(f"\n Aprovados: {aprovados}")
    print(f"\n Recuperação: {recuperacao}")
    print(f"\n Reprovados: {reprovados}")
    print(f"\n Maior nota: {max(obter_nota(aluno) for aluno in alunos)}")
    print(f"\n Menor nota: {min(obter_nota(aluno) for aluno in alunos)}")
    print(f"\n Média da turma: {sum(obter_nota(aluno) for aluno in alunos) / len(alunos)}")

def alunos_por_situacao(alunos, situacao_desejada):
    alunos_filtrados = [aluno for aluno in alunos if verificar_situacao(obter_nota(aluno)) == situacao_desejada]
    if not alunos_filtrados:
        print(f"Nenhum aluno com situação '{situacao_desejada}'.")
        return
    for aluno in alunos_filtrados:
        print(f"Nome: {aluno['nome']}, Nota: {aluno['nota']}\n")
    print(f"Total de alunos com situação '{situacao_desejada}': {len(alunos_filtrados)}")
    print("==========================================")

def consultar_alunos_por_situacao(alunos):
    while True:
        print("Escolha a situação desejada:")
        print("1. Aprovado")
        print("2. Recuperação")
        print("3. Reprovado")
        print("0. Voltar")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            alunos_por_situacao(alunos, "Aprovado")
        elif opcao == "2":
            alunos_por_situacao(alunos, "Recuperação")
        elif opcao == "3":
            alunos_por_situacao(alunos, "Reprovado")
        elif opcao == "0":
            return
        else:
            print("Opção inválida.")
def ordenar_alunos(alunos):
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
            alunos_ordenado = sorted(alunos, key=lambda aluno: obter_nota(aluno), reverse=True)
            alunos_cadastrados(alunos_ordenado)
        elif opcao == "2":
            print("Ordenando alunos por Menor nota\n")
            alunos_ordenado = sorted(alunos, key=lambda aluno: obter_nota(aluno), reverse=False)
            alunos_cadastrados(alunos_ordenado)
        elif opcao == "3":
            print("Ordenando alunos por ordem alfabética A-Z\n")
            alunos_ordenado = sorted(alunos, key=lambda aluno: aluno['nome'])
            alunos_cadastrados(alunos_ordenado)
        elif opcao == "4":
            print("Ordenando alunos por ordem alfabética Z-A\n")
            alunos_ordenado = sorted(alunos, key=lambda aluno: aluno['nome'], reverse=True)
            alunos_cadastrados(alunos_ordenado)
        elif opcao == "0":
            break
        else:
            print("Opção inválida. Tente novamente.")
    
    
    
