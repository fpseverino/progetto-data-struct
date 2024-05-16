from adt.MapBase import MapBase
from random import randrange

class HashMapBase(MapBase):
    """
    Classe astratta di base per la mappa che usa la tabella hash con compressione MAD.
    """

    def __init__(self, cap=11, p=109345121):
        """
        Crea una mappa tabella hash vuota.
        """
        self._table = cap * [None]
        self._n = 0                                     # numero di voci nella mappa
        self._prime = p                                 # numero primo per compressione MAD
        self._scale = 1 + randrange(p - 1)              # scala da 1 a p-1 per MAD
        self._shift = randrange(p)                      # shift da 0 a p-1 per MAD

    def _hash_function(self, k):
        """
        Calcola hash per il valore k.
        """
        return (hash(k) * self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        """
        Restituisce il numero di elementi distinti attualmente memorizzati nella tabella hash.
        """
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k)       # può sollevare un KeyError

    def __setitem__(self, k, v):
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v)                   # la sottoroutine aggiorna self._n
        if self._n > len(self._table) // 2:             # mantiene il fattore di carico <= 0.5
            self._resize(2 * len(self._table) - 1)      # il numero 2^x - 1 è spesso primo

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j, k)                  # può sollevare un KeyError
        self._n -= 1

    def _resize(self, c):
        """
        Ridimensiona l'array di bucket alla capacità c.
        """
        old = list(self.items())                # si usa l'iterazione per registrare elementi esistenti
        self._table = c * [None]                # ripristina la tabella alla capacità desiderata
        self._n = 0                             # _n è ricalcolato duratne le aggiunte successive
        for (k, v) in old:
            self[k] = v                         # re-inserisce le vecchie coppie chiave-valore
