from random import randint


class GameEnv:

    ATTACK = 0
    HUNT = 1
    FLEE = 2

    def __init__(self, health, dmg) -> None:
        super().__init__()
        self.health = health
        self.dmg = dmg

    # next_state, reward, done
    def step(self, action) -> tuple:
        return 123, 10, False

    def sample(self) -> int:
        return randint(0, 2)
