from __future__ import annotations
from enum import Enum
from random import randint, shuffle
from EventSystemTemplate import Event, EventManager
from typing import Callable, Dict, List, Literal

# Define a Color class for text priting
class Color:
	PURPLE = '\033[95m'
	BLUE = '\033[94m'
	CYAN = '\033[96m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	BLANK = '\033[0m'

# Define enums for Elements, Card Types, Card Tags and Card Piles
class Elements(Enum):
	LIFE = "Life"
	SOUL = "Soul"
	BELIEF = "Belief"
	NATURE = "Nature"

class CardType(Enum):
	CREATION = "Creation"
	SPELL = "Spell"
	DOGMA = "Dogma"

class CardTags(Enum):
	GENESIS = "Genesis"
	APOCALYPSE = "Apocalypse"

class CardPile(Enum):
	DRAW = "draw"
	HAND = "hand"
	DISCARD = "discard"
	WORLD = "world"
	ABOVE = "above"
	BELOW = "below"


# Modifies the EventManager to fit 1v1 combat, adding a way to get a player's opponent
class CombatManager(EventManager):
	def __init__(self, player1: Actor, player2: Actor) -> None:
		super().__init__()
		self.player1 = player1
		self.player2 = player2

	def getOpponent(self, player: Actor) -> Actor:
		if player == self.player1:
			return self.player2
		elif player == self.player2:
			return self.player1
		else:
			raise ValueError


# Define a CardStack class, representing an ordered pile of cards
class CardStack:
	def __init__(self, values: List[Card] = []) -> None:
		self.values: List[Card] = values.copy()

	def __getitem__(self, key: int) -> Card:
		return self.values[key]
	
	def __delitem__(self, key: int) -> None:
		del self.values[key]

	def __add__(self, other: CardStack) -> CardStack:
		return CardStack(self.values + other.values)

	def __len__(self) -> int:
		return len(self.values)

	def __str__(self) -> str:
		return "\n".join([f"[{Color.PURPLE}{i+1}{Color.BLANK}] {Color.GREEN}{card.name}{Color.BLANK}" for i, card in enumerate(self.values)])

	def valueStr(self) -> str:
		return "\n".join([f"[{Color.PURPLE}{i+1}{Color.BLANK}] {Color.GREEN}{card.name}{Color.BLANK} = ({', '.join([f'{Color.CYAN}{i.value}{Color.BLANK}: {Color.PURPLE}{card.value[i]}{Color.BLANK}' for i in card.value])})" for i, card in enumerate(self.values)])

	def append(self, object: Card) -> None:
		self.values.append(object)

	def extend(self, other: CardStack) -> None:
		self.values.extend(other.values)

	def remove(self, object: Card) -> None:
		self.values.remove(object)

	def pop(self) -> Card:
		return self.values.pop()

	def shuffle(self) -> None:
		shuffle(self.values)

	def copy(self) -> CardStack:
		return CardStack(self.values.copy())

	def random(self) -> Card:
		return self.values[randint(0, len(self))]


# Define an Actor class, representing a player
class Actor:
	def __init__(self, name: str, health: int, deck: List[Card]) -> None:
		# Attributes
		self.name = name
		self.deck = CardStack(deck)

		# Variables
		self.health = health
		self.initialDraw = 4
		self.handSize = 8
		self.drawPower = 1

		# Card Piles
		self.draw = CardStack()
		self.hand = CardStack()
		self.discard = CardStack()

		self.world = CardStack()
		self.above = CardStack()
		self.below = CardStack()

	def setDeck(self, deck: List[Card]) -> None:
		self.deck = CardStack(deck)

	def setName(self, name: str) -> None:
		self.name = name

	def worldValue(self) -> Dict[Elements, int]:
		output: Dict[Elements, int] = {}
		for card in self.world:
			for elem in card.value:
				output[elem] = output.get(elem, 0) + card.value[elem]
		return output


# Define a Card class, representing a playing card
class Card:
	def __init__(self) -> None:
		self.name: str
		self.description: str
		self.type: CardType

		self.cost: Dict[Elements, int] = {}
		self.value: Dict[Elements, int] = {}
		self.tags: List[CardTags] = []

	def onPlay(self, source: Actor, origin: CardPile) -> None:
		# Function comparing two value dictionaries
		def compareDicts(payed: Dict[Elements, int], toPay: Dict[Elements, int]):
			return all([payed.get(i, 0) >= toPay[i] for i in toPay])

		# Create a copy of the player's world
		worldCopy = source.world.copy()
		# Create an empty CardStack
		payedCard = CardStack()
		# While the value of cards chosen is not enough to pay the cost of the card played
		while not compareDicts(calculateValue(payedCard), self.cost):
			# Display the current available selection to the player
			print(worldCopy.valueStr())
			try:
				# Ask the player which card to choose
				choice = int(input(f"{Color.YELLOW}Enter the number of the card you wish to choose: {Color.BLANK}")) - 1
				# If the player enter 0
				if choice == -1:
					# And there is cards currently selected, remove the last selection
					if len(payedCard) >= 1:
						worldCopy.append(payedCard[-1])
						del payedCard[-1]
					# Else, cancel the action
					else:
						return
				# If it is a valid value in the range, add the card to the selection and remove it from the posibilities
				elif choice in range(len(worldCopy)):
					payedCard.append(worldCopy[choice]) # type: ignore
					del worldCopy[choice]
				# Else, raise an error
				else:
					raise ValueError
				
			# In case of an invalid input, inform the player and continue the loop
			except (ValueError, TypeError):
				print(f"{Color.RED}Please enter a valid input!{Color.BLANK}\n")
		
		# For every card selected
		for card in payedCard:
			# Activate its active discard effect
			card.onActiveDiscard(source)
			# Remove it from the player's world and add it to their discard
			source.world.remove(card)
			source.discard.append(card)

		# Activate effects on card play
		for card in source.world:
			card.onPlayAnotherCard(source, self)

		# Get the current pile the card is in, and remove it
		pile = getCardStack(source, origin)
		pile.remove(self)
		# Then add the card to the corresponding pile, world for a creation, discard for the rest
		if self.type == CardType.CREATION:
			source.world.append(self)
		else:
			source.discard.append(self)

	def canPlay(self, source: Actor) -> bool:
		return True

	def onDraw(self, source: Actor) -> None:
		pass

	def onActiveDiscard(self, source: Actor) -> None:
		pass

	def onAscend(self, source: Actor) -> None:
		pass

	def onDescend(self, source: Actor) -> None:
		pass

	def onReturn(self, source: Actor, origin: Literal[CardPile.ABOVE, CardPile.BELOW]) -> None:
		pass

	def onPlayAnotherCard(self, source: Actor, card: Card) -> None:
		pass

	def dynamicDescription(self) -> str:
		return eval(f"f'{self.description}'")

	def __str__(self) -> str:
		output = f"{Color.GREEN}{self.name}{Color.BLANK}, {Color.UNDERLINE}{self.type.value}{Color.BLANK}:"
		if self.description != "":
			output += f"\n{self.dynamicDescription()}"
		if self.cost != {}:
			output += f"\n{Color.BOLD}Cost{Color.BLANK} = ({', '.join([f'{Color.CYAN}{i.value}{Color.BLANK}: {Color.PURPLE}{self.cost[i]}{Color.BLANK}' for i in self.cost])})"
		if self.value != {}:
			output += f"\n{Color.BOLD}Value{Color.BLANK} = ({', '.join([f'{Color.CYAN}{i.value}{Color.BLANK}: {Color.PURPLE}{self.value[i]}{Color.BLANK}' for i in self.value])})"
		
		return output + "\n"


# Function transforming a CardPile argument into the corresponding CardStack
def getCardStack(source: Actor, pile: CardPile) -> CardStack:
	return getattr(source, pile.value)

# Funnction calculating the total value of a CardStack
def calculateValue(pile: CardStack) -> Dict[Elements, int]:
	output: Dict[Elements, int] = {}
	for card in pile:
		for elem in card.value:
			output[elem] = output.get(elem, 0) + card.value[elem]
	return output


""" Events """

# Event called for each player at the beginning of a match, handling card shuffle
class SetupEvent(Event):
	def __init__(self, target: Actor) -> None:
		super().__init__()
		self.target = target
	
	def update(self) -> None:
		# Create the draw, a copy of the deck
		self.target.draw = self.target.deck.copy()

		# Create 2 separate piles, for future shuffle
		genesis = CardStack()
		apocalypse = CardStack()
		# Put cards tagged Genesis and Apocalypse into these piles
		for card in self.target.draw:
			if CardTags.GENESIS in card.tags:
				self.target.draw.remove(card)
				genesis.append(card)
			elif CardTags.APOCALYPSE in card.tags:
				self.target.draw.remove(card)
				apocalypse.append(card)

		# Shuffle all 3 piles
		self.target.draw.shuffle()
		genesis.shuffle()
		apocalypse.shuffle()

		# Put the 3 piles together, with apocalypse at the bottom and genesis at the top
		self.target.draw = apocalypse + self.target.draw + genesis

		# Tell the event manager we're done
		self.isDone = True

class DrawEvent(Event):
	def __init__(self, source: Actor, potency: int) -> None:
		super().__init__()
		self.source = source
		self.potency = potency
	
	def update(self) -> None:
		for _ in range(self.potency):
			try:
				card = self.source.draw.pop()
				card.onDraw(self.source)
				self.source.hand.append(card)

			except IndexError:
				GameManager.addToBot(LoseLifeEvent(self.source, 2))

		self.isDone = True

# Standard damage event, handling possible multi-hits
class DamageEvent(Event):
	def __init__(self, source: Actor, target: Actor, damage: int, repeat: int = 1) -> None:
		super().__init__()
		self.source = source
		self.target = target
		self.damage = damage
		self.repeat = repeat

	def update(self) -> None:
		# Execute the next steps for each repeat stack
		for _ in range(self.repeat):
			# Subtract health
			self.target.health = max(self.target.health - self.damage, 0)
			
			# Display result accordingly
			if self.target.health > 0:
				print(f"{Color.BLUE}{self.target.name}{Color.BLANK} lost {Color.PURPLE}{self.damage}{Color.BLANK} HP. They have {Color.PURPLE}{self.target.health}{Color.BLANK} HP left.")
			else:
				print(f"{Color.BLUE}{self.target.name}{Color.BLANK} is dead.")
				break

		# Tell the event manager that it can continue
		self.isDone = True

# Standard HP loss event
class LoseLifeEvent(Event):
	def __init__(self, target: Actor, damage: int) -> None:
		super().__init__()
		self.target = target
		self.damage = damage

	def update(self) -> None:
		# Subtract health
		self.target.health = max(self.target.health - self.damage, 0)
		
		# Display result accordingly
		if self.target.health > 0:
			print(f"{Color.BLUE}{self.target.name}{Color.BLANK} lost {Color.PURPLE}{self.damage}{Color.BLANK} HP. They have {Color.PURPLE}{self.target.health}{Color.BLANK} HP left.")
		else:
			print(f"{Color.BLUE}{self.target.name}{Color.BLANK} is dead.")

		# Tell the event manager that it can continue
		self.isDone = True

# Standard healing event
class RecoverEvent(Event):
	def __init__(self, target: Actor, potency: int) -> None:
		super().__init__()
		self.target = target
		self.potency = potency
	
	def update(self) -> None:
		# Add the health
		self.target.health += self.potency

		# Tell the player how much health was healed
		print(f"{Color.BLUE}{self.target.name}{Color.BLANK} healed {Color.PURPLE}{self.potency}{Color.BLANK} HP. They have {Color.PURPLE}{self.target.health}{Color.BLANK} HP left.")

		# Tell the event manager that it can continue
		self.isDone = True

# Streamlined event to select cards based on user input
class SelectCardsEvent(Event):
	def __init__(self, owner: Actor, source: CardPile,  potency: int, anyNumber: bool, random: bool, filter: Callable[[Card], bool], consumer: Callable[[CardStack], None]) -> None:
		super().__init__()
		self.owner = owner
		self.source = source
		self.potency = potency
		self.anyNumber = anyNumber
		self.random = random
		self.filter = filter
		self.consumer = consumer
	
	def update(self) -> None:
		# Create a new pile and filter the base pile depending on the chosen condition into it
		pile = CardStack()
		for card in getCardStack(self.owner, self.source):
			if self.filter(card):
				pile.append(card)
		# Create an empty pile for the selected pile
		selection = CardStack()
		
		# For every card to choose
		while self.potency > 0:
			# If chosen randomly
			if self.random:
				# If there is something left to choose
				if len(pile) >= 1:
					# Make a choice randomly, add it to the selection an remove it from the posibilities
					choice = pile.random()
					selection.append(choice)
					pile.remove(choice)

					# Decrement the potency of the effect, indicationg that a card has been succesfully chosen
					self.potency -= 1
				else:
					break
			# If there is enough cards to need a choice, or anyNumber is true
			elif len(pile) > self.potency or (self.anyNumber and len(pile) > 0):
				# Display the choice to the player
				print(pile)
				try:
					# Ask the player which card to choose
					choice = int(input(f"{Color.YELLOW}Enter the number of the card you wish to choose: {Color.BLANK}")) - 1
					# If 0 is chosen and anyNumber is true, abort
					if choice == -1 and self.anyNumber:
						break
					# If it is a valid value in the range, add the card to the selection and remove it from the posibilities
					elif choice in range(len(pile)):
						selection.append(pile[choice])
						del pile[choice]
					# Else, raise an error
					else:
						raise ValueError

					# Decrement the potency of the effect, indicationg that a card has been succesfully chosen
					self.potency -= 1	
				# In case of an invalid input, inform the player and continue the loop
				except (ValueError, TypeError):
					print(f"{Color.RED}Please enter a valid input!{Color.BLANK}\n")
			# If no choice is needed, simply add all available cards and abort
			else:
				selection.extend(pile)
				break

		# Apply the consumer unto all the cards chosen
		self.consumer(selection)

		# Tell the event manager that it can continue
		self.isDone = True

# Standard Ascend event
class AscendEvent(Event):
	def __init__(self, owner: Actor, source: CardPile, potency: int, anyNumber: bool, random: bool) -> None:
		super().__init__()
		self.owner = owner
		self.source = source
		self.potency = potency
		self.anyNumber = anyNumber
		self.random = random
	
	def update(self) -> None:
		# Create a consumer that move each card to the Above and use their onAscend method
		def ascendConsumer(list: CardStack):
			for card in list:
				pile: CardStack = getattr(self.owner, self.source.value.lower())

				card.onAscend(self.owner)
				self.owner.above.append(card)
				pile.remove(card)
		
		# Add the event to the event queue
		GameManager.addToBot(SelectCardsEvent(self.owner, self.source, self.potency, self.anyNumber, self.random, lambda _: True, ascendConsumer))

		# Tell the event manager that it can continue
		self.isDone = True

class DiscardEvent(Event):
	def __init__(self, owner: Actor, potency: int, anyNumber: bool, random: bool) -> None:
		super().__init__()
		self.owner = owner
		self.potency = potency
		self.anyNumber = anyNumber
		self.random = random

	def update(self) -> None:
		def discardConsumer(list: CardStack):
			for card in list:
				card.onActiveDiscard(self.owner)
				self.owner.discard.append(card)
				self.owner.hand.remove(card)

		GameManager.addToBot(SelectCardsEvent(self.owner, CardPile.HAND, self.potency, self.anyNumber, self.random, lambda _: True, discardConsumer))

		self.isDone = True


""" Cards """

# # Creations

# Free to play and Value = 1 + 1

class Shrine(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Altar"
		self.description = ""
		self.type = CardType.CREATION

		self.value[Elements.BELIEF] = 1
		self.value[Elements.LIFE] = 1

class Glade(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Glade"
		self.description = ""
		self.type = CardType.CREATION

		self.value[Elements.BELIEF] = 1
		self.value[Elements.NATURE] = 1

class Crypt(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Crypt"
		self.description = ""
		self.type = CardType.CREATION

		self.value[Elements.BELIEF] = 1
		self.value[Elements.SOUL] = 1

class Hamlet(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Hamlet"
		self.description = ""
		self.type = CardType.CREATION

		self.value[Elements.LIFE] = 1
		self.value[Elements.NATURE] = 1

class Memorial(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Memorial"
		self.description = ""
		self.type = CardType.CREATION

		self.value[Elements.LIFE] = 1
		self.value[Elements.SOUL] = 1

class BurialGrounds(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Burial Grounds"
		self.description = ""
		self.type = CardType.CREATION

		self.value[Elements.NATURE] = 1
		self.value[Elements.SOUL] = 1


# Free to play and Value = 2

class Village(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Village"
		self.description = ""
		self.type = CardType.CREATION

		self.value[Elements.LIFE] = 2

class Cemetery(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Cemetery"
		self.description = ""
		self.type = CardType.CREATION

		self.value[Elements.SOUL] = 2

class Forest(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Forest"
		self.description = ""
		self.type = CardType.CREATION

		self.value[Elements.NATURE] = 2

class Church(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Church"
		self.description = ""
		self.type = CardType.CREATION

		self.value[Elements.BELIEF] = 2


# Free to play, Value = 1 and minor effect

class Altar(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Altar"
		self.description = "When played, draw {Color.PURPLE}1{Color.BLANK} card."
		self.type = CardType.CREATION

		self.value[Elements.BELIEF] = 1

	def onPlay(self, source: Actor, origin: CardPile) -> None:
		super().onPlay(source, origin)

		GameManager.addToBot(DrawEvent(source, 1))

class Hut(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Hut"
		self.description = "When played, draw {Color.PURPLE}1{Color.BLANK} card"
		self.type = CardType.CREATION

		self.value[Elements.LIFE] = 1

	def onPlay(self, source: Actor, origin: CardPile) -> None:
		super().onPlay(source, origin)

		GameManager.addToBot(DrawEvent(source, 1))

class Grove(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Grove"
		self.description = "When played, draw {Color.PURPLE}1{Color.BLANK} card."
		self.type = CardType.CREATION

		self.value[Elements.NATURE] = 1
	
	def onPlay(self, source: Actor, origin: CardPile) -> None:
		super().onPlay(source, origin)

		GameManager.addToBot(DrawEvent(source, 1))

class Tomb(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Tomb"
		self.description = "When played, draw {Color.PURPLE}1{Color.BLANK} card."
		self.type = CardType.CREATION

		self.value[Elements.SOUL] = 1

	def onPlay(self, source: Actor, origin: CardPile) -> None:
		super().onPlay(source, origin)

		GameManager.addToBot(DrawEvent(source, 1))


# Free to play, Total Value = 3/4 and drawback

class GreatOak(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Great Oak"
		self.description = "Discard {Color.PURPLE}1{Color.BLANK} card."
		self.type = CardType.CREATION

		self.value[Elements.BELIEF] = 1
		self.value[Elements.NATURE] = 3
	
	def onPlay(self, source: Actor, origin: CardPile) -> None:
		super().onPlay(source, origin)

		GameManager.addToBot(DiscardEvent(source, 1, False, False))

	def canPlay(self, source: Actor) -> bool:
		return len(source.hand) >= 2

class DeadForest(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Dead Forest"
		self.description = "Lose {Color.PURPLE}5{Color.BLANK} HP."
		self.type = CardType.CREATION

		self.value[Elements.NATURE] = 2
		self.value[Elements.SOUL] = 2
	
	def onPlay(self, source: Actor, origin: CardPile) -> None:
		super().onPlay(source, origin)

		GameManager.addToBot(LoseLifeEvent(source, 5))

	def canPlay(self, source: Actor) -> bool:
		return source.health > 5


# Special

class Pantheon(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Pantheon"
		self.description = "When played, you and your opponent recover {Color.PURPLE}{self.healing}{Color.BLANK} HP."
		self.type = CardType.CREATION

		self.cost[Elements.BELIEF] = 1
		self.cost[Elements.LIFE] = 1

		self.value[Elements.BELIEF] = 3
		self.value[Elements.LIFE] = 1

		self.healing = 10
	
	def onPlay(self, source: Actor, origin: CardPile) -> None:
		super().onPlay(source, origin)

		GameManager.addToBot(RecoverEvent(source, self.healing))
		GameManager.addToBot(RecoverEvent(GameManager.getOpponent(source), self.healing))

class Yggdrasil(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Yggdrasil"
		self.description = "Whenever you play a {Color.UNDERLINE}Creation{Color.BLANK}, heal HP equal to its {Color.CYAN}Nature{Color.BLANK} value."
		self.type = CardType.CREATION

		self.cost[Elements.LIFE] = 2
		self.cost[Elements.NATURE] = 4
		self.cost[Elements.SOUL] = 2

		self.value[Elements.BELIEF] = 3
		self.value[Elements.NATURE] = 6

	def onPlayAnotherCard(self, source: Actor, card: Card) -> None:
		natureValue = card.value.get(Elements.NATURE, 0)
		if natureValue > 0:
			GameManager.addToBot(RecoverEvent(source, natureValue))

# # Spells

class Lamentation(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Lamentation"
		self.description = "Deal {Color.PURPLE}{self.damage}{Color.BLANK} damage."
		self.type = CardType.SPELL

		self.cost[Elements.SOUL] = 5
		self.damage = 12
	
	def onPlay(self, source: Actor, origin: CardPile) -> None:
		super().onPlay(source, origin)

		GameManager.addToBot(DamageEvent(source, GameManager.getOpponent(source), self.damage))

class Requiem(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Requiem"
		self.description = "Deal {Color.PURPLE}{self.damage}{Color.BLANK} damage."
		self.type = CardType.SPELL

		self.cost[Elements.SOUL] = 24
		self.damage = 666

	def onPlay(self, source: Actor, origin: CardPile) -> None:
		super().onPlay(source, origin)

		GameManager.addToBot(DamageEvent(source, GameManager.getOpponent(source), self.damage))


# # Dogmas




""" Final Setup """

# Pre-create the two players and the GameManager
Player1 = Actor("", 100, [])
Player2 = Actor("", 100, [])
GameManager = CombatManager(Player1, Player2)