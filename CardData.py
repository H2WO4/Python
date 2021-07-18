from __future__ import annotations
from EventSystemTemplate import Event, EventManager
from typing import List, Literal

CardType = Literal["ATK", "SKL", "POW"]
CardTarget = Literal["ONE", "NAN"]
DamageType = Literal["NORMAL", "PIERCE", "MAGIC"]

GameManager = EventManager()


class Actor:
	def __init__(self, name: str, health: int, deck: List[Card]) -> None:
		self.name = name
		self.health = health
		self.deck = deck

		self.energy = 0
		self.block = 0
		self.statues: List[Status] = []

		self.draw: List[Card] = []
		self.hand: List[Card] = []
		self.discard: List[Card] = []
		self.exhaust: List[Card] = []
		self.cemetery: List[Card] = []
		self.powers: List[Card] = []

	def getStatus(self, other: str) -> Status | None:
		for i in self.statues:
			if i.name == other:
				return i

	def turn(self, energy: int) -> None:
		pass


class Card:
	def __init__(self, name: str, cost: int, type: CardType, target: CardTarget) -> None:
		self.name = name
		self.cost = cost
		self.type = type
		self.target = target

	def onPlay(self, source: Actor, target: Actor) -> None:
		pass

	def onDraw(self, source: Actor) -> None:
		pass

	def onDiscard(self, source: Actor) -> None:
		pass

	def onExhaust(self, source: Actor) -> None:
		pass

	def onBan(self, source: Actor) -> None:
		pass


class Status:
	def __init__(self, name: str, owner: Actor, potency: int, turn: int) -> None:
		self.name = name
		self.owner = owner
		self.potency = potency
		self.turn = turn

	def __eq__(self, other: Status) -> bool:
		return self.name == other.name and self.owner == other.owner

	def __add__(self, other: Status) -> Status:
		if self == other:
			return Status(self.name, self.owner, self.potency + other.potency, self.turn + other.turn)
		else:
			raise TypeError

	def onPlayCard(self, card: Card) -> None:
		pass

	def onTurnStart(self, energy: int) -> None:
		pass

	def onTurnEnd(self) -> None:
		pass

	def onDiscard(self, card: Card) -> None:
		pass

	def onDraw(self, cards: List[Card]) -> None:
		pass

	def onExhaust(self, card: Card) -> None:
		pass

	def onBan(self, card: Card) -> None:
		pass

	def onLoseHP(self, amount: int) -> int:
		return amount

class PermanentStatus(Status):
	def __init__(self, name: str, owner: Actor, potency: int) -> None:
		super().__init__(name, owner, potency, -1)
	
	def __add__(self, other: Status) -> Status:
		if self == other:
			return Status(self.name, self.owner, self.potency + other.potency, -1)
		else:
			raise TypeError

	def onTurnEnd(self) -> None:
		pass

class TurnBasedStatus(Status):
	def __init__(self, name: str, owner: Actor, turn: int) -> None:
		super().__init__(name, owner, -1, turn)

	def __add__(self, other: Status) -> Status:
		if self == other:
			return Status(self.name, self.owner, -1, self.turn + other.turn)
		else:
			raise TypeError

	def onTurnEnd(self) -> None:
		self.turn -= 1
		if self.turn == 0:
			status = self.owner.getStatus(self.name)
			if status is not None:
				self.owner.statues.remove(status)

""" Events """

class DamageEvent(Event):
	def __init__(self, source: Actor, target: Actor, damage: int, damageType: DamageType) -> None:
		super().__init__()
		self.source = source
		self.target = target
		self.damage = damage
		self.damageType = damageType

	def update(self) -> None:
		# Apply Strength, if any
		if self.damageType != "MAGIC":
			strength = self.source.getStatus("Strength")
			if strength is not None:
				self.damage += strength.potency
		
			# Return if damage is now 0
			if self.damage <= 0:
				return

		if self.damageType != "MAGIC":
			# Use Block, if any
			if self.target.block > 0:
				# Subtract Block and damage
				self.target.block = max(self.target.block - self.damage, 0)
				self.damage = max(self.damage - self.target.block, 0)
				# Displays result accordingly
				if self.target.block > 0:
					print(f"{self.target.name} lost {self.damage} Block. They have {self.target.block} Block left.")
				else:
					print(f"{self.target.name} lost {self.damage} Block. Their Block was broken.")

			# Return if damage is now 0
			if self.damage <= 0:
				return

		# Apply Statues, if any
		for st in self.target.statues:
			self.damage = st.onLoseHP(self.damage)

		# Return if damage is now 0
		if self.damage <= 0:
			return

		# Subtract health
		self.target.health = max(self.target.health - self.damage, 0)
		
		# Display result accordingly
		if self.target.health > 0:
			print(f"{self.target.name} lost {self.damage} HP. They have {self.target.health} HP.")
		else:
			print(f"{self.target.name} is dead.")

		# Tell the event manager that it can continue
		self.isDone = True


""" Statuses """

class StrengthStatus(PermanentStatus):
	def __init__(self, owner: Actor, potency: int) -> None:
		super().__init__("Strength", owner, potency)


""" Cards """

class Strike(Card):
	def __init__(self) -> None:
		super().__init__("Strike", 1, "ATK", "ONE")
		self.damage = 6
	
	def onPlay(self, source: Actor, target: Actor) -> None:
		GameManager.addToBot(DamageEvent(source, target, self.damage, "NORMAL"))
