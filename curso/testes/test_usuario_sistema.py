import pytest
import sqlite3
from usuario_sistema import adicionar_usuario, buscar_usuario


@pytest.fixture
def db_connection():
    conn = sqlite3.connect(":memory:")  # cria bd em memória
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE usuarios(
        id INTEGER PRIMARY KEY,
        nome TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """)

    conn.commit()
    yield conn, cursor

    conn.close()


@pytest.mark.parametrize(
    "id, nome, email, esperado_nome",
    [
        (1, "Alice", "alice@example.com", "Alice"),
        (2, "Bob", "bob@example.com", "Bob"),
        (3, "Charlie", "charlie@example.com", "Charlie"),
    ]
)
@pytest.mark.unit
def test_adicionar_usuario(db_connection, id, nome, email, esperado_nome):
    _, cursor = db_connection
    adicionar_usuario(cursor, id, nome, email)
    resultado = buscar_usuario(cursor, email)

    assert resultado is not None
    assert resultado[1] == esperado_nome
    assert resultado[2] == email


@pytest.mark.integration
def test_buscar_usuario_com_email_inexistente(db_connection):
    _, cursor = db_connection
    resultado = buscar_usuario(cursor, "emailinexistente@email.com")

    assert resultado is None


@pytest.mark.slow
@pytest.mark.integration
def test_adicionar_e_buscar_varios_usuarios(db_connection):
    import time
    conn, cursor = db_connection

    for i in range(100):
        adicionar_usuario(cursor, i, f"User{i}", f"user{i}@example.com")
    conn.commit()

    time.sleep(3)

    for i in range(100):
        resultado = buscar_usuario(cursor, f"user{i}@example.com")

        assert resultado is not None
        assert resultado[1] == f"User{i}"
        assert resultado[2] == f"user{i}@example.com"
