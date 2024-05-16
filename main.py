import adt.LinkedStack as LinkedStack
import adt.UnsortedTableMap as UnsortedTableMap
import Contenuti
import adt.LinkedBinaryTree as Linked_binary_tree

mappa_film = UnsortedTableMap.UnsortedTableMap()
mappa_serie_tv = UnsortedTableMap.UnsortedTableMap()
pila = LinkedStack.LinkedStack()
albero = Linked_binary_tree.LinkedBinaryTree()


def caricamento_mappa():
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
def elenco_film_serie_tv():

    file = open("film.txt", "r")

    print("------------------------Film-------------------------")

    for k in mappa_film:
        print("Titolo:", k)
        print("Genere:", mappa_film[k].genere)
        print("Durata:", mappa_film[k].durata)
        print("Regista:", mappa_film[k].regista)
        print("-----------------------------------------------------")


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
    else:
        print("Scelta non valida")


def ordinamento_alfabetico(titolo):
    if albero.root() is None:
        albero.add_root(titolo)
        return

    current = albero.root()
    while True:
        nodo = current.element()
        if titolo == nodo:
            return
        elif titolo < nodo:
            if albero.left(current) is None:
                albero.add_left(current, titolo)
                return
            else:
                current = albero.left(current)
        else:
            if albero.right(current) is None:
                albero.add_right(current, titolo)
                return
            else:
                current = albero.right(current)


def ordinamento(mappa_film, mappa_serie_tv):
    for k in mappa_film:
        ordinamento_alfabetico(k)
    for k in mappa_serie_tv:
        ordinamento_alfabetico(k)
    stampa_albero_inorder(albero.root())


def stampa_albero_inorder(nodo):
    if nodo is not None:
        figlio_sinistro = albero.left(nodo)
        figlio_destro = albero.right(nodo)
        stampa_albero_inorder(figlio_sinistro)
        print(nodo.element())
        stampa_albero_inorder(figlio_destro)


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
        if len(pila) != 0:
            pila.pop()


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
        if len(pila) != 0:
            pila.pop()

    # Codice per i correlati con albero binario


# def classifica():
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
        print("2. Visualizza i film e le serie tv per ordine alfabetico")
        print("2. Visualizza i continua a guardare")
        print("3. Classifica")
        print("4. Esci")

        scelta = input()
        if scelta == "1":
            caricamento_mappa()
            elenco_film_serie_tv()
        elif scelta == "2":
            caricamento_mappa()
            ordinamento(mappa_film, mappa_serie_tv)
        elif scelta == "3":
            continua_a_guardare()
        elif scelta == "4":
            # implementare classifica
            elenco_film_serie_tv()
        elif scelta == "5":
            exit(0)
        else:
            print("Scelta non valida")

