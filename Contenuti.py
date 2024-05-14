class ContenutoFilm:
    def __init__(self,genere,durata,regista):
        self.genere = genere
        self.durata = durata
        self.regista = regista

class ContenutoSerieTv:
    def __init__(self,genere,durata,regista,num_episodi,num_stagioni):
        self.genere = genere
        self.durata = durata
        self.regista = regista
        self.num_episodi = num_episodi
        self.num_stagioni = num_stagioni

class Utente:
    def __init__(self, nome, email, password):
        self.nome = nome
        self.email = email
        self.password = password
