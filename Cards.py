from typing import Any, Callable, Dict, Tuple
from inspect import getsource

class Card:

    total = 0

    def __init__(self, name: str, desc: str, cost: int, vars: Dict[str, int], use: Callable[[Any, Any], None], can_use: Callable[[Any, Any], bool]) -> None:
        self.name = name
        self.desc = desc
        self.cost = cost
        self.vars = vars
        self.useFunc = use
        self.can_useFunc = can_use
        Card.total += 1

    def can_use(self, source, target) -> bool:
        return self.can_useFunc(self, source, target)

    def use(self, source, target) -> None:
        return self.useFunc(self, source, target)


class Modifier:
    def __init__(self, name: str, priority: Tuple[int, int, int], varsModif: Dict[str, Tuple[str, int]], cost: int = 0, use: str = "", can_use: str = "") -> None:
        self.name = name
        self.priority = priority
        self.cost = cost
        self.varsModif = varsModif
        self.use = use
        self.can_use = can_use
    
    def __str__(self) -> str:
        return self.name
    
    def __lt__(self, other) -> bool:
        if self.priority < other.priority:
            return True
        return False


def create_card(name: str, *modifiers: Modifier) -> Card:
    vars = {"atk": 0, "draw": 0}
    cost = 0
    use = "def card_use_{}(card, source, target):\n".format(Card.total) + "\tprint(\"Used {} energy\".format(card.cost))\n"
    can_use = "def card_can_use_{}(card, source, target):\n\tresult = True\n".format(Card.total)
    for i in sorted(modifiers, key = lambda x: x.priority[0]):
        for j in i.varsModif:
            if i.varsModif[j][0] == "plus":
                vars[j] += i.varsModif[j][1]
            if i.varsModif[j][0] == "times":
                vars[j] *= i.varsModif[j][1]
        
        cost += i.cost
        
    
    for i in sorted(modifiers, key = lambda x: x.priority[1]):
        if i.use != "":
            use += "\t" + i.use + "\n"
    
    for i in sorted(modifiers, key = lambda x: x.priority[2]):
        if i.can_use != "":
            can_use += "\t" + i.can_use + "\n"
    
    can_use += "\treturn result\n"
    for i in vars:
        vars[i] = int(vars[i])
    
    if vars["draw"] == 1:
        use += "\tprint(\"Draw {} card\".format(card.vars['draw']))\n"
    if vars["draw"] > 1:
        use += "\tprint(\"Draw {} cards\".format(card.vars['draw']))\n"

    exec(use)
    exec(can_use)

    return Card(name, "", cost, vars, eval("card_use_{}".format(Card.total)), eval("card_can_use_{}".format(Card.total)))


basicDamage = Modifier("Basic Damage", (0, 50, 100), {"atk": ("plus", 9)}, 1, "print(\"Deal {} damage\".format(card.vars['atk']))", "")
damageMultiplexer = Modifier("Damage Muliplexer", (5, 100, 100), {"atk": ("times", 2)}, 1)
costDown = Modifier("Cost Down", (51, 100, 100), {"atk": ("times", 0.7)}, -1)
drawOne = Modifier("Draw One", (50, 51, 100), {"atk": ("plus", -2), "draw": ("plus", 1)})
drawTwo = Modifier("Draw Two", (50, 51, 100), {"atk": ("plus", -5), "draw": ("plus", 2)})

A = create_card("Test", basicDamage, damageMultiplexer, drawOne, costDown)
A.use(0, 0)

print()

B = create_card("Test", basicDamage, damageMultiplexer, drawTwo, costDown)
B.use(0, 0)