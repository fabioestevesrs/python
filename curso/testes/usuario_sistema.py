def adicionar_usuario(cursor, id, nome, email):
    cursor.execute("""
    INSERT INTO usuarios(id, nome, email) VALUES(?, ?, ?)
    """, (id, nome, email))


def buscar_usuario(cursor, email):
    cursor.execute("SELECT * FROM usuarios WHERE email = ?", (email,))

    return cursor.fetchone()
