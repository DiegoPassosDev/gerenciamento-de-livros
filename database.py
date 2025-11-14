import sqlite3

# Gerar ou conectar conexão com o banco de dados SQLite
connection = sqlite3.connect('database.db')

# Gerar tabela de livros
connection.execute('CREATE TABLE livros( \
                    id INTEGER PRIMARY KEY, \
                    titulo TEXT, \
                    autor TEXT, \
                    editora TEXT, \
                    ano_publicacao INTEGER, \
                    isbn TEXT)'
                   )

# Gerar tabela de usuários
connection.execute('CREATE TABLE usuarios( \
                    id INTEGER PRIMARY KEY, \
                    nome TEXT, \
                    sobrenome TEXT, \
                    endereco TEXT, \
                    email TEXT, \
                    telefone TEXT)'
                   )

# Gerar tabela de empréstimos
connection.execute('CREATE TABLE emprestimos( \
                    id INTEGER PRIMARY KEY, \
                    livro_id INTEGER, \
                    usuario_id INTEGER, \
                    data_emprestimo TEXT, \
                    data_devolucao TEXT, \
                    FOREIGN KEY(livro_id) REFERENCES livros(id), \
                    FOREIGN KEY(usuario_id) REFERENCES usuarios(id))'
                   )
