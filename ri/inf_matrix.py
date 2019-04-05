from typing import Sequence


class Influence:

    def __init__(self, value, x, y) -> None:
        super().__init__()
        self.value = value
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "value: {}, x: {}, y: {}".format(self.value, self.x, self.y)

    def to_tuple(self) -> tuple:
        return tuple((self.x, self.y))


class Actor:
    x = 0
    y = 0

    def __init__(self) -> None:
        super().__init__()

    def move_to(self, x, y) -> None:
        self.x = x
        self.y = y

    def intersection(self, lst1: Sequence[Influence], lst2: Sequence[Influence]) -> []:
        _temp = set([value.to_tuple() for value in lst2])
        _lst3 = [value for value in lst1 if value.to_tuple() in _temp]
        return _lst3

    def create_inf_matrix(self, radius) -> []:
        _matrix = []
        for i in range(-radius, radius + 1):
            for j in range(-radius, radius + 1):
                _r = max(abs(i), abs(j))
                _matrix.append(Influence(radius - _r + 1, j, i))

        return _matrix


act1 = Actor()
act2 = Actor()

m1 = act1.create_inf_matrix(1)
m2 = act1.create_inf_matrix(2)

inters = act1.intersection(m1, m2)

[print(i) for i in m2]
print("intersection")
[print(i) for i in inters]

