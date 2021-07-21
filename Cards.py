from CardData import *

PlayerA = Actor("A", 100, [])
PlayerB = Actor("B", 100, [])


StrikeA = Strike()

PlayerA.status.append(StrengthStatus(PlayerA, 6))

PlayerB.block = 8


print(StrikeA)
PlayerA.playCard(StrikeA, PlayerB)
GameManager.execQueue()