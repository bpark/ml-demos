from abc import ABCMeta, abstractmethod
from random import randint
from typing import List


class Actor:

    def __init__(self, id, total_hp: int, base_dmg: int, ab: List) -> None:
        super().__init__()
        self.id = id
        self.total_hp = total_hp
        self.base_dmg = base_dmg
        self.ab = ab
        self.effects = {
            "dmg": 0,
            "total_hp": total_hp,
            "current_hp": total_hp
        }

    def apply(self, ab_index: int) -> None:
        self.ab[ab_index].apply(actor=self)


class Ability(metaclass=ABCMeta):

    @abstractmethod
    def apply(self, actor: Actor) -> None:
        pass


class Strike(Ability):

    def __init__(self) -> None:
        super().__init__()

    def apply(self, actor: Actor) -> None:
        actor.effects["dmg"] = actor.base_dmg
        print("Performing Strike with dmg: " + str(actor.effects["dmg"]))


class GameEnv:

    def __init__(self) -> None:
        super().__init__()
        self.actors = {}

    def add_actor(self, actor: Actor) -> None:
        self.actors[actor.id] = actor

    # next_state, reward, done
    def step(self, action) -> tuple:
        return 123, 10, False

    def sample(self) -> int:
        return randint(0, 2)


a1 = Actor(1, 500, 50, ab=[Strike()])
a1.apply(0)
