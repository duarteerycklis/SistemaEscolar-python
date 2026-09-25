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

Descrição dos arquivos

main.py
Responsável pelo menu principal e pela interação com o usuário.

banco.py
Responsável pela conexão com o banco de dados SQLite, criação das tabelas e operações de inserção, consulta, atualização e remoção.

alunos.py
Contém as funcionalidades relacionadas aos alunos, como cadastro, atualização, remoção, notas e situação.

disciplinas.py
Responsável pelo gerenciamento das disciplinas e pela associação entre alunos e disciplinas.

estatisticas.py
Contém as funcionalidades de estatísticas, classificação e ordenação dos alunos.

exibicao.py
Responsável pela apresentação das informações dos alunos.

validacoes.py
Contém as funções utilizadas para validar entradas, como idade e notas.

Banco de dados

O sistema utiliza SQLite para armazenar os dados.

O arquivo escola.db é criado automaticamente quando o sistema é executado.

Os arquivos do banco de dados não são versionados no GitHub, pois estão configurados no .gitignore.

Como executar
1. Clone o repositório
git clone URL_DO_SEU_REPOSITORIO
2. Entre na pasta
cd SistemaEscolar-python
3. Execute o sistema
python main.py

O banco de dados será criado automaticamente na primeira execução.

Objetivo do projeto

Este projeto foi desenvolvido com o objetivo de praticar conceitos de programação em Python, organização de código, modularização, persistência de dados com SQLite e utilização do Git e GitHub para controle de versão.

Autor

Erycklis Duarte

Projeto desenvolvido para fins acadêmicos e de aprendizado em desenvolvimento de software.
