import Contenuti
import random
from adt import PositionalList

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
            visualizzazioni = random.randint(1000, 1500)
            contenuti_film = Contenuti.Film(genere, durata, regista,visualizzazioni)
            mappa_film[titolo] = contenuti_film
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
            visualizzazioni = random.randint(1000, 1500)
            contenuto_serie = Contenuti.SerieTv(genere, durata, regista, num_episodi, visualizzazioni)
            mappa_serie_tv[titolo] = contenuto_serie
    file.close()

def crea_utenti(tabella_utenti):
    utente1, password1 = Contenuti.Utente("Mario", "mario@email.com", PositionalList.PositionalList()), "password"
    utente2, password2 = Contenuti.Utente("Luigi", "luigi@email.com", PositionalList.PositionalList()), "1234"
    utente3, password3 = Contenuti.Utente("Bowser", "bowser@email.com", PositionalList.PositionalList()), "peach"
    tabella_utenti[password1] = utente1
    tabella_utenti[password2] = utente2
    tabella_utenti[password3] = utente3

def login(tabella_utenti):
    print("Benvenuto! Accedi o registrati per continuare.")
    print(" 1 - Accedi")
    print(" 2 - Registrati")
    scelta = input("? ")
    while scelta != "1" and scelta != "2":
        print("\nERRORE: Scelta non valida.")
        print(" 1 - Accedi")
        print(" 2 - Registrati")
        scelta = input("? ")
    if scelta == "1":
        password = input("\nInserisci la password: ")
        while password not in tabella_utenti:
            print(" ERRORE: Password non trovata.\n")
            password = input("Inserisci la password: ")
        utente = tabella_utenti[password]
        print("\nBenvenuto {}!".format(utente.nome))
        return utente
    else:
        nome = input("\nInserisci il tuo nome: ")
        email = input("Inserisci la tua email: ")
        password = input("Inserisci una password: ")
        while password in tabella_utenti:
            print("\n ERRORE: Password già in uso.")
            password = input("Inserisci una password: ")
        utente = Contenuti.Utente(nome, email, PositionalList.PositionalList())
        tabella_utenti[password] = utente
        print("\nBenvenuto {}!".format(utente.nome))
        return utente