import LinkedStack
import UnsortedTableMap
import Contenuti

mappa_film = UnsortedTableMap.UnsortedTableMap()
mappa_serie_tv = UnsortedTableMap.UnsortedTableMap()
pila = LinkedStack.LinkedStack()

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
            contenutifilm = Contenuti.ContenutoFilm(genere, durata, regista)
            mappa_film.__setitem__(titolo, contenutifilm)

    print("------------------------Film-------------------------")

    for k in mappa_film:
        print("Titolo:", k)
        print("Genere:", mappa_film[k].genere)
        print("Durata:", mappa_film[k].durata)
        print("Regista:", mappa_film[k].regista)
        print("-----------------------------------------------------")

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
            contenutoserie = Contenuti.ContenutoSerieTv(genere, durata, regista, num_episodi, num_stagioni)
            mappa_serie_tv.__setitem__(titolo, contenutoserie)
    file.close()
    print("---------------------Serie Tv:-----------------------")

    for k in mappa_serie_tv:
        print("Titolo:", k)
        print("Genere:", mappa_serie_tv[k].genere)
        print("Durata media di un episodio:", mappa_serie_tv[k].durata)
        print("Regista:", mappa_serie_tv[k].regista)
        print("Numero episodi:", mappa_serie_tv[k].num_episodi)
        print("Numero stagioni:", mappa_serie_tv[k].num_stagioni)
        print("-----------------------------------------------------")

    print("Vuoi guardare un contenuto presente nella lista?")
    print("1. SI")
    print("2. NO")
    scegli = input()
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
    elif scegli == "2":
        print("Arrivederci")
        exit(0)
    else :
        print("Scelta non valida")


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
        print("Contenuto aggiunto nella cronologia")
        # inserire qui il codice per lista posizionale

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
        print("Contenuto aggiunto nella cronologia")
        # inserire qui il codice per lista posizionale

    # Codice per i correlati con albero binario


def continua_a_guardare():

    if not pila.is_empty():
        print("Contenuto presente nella sezione continua a guardare")
        print(pila.top())
        print("Vuoi guardare questo contenuto?")
        print("1. SI")
        print("2. NO")
        scegli = input()
        if scegli == "1":
            elemento = pila.top()
            if elemento in mappa_film:
                guarda_contenuto_film(mappa_film, elemento)
            else:
                guarda_contenuto_serie_tv(mappa_serie_tv, elemento)
        else:
            print("Arrivederci")

    else:
        print("Nessun contenuto presente nella sezione continua a guardare")


if __name__ == "__main__":
    print("Ciao, benvenuto ti mostreremo la lista di tutti i film e le serie tv, adesso procederemo con il login "
          "all'applicazione")

    # implementare login con tabella hash
    # implementare Coda prioritaria degli utenti nella schermata iniziale

    print("Login effettuato con successo")
    while True:
        print("---------------------MENU-----------------------")
        print("scegli una voce nel menù")
        print("1. Visualizzazione lista dettagliata")
        print("2. Visualizzazione cronologia")
        print("3. Visualizza i continua a guardare")
        print("4. Classifica")
        print("5. Esci")

        scelta = input()
        if scelta == "1":
            elenco_film_serie_tv()
        elif scelta == "2":
            # implementare cronologia
            elenco_film_serie_tv()
        elif scelta == "3":
            # implementare Continua a guardare
            continua_a_guardare()
        elif scelta == "4":
            # implementare classifica
            elenco_film_serie_tv()
        elif scelta == "5":
            exit(0)
        else:
            print("Scelta non valida")