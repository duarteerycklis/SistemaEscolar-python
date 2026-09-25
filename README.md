# Sistema de Cadastro de Alunos

Sistema de gerenciamento escolar desenvolvido em Python, com armazenamento de dados utilizando SQLite.

O projeto permite cadastrar e gerenciar alunos, disciplinas, notas e realizar diferentes consultas e estatísticas.

## Funcionalidades

### Alunos
- Cadastrar aluno
- Listar alunos
- Pesquisar aluno
- Atualizar dados do aluno
- Remover aluno
- Atualizar nota
- Consultar situação do aluno
- Calcular média da turma

### Disciplinas
- Cadastrar disciplinas
- Associar disciplinas aos alunos
- Atualizar nota de uma disciplina
- Remover disciplina de um aluno
- Consultar nota de uma disciplina
- Consultar situação da disciplina

### Estatísticas
- Estatísticas da turma
- Estatísticas de uma disciplina
- Estatísticas de todas as disciplinas
- Consultar alunos por situação
- Ordenar alunos por:
  - Maior nota
  - Menor nota
  - Ordem alfabética A-Z
  - Ordem alfabética Z-A

## Tecnologias utilizadas

- Python
- SQLite
- Git
- GitHub

## Estrutura do projeto

```text
SistemaEscolar-python/
│
├── main.py
├── banco.py
├── alunos.py
├── disciplinas.py
├── estatisticas.py
├── exibicao.py
├── validacoes.py
├── README.md
└── .gitignore
