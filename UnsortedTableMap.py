from map_base import MapBase


class UnsortedTableMap(MapBase):
    """
    Implementazione della mappa utilizzando una lista non ordinata.
    """

    def __init__(self):
        """
        Crea una mappa vuota.
        """
        self._table = []                # lista di _Item

    def __getitem__(self, k):
        """
        Restituisce il valore associato alla chive 'k'.

        Solleva un KeyError se non trovato.
        """
        for item in self._table:
            if k == item._key:
                return item._value
        raise KeyError('Keyerror: ' + repr(k))          # repr(): restituisce stringa

    def __setitem__(self, k, v):
        """
        Assegna il valore 'v' alla chiave 'k', sovrascrivendo il valore esistente se presente.
        """
        for item in self._table:
            if k == item._key:          # se trova la chiave
                item._value = v         # sovrascrive il valore
                return                  # esce
        # se non trova la chiave
        self._table.append(self._Item(k, v))

    def __delitem__(self, k):
        """
        Rimuove l'elemento associato alla chiave 'k'.

        Solleva un KeyError se non trovato.
        """
        for j in range(len(self._table)):
            if k == self._table[j]._key:            # se trova la chiave
                self._table.pop(j)                  # rimuove l'elemento
                return                              # esce
        raise KeyError('Keyerror: ' + repr(k))

    def __len__(self):
        """
        Restituisce il numero di elementi nella mappaa
        """
        return len(self._table)

    def __iter__(self):
        """
        Genera iterazione delle chiavi della mappa.
        """
        for item in self._table:
            yield item._key
