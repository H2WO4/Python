from __future__ import annotations
from random import shuffle
from EventSystemTemplate import Event, EventManager
from typing import Dict, List, Literal

class TextColors:
    PURPLE = '\033[95m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    BLANK = '\033[0m'


class ElementsT:
	def __init__(self, value: str) -> None:
		self.value = value	
class CardColorT:
	def __init__(self, value: str) -> None:
		self.value = value
class TagsT:
	def __init__(self, value: str) -> None:
		self.value = value


class Elements:
	LIGHT = ElementsT("ELEMENT_LIGHT")
	DARK = ElementsT("ELEMENT_DARK")
	LIFE = ElementsT("ELEMENT_LIFE")


class CardColor:
	WHITE = CardColorT("COLOR_WHITE")
	BLACK = CardColorT("COLOR_BLACK")
	GREY = CardColorT("COLOR_GREY")
	PURPLE = CardColorT("COLOR_PURPLE")


class Tags:
	GENESIS = TagsT("TAG_GENESIS")
	APOCALYPSE = TagsT("TAG_APOCALYPSE")


AllElements: List[ElementsT] = [getattr(Elements, attr) for attr in vars(Elements) if not attr.startswith("__")]
AllCardColors: List[CardColorT] = [getattr(CardColor, attr) for attr in vars(CardColor) if not attr.startswith("__")]
AllTags: List[TagsT] = [getattr(Tags, attr) for attr in vars(Tags) if not attr.startswith("__")]

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


class Actor:
	def __init__(self, name: str, health: int, deck: List[Card]) -> None:
		# Attributes
		self.name = name
		self.deck = deck

		# Variables
		self.health = health
		self.initialDraw = 4
		self.handSize = 8
		self.drawPower = 1

		# Card Piles
		self.draw: List[Card] = []
		self.hand: List[Card] = []

		self.world: List[Card] = []

		self.above: List[Card] = []
		self.below: List[Card] = []

	def playCard(self, card: Card) -> None:
		pass

	def setDeck(self, deck: List[Card]) -> None:
		self.deck = deck

	def setName(self, name: str) -> None:
		self.name = name

	def worldValue(self) -> Dict[ElementsT, int]:
		output: Dict[ElementsT, int] = {i: 0 for i in AllElements}
		for i in self.world:
			for j in i.value:
				output[j] += i.value[j]
		return output


class Card:
	def __init__(self, name: str, description: str, color: CardColorT) -> None:
		self.name = name
		self.description = description
		self.color = color

		self.value: Dict[ElementsT, int] = {}
		self.tags: List[TagsT] = []

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
		return f"{self.name}, {self.color}\n{self.dynamicDescription()}"


""" Events """

class SetupEvent(Event):
	def __init__(self, target: Actor) -> None:
		super().__init__()
		self.target = target
	
	def update(self) -> None:
		# Create the draw, a copy of the deck
		self.target.draw = self.target.deck.copy()

		# Create 2 separate piles, for future shuffle
		genesis: List[Card] = []
		apocalypse: List[Card] = []
		# Put cards tagged Genesis and Apocalypse into these piles
		for i in self.target.draw.copy():
			if "GENESIS" in i.tags:
				self.target.draw.remove(i)
				genesis.append(i)
			elif "APOCALYPSE" in i.tags:
				self.target.draw.remove(i)
				apocalypse.append(i)

		# Shuffle the main draw pile
		shuffle(self.target.draw)

		# Put the 3 piles together, with apocalypse at the bottom and genesis at the top
		self.target.draw = apocalypse + self.target.draw + genesis

		self.isDone = True

class DamageEvent(Event):
	def __init__(self, source: Actor, target: Actor, damage: int, repeat: int) -> None:
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

""" Cards """




""" Final Setup """

Player1 = Actor("", 100, [])
Player2 = Actor("", 100, [])
GameManager = CombatManager(Player1, Player2)