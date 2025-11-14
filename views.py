import sqlite3


# Conectar ao banco de dados SQLite
def get_db_connection():
    connection = sqlite3.connect("database.db")
    return connection


# Funções para os livros
def create_book(titulo, autor, editora, ano_publicacao, isbn):
    connection = get_db_connection()
    connection.execute(
        "INSERT INTO livros (titulo, autor, editora,         ano_publicacao,isbn)\
                      VALUES (?, ?, ?, ?, ?)",
        (titulo, autor, editora, ano_publicacao, isbn),
    )
    connection.commit()
    connection.close()


def delete_book(book_id):
    connection = get_db_connection()
    connection.execute("DELETE FROM livros WHERE id = ?", (book_id,))
    connection.commit()
    connection.close()


def read_books():
    connection = get_db_connection()
    books = connection.execute("SELECT * FROM livros").fetchall()
    connection.close()
    return books


def update_book(book_id, titulo, autor, editora, ano_publicacao, isbn):
    connection = get_db_connection()
    connection.execute(
        "UPDATE livros SET titulo = ?, autor = ?, editora = ?, ano_publicacao = ?, isbn = ? \
                      WHERE id = ?",
        (titulo, autor, editora, ano_publicacao, isbn, book_id),
    )
    connection.commit()
    connection.close()


# Funções para os usuários
def create_user(nome, sobrenome, endereco, email, telefone):
    connection = get_db_connection()
    connection.execute(
        "INSERT INTO usuarios (nome, sobrenome, endereco, email, telefone) \
                      VALUES (?, ?, ?, ?, ?)",
        (nome, sobrenome, endereco, email, telefone),
    )
    connection.commit()
    connection.close()


def delete_user(user_id):
    connection = get_db_connection()
    connection.execute("DELETE FROM usuarios WHERE id = ?", (user_id,))
    connection.commit()
    connection.close()


def read_users():
    connection = get_db_connection()
    users = connection.execute("SELECT * FROM usuarios").fetchall()
    connection.close()
    return users


def update_user(user_id, nome, sobrenome, endereco, email, telefone):
    connection = get_db_connection()
    connection.execute(
        "UPDATE usuarios SET nome = ?, sobrenome = ?, endereco = ?, email = ?, telefone = ? \
                      WHERE id = ?",
        (nome, sobrenome, endereco, email, telefone, user_id),
    )
    connection.commit()
    connection.close()


def check_book_exists(book_id):
    connection = get_db_connection()
    book = connection.execute(
        "SELECT id FROM livros WHERE id = ?", (book_id,)
    ).fetchone()
    connection.close()
    return book is not None


def check_user_exists(user_id):
    connection = get_db_connection()
    user = connection.execute(
        "SELECT id FROM usuarios WHERE id = ?", (user_id,)
    ).fetchone()
    connection.close()
    return user is not None


def check_loan_exists(loan_id):
    connection = get_db_connection()
    loan = connection.execute(
        "SELECT id FROM emprestimos WHERE id = ?", (loan_id,)
    ).fetchone()
    connection.close()
    return loan is not None


# Funções para os empréstimos
def create_loan(livro_id, usuario_id, data_emprestimo, data_devolucao):
    connection = get_db_connection()
    connection.execute(
        "INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo, data_devolucao) \
                      VALUES (?, ?, ?, ?)",
        (livro_id, usuario_id, data_emprestimo, data_devolucao),
    )
    connection.commit()
    connection.close()


def delete_loan(loan_id):
    connection = get_db_connection()
    connection.execute("DELETE FROM emprestimos WHERE id = ?", (loan_id,))
    connection.commit()
    connection.close()


def read_loans():
    connection = get_db_connection()
    loans = connection.execute(
        "SELECT emprestimos.id, livros.titulo, usuarios.nome || ' ' || usuarios.sobrenome, emprestimos.data_emprestimo, emprestimos.data_devolucao \
                               FROM livros \
                               INNER JOIN emprestimos ON livros.id = emprestimos.livro_id \
                               INNER JOIN usuarios ON usuarios.id = emprestimos.usuario_id"
    ).fetchall()
    connection.close()
    return loans


def update_loan_return(loan_id, date_return):
    connection = get_db_connection()
    connection.execute(
        "UPDATE emprestimos SET data_devolucao = ? WHERE id = ?", (date_return, loan_id)
    )
    connection.commit()
    connection.close()


# testando função de ver os livros
