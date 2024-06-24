# progetto-data-struct
Corso di Algoritmi e Strutture Dati UNIKORE A.A. 2023/2024 - Progetto di fine semestre

## Pyflix - Simulazione di una piattaforma di streaming

### Descrizione dettagliata
Il progetto ha come obiettivo quello di creare un’applicazione di gestione di contenuti multimediali, che permette agli utenti di visualizzare e continuare a guardare contenuti, come film e serie TV. Le funzionalità principali includono la gestione degli utenti, la visualizzazione degli elenchi dei contenuti, l’ordinamento alfabetico, la visualizzazione delle classifiche per visualizzazioni e la gestione dei contenuti prossimi in uscita.

Il file `AggiungiFilmeSerieTv.py` permette il salvataggio di nuovi film e serie TV e raccoglie tutte le informazioni necessarie attraverso input dell’utente. Una volta ottenute tutte le informazioni, crea un oggetto `Film` o `SerieTV` e lo salva nel rispettivo file di testo utilizzando le funzioni `salva_film` e `salva_serie_tv`.

Nel file `Contenuti.py` troviamo le definizioni delle principali classi che rappresentano i dati del sistema (`Film`, `SerieTV`, `Utente`).

Il file `func.py` contiene funzioni di supporto essenziali per caricare i dati, creare utenti e gestire il login. In questo file vengono letti i dati dai file di testo `film.txt` e `serietv.txt` e popolate le strutture dati con oggetti `Film` e `SerieTV`.
Un’altra funzione importante è `crea_utenti`, che crea alcuni utenti predefiniti e li aggiunge alla loro tabella hash.
La funzione `login` gestisce il processo di autenticazione dell’utente richiedendo la password e restituendo l’oggetto utente corrispondente, o in alternativa la registrazione di un nuovo utente.

Il file principale dell’applicazione è `main.py`, che coordina l’intero flusso dell’applicazione interagendo con l’utente.
All’avvio, il file inizializza diverse strutture dati per memorizzare film, serie TV e utenti. Carica tutto il necessario tramite l’utilizzo dei metodi sopra elencati, e in seguito gestisce il login degli utenti tramite la funzione `login`, che richiede la password e avvia la sessione per l’utente autenticato.
L’applicazione presenta quindi un menu di opzioni all’utente per eseguire diverse operazioni. Tra queste, l’utente può visualizzare elenchi di contenuti, ordinarli alfabeticamente, continuare a guardare contenuti in sospeso, vedere le classifiche di visualizzazioni e scoprire i prossimi contenuti in uscita. Ogni opzione richiama la funzione appropriata per eseguire l’operazione selezionata, orendo un’esperienza interattiva e personalizzata per ogni utente.

### Strutture dati utilizzate
- Pila o Coda:

è stata implementata una pila per ogni serie TV, tutte salvate all’interno della lista posizionale che gestisce la sezione “Continua a guardare”. Se, all’atto di guardare una serie, questa non è presente nella lista posizionale, vengono caricati in una pila gli episodi della serie, dall’ultimo al primo. Successivamente, tramite il metodo `top` è possibile visualizzare il prossimo episodio della serie da guardare. Quando l’utente vuole guardare la serie, viene richiamato il metodo `pop` della pila tante volte quanti sono gli episodi che l’utente vuole guardare.
- Lista posizionale:

è stata implementata una lista posizionale per ogni utente, al fine di gestire i contenuti che l’utente può continuare a guardare. La lista viene inizializzata al momento di creazione dell’utente. Se un utente guarda un film o una serie TV ma non completamente, il contenuto viene aggiunto alla prima posizione della lista, salvando il titolo e i minuti rimanenti o la pila degli episodi. Se l’utente continua a guardare un contenuto che non si trova alla prima posizione della lista, questo viene rimosso e riaggiunto alla lista al primo posto, aggiornando i minuti rimanenti o la pila. Se l’utente guarda completamente un contenuto nella lista, viene rimosso. È possibile visualizzare i contenuti della lista “Continua a guardare” in ordine, da quello visto più recentemente in poi, posizione per posizione.
- Albero:

è stato implementato un albero binario per poter stampare i titoli dei film e delle serie TV in ordine alfabetico.
- Coda prioritaria:

è stata implementata per poter stampare i titoli dei film e delle serie TV in ordine di uscita.
- Heap:

è stato implementato un heap per stampare i titoli dei film e delle Serie TV ordinati in base al numero di visualizzazioni.
- Mappa:

sono state impiegate due mappe, per contenere ciascuna i dati di tutti i film e di tutte le serie TV nel catalogo. All’avvio dell’applicazione questi dati vengono letti da due file di testo, e salvati in oggetti delle classi `Film` e `SerieTV` e caricati nelle mappe. Per ogni coppia chiave-valore la chiave sarà il titolo e il valore l’oggetto della relativa classe.
- Tabella hash:

è stata implementata una tabella hash che contiene i dati degli utenti. Le chiavi rappresentano le password di ciascun utente, e il valore associato contiene i rispettivi dati (nome, email, lista posizionale “Continua a guardare”) salvati all’interno di oggetti di classe `Utente`. All’avvio dell’applicazione è possibile eettuare il login, ossia una ricerca della chiave fornita, o la registrazione, ovvero la creazione di un nuovo utente, e quindi di una nuova coppia chiave-valore all’interno della mappa.
