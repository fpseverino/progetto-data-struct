import Contenuti
from adt import SortedPriorityQueue

def caricamento_mappe(mappa_film, mappa_serie_tv):
    file = open("film.txt", "r")
    for line in file:
        if line.startswith("Titolo:"):
            titolo = line.split(":")[1]
            titolo = titolo.split("\n")[0]
        elif line.startswith("Genere:"):
            genere = line.split(":")[1]
            genere = genere.split("\n")[0]
        elif line.startswith("Durata:"):
            durata = line.split(":")[1]
            durata = durata.split("\n")[0]
        elif line.startswith("Regista:"):
            regista = line.split(":")[1]
            regista = regista.split("\n")[0]
            contenutiFilm = Contenuti.Film(genere, durata, regista)
            mappa_film[titolo] = contenutiFilm
    file.close()

    file = open("serietv.txt", "r")
    for line in file:
        if line.startswith("Titolo:"):
            titolo = line.split(":")[1]
            titolo = titolo.split("\n")[0]
        elif line.startswith("Genere:"):
            genere = line.split(":")[1]
            genere = genere.split("\n")[0]
        elif line.startswith("Durata:"):
            durata = line.split(":")[1]
            durata = durata.split("\n")[0]
        elif line.startswith("Regista:"):
            regista = line.split(":")[1]
            regista = regista.split("\n")[0]
        elif line.startswith("Numero episodi:"):
            num_episodi = line.split(":")[1]
            num_episodi = num_episodi.split("\n")[0]
        elif line.startswith("Numero stagioni:"):
            num_stagioni = line.split(":")[1]
            num_stagioni = num_stagioni.split("\n")[0]
            contenutoSerie = Contenuti.SerieTv(genere, durata, regista, num_episodi, num_stagioni)
            mappa_serie_tv[titolo] = contenutoSerie
    file.close()

def creaUtenti(tabellaUtenti):
    utente1, password1 = Contenuti.Utente("Mario", "mario@email.com", SortedPriorityQueue.SortedPriorityQueue()), "password"
    utente2, password2 = Contenuti.Utente("Luigi", "luigi@email.com", SortedPriorityQueue.SortedPriorityQueue()), "1234"
    utente3, password3 = Contenuti.Utente("Bowser", "bowser@email.com", SortedPriorityQueue.SortedPriorityQueue()), "peach"
    tabellaUtenti[password1] = utente1
    tabellaUtenti[password2] = utente2
    tabellaUtenti[password3] = utente3

def login(tabellaUtenti):
    password = input("Inserisci la password: ")
    while password not in tabellaUtenti:
        print(" ERRORE: Password non trovata.\n")
        password = input("Inserisci la password: ")
    utente = tabellaUtenti[password]
    print("\nBenvenuto {}!".format(utente.nome))
    return utente