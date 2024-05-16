from adt.Tree import Tree

class BinaryTree(Tree):
    """
    Classe base astratta che rappresenta una struttura ad albero binario.
    """

    # ------------------------------- metodi astratti addizionali -------------------------------
    def left(self, p):
        """
        Restituisce una Position che rappresenta il figlio sinistro di 'p'.

        Restituisce None se 'p' non ha un figlio sinistro.
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    def right(self, p):
        """
            Restituisce una Position che rappresenta il figlio destro di 'p'.

            Restituisce None se 'p' non ha un figlio destro.
        """
        raise NotImplementedError('Deve essere implementato dalla sottoclasse')

    # ------------------------------- metodi concreti implementati in questa classe -------------------------------
    def sibling(self, p):
        """
        Restituisce una position che rappresenta il fratello di 'p' (o None se non è fratello).
        """
        parent = self.parent(p)
        if parent is None:                                  # allora p è la radice
            return None                                     # la radice non ha fratelli
        else:
            if p == self.left(parent):
                return self.right(parent)                   # possibilmente None
            else:
                return self.left(parent)                    # possibilmente None

    def children(self, p):
        """
        Restituisce un contenitore iterabile con i figli della posizione 'p'.
        """
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    # ------------------------------- metodi di attraversamento -------------------------------
    def inorder(self):
        """
        Genera un'iterazione in ordine delle posizioni nell'albero.
        """
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        """
        Genera un'iterazione in ordine delle posizioni nel sottoalbero con radice 'p'.
        """
        if self.left(p) is not None:                                    # se esiste il figlio sinistro attraversa il suo sottoalbero
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p                                                         # visita 'p' tra i suoi sottoalberi
        if self.right(p) is not None:
            for other in self._subtree_inorder(self.right(p)):          # se esiste il figlio destro attraversa il suo sottoalbero
                yield other

    def position(self):
        """
        Restituisce un contenitore iterabile con tutte le posizioni dell'albero.
        """
        return self.inorder()

