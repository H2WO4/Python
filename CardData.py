from __future__ import annotations
from random import choices, shuffle
from EventSystemTemplate import Event, EventManager
from typing import Callable, Dict, List, Literal

# Define a color enum for text priting
class TextColor:
	PURPLE = '\033[95m'
	BLUE = '\033[94m'
	CYAN = '\033[96m'
	GREEN = '\033[92m'
	YELLOW = '\033[93m'
	RED = '\033[91m'
	BOLD = '\033[1m'
	UNDERLINE = '\033[4m'
	BLANK = '\033[0m'

# Define Types for enforcing types and reducing chances of bugs
class ElementsT:
	def __init__(self, value: str) -> None:
		self.value = value	

class CardColorT:
	def __init__(self, value: str) -> None:
		self.value = value
	
	def __str__(self) -> str:
		return self.value.title()

class CardTagsT:
	def __init__(self, value: str) -> None:
		self.value = value

class CardPileT:
	def __init__(self, value: str) -> None:
		self.value = value


# Define enums for Elements, Card Colors and Card Tags
class Elements:
	LIGHT = ElementsT("LIGHT")
	DARK = ElementsT("DARK")
	LIFE = ElementsT("LIFE")

class CardColor:
	WHITE = CardColorT("WHITE")
	BLACK = CardColorT("BLACK")
	GREY = CardColorT("GREY")
	PURPLE = CardColorT("PURPLE")

class CardTags:
	GENESIS = CardTagsT("GENESIS")
	APOCALYPSE = CardTagsT("APOCALYPSE")

class CardPile:
	DRAW = CardPileT("DRAW")
	HAND = CardPileT("HAND")
	DISCARD = CardPileT("DISCARD")
	WORLD = CardPileT("WORLD")
	ABOVE = CardPileT("ABOVE")
	BELOW = CardPileT("BELOW")


# Define lists containing the entire enums
AllElements: List[ElementsT] = [getattr(Elements, attr) for attr in vars(Elements) if not attr.startswith("__")]
AllCardColors: List[CardColorT] = [getattr(CardColor, attr) for attr in vars(CardColor) if not attr.startswith("__")]
AllTags: List[CardTagsT] = [getattr(CardTags, attr) for attr in vars(CardTags) if not attr.startswith("__")]
AllPiles: List[CardPileT] = [getattr(CardPile, attr) for attr in vars(CardPile) if not attr.startswith("__")]


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

	def playCard(self, card: Card) -> None:
		pass

	def setDeck(self, deck: List[Card]) -> None:
		self.deck = CardStack(deck)

	def setName(self, name: str) -> None:
		self.name = name

	def worldValue(self) -> Dict[ElementsT, int]:
		output: Dict[ElementsT, int] = {i: 0 for i in AllElements}
		for i in self.world:
			for j in i.value:
				output[j] += i.value[j]
		return output


# Define a Card class, representing a playing card
class Card:
	def __init__(self, name: str, description: str, color: CardColorT) -> None:
		self.name = name
		self.description = description
		self.color = color

		self.value: Dict[ElementsT, int] = {}
		self.tags: List[CardTagsT] = []

	def onPlay(self, source: Actor) -> None:
		pass

	def onDraw(self, source: Actor) -> None:
		pass

	def onAscend(self, source: Actor) -> None:
		pass

	def onDescend(self, source: Actor) -> None:
		pass

	def onReturn(self, source: Actor, origin: Literal["ABOVE", "BELOW"]) -> None:
		pass

	def dynamicDescription(self) -> str:
		return eval(f"f'{self.description}'")

	def __str__(self) -> str:
		return f"{self.name}, {self.color}:\n{self.dynamicDescription()}"


# Define a CardStack class, representing an ordered pile of cards
class CardStack(List[Card]):
	def __getitem__(self, key: int | slice) -> CardStack:
		return list.__getitem__(self, key) # type: ignore
	
	def __add__(self, other: List[Card]) -> CardStack:
		return list.__add__(self, other) # type: ignore

	def __str__(self) -> str:
		return "\n".join([f"[{TextColor.PURPLE}{i}{TextColor.BLANK}] {TextColor.GREEN}{card.name}{TextColor.BLANK}" for i, card in enumerate(self)])

	def getTopNCard(self, n: int) -> List[Card]:
		return self[n:]

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

# Standart damage event, handling possible multi-hits
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
				print(f"{self.target.name} lost {self.damage} HP. They have {self.target.health} HP left.")
			else:
				print(f"{self.target.name} is dead.")
				break

		# Tell the event manager that it can continue
		self.isDone = True

class SelectCardsEvent(Event):
	def __init__(self, owner: Actor, source: CardPileT, potency: int, anyNumber: bool, random: bool, filter: Callable[[Card], bool], consumer: Callable[[List[Card]], None]) -> None:
		super().__init__()
		self.owner = owner
		self.source = source
		self.potency = potency
		self.anyNumber = anyNumber
		self.random = random
		self.filter = filter
		self.consumer = consumer
	
	def update(self) -> None:
		# Obtain the pile concerned for the action
		basePile: CardStack = getattr(self.owner, self.source.value.lower())
		# Create a new pile and filter the base pile depending on the chosen condition into it
		pile = CardStack()
		for card in basePile:
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
					choice = int(input(f"{TextColor.YELLOW}Enter the number of the card you wish to choose: {TextColor.BLANK}")) - 1
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
					print(f"{TextColor.RED}Please enter a valid input!{TextColor.BLANK}\n")
			# If no choice is needed, simply add all available cards and abort
			else:
				selection.extend(pile)
				break

		# Apply the consumer unto all the cards chosen
		self.consumer(selection)

		# Tell the event manager that it can continue
		self.isDone = True

# Standart Ascend event
class AscendEvent(Event):
	def __init__(self, owner: Actor, source: CardPileT, potency: int, anyNumber: bool, random: bool) -> None:
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

class Test(Card):
	def __init__(self) -> None:
		super().__init__("Test Card", "This is a test", CardColor.PURPLE)

class Test2(Card):
	def __init__(self) -> None:
		super().__init__("Test Card 2", "This is a test", CardColor.PURPLE)


""" Final Setup """

# Pre-create the two players and the GameManager
Player1 = Actor("", 100, [])
Player2 = Actor("", 100, [])
GameManager = CombatManager(Player1, Player2)