from adt import LinkedQueue

class Tree:
    """
    Classe base astratta che rappresenta una struttura ad albero.
    """

    # ------------------------------- classe Position innestata -------------------------------
    class Position:
        """
        Un'astrazione che rappresenta la posizione di un singolo elemento
        """

        def element(self):
            """
            Restituisce l'elemento memorizzato in questa Position
            """
            raise NotImplementedError('Deve essere implementato dalla sottoclasse')

        def __eq__(self, other):
            """
            Restituisce True se 'other' non rappresenta la stessa posizione.
            """
            raise NotImplementedError('Deve essere implementato dalla sottoclasse')

        def __ne__(self, other):
            """
            Restituisce True se 'other' non rappresenta la stessa posizione
            """
            return not (self == other)      # opposto a __eq__

    # ------------------------------- metodi astratti che la stottoclasse concreta deve suppotare -------------------------------
    def root(self):
        """
        Restituisce Position che rappresenta la radice dell'albero (None se è vuoto).
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    def parent(self, p):
        """
        Restituisce Position che rappresenta il genitore di 'p'(None se 'p' è radice).
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    def num_children(self, p):
        """
        Restituisce il numero di figli della Position p.
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    def children(self, p):
        """
        Restituisce un contenitore iterabile con i figli della posizione 'p'.
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    def __len__(self):
        """
        Restituisce il numero totale di elementi nell'albero.
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    # ------------------------------- metodi concreti implementati in questa classe-------------------------------
    def is_root(self, p):
        """
        Restituisce True se la Position 'p' è la radice dell'albero.
        """
        return self.root() == p

    def is_leaf(self, p):
        """
        Restituisce True se la Postition 'p' non ha figli.
        """
        return self.num_children(p) == 0

    def is_empty(self):
        """
        Restituisce True se l'albero è vuoto.
        """
        return len(self) == 0

    def depth(self, p):
        """"
        Restituisce il numero di livelli che separano la Position 'p' dalla radice.
        """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.dept(self.parent(p))

    def _heigh2(self, p):
        """"
        Restituisce l'altezza del sottoalbero radiato in Position 'p'.
        """
        if self._is_leaf(p):
            return 0
        else:
            return 1 + max(self._heigh2(c) for c in self.children(p))

    def heigh(self, p=None):
        """"
        Restituisce l'altezza del sottoalbero radicato in Position 'p'.

        Se 'p' è None restituisce l'altezza dell'intero albero
        """
        if p is None:
            p = self.root()
        return self._heigh2(p)

    def __iter__(self):
        """
        Restituisce un iteratore che scandisce tutti gli elementi dell'albero
        """
        for p in self.position():
            yield p.element()                                   # restituisce l'elemento

    def preorder(self):
        """
        Genera un'iterazione preordinata delle posizioni nell'albero
        """
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()):       # inizia la ricorsione
                yield p

    def _subtree_preorder(self, p):
        """
        Genera un'iterazione preodinata delle posizioni nel sottoalbero con radice 'p'.
        """
        yield p                                                 # visita 'p' prima dei suoi sotto alberi
        for c in self.children(p):                              # per ogni figlio di 'c'
            for other in self._subtree_preorder(c):             # effettua il pre-ordine dei sottoalberi di 'c'
                yield other                                     # restituisce la posizione

    def position(self):
        """
        Restituisce un contenitore iterabile con tutte le posizioni dell'albero.
        """
        return self.preorder()

    def postorder(self):
        """
        Generea un'iterazione postordinata delle posizioni nell'albero
        """
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):      # inizia la ricorsione
                yield p

    def _subtree_postorder(self, p):
        """
        Gnenera un'iterazione postordinata delle posizioni nel sottoalbero con radice 'p'.
        """
        for c in self.children(p):                              # per ogni figlio di 'c'
            for other in self._subtree_postorder(c):            # effettua il post-ordine dei sottoalberi di 'c'
                yield other                                     # restituisce
        yield p                                                 # visita 'p' dopo i suoi sotto alberi

    def breadthfirst(self):
        """
        Generare un'iterazione in ampiezza delle posizioni dell'albero.
        """
        if not self.is_empty():
            fringe = LinkedQueue()                              # posizioni note non ancora restituite
            fringe.enqueue(self.root())                         # si inizia con la radice
            while not fringe.is_empty():
                p = fringe.dequeue()                            # rimuovere dall'inizio della coda
                yield p                                         # restituisce la posizione
                for c in self.children(p):
                    fringe.enqueue(c)                           # aggiunge il figlio alla fine della coda
