from adt.Empty import Empty

class LinkedStack:
    """
    Implementazione di pila LIFO utilizzando una lista semplicemente concatenata per l'archiviazione.
    """

    # --------------------------------- classe _Node innestata ----------------------------------
    class _Node:
        """
        Classe leggera, non pubblica per la memorizzazione di un nodo collegato singolarmente.
        """
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            """
            Inizializza i campi del nodo
            """
            self._element = element
            self._next = next

    # --------------------------------- metodi della pila ----------------------------------
    def __init__(self):
        """
        Crea una pila vuota
        """
        self._head = None
        self._size = 0

    def __len__(self):
        """
        Restituisce il numero di elementi nella pila.
        """
        return self._size

    def is_empty(self):
        """
        Restituisce True se la pila è vuota
        """
        return self._size == 0

    def push(self, e):
        """
        Aggiunge un elemento 'e' in cima alla pila
        """
        self._head = self._Node(e, self._head)      # collegamento al nuovo nodo
        self._size += 1

    def top(self):
        """
        Restituisce senza eliminare l'elemento in cima alla pila.

        Solleva l'eccezione Empty se la pila è vuota
        """
        if self.is_empty():
            raise Empty("La pila è vuota")
        return self._head._element      # la cima della pila è alla fine della lista

    def pop(self):
        """
        Restituisce e rimuove l'elemento in cima alla pila (LIFO)

        Solleva l'eccezione Empty se la pila è vuota
        """
        if self.is_empty():
            raise Empty("La pila è vuota")
        answer = self._head._element
        self._head = self._head._next
        self._size -= 1
        return answer
    