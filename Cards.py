from CardData import *

Player1.setName("Jean")
Player2.setName("Claude")

deck: List[Card] = []

Player1.setDeck(deck)

GameManager.addToBot(SetupEvent(Player1))
GameManager.execQueue()

print(Pantheon())