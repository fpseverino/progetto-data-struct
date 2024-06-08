from adt.Empty import Empty
from adt.PriorityQueueBase import PriorityQueueBase

class HeapPriorityQueue(PriorityQueueBase):
    """
    Coda con priorità min-oriented implementata con un heap binario
    """

    # --------------------------------- metodi non pubblici ---------------------------------
    def _parent(self, j):
        return (j-1) // 2

    def _left(self, j):
        return 2 * j + 1

    def _right(self, j):
        return 2 * j + 2

    def _has_left(self, j):
        return self._left(j) < len(self._data)

    def _has_right(self, j):
        return self._right(j) < len(self._data)

    def _swap(self, i, j):
        """
        Scambia gli elementi negli indici 'i' e 'j' dell'array.
        """
        self._data[i], self._data[j] = self._data[j], self._data[i]

    def _uphead(self, j):
        parent = self._parent(j)
        if j > 0 and self._data[j] < self._data[parent]:
            self._swap(j, parent)
            self._uphead(parent)            # prosegue nella posizione del genitore

    def _downhead(self, j):
        if self._has_left(j):
            left = self._left(j)
            small_child = left          # anche se la destra potrebbe essere più piccola
            if self._has_right(j):
                right = self._right(j)
                if self._data[right] < self._data[left]:
                    small_child = right
            if self._data[small_child] < self._data[j]:
                self._swap(j, small_child)
                self._downhead(small_child)         # prosegue nella posizione dello small_child

    # --------------------------------- metodi pubblici ---------------------------------
    def __init__(self):
        """
        Crea una coda prioritaria vuota.
        """
        self._data = []

    def __len__(self):
        """
        Restituisce il numero di elementi nella coda prioritaria.
        """
        return len(self._data)

    def add(self, key, value):
        """
        Aggiunge una coppia chiave valore alla coda prioritaria.
        """
        self._data.append(self._Item(key, value))
        self._uphead(len(self._data) - 1)           # "fa risalire" la posizione appena aggiunta

    def min(self):
        """
        Restituisce ma non rimuove la tupla (k, v) con chiave minima.

        Solleva l'eccezione Empti se la coda è vuota.
        """
        if self.is_empty():
            raise Empty('La coda prioritaria è vuota.')
        item = self._data[0]
        return (item._key, item._value)

    def remove_min(self):
        """
        Restituisce e rimuove la tupla (k, v) con chiave minima.

        Solleva l'eccezione Empty se la coda è vuota.
        """
        if self.is_empty():
            raise Empty('La coda prioritaria è vuota.')
        self._swap(0, len(self._data) - 1)                # mette l'elemento più piccolo alla fine
        item = self._data.pop()                           # elimina l'elemento dalla lista
        self._downhead(0)                                 # fix della radice
        return (item._key, item._value)
