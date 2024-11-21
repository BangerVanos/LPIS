class WrappedSet:

    def __init__(self, values) -> None:
        self._set = set(values)
    
    @property
    def inner_set(self):
        return self._set
    
    def __add__(self, other):
        if isinstance(other, int):
            return WrappedSet(self._set.add(other))
        elif isinstance(other, WrappedSet):
            return WrappedSet(self._set.union(other.inner_set))
    
    def __mul__(self, other):
        if isinstance(other, int):
            return WrappedSet(self._set.add(other))
        elif isinstance(other, WrappedSet):
            return WrappedSet(self._set.intersection(other._set))

    def __sub__(self, other):
        if isinstance(other, int):
            return WrappedSet(self._set.add(other))
        elif isinstance(other, WrappedSet):
            return WrappedSet(self._set - other._set)

    def __div__(self, other):
        if isinstance(other, int):
            return WrappedSet(self._set.add(other))
        elif isinstance(other, WrappedSet):
            return WrappedSet(self._set ^ other._set)

    def __str__(self) -> str:
        return str(self._set)

    def __repr__(self) -> str:
        return self.__str__()        

if __name__ == '__main__':
    s1 = WrappedSet([1, 2, 4])
    s2 = WrappedSet([2, 3, 4])
    a = 1
    b = 3
    if (a > b):
        print((s1 + s2))
    else:
        print((s1 * s2))
    for i in range(1, 5):
        print(i, end='')

