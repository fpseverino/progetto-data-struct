import Contenuti
from func import*

def salva_film(k, v):
    """
        Salva i dati di un film nel file di testo "film.txt".

        Args:
            k (str): Il titolo del film da salvare.
            v (Contenuti.Film): L'oggetto film contenente le informazioni da salvare.

        Return: None
    """
    file = open("film.txt","a")
    file.write(f"Titolo:{k}")
    file.write("\n")
    file.write(f"Genere:{v.genere}")
    file.write("\n")
    file.write(f"Durata:{v.durata}")
    file.write("\n")
    file.write(f"Regista:{v.regista}")
    file.write("\n")
    file.close()

def salva_serie_tv(k, v):
    """
    Salva i dati di una serie TV nel file di testo "serietv.txt".

    Args:
        k (str): Il titolo della serie TV da salvare.
        v (Contenuti.SerieTv): L'oggetto serie TV contenente le informazioni da salvare.

    Return: None
    """
    file = open("serietv.txt", "a")
    file.write(f"Titolo:{k}")
    file.write("\n")
    file.write(f"Genere:{v.genere}")
    file.write("\n")
    file.write(f"Durata:{v.durata}")
    file.write("\n")
    file.write(f"Regista:{v.regista}")
    file.write("\n")
    file.write(f"Numero episodi:{v.num_episodi}")
    file.write("\n")
    file.close()

while True:
    print("Cosa vuoi salvare?\n1. Film\n2. Serie Tv\n3. Esci")
    scelta = input()
    if scelta == '1':
        titolo = valida_testo("Titolo del film\n")
        genere = valida_testo("Inserisci il genere\n")
        durata = valida_intero("Inserisci la durata (in minuti)\n")
        regista = valida_testo("Inserisci il regista\n")
        contenuto_film = Contenuti.Film(genere, durata, regista)
        salva_film(titolo, contenuto_film)
    elif scelta == '2':
        titolo = valida_testo("Titolo Serie Tv\n")
        genere = valida_testo("Inserisci il genere\n")
        durata = valida_intero("Inserisci la durata media di un episodio (in minuti)\n")
        regista = valida_testo("Inserisci il regista\n")
        num_episodi = valida_intero("Inserisci il numero di episodi\n")
        contenuto_serie = Contenuti.SerieTv(genere, durata, regista, num_episodi)
        salva_serie_tv(titolo, contenuto_serie)
    elif scelta == '3':
        print("\nUscita dall'applicazione.")
        print("----------------------------------------------------------------")
        exit(0)
    else:
        print("\nERRORE: Scegli un'opzione dal menù.")
