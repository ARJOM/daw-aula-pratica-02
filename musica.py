class Musica:
    """
    Classe que representa uma música no banco de dados do sistema
    """

    def __init__(self, titulo, duracao, genero, compositor, artista, id=None):
        self.__titulo = titulo
        self.__duracao = duracao
        self.__genero = genero
        self.__compositor = compositor
        self.__artista = artista
        self.__id = id

    def get_id(self):
        return self.__id

    def set_id(self, id):
        self.__id = id

    def get_titulo(self):
        return self.__titulo

    def set_titulo(self, titulo):
        self.__titulo = titulo

    def get_duracao(self):
        return self.__duracao

    def set_duracao(self, duracao):
        self.__duracao = duracao

    def get_genero(self):
        return self.__genero

    def set_genero(self, genero):
        self.__genero = genero

    def get_artista(self):
        return self.__artista

    def set_artista(self, artista):
        self.__artista = artista

    def get_compositor(self):
        return self.__compositor

    def set_compositor(self, compositor):
        self.__compositor = compositor

    def __str__(self):
        return f"Título: {self.__titulo} \n" \
               f"Artista: {self.__artista} \n" \
               f"Compositor: {self.__compositor} \n" \
               f"Gênero: {self.__genero} \n" \
               f"Duração: {self.__duracao}"

if __name__=="__main__":
    musica = Musica("Red", "3:41", "Pop", "Taylor Swift", "Taylor Swift")
    print(musica)