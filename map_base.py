from collections.abc import MutableMapping


class MapBase(MutableMapping):
    """
    Classe base astratta che include una classe _Item non pubblica.
    """

    # ----------------------------------------- classe _item innestata -----------------------------------------
    class _Item:
        """
        Composito leggero per archiviare le coppie chiave-valore come elementi della mappa.
        """
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key              # confronta gli elementi in base alle loro chiavi

        def __ne__(self, other):
            return not (self == other)                  # opposto di __eq__

        def __lt__(self, other):
            return self._key < other._key               # confronta gli elementi in base alle loro chiavi
