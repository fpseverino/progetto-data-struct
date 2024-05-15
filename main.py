import adt.LinkedStack as LinkedStack
import adt.UnsortedTableMap as UnsortedTableMap
import Contenuti
import adt.albero_binario as albero_binario
import adt.ProbeHashMap as ProbeHashMap

mappa_film = UnsortedTableMap.UnsortedTableMap()
mappa_serie_tv = UnsortedTableMap.UnsortedTableMap()
tabellaUtenti = ProbeHashMap.ProbeHashMap()
pila = LinkedStack.LinkedStack()
correlati = albero_binario.BinaryTree()

def elenco_film_serie_tv():
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
            contenutiFilm = Contenuti.ContenutoFilm(genere, durata, regista)
            mappa_film[titolo] = contenutiFilm
    print("---------------------------- Film -----------------------------")

    for k in mappa_film:
        print("Titolo:", k)
        print("Genere:", mappa_film[k].genere)
        print("Durata:", mappa_film[k].durata)
        print("Regista:", mappa_film[k].regista)
        print("----------------------------------------------------------------")
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
            contenutoSerie = Contenuti.ContenutoSerieTv(genere, durata, regista, num_episodi, num_stagioni)
            mappa_serie_tv[titolo] = contenutoSerie
    file.close()
    print("-------------------------- Serie TV ---------------------------")

    for k in mappa_serie_tv:
        print("Titolo:", k)
        print("Genere:", mappa_serie_tv[k].genere)
        print("Durata media di un episodio:", mappa_serie_tv[k].durata)
        print("Regista:", mappa_serie_tv[k].regista)
        print("Numero episodi:", mappa_serie_tv[k].num_episodi)
        print("Numero stagioni:", mappa_serie_tv[k].num_stagioni)
        print("----------------------------------------------------------------")

    print("Vuoi guardare un contenuto presente nella lista?")
    print(" 1 - SI")
    print(" 2 - NO")
    scegli = input("? ")
    if scegli == "1":
        print("Cosa vuoi guardare?")
        titolo = input()
        for k in mappa_film:
            if k == titolo:
                guarda_contenuto_film(mappa_film, k)

        for k in mappa_serie_tv:
            if k == titolo:
                guarda_contenuto_serie_tv(mappa_serie_tv, k)
            elif k != titolo:
                continue
            else:
                print("Contenuto non trovato")
    else:
        print("\nRitorno al menu principale...")

def guarda_contenuto_film(mappa_film, k):
    print("Il film ha una durata di:", mappa_film[k].durata, "minuti")
    print("Quanti minuti del film vuoi guardare?")
    minuti_da_guardare = int(input())
    if minuti_da_guardare > int(mappa_film[k].durata):
        print("Durata non valida")
    elif minuti_da_guardare < int(mappa_film[k].durata):
        print("Contenuto aggiunto alla sezione continua a guardare")
        # inserire qui il codice per pila
        pila.push(k)
    else:
        pila.pop()

    # codice per i correlati con albero binario

def guarda_contenuto_serie_tv(mappa_serie_tv, k):
    print("La serie è formata da:", mappa_serie_tv[k].num_episodi, "episodi")
    print("Quanti episodi vuoi guardare?")
    episodi_da_guardare = int(input())
    if episodi_da_guardare > int(mappa_serie_tv[k].num_episodi):
        print("Numero di episodi non valido")
    elif episodi_da_guardare < int(mappa_serie_tv[k].num_episodi):
        print("Contenuto aggiunto alla sezione continua a guardare")
        pila.push(k)
        # inserire qui il codice per pila
    else:
        pila.pop()

    # Codice per i correlati con albero binario

def continua_a_guardare():
    if not pila.is_empty():
        print("Contenuto presente nella sezione continua a guardare")
        print(pila.top())
        print("Vuoi guardare questo contenuto?")
        print(" 1 - SI")
        print(" 2 - NO")
        scegli = input()
        if scegli == "1":
            elemento = pila.top()
            if elemento in mappa_film:
                guarda_contenuto_film(mappa_film, elemento)
            else:
                guarda_contenuto_serie_tv(mappa_serie_tv, elemento)
        else:
            print("\nRitorno al menu principale...")
    else:
        print("\nNessun contenuto presente nella sezione continua a guardare.")
        print("Ritorno al menu principale...")

def creaUtenti():
    utente1 = Contenuti.Utente("Mario", "mario@email.com", "password")
    utente2 = Contenuti.Utente("Luigi", "luigi@email.com", "1234")
    utente3 = Contenuti.Utente("Bowser", "bowser@email.com", "peach")
    tabellaUtenti[utente1.password] = utente1
    tabellaUtenti[utente2.password] = utente2
    tabellaUtenti[utente3.password] = utente3

if __name__ == "__main__":
    creaUtenti()
    print("----------------------------------------------------------------")
    password = input("Inserisci la password: ")
    while password not in tabellaUtenti:
        print(" ERRORE: Password non trovata.")
        password = input("Inserisci la password: ")
    utente = tabellaUtenti[password]
    print("Benvenuto {}!".format(utente.nome))

    while True:
        print("\n*** MENU PRINCIPALE ***")
        print(" 1 - Visualizzazione lista dettagliata")
        print(" 2 - Continua a guardare")
        print(" 3 - Classifica")
        print(" 4 - Cambia account")
        print(" 5 - Esci")
        scelta = input("? ")

        if scelta == "1":
            elenco_film_serie_tv()
        elif scelta == "2":
            continua_a_guardare()
        elif scelta == "3":
            print("\nUscita dall'applicazione.")
            print("----------------------------------------------------------------")
            exit(0)
        elif scelta == "4":
            password = input("Inserisci la password: ")
            while password not in tabellaUtenti:
                print(" ERRORE: Password non trovata.")
                password = input("Inserisci la password: ")
            utente = tabellaUtenti[password]
            print("Benvenuto {}!".format(utente.nome))
        elif scelta == "5":
            print("\nUscita dall'applicazione.")
            print("----------------------------------------------------------------")
            exit(0)
        else:
            print("\nERRORE: Scegli un'opzione dal menù.")