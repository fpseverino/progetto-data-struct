from adt.Empty import Empty
from adt.PositionalList import PositionalList
from adt.PriorityQueueBase import PriorityQueueBase


class SortedPriorityQueue(PriorityQueueBase):       # la classe base definisce _Item
    """
    Coda con priorità min-oriented implementata con una lista ordinata
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
        newest = self._Item(key, value)             # crea una nuova istanza di _Item
        walk = self._data.last()                    # "cammina" all'indietro per creare una chiave più piccola
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)            # la nuova chiave è più piccola
        else:
            self._data.add_after(walk, newest)      # newest inserito dopo walk

    def min(self):
        """
        Restituisce ma non rimuove la tupla (k,v) con chiave minima.
        """
        if self.is_empty():
            raise Empty('la coda prioritaria è vuota')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        """
        Restituisce e rimuove la tupla (k, v) con chiave minima.
        """
        if self.is_empty():
            raise Empty('La coda prioritaria è vuota')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)
