class Film:
    def __init__(self, genere, durata, regista):
        self.genere = genere
        self.durata = durata
        self.regista = regista

class SerieTv:
    def __init__(self, genere, durata, regista, num_episodi):
        self.genere = genere
        self.durata = durata
        self.regista = regista
        self.num_episodi = num_episodi

class Utente:
    def __init__(self, nome, email, continuaAGuardare):
        self.nome = nome
        self.email = email
        self.continuaAGuardare = continuaAGuardare
