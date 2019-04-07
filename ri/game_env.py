
class GameEnv:

    ATTACK = 0
    PREY = 1
    FLEE = 2

    def __init__(self, health, dmg) -> None:
        super().__init__()
        self.health = health
        self.dmg = dmg


