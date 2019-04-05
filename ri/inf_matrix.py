from typing import Sequence
import matplotlib.pyplot as plt


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

    def move_to(self, x, y) -> None:
        self.x = self.x + x
        self.y = self.y + y


class Actor:

    def __init__(self, size) -> None:
        super().__init__()
        self.x = 0
        self.y = 0
        self._create_inf_matrix(size)

    def move_to(self, x, y) -> None:
        self.x = x
        self.y = y
        [i.move_to(x, y) for i in self.matrix]

    def intersection(self, lst1: Sequence[Influence], lst2: Sequence[Influence]) -> []:
        _temp = set([value.to_tuple() for value in lst2])
        _lst3 = [value for value in lst1 if value.to_tuple() in _temp]
        return _lst3

    def _create_inf_matrix(self, radius) -> []:
        self.matrix = []
        for i in range(-radius, radius + 1):
            for j in range(-radius, radius + 1):
                _r = max(abs(i), abs(j))
                self.matrix.append(Influence(radius - _r + 1, j, i))


act1 = Actor(1)
act1.move_to(3, 3)
act2 = Actor(2)
act2.move_to(7, 7)

m1 = act1.matrix
m2 = act2.matrix

# inters = act1.intersection(m1, m2)

[print(i) for i in m1]
print("m2")
[print(i) for i in m2]
print("intersection")
# [print(i) for i in inters]

m1t = [i.to_tuple() for i in m1]
m2t = [i.to_tuple() for i in m2]

px = list(map(lambda xc: xc[0], m1t))
py = list(map(lambda xc: xc[1], m1t))

plt.scatter(px, py)

p2x = list(map(lambda xc: xc[0], m2t))
p2y = list(map(lambda xc: xc[1], m2t))

plt.scatter(p2x, p2y)

plt.grid(True)

plt.show()
