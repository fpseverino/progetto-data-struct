from adt import UnsortedTableMap
from adt import LinkedBinaryTree
from adt import ProbeHashMap
from adt import LinkedStack
from adt import HeapPriorityQueue
from adt import SortedPriorityQueue
from func import*
import time


coda_p = SortedPriorityQueue.SortedPriorityQueue()
mappa_film = UnsortedTableMap.UnsortedTableMap()
mappa_serie_tv = UnsortedTableMap.UnsortedTableMap()
tabella_utenti = ProbeHashMap.ProbeHashMap()
utente = None
albero = LinkedBinaryTree.LinkedBinaryTree()
heap = HeapPriorityQueue.HeapPriorityQueue()


def scelta_contenuto():
    """
    Una funzione che permette all'utente di scegliere il contenuto da guardare.
    Chiede all'utente di inserire il titolo del contenuto da guardare e poi verifica se il titolo
    è presente nelle mappe dei film o delle serie TV. Se trovato, chiama la funzione corrispondente
    per guardare il contenuto. Se non trovato, visualizza un messaggio di errore.
    """
    print()
    titolo = input("Inserisci il titolo del contenuto da guardare ('n' per uscire): ")
    if titolo == "n":
        print("Ritorno al menu principale...")
        return
    if titolo in mappa_film:
        guarda_film(titolo)
    elif titolo in mappa_serie_tv:
        guarda_serie_tv(titolo)
    else:
        print(" ERRORE: Contenuto non trovato")


def elenco_film_serie_tv():
    """
    Funzione per visualizzare l'elenco dei film e delle serie TV memorizzati nelle rispettive mappe.
    """
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
        print("----------------------------------------------------------------")
    scelta_contenuto()


def rimuovi_da_continua_a_guardare(titolo):
    """
    Rimuove un titolo specifico dalla lista posizionale 'continua a guardare' dell'utente.

    Arg:
        titolo: Il titolo da rimuovere.

    Return: None
    """
    posizione = utente.continuaAGuardare.first()
    for _ in range(0, len(utente.continuaAGuardare)):
        titolo_i, _ = posizione.element()
        if titolo_i == titolo:
            utente.continuaAGuardare.delete(posizione)
            break
        posizione = utente.continuaAGuardare.after(posizione)


def guarda_film(titolo):
    """
    Una funzione che gestisce il processo di salvataggio del progresso di un film.
    La funzione chiede all'utente di inserire quanti minuti del film desidera guardare.
    Successivamente, aggiorna la sezione 'Continua a guardare' dell'utente in base all'input fornito.

    Arg:
        titolo: Il titolo del film da gestire.

    Return: None
    """
    print("\nIl film ha una durata di", mappa_film[titolo].durata, "minuti.")

    dati_film = None
    for elemento in utente.continuaAGuardare:
        if titolo == elemento[0]:
            dati_film = elemento
            break
    
    if dati_film is None:
        dati_film = (titolo, int(mappa_film[titolo].durata))
    
    print("Rimangono da guardare", dati_film[1], "minuti.")

    while True:
        minuti_da_guardare = valida_intero("Quanti minuti del film vuoi guardare? ")
        if minuti_da_guardare > int(dati_film[1]):
            print(" ERRORE: Durata non valida.")
        elif minuti_da_guardare < int(dati_film[1]):
            print("\nContenuto aggiunto alla sezione Continua a guardare.")
            if dati_film not in utente.continuaAGuardare:
                utente.continuaAGuardare.add_first((titolo, dati_film[1] - minuti_da_guardare))
            else:
                rimuovi_da_continua_a_guardare(titolo)
                utente.continuaAGuardare.add_first((titolo, dati_film[1] - minuti_da_guardare))
            break
        else:
            print("\nContenuto guardato completamente.")
            mappa_film[titolo].visualizzazioni += 1
            rimuovi_da_continua_a_guardare(titolo)
            break


