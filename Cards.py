from CardData import *

Player1.setName("Jean")
Player2.setName("Claude")

deck: List[Card] = [Test() for _ in range(5)]
deck.extend([Test2() for _ in range(3)])

Player1.setDeck(deck)

GameManager.addToBot(SetupEvent(Player1))
GameManager.execQueue()

GameManager.addToBot(AscendEvent(Player1, CardPile.DRAW, 1, True, False))
GameManager.execQueue()