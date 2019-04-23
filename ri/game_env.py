from abc import ABCMeta, abstractmethod
from random import randint
from typing import List, Dict

import math


def auto_str(cls):
    def __str__(self):
        return '%s(%s)' % (
            type(self).__name__,
            ', '.join('%s=%s' % item for item in vars(self).items())
        )

    cls.__str__ = __str__
    return cls


@auto_str
class State:

    def __init__(self, rlvl: float = 0, rtothp: float = 0, rcurrhp: float = 0) -> None:
        super().__init__()
        self.rlvl = rlvl
        self.rtothp = rtothp
        self.rcurrhp = rcurrhp

    def __eq__(self, o: object) -> bool:
        if isinstance(o, State):
            return self.rlvl == o.rlvl and self.rtothp == o.rtothp and self.rcurrhp == o.rcurrhp

    def __hash__(self) -> int:
        return int(self.rlvl * 100000 + self.rtothp * 1000 + self.rcurrhp * 10)


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

        opponents = self._opponents(actor_id)

        state = State()
        for opponent in opponents:
            state.rlvl = round(math.log(actor.lvl / opponent.lvl), 1)
            state.rtothp = round(math.log(actor.state["total_hp"] / opponent.state["total_hp"]), 1)
            state.rcurrhp = round(math.log(actor.state["current_hp"] / opponent.state["current_hp"]), 1)
            print(state)

        return hash(state), reward, False

    def observation_space_n(self) -> int:
        return pow(41, 3)

    def action_space_n(self) -> int:
        return 2

    def sample(self, actor_id) -> str:
        return randint(0, len(self.actors[actor_id].ab_dict.keys()) - 1)

    def _opponents(self, actor_id):
        return [v for k, v in self.actors.items() if k not in [actor_id]]


a1 = Actor(1, 6, 100, 50, ab=[Strike(), Heal(40)])
a2 = Actor(2, 2, 100, 50, ab=[Strike(), Heal(40)])

env = GameEnv()
env.add_actor(a1)
env.add_actor(a2)
# env.step(1, "strike")
state, reward, end = env.step(1, "heal")

print("state=" + str(state) + ", reward=" + str(reward) + ", end=" + str(end))
