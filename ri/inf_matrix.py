import numpy as np


class Influence:

    def __init__(self, value, x, y) -> None:
        super().__init__()
        self.value = value
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return "value: {}, x: {}, y: {}".format(self.value, self.x, self.y)

    @staticmethod
    def np_dtype() -> np.dtype:
        return np.dtype([("x", np.int32), ("y", np.int32)])

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

    def create_inf_matrix(self, size) -> []:
        #       matrix = np.empty(In)
        #       for x in range(size):
        #           for y in range(size):

        return np.array([Influence(3, 1, 2).to_tuple(), Influence(2, 2, 2).to_tuple(), Influence(2, 2, 3).to_tuple()],
                        dtype=Influence.np_dtype())


act1 = Actor()
act2 = Actor()

res = np.intersect1d(act1.create_inf_matrix(5), act2.create_inf_matrix(3))
print(res)