def guarda_serie_tv(titolo):
    """
    Una funzione che gestisce il processo di salvataggio del progresso di una serie TV.
    La funzione chiede all'utente di inserire quanti episodi della serie desidera guardare.
    Successivamente, aggiorna la sezione 'Continua a guardare' dell'utente in base all'input fornito.

    Arg:
        titolo: Il titolo della serie da gestire.

    Return: None
    """
    print("\nLa serie è composta da", mappa_serie_tv[titolo].num_episodi, "episodi.")

    dati_serie = None
    for elemento in utente.continuaAGuardare:
        if titolo == elemento[0]:
            dati_serie = elemento
            break

    if dati_serie is None:
        pila_serie = LinkedStack.LinkedStack()
        for i in range(int(mappa_serie_tv[titolo].num_episodi), 0, -1):
            pila_serie.push("Episodio " + str(i))
        dati_serie = (titolo, pila_serie)
    
    print("Rimangono da guardare", len(dati_serie[1]), "episodi.")
    print("Il prossimo episodio è:", dati_serie[1].top())

    while True:
        episodi_da_guardare = valida_intero("Quanti episodi vuoi guardare? ")
        if episodi_da_guardare > len(dati_serie[1]):
            print(" ERRORE: Numero di episodi non valido")
        else:
            for _ in range(0, episodi_da_guardare):
                dati_serie[1].pop()
            break
    
    if dati_serie[1].is_empty():
        print("\nContenuto guardato completamente.")
        mappa_serie_tv[titolo].visualizzazioni += 1
        rimuovi_da_continua_a_guardare(titolo)
    else:
        print("\nContenuto aggiunto alla sezione Continua a guardare.")
        if dati_serie not in utente.continuaAGuardare:
            utente.continuaAGuardare.add_first((titolo, dati_serie[1]))
        else:
            rimuovi_da_continua_a_guardare(titolo)
            utente.continuaAGuardare.add_first((titolo, dati_serie[1]))
        print("Il prossimo episodio è:", dati_serie[1].top())


def continua_a_guardare(posizione):
    """
    Una funzione che permette di continuare a guardare un film o una serie TV in base all'input dell'utente.

    Args:
        posizione: La posizione del primo elemento della lista posizionale associata all'utente.

    Returns:
        None
    """
    while True:
        if not utente.continuaAGuardare.is_empty():
            # except si attiva nel caso in cui ci si trova alla fine della lista posizionale
            try:
                titolo, _ = posizione.element()
            except:
                print("\nNessun contenuto presente nella sezione continua a guardare.")
                print("Ritorno al menu principale...")
                return
            print("\nVuoi continuare a guardare {}?".format(titolo))
            print(" 1 - SI")
            print(" 2 - NO")
            scelta1 = input("? ")
            if scelta1 == "1":
                if titolo in mappa_film:
                    guarda_film(titolo)
                    break
                elif titolo in mappa_serie_tv:
                    guarda_serie_tv(titolo)
                    break
            elif scelta1 == "2":
                posizione = utente.continuaAGuardare.after(posizione)
            else:
                print("\nOpzione non valida")
        else:
            print("\nNessun contenuto presente nella sezione continua a guardare.")
            print("Ritorno al menu principale...")
            break


def ordinamento_alfabetico(titolo):
    """
    Funzione per inserire un titolo di un contenuto in un albero binario 
    in modo tale che questo abbia le caratteristiche di un albero binario di ricerca e si possa stampare cosi' i titoli in ordine alfabetico.

    Parameters:
    - titolo: il titolo da inserire nell'albero binario di ricerca.

    Returns:
    Questa funzione non restituisce esplicitamente nulla.
    """
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


def ordinamento():
    """
    Una funzione esegue diverse operazioni, tra cui:
        -inserire i titoli presenti nella mappe nell'albero binario di ricerca
        -la stampa dell'albero binario di ricerca
        -la selezione di un contenuto.
    """
    print()
    for k in mappa_film:
        ordinamento_alfabetico(k)
    for k in mappa_serie_tv:
        ordinamento_alfabetico(k)
    stampa_albero_inorder(albero.root())
    scelta_contenuto()


