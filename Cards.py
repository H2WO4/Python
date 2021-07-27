from CardData import *

Player1.setName("Jean")
Player2.setName("Claude")

deck: List[Card] = []

Player1.setDeck(deck)

GameManager.addToBot(SetupEvent(Player1))
GameManager.execQueue()

print(Shrine())
print(Glade())
print(Crypt())
print(Hamlet())
print(Memorial())
print(BurialGrounds())
print()
print(Church())
print(Village())
print(Forest())
print(Cemetery())
print()
print(Altar())
print(Hut())
print(Grove())
print(Tomb())
print()
print(GreatOak())
print(DeadForest())
print()
print(Yggdrasil())