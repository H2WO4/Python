from CardData import *

PlayerA = Actor("A", 100, [])
PlayerB = Actor("B", 100, [])


StrikeA = Strike()

PlayerA.statues.append(StrengthStatus(PlayerA, 6))

PlayerB.block = 8

StrikeA.onPlay(PlayerA, PlayerB)
GameManager.execQueue()