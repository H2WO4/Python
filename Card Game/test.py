from typing import Callable, Tuple

class Player:
    pass

class Card:
    pass

class Card:
    def __init__(self, name: str, description: str, cost: int, *effects: Tuple[Callable[[Player, Player], None], ...]):
        self.name = name
        self.description = description
        self.cost = cost
        self.effects = effects

class Player:
    def __init__(self, name: str, hp: int, maxEnergy: int):
        self.name = name
        self.hp = hp
        self.maxEnergy = maxEnergy
        self.energy = self.maxEnergy
    
    def use(self, card: Card, target: Player):
        if self.energy >= card.cost:
            self.energy -= card.cost
            for i in card.effects:
                i(self, target)