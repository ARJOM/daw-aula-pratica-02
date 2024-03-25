import sqlite3


def init_db():
    conn = sqlite3.connect("sound")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS musicas(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        titulo VARCHAR(255) NOT NULL,
        compositor VARCHAR(255) NOT NULL,
        artista VARCHAR(255) NOT NULL,
        genero VARCHAR(255) NOT NULL,
        duracao VARCHAR(4) NOT NULL
        )
    """)

    conn.close()

if __name__ == "__main__":
    init_db()