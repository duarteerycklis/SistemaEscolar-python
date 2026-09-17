import sqlite3

def conectar_banco():
    return sqlite3.connect("escola.db")
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
def converter_alunos(alunos):
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
