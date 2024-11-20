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

def add(x: int, y: int):
    return (x + y)

def add(x: set, y: set):
    return (x + y)

def sub(x: set, y: set):
    return (x - y)

if __name__ == '__main__':
    s1 = WrappedSet([1, 2, 3])
    s2 = WrappedSet([2, 3, 4])
    a = 1
    b = 2
    c = (a + b)
    print(add(s1, s2))
    print(sub(s1, s2))
    print((s1 * s2))
    print(add(a, b))
    for i in range(1, 10):
        print(i)
    if (a > b):
        print(a)
    elif (a < b):
        print(b)
    else:
        print(a)

