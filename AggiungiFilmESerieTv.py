import UnsortedTableMap
import Contenuti

def salva_film(k,v):
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
    file.write(f"Numero stagioni:{v.num_stagioni}")
    file.write("\n")
    file.close()

#map = UnsortedTableMap.UnsortedTableMap()

while True:
    print("Cosa vuoi salvare?\n1. Film\n2. Serie Tv")
    scelta = int(input())
    if scelta == 1:

        titolo = input("Titolo del film\n")

        print("Inserisci il genere")
        genere = input()
        print("Inserisci la durata")
        durata = input()
        print("Inserisci il regista")
        regista = input()
        contenutofilm = Contenuti.ContenutoFilm(genere, durata, regista)
        map.__setitem__(titolo, contenutofilm)
        salva_film(titolo, contenutofilm)

    else:
        titolo = input("Titolo Serie Tv\n")
        print("Inserisci il genere")
        genere = input()
        print("Inserisci la durata media di un episodio")
        durata = input()
        print("Inserisci il regista")
        regista = input()
        print("Inserisci il numero di episodi")
        num_episodi = input()
        print("Inserisci il numero di stagioni")
        num_stagioni = input()
        contenutoserie = Contenuti.ContenutoSerieTv(genere, durata, regista, num_episodi, num_stagioni)
        map.__setitem__(titolo, contenutoserie)
        salva_serie_tv(titolo, contenutoserie)