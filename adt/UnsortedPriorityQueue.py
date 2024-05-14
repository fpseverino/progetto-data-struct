from empty import Empty
from adt.lista_posizionale import PositionalList
from coda_prio_base import PriorityQueueBase


class UnsortedPriorityQueue(PriorityQueueBase):     # la classe base definisce _Item
    """
    Coda con priorità min-oriented implementata con una lista non ordinata.
    """

    def __init__(self):
        """
        Crea una nuova coda prioritaria vuota.
        """
        self._data = PositionalList()

    def __len__(self):
        """
        Restituisce il numero di elementi nella coda prioritaria.
        """
        return len(self._data)

    def add(self, key, value):
        """
        Aggiunge una coppia chiave-valore.
        """
        self._data.add_last(self._Item(key, value))

    def _find_min(self):                # metodo non pubblico
        """
        Restituisce la Position dell'item con chiave minima.
        """
        if self.is_empty():             # metodo ereditato
            raise Empty('La coda prioritaria è vuota')
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def min(self):
        """
        Restituisce ma non rimuove la tupla (k, v) con chiave minima.
        """
        p = self._find_min()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """
        Restituisce e rimuove la tupla (k, v) con chiave minima.
        """
        p = self._find_min()
        item = self._data.delete(p)
        return (item._key, item._value)
