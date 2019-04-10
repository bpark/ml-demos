from abc import ABCMeta, abstractmethod
from random import randint
from typing import List, Dict


class Actor:

    def __init__(self, actor_id: int, lvl: int, total_hp: int, base_dmg: int, ab: List) -> None:
        super().__init__()
        self.actor_id = actor_id
        self.lvl = lvl
        self.total_hp = total_hp
        self.base_dmg = base_dmg
        self.ab_dict = {x.name(): x for x in ab}
        self.state = {
            "total_hp": total_hp * lvl,
            "current_hp": total_hp * lvl,
            "dmg": 0,
            "heal": 0
        }

    def apply(self, ab_id: str) -> int:
        return self.ab_dict[ab_id].apply(actor=self)

    def perc_hp(self) -> float:
        return self.state["current_hp"] / self.state["total_hp"]


class Ability(metaclass=ABCMeta):

    @abstractmethod
    def name(self) -> str:
        pass

    @abstractmethod
    def apply(self, actor: Actor) -> int:
        pass


class Strike(Ability):

    def __init__(self) -> None:
        super().__init__()

    def apply(self, actor: Actor) -> int:
        actor.state["dmg"] = round(actor.base_dmg * 0.5 * actor.lvl)
        print("Performing Strike with dmg: " + str(actor.state["dmg"]))
        return 10

    def name(self) -> str:
        return "strike"


class Heal(Ability):

    def __init__(self, base_heal: int) -> None:
        super().__init__()
        self.base_heal = base_heal

    def apply(self, actor: Actor) -> int:
        actor.state["heal"] = self.base_heal * actor.lvl
        print("Performing Heal with +" + str(actor.state["heal"]))
        print(actor.perc_hp())
        return round(40 * (1 - actor.perc_hp()))

    def name(self) -> str:
        return "heal"


class GameEnv:

    def __init__(self) -> None:
        super().__init__()
        self.actors: Dict[int, Actor] = {}

    def add_actor(self, actor: Actor) -> None:
        self.actors[actor.actor_id] = actor

    # next_state, reward, done
    def step(self, actor_id, action: str) -> tuple:
        actor = self.actors[actor_id]
        reward = actor.apply(action)
        print("reward: " + str(reward))

        opponents = [v for k, v in self.actors.items() if k not in [actor_id]]

        return 123, 10, False

    def sample(self, actor_id) -> str:
        return randint(0, len(self.actors[actor_id].ab_dict.keys()) - 1)


a1 = Actor(1, 4, 500, 50, ab=[Strike(), Heal(20)])
a2 = Actor(2, 7, 1500, 5, ab=[Strike(), Heal(40)])

env = GameEnv()
env.add_actor(a1)
env.add_actor(a2)
env.step(1, "strike")
