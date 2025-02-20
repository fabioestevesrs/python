import pytest
import sqlite3


@pytest.fixture
def db_connection():
    conn = sqlite3.connect(":memory:")  # cria bd em memória
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE users(
        id INTEGER PRIMARY KEY,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """)

    conn.commit()
    yield conn, cursor

    conn.close()


def test_database_insert(db_connection):
    conn, cursor = db_connection
    cursor.execute("""
   INSERT INTO users(name, email) VALUES(?, ?)
   """, ("Maria", "maria@email.com"))

    conn.commit()

    cursor.execute("SELECT * FROM users WHERE email = ?", ("maria@email.com",))
    user = cursor.fetchone()
    assert user is not None
    assert user[1] == "Maria"
    assert user[2] == "maria@email.com"


def test_database_no_duplicate_emails(db_connection):
    conn, cursor = db_connection
    cursor.execute("""
       INSERT INTO users(name, email) VALUES(?, ?)
       """, ("Baiano", "baiano@email.com"))

    conn.commit()

    with pytest.raises(sqlite3.IntegrityError):
        cursor.execute("""
               INSERT INTO users(name, email) VALUES(?, ?)
               """, ("Baiano Duplicado", "baiano@email.com"))

        conn.commit()
