import sqlite3


def conectar():
    return sqlite3.connect('curso/app_web_sqlite/titulo.db')


def inserir(nome, ano, nota):
    conexao = conectar()
    conexao.cursor().execute(
        """
        INSERT INTO filmes(nome, ano, nota)
        VALUES(?, ?, ?)
        """,
        (nome, ano, nota)
    )

    conexao.commit()
    conexao.close()


def obter_dados():
    cursor = conectar().cursor()
    cursor.execute("SELECT * FROM filmes")
    dados = cursor.fetchall()
    cursor.close()

    return dados
