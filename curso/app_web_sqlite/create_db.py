import sqlite3

cursor = sqlite3.connect('titulo.db').cursor()
cursor.execute(
    """
    CREATE TABLE filmes(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        ano INTEGER NOT NULL,
        nota INTEGER NOT NULL
    )
    """
)

cursor.close()
print("Tabela criada!")