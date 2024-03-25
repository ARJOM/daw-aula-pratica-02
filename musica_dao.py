import sqlite3

from musica import Musica


class MusicaDao:

    def __init__(self):
        self.conn = None

    def get_conn(self):
        self.conn = sqlite3.connect("sound")

    def close_conn(self):
        self.conn.close()
        self.conn = None

    def inserir(self, musica: Musica):
        self.get_conn()
        cursor = self.conn.cursor()

        cursor.execute(
            f"""
            INSERT INTO musicas(titulo, duracao, artista, compositor, genero)
            VALUES ('{musica.get_titulo()}', '{musica.get_duracao()}', '{musica.get_artista()}', '{musica.get_compositor()}', '{musica.get_genero()}')
            """
        )

        self.conn.commit()
        self.close_conn()

    def ler_por_id(self, id: int):
        self.get_conn()
        cursor = self.conn.cursor()

        valor = cursor.execute(f"SELECT titulo, duracao, genero, compositor, artista, id FROM musicas WHERE id={id}")
        item = valor.fetchone()
        musica = Musica(item[0], item[1], item[2], item[3], item[4], item[5])
        self.close_conn()
        return musica

    def ler_todos(self):
        self.get_conn()
        cursor = self.conn.cursor()

        valores = cursor.execute("SELECT titulo, duracao, genero, compositor, artista, id FROM musicas")
        itens = valores.fetchall()
        musicas = []
        for item in itens:
            musica = Musica(item[0], item[1], item[2], item[3], item[4], item[5])
            musicas.append(musica)
        self.close_conn()
        return musicas