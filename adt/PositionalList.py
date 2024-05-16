from adt.DoublyLinkedBase import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    """
    Contenitore sequenziale di elementi che consente l'accesso posizionale.
    """
    # ------------------------------- classe innestata Position -------------------------------
    class Position:
        """
        Astrazione che rappresenta la posizione di un singolo elemento
        """

        def __init__(self, container, node):
            """
            Costruttore
            """
            self._container = container
            self._node = node

        def element(self):
            """
            Restituisce l'elemento memorizzato in questa posizione
            """
            return self._node._element

        def __eq__(self, other):
            """
            Restituisce True se 'other' è una posizione che rappresenta la stessa posizione.
            """
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            """
            Restituisce True se 'other' non rappresenta la stessa posizione.
            """
            return not (self == other)      # opposto di __eq__

    # ------------------------------- metodi di utilità -------------------------------
    def _validate(self, p):
        """
        Restituisce la posizione del nodo o solleva l'errore appropriato se non valido.
        """
        if not isinstance(p, self.Position):
            raise TypeError('p deve essere ti tipo Position')
        if p._container is not self:
            raise ValueError('p non appartiene a questo contenitore')
        if p._node._next is None:
            raise ValueError('p non è più valida')
        return p._node

    def _make_position(self, node):
        """
        Restituisce l'istanza Position per il nodo dato (o None se sentinel).
        """
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    # ------------------------------- metodi accessori -------------------------------
    def first(self):
        """
        Restituisce la prima Position nella lista (None se la lista è vuota).
        """
        return self._make_position(self._header._next)

    def last(self):
        """
        Restituisce l'ultima Position nella lista (None se la lista è vuota).
        """
        return self._make_position(self._trailer._prev)

    def before(self, p):
        """
        Restituisce la Position prima della Position p (None se p è la prima posizione).
        """
        node = self._validate(p)
        return self._make_position(node._prev)

    def after(self, p):
        """
        Restituisce la Position dopo la Position p (None se p è l'ultima posizione).
        """
        node = self._validate(p)
        return self._make_position(node._next)

    def __iter__(self):
        """
        Genera un'iterazione in avanti degli elementi della lista.
        """
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    # ------------------------------- mutuatori -------------------------------
    # override la versione ereditata per restituire Position, anzichè Node
    def _insert_between(self, e, predecessor, successor):
        """
        Aggiunge un elemento tra nodi esistenti e restituisce Position
        """
        node = super()._insert_between(e, predecessor, successor)
        return self._make_position(node)

    def add_first(self, e):
        """
        Aggiunge l'elemento all'inizio della lista e restituisce Position.
        """
        return self._insert_between(e, self._header, self._header._next)

    def add_last(self, e):
        """
        Aggiunge l'elemento alla fine della lista e restituisce Position.
        """
        return self._insert_between(e, self._trailer._prev, self._trailer)

    def add_before(self, p, e):
        """
        Inserisce l'elemento 'e' nella lista prima della Position 'p' e restituisce nuova Position
        """
        original = self._validate(p)
        return self._insert_between(e, original._prev, original)

    def add_after(self, p, e):
        """
        Inserisce l'elemento 'e' nella lista dopo Position 'p' e restituisce nuova Position.
        """
        original = self._validate(p)
        return self._insert_between(e, original, original._next)

    def delete(self, p):
        """
        Rimuove e restituisce l'elemento in Position p.
        """
        original = self._validate(p)
        return self._delete_node(original)  # ereditato

    def replace(self, p, e):
        """
        Ssitutisce l'elemento nella Position 'p' con l'elemento 'e'

        Restituisce l'elemento precedentemente in Position 'p'
        """
        original = self._validate(p)
        old_value = original._element
        original._element = e
        return old_value