def stampa_albero_inorder(nodo):
    """
    Una funzione ricorsiva che stampa gli elementi di un albero binario di ricerca con una visita in-order.

    Parameters:
    - nodo: un nodo dell'albero binario

    Returns: None
    """
    if nodo is not None:
        figlio_sinistro = albero.left(nodo)
        figlio_destro = albero.right(nodo)
        albero.inorder()
        stampa_albero_inorder(figlio_sinistro)
        print(nodo.element())
        stampa_albero_inorder(figlio_destro)
    
   

def classifica_per_visualizzazioni():
    """
    Stampa la classifica dei contenuti per numero di visualizzazioni.
    Implementato con un heap.
    """
    print()
    for k in mappa_film:
        visual = mappa_film[k].visualizzazioni
        titolo = k
        heap.add(-visual, titolo)
    for k in mappa_serie_tv:
        visual = mappa_serie_tv[k].visualizzazioni
        titolo = k
        heap.add(-visual, titolo)
    i = 1
    while not heap.is_empty():
        neg_views, titolo = heap.remove_min()
        print(f"{i}. {titolo}: {-neg_views} visualizzazioni")
        i += 1


def riempi_coda():
    """
    Riempie la coda prioritaria con i prossimi contenuti in arrivo.
    """
    formato_data = "%Y/%m/%d"
    stringa_data = "2027/04/16"
    data = time.strptime(stringa_data, formato_data)
    coda_p.add(data, "Star Wars: Lost Horizons")

    stringa_data = "2025/09/12"
    data = time.strptime(stringa_data, formato_data)
    coda_p.add(data, "Avatar 3")

    stringa_data = "2026/05/02"
    data = time.strptime(stringa_data, formato_data)
    coda_p.add(data, "Avengers: The Kang Dinasty")

    stringa_data = "2025/04/12"
    data = time.strptime(stringa_data, formato_data)
    coda_p.add(data, "Deadpool 4")

    stringa_data = "2026/09/12"
    data = time.strptime(stringa_data, formato_data)
    coda_p.add(data, "Boris 5")


def coming_soon():
    """
    Una funzione che mostra all'utente i contenuti futuri e chiede ulteriori azioni.
    """
    if coda_p.is_empty():
        print()
        print("Non ci sono più contenuti in arrivo.")
        print("Ritorno al menu principale...")
        return
    prossima_uscita = coda_p.remove_min()
    print()
    data = prossima_uscita[0]
    data_formattata =time.strftime("%d/%m/%Y",data)
    print("Prossima uscita:", prossima_uscita[1])
    print("In uscita il:", data_formattata)
    print("Vuoi vedere il prossimo contenuto?")
    print(" 1 - SI")
    print(" 2 - NO")
    opinione = input("? ")
    if opinione == "1":
        coming_soon()
    else:
        print("Ritorno al menu principale...")
        return


if __name__ == "__main__":
    caricamento_mappe(mappa_film, mappa_serie_tv)
    crea_utenti(tabella_utenti)
    print("----------------------------------------------------------------")
    utente = login(tabella_utenti)
    while True:
        print("\n*** MENU PRINCIPALE ***")
        print(" 1 - Visualizzazione lista dettagliata")
        print(" 2 - Visualizza i film e le serie tv per ordine alfabetico")
        print(" 3 - Continua a guardare")
        print(" 4 - I più visti")
        print(" 5 - Coming soon...")
        print(" 6 - Cambia account")
        print(" 7 - Esci")
        scelta = input("? ")
        if scelta == "1":
            elenco_film_serie_tv()
        elif scelta == "2":
            ordinamento()
        elif scelta == "3":
            continua_a_guardare(utente.continuaAGuardare.first())
        elif scelta == "4":
            classifica_per_visualizzazioni()
        elif scelta == "5":
            riempi_coda()
            coming_soon()
        elif scelta == "6":
            print()
            utente = login(tabella_utenti)
        elif scelta == "7":
            print("\nUscita dall'applicazione.")
            print("----------------------------------------------------------------")
            exit(0)
        