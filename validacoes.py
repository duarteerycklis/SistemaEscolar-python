def notas_validas(mensagem):
    while True:
        try:
            nota = float(input(mensagem))
            if 0 <= nota <= 10:
                return nota
            else:
                print("Digite uma nota válida (0 a 10).")
        except ValueError:
            print("Digite um número válido.")

def validar_idade(mensagem):

    while True:
        try:
            idade = int(input(mensagem))
            if 0 <= idade <= 120:
                return idade
            else:
                print("Digite uma idade válida (0 a 120).")
        except ValueError:
            print("Digite um número válido.")
        
    # Função para validar se a idade está entre 0 e 120

def disciplinas_validas(mensagem):
    while True:
        nome = input(mensagem).strip()
        if nome:
            return nome
        else:
            print("O nome da disciplina não pode ficar vazio.")