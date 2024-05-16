from adt import UnsortedTableMap
from adt import LinkedBinaryTree
from adt import ProbeHashMap
from adt import LinkedStack
from func import caricamento_mappe, creaUtenti, login

mappa_film = UnsortedTableMap.UnsortedTableMap()
mappa_serie_tv = UnsortedTableMap.UnsortedTableMap()
tabellaUtenti = ProbeHashMap.ProbeHashMap()
utente = None
albero = LinkedBinaryTree.LinkedBinaryTree()

def scelta_contenuto():
    print()
    titolo = input("Inserisci il titolo del contenuto da guardare ('n' per uscire): ")
    if titolo == "n":
        print("Ritorno al menu principale...")
        return
    if titolo in mappa_film:
        guarda_film(mappa_film, titolo)
    elif titolo in mappa_serie_tv:
        guarda_serie_tv(mappa_serie_tv, titolo)
    else:
        print(" ERRORE: Contenuto non trovato")

def elenco_film_serie_tv():
    print("\n----------------------------- Film -----------------------------")
    for titolo in mappa_film:
        print("Titolo:", titolo)
        print("Genere:", mappa_film[titolo].genere)
        print("Durata:", mappa_film[titolo].durata)
        print("Regista:", mappa_film[titolo].regista)
        print("----------------------------------------------------------------")
    print("--------------------------- Serie TV ---------------------------")
    for titolo in mappa_serie_tv:
        print("Titolo:", titolo)
        print("Genere:", mappa_serie_tv[titolo].genere)
        print("Durata media di un episodio:", mappa_serie_tv[titolo].durata)
        print("Regista:", mappa_serie_tv[titolo].regista)
        print("Numero episodi:", mappa_serie_tv[titolo].num_episodi)
        print("Numero stagioni:", mappa_serie_tv[titolo].num_stagioni)
        print("----------------------------------------------------------------")
    scelta_contenuto()

def rimuovi_da_continua_a_guardare(titolo):
    print("\nContenuto in rimozione.") # DEBUG
    posizione = utente.continuaAGuardare.first()
    for _ in range(0, len(utente.continuaAGuardare)):
        titolo_i, _ = posizione.element()
        print("Titolo:", titolo_i) # DEBUG
        if titolo_i == titolo:
            print("Sono uguali.") # DEBUG
            utente.continuaAGuardare.delete(posizione)
            break
        posizione = utente.continuaAGuardare.after(posizione)

def guarda_film(mappa_film, titolo):
    print("\nIl film ha una durata di", mappa_film[titolo].durata, "minuti.")
    minuti_da_guardare = int(input("Quanti minuti del film vuoi guardare? "))
    if minuti_da_guardare > int(mappa_film[titolo].durata):
        print(" ERRORE: Durata non valida.")
    elif minuti_da_guardare < int(mappa_film[titolo].durata):
        print("\nContenuto aggiunto alla sezione Continua a guardare.")
        if titolo not in utente.continuaAGuardare:
            utente.continuaAGuardare.add_first(titolo)
        else:
            rimuovi_da_continua_a_guardare(titolo)
            utente.continuaAGuardare.add_first(titolo)
    else:
        print("\nContenuto guardato completamente.")
        rimuovi_da_continua_a_guardare(titolo)

def guarda_serie_tv(mappa_serie_tv, titolo):
    print("\nLa serie è composta da", mappa_serie_tv[titolo].num_episodi, "episodi.")
    pila_serie = None
    # Itera la lista posizionale per vedere se la serie è già stata iniziata (e quindi ha una pila associata)
    posizione = utente.continuaAGuardare.first()
    for _ in range(0, len(utente.continuaAGuardare)):
        titolo_i, pila_i = posizione.element()
        if titolo_i == titolo:
            pila_serie = pila_i
            break
        posizione = utente.continuaAGuardare.after(posizione)
    # Se la serie non è stata trovata nella lista posizionale, la pila sarà uguale a None
    if pila_serie is not None:
        print("Rimangono da guardare", len(pila_serie), "episodi.")
    else:
        # Se la serie non è stata trovata nella lista posizionale, crea una nuova pila
        pila_serie = LinkedStack.LinkedStack()
        for i in range(0, int(mappa_serie_tv[titolo].num_episodi)):
            pila_serie.push(i)
        print("Rimangono da guardare", len(pila_serie), "episodi.")
    
    episodi_da_guardare = int(input("Quanti episodi vuoi guardare? "))
    if episodi_da_guardare > len(pila_serie):
        print(" ERRORE: Numero di episodi non valido")
        return
    
    for _ in range(0, episodi_da_guardare):
        pila_serie.pop()
        
    if pila_serie.is_empty():
        print("\nContenuto guardato completamente.")
        rimuovi_da_continua_a_guardare(titolo)
    else:
        print("\nContenuto aggiunto alla sezione Continua a guardare.")
        if titolo not in utente.continuaAGuardare:
            utente.continuaAGuardare.add_first((titolo, pila_serie))
        else:
            rimuovi_da_continua_a_guardare(titolo)
            utente.continuaAGuardare.add_first((titolo, pila_serie))

def continua_a_guardare(posizione):
    if not utente.continuaAGuardare.is_empty():
        try:
            titolo, _ = posizione.element()
        except:
            print("\nNessun contenuto presente nella sezione continua a guardare.")
            print("Ritorno al menu principale...")
            return
        print("\nVuoi continuare a guardare {}?".format(titolo))
        print(" 1 - SI")
        print(" 2 - NO")
        scelta = input("? ")
        if scelta == "1":
            if titolo in mappa_film:
                guarda_film(mappa_film, titolo)
            elif titolo in mappa_serie_tv:
                guarda_serie_tv(mappa_serie_tv, titolo)
        elif scelta == "2":
            continua_a_guardare(utente.continuaAGuardare.after(posizione))
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
            continua_a_guardare(utente.continuaAGuardare.first())
        elif scelta == "4":
            pass # TODO: implementare classifica
        elif scelta == "5":
            print()
            utente = login(tabellaUtenti)
        elif scelta == "6":
            print("\nUscita dall'applicazione.")
            print("----------------------------------------------------------------")
            exit(0)
        else:
            print("\nERRORE: Scegli un'opzione dal menù.")
