from adt.HashMapBase import HashMapBase

class ProbeHashMap(HashMapBase):
    """
    Mappa hash implementata con esplorazione lineare per la risoluzione delle collisioni
    """

    _AVAIL_ = object()              # oggetto generico: locazioni di segni dentinelle relative a cancellazioni precedenti

    def _is_available(self, j):
        """
        Restituisce True se l'indice j è disponibile nella tabella.
        """
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL_

    def _find_slot(self, j, k):
        """
        Cerca la chiave k nel bucket all'indice j.

        Restituisce la tupla ('successo', 'indice') nei seguenti casi:
        - se è stata trovata una corrispondenza, 'successo' sarà True e 'indice' indica la sua posizione;
        - se non è stata trovata una corrispondenza, 'successo' sarà False e 'indice' indica il primo slot disponibile.
        """

        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j                      # lo marca come primo disponibile
                if self._table[j] is None:
                    return (False, firstAvail)          # ricerca fallita
            elif k == self._table[j]._key:
                return (True, j)                        # corrispondenza trovata
            j = (j + 1) % len(self._table)              # continua a guardare (ciclicamente)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error' + repr(k))       # nessuna corrispondenza
        return self._table[s]._value

    def _bucket_setitem(self, j, k, v):
        found, s = self._find_slot(j, k)
        if not found:
            self._table[s] = self._Item(k, v)           # inserisce il nuovo elemento
            self._n += 1                                # incrementa la dimensione
        else:
            self._table[s]._value = v                   # sovrascrive quello esistente

    def _bucket_delitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError('Key Error' + repr(k))       # nessuna corrispondenza
        self._table[s] = ProbeHashMap._AVAIL_           # contrassegnato come libero

    def __iter__(self):
        for j in range(len(self._table)):
            if not self._is_available(j):
                yield self._table[j]._key
