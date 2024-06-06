from adt.UnsortedTableMap import UnsortedTableMap
from adt.HashMapBase import HashMapBase

class ChainHashMap(HashMapBase):
    """
    Mappa hash implementata con concatenazione separata per la risoluzione delle collisioni.
    """

    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error' + repr(k))       # nessuna corrispondenza
        return bucket[k]                                # delega la ricerca al bucket
    
    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap()          # crea un nuovo bucket
        oldsize = len(self._table[j])
        self._table[j][k] = v                           # inserisce/modifica l'elemento
        if len(self._table[j]) > oldsize:                # incrementa la dimensione
            self._n += 1
    
    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError('Key Error' + repr(k))       # nessuna corrispondenza
        del bucket[k]                                   # delega la cancellazione al bucket

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None:
                for key in bucket:
                    yield key