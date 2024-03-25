from flask import Flask, render_template, request

from musica import Musica
from musica_dao import MusicaDao

app = Flask(__name__)
musica_dao = MusicaDao()

@app.route('/', methods=["GET", "POST"])
def list():
    if request.method == "POST":
        dados = request.form.to_dict()
        nova_musica = Musica(titulo=dados.get("titulo"), duracao=dados.get("duracao"), genero=dados.get("genero"), artista=dados.get("artista"), compositor=dados.get("compositor"))
        musica_dao.inserir(nova_musica)
    musicas = musica_dao.ler_todos()
    return render_template("list.html", musicas=musicas)


if __name__ == '__main__':
    app.run()
