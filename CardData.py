from __future__ import annotations
from enum import Enum
from random import choices, shuffle
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

# Define enums for Elements, Card Types, Card Colors and Card Tags
class Elements(Enum):
	LIFE = "Life"
	SOUL = "Soul"
	VIRTUE = "Virtue"
	SIN = "Sin"
	BELIEF = "Belief"
	NATURE = "Nature"

class CardType(Enum):
	CREATION = "Creation"
	SPELL = "Spell"
	DOGMA = "Dogma"

class CardColor(Enum):
	WHITE = "White"
	BLACK = "Black"
	GREY = "Grey"
	PURPLE = "Purple"

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
		self.color: CardColor

		self.value: Dict[Elements, int] = {}
		self.tags: List[CardTags] = []

	def onPlay(self, source: Actor, origin: CardPile) -> None:
		pile = getCardStack(source, origin)
		pile.remove(self)
		if self.type == CardType.CREATION:
			source.world.append(self)
		else:
			source.discard.append(self)

	def onDraw(self, source: Actor) -> None:
		pass

	def onAscend(self, source: Actor) -> None:
		pass

	def onDescend(self, source: Actor) -> None:
		pass

	def onReturn(self, source: Actor, origin: Literal[CardPile.ABOVE, CardPile.BELOW]) -> None:
		pass

	def dynamicDescription(self) -> str:
		return eval(f"f'{self.description}'")

	def __str__(self) -> str:
		return f"{Color.GREEN}{self.name}{Color.BLANK}, {Color.UNDERLINE}{self.type.value}{Color.BLANK}, {Color.UNDERLINE}{self.color.value}{Color.BLANK}:\n{self.dynamicDescription()}"


# Define a CardStack class, representing an ordered pile of cards
class CardStack(List[Card]):
	def __getitem__(self, key: int | slice) -> CardStack:
		return list.__getitem__(self, key) # type: ignore
	
	def __add__(self, other: List[Card]) -> CardStack:
		return list.__add__(self, other) # type: ignore

	def __str__(self) -> str:
		return "\n".join([f"[{Color.PURPLE}{i}{Color.BLANK}] {Color.GREEN}{card.name}{Color.BLANK}" for i, card in enumerate(self)])

	def getTopNCard(self, n: int) -> List[Card]:
		return self[n:]


# Function transforming a CardPile argument into the corresponding CardStack
def getCardStack(source: Actor, pile: CardPile) -> CardStack:
	return getattr(source, pile.value)


""" Events """

# Event called for each player at the beginning of a match, handling card shuffle
class SetupEvent(Event):
	def __init__(self, target: Actor) -> None:
		super().__init__()
		self.target = target
	
	def update(self) -> None:
		# Create the draw, a copy of the deck
		self.target.draw = self.target.deck[:]

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
		shuffle(self.target.draw)
		shuffle(genesis)
		shuffle(apocalypse)

		# Put the 3 piles together, with apocalypse at the bottom and genesis at the top
		self.target.draw = apocalypse + self.target.draw + genesis

		# Tell the event manager we're done
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
	def __init__(self, owner: Actor, source: CardPile,  potency: int, anyNumber: bool, random: bool, filter: Callable[[Card], bool], consumer: Callable[[List[Card]], None]) -> None:
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
					choice = choices(pile, k=1)[0]
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
					# If it is a valid value in the range, add the carde to the selection and remove it from the posibilities
					elif choice in range(len(pile)):
						selection.append(pile[choice]) # type: ignore
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
		def ascendConsumer(list: List[Card]):
			for card in list:
				pile: CardStack = getattr(self.owner, self.source.value.lower())

				card.onAscend(self.owner)
				self.owner.above.append(card)
				pile.remove(card)
		
		# Add the event to the event queue
		GameManager.addToBot(SelectCardsEvent(self.owner, self.source, self.potency, self.anyNumber, self.random, lambda _: True, ascendConsumer))

		# Tell the event manager that it can continue
		self.isDone = True


""" Cards """

class Pantheon(Card):
	def __init__(self) -> None:
		super().__init__()
		self.name = "Pantheon"
		self.description = "When played, you and your opponent recover {Color.PURPLE}{self.healing}{Color.BLANK} HP."
		self.type = CardType.CREATION
		self.color = CardColor.WHITE

		self.value[Elements.BELIEF] = 3
		self.value[Elements.VIRTUE] = 1
		self.healing = 10
	
	def onPlay(self, source: Actor, origin: CardPile) -> None:
		GameManager.addToBot(RecoverEvent(source, self.healing))
		GameManager.addToBot(RecoverEvent(GameManager.getOpponent(source), self.healing))

		super().onPlay(source, origin)


""" Final Setup """

# Pre-create the two players and the GameManager
Player1 = Actor("", 100, [])
Player2 = Actor("", 100, [])
GameManager = CombatManager(Player1, Player2)