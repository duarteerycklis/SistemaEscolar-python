import sqlite3

def conectar_banco():
    conn = sqlite3.connect("escola.db")
    conn.execute("PRAGMA foreign_keys = ON")
    return conn
def criar_tabelas():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS alunos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        idade INTEGER NOT NULL,
        nota REAL NOT NULL
    )
    """)
    conn.commit()
    conn.close()
    criar_tabela_disciplina()
    criar_tabela_aluno_disciplina()

def inserir_aluno(nome, idade, nota):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
    INSERT INTO alunos (nome, idade, nota)
    VALUES (?, ?, ?)
    """, (nome, idade, nota))
    conn.commit()
    conn.close()
def listar_alunos_banco():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, idade, nota FROM alunos")
    alunos = cursor.fetchall()
    conn.close()
    return alunos

def pesquisar_aluno_banco(nome):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome, idade, nota FROM alunos WHERE nome LIKE ?", ('%' + nome + '%',))
    alunos = cursor.fetchall()
    conn.close()
    return alunos
def nome_ja_cadastrado_banco(nome):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM alunos WHERE nome = ?", (nome,))
    aluno = cursor.fetchone()
    conn.close()
    return aluno is not None
def converter_aluno(alunos):
    alunos_convertidos = []
    for aluno in alunos:
        alunos_convertidos.append({
            "id": aluno[0],
            "nome": aluno[1],
            "idade": aluno[2],
            "nota": aluno[3]
        })
    return alunos_convertidos
def atualizar_aluno_banco(id, nome, idade):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE alunos
    SET nome = ?, idade = ?
    WHERE id = ?
    """, (nome, idade, id))
    conn.commit()
    resultado = cursor.rowcount
    conn.close()
    return resultado
def atualizar_nota_banco(id, nota):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
    UPDATE alunos
    SET nota = ?
    WHERE id = ?
    """, (nota, id))
    conn.commit()
    resultado = cursor.rowcount
    conn.close()
    return resultado
def remover_aluno_banco(id):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM alunos WHERE id = ?", (id,))
    conn.commit()
    resultado = cursor.rowcount
    conn.close()
    return resultado
def criar_tabela_disciplina():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS disciplinas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()
def criar_disciplina_banco(nome):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO disciplinas (nome) VALUES (?)", (nome,))
    conn.commit()
    resultado = cursor.rowcount
    conn.close()
    return resultado

def criar_tabela_aluno_disciplina():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS aluno_disciplina (
        aluno_id INTEGER NOT NULL,
        disciplina_id INTEGER NOT NULL,
        nota REAL,
        PRIMARY KEY (aluno_id, disciplina_id),
        FOREIGN KEY (aluno_id) REFERENCES alunos(id),
        FOREIGN KEY (disciplina_id) REFERENCES disciplinas(id)
    )
    """)
    conn.commit()
    conn.close()

def remover_disciplina_banco(id):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM disciplinas WHERE id = ?", (id,))
    conn.commit()
    resultado = cursor.rowcount
    conn.close()
    return resultado

def atualizar_disciplina_banco(id, nome):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("UPDATE disciplinas SET nome = ? WHERE id = ?", (nome, id))
    conn.commit()
    resultado = cursor.rowcount
    conn.close()
    return resultado
def listar_disciplina_banco():
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT id, nome FROM disciplinas")
    disciplinas = cursor.fetchall()
    conn.close()
    return disciplinas
def disciplina_ja_cadastrada(nome):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("SELECT id FROM disciplinas  WHERE nome = ?", (nome,))
    disciplina = cursor.fetchone()
    conn.close()
    return disciplina is not None
def adicionar_disciplinas_aluno_banco(id_aluno, id_disciplina, nota):
    conn = conectar_banco()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO aluno_disciplina (aluno_id, disciplina_id, nota) VALUES (?, ?, ?)",
        (id_aluno, id_disciplina, nota))
    conn.commit()
    resultado = cursor.rowcount
    conn.close()
    return resultado
