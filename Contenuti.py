class Film:
    def __init__(self, genere, durata, regista, visualizzazioni):
        self.genere = genere
        self.durata = durata
        self.regista = regista
        self.visualizzazioni = visualizzazioni

class SerieTv:
    def __init__(self, genere, durata, regista, num_episodi, visualizzazioni):
        self.genere = genere
        self.durata = durata
        self.regista = regista
        self.num_episodi = num_episodi
        self.visualizzazioni = visualizzazioni

class Utente:
    def __init__(self, nome, email, continuaAGuardare):
        self.nome = nome
        self.email = email
        self.continuaAGuardare = continuaAGuardare
