from adt import LinkedStack
from adt import UnsortedTableMap
from adt import LinkedBinaryTree
from adt import ProbeHashMap
from func import caricamento_mappe, creaUtenti, login

mappa_film = UnsortedTableMap.UnsortedTableMap()
mappa_serie_tv = UnsortedTableMap.UnsortedTableMap()
tabellaUtenti = ProbeHashMap.ProbeHashMap()
pila = LinkedStack.LinkedStack()
albero = LinkedBinaryTree.LinkedBinaryTree()

def scelta_contenuto():
    print("Vuoi guardare un contenuto presente nella lista?")
    print(" 1 - SI")
    print(" 2 - NO")
    if input("? ") == "1":
        titolo = input("Inserisci il titolo: ")
        if titolo in mappa_film:
            guarda_contenuto_film(mappa_film, titolo)
        elif titolo in mappa_serie_tv:
            guarda_contenuto_serie_tv(mappa_serie_tv, titolo)
        else:
            print(" ERRORE: Contenuto non trovato")
    else:
        print("Ritorno al menu principale...")

def elenco_film_serie_tv():
    print("------------------------ Film ------------------------")
    for titolo in mappa_film:
        print("Titolo:", titolo)
        print("Genere:", mappa_film[titolo].genere)
        print("Durata:", mappa_film[titolo].durata)
        print("Regista:", mappa_film[titolo].regista)
        print("----------------------------------------------------------------")
    print("-------------------------- Serie TV --------------------------")
    for titolo in mappa_serie_tv:
        print("Titolo:", titolo)
        print("Genere:", mappa_serie_tv[titolo].genere)
        print("Durata media di un episodio:", mappa_serie_tv[titolo].durata)
        print("Regista:", mappa_serie_tv[titolo].regista)
        print("Numero episodi:", mappa_serie_tv[titolo].num_episodi)
        print("Numero stagioni:", mappa_serie_tv[titolo].num_stagioni)
        print("----------------------------------------------------------------")
    scelta_contenuto()

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

def continua_a_guardare():
    if not pila.is_empty():
        print("Contenuto presente nella sezione continua a guardare")
        print(pila.top())
        print("Vuoi guardare questo contenuto?")
        print(" 1 - SI")
        print(" 2 - NO")
        scegli = input("? ")
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
    scelta_contenuto()

def stampa_albero_inorder(nodo):
    if nodo is not None:
        figlio_sinistro = albero.left(nodo)
        figlio_destro = albero.right(nodo)
        stampa_albero_inorder(figlio_sinistro)
        print(nodo.element())
        stampa_albero_inorder(figlio_destro)

if __name__ == "__main__":
    caricamento_mappe(mappa_film, mappa_serie_tv)
    creaUtenti(tabellaUtenti)
    print("----------------------------------------------------------------")
    utente = login(tabellaUtenti)

    while True:
        print("\n*** MENU PRINCIPALE ***")
        print(" 1 - Visualizzazione lista dettagliata")
        print(" 2 - Visualizza i film e le serie tv per ordine alfabetico")
        print(" 3 - Continua a guardare")
        print(" 4 - Classifica")
        print(" 5 - Cambia account")
        print(" 6 - Esci")
        scelta = input("? ")

        if scelta == "1":
            elenco_film_serie_tv()
        elif scelta == "2":
            ordinamento(mappa_film, mappa_serie_tv)
        elif scelta == "3":
            continua_a_guardare()
        elif scelta == "4":
            pass # implementare classifica
        elif scelta == "5":
            utente = login(tabellaUtenti)
        elif scelta == "6":
            print("\nUscita dall'applicazione.")
            print("----------------------------------------------------------------")
            exit(0)
        else:
            print("\nERRORE: Scegli un'opzione dal menù.")
