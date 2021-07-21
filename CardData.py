from __future__ import annotations
from EventSystemTemplate import Event, EventManager
from typing import List, Literal, Tuple

CardType = Literal["ATK", "SKL", "POW"]
CardTarget = Literal["ONE", "NAN"]
DamageType = Literal["NORMAL", "PIERCE", "MAGIC"]

GameManager = EventManager()


class Actor:
	def __init__(self, name: str, health: int, deck: List[Card]) -> None:
		self.name = name
		self.health = health
		self.deck = deck

		self.maxEnergy = 3
		self.energy = 0
		self.block = 0
		self.status: List[Status] = []

		self.draw: List[Card] = []
		self.hand: List[Card] = []
		self.discard: List[Card] = []
		self.exhaust: List[Card] = []
		self.cemetery: List[Card] = []
		self.powers: List[Card] = []

	def getStatus(self, other: str) -> Status | None:
		for i in self.status:
			if i.name == other:
				return i

	def turn(self) -> None:
		pass

	def playCard(self, card: Card, target: Actor, freePlay: bool = False) -> None:
		if not freePlay:
			self.energy = max(self.energy - card.cost, 0)
		card.onPlay(self, target)


class Card:
	def __init__(self, name: str, description: str, cost: int, type: CardType, target: CardTarget) -> None:
		self.name = name
		self.description = description
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

	def dynamicDescription(self) -> str:
		return eval(f"f'{self.description}'")

	def __str__(self) -> str:
		return f"{self.name}, {self.type}, {self.cost}E\n{self.dynamicDescription()}"


class Status:
	def __init__(self, name: str, owner: Actor, potency: int, turn: int, buff: bool | None = True, canNegative: bool = False) -> None:
		self.name = name
		self.owner = owner
		self.potency = potency
		self.turn = turn
		self.canNegative = canNegative
		if canNegative:
			self.buff = potency > 0
		else:
			self.buff = buff

	def __eq__(self, other: Status) -> bool:
		return self.name == other.name and self.owner == other.owner

	def __add__(self, other: Status) -> Status:
		if self == other:
			newTurn, newPotency = self.turn + other.turn, self.potency + other.potency
			if newTurn == 0 or newPotency == 0:
				status = self.owner.getStatus(self.name)
				if status is not None:
					self.owner.status.remove(status)
			
			return Status(self.name, self.owner, newPotency, newTurn, self.buff, self.canNegative)
		else:
			raise TypeError

	def __iadd__(self, other: Status) -> Status:
		return self.__add__(other)

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

	def onAttack(self, damage: int, repeat: int, damageType: DamageType) -> Tuple[int, int]:
		return damage, repeat

	def onDefend(self, amount: int) -> int:
		return amount

class PermanentStatus(Status):
	def __init__(self, name: str, owner: Actor, potency: int, buff: bool | None = True, canNegative: bool = False) -> None:
		super().__init__(name, owner, potency, -1, buff, canNegative)
	
	def __add__(self, other: Status) -> Status:
		if self == other:
			newPotency = self.potency + other.potency
			if newPotency == 0:
				status = self.owner.getStatus(self.name)
				if status is not None:
					self.owner.status.remove(status)
			
			return Status(self.name, self.owner, newPotency, -1, self.buff, self.canNegative)
		else:
			raise TypeError

class TurnBasedStatus(Status):
	def __init__(self, name: str, owner: Actor, turn: int, buff: bool = True) -> None:
		super().__init__(name, owner, -1, turn, False, buff)

	def __add__(self, other: Status) -> Status:
		if self == other:
			newTurn= self.turn + other.turn
			if newTurn == 0:
				status = self.owner.getStatus(self.name)
				if status is not None:
					self.owner.status.remove(status)
			
			return Status(self.name, self.owner, -1, newTurn, self.buff, self.canNegative)
		else:
			raise TypeError

	def onTurnEnd(self) -> None:
		self.turn -= 1
		if self.turn == 0:
			status = self.owner.getStatus(self.name)
			if status is not None:
				self.owner.status.remove(status)


""" Events """

class DamageEvent(Event):
	def __init__(self, source: Actor, target: Actor, damage: int, repeat: int, damageType: DamageType) -> None:
		super().__init__()
		self.source = source
		self.target = target
		self.damage = damage
		self.repeat = repeat
		self.damageType: DamageType = damageType

	def update(self) -> None:
		# Apply offensive damage modifiers, if any
		for st in self.source.status:
			self.damage, self.repeat = st.onAttack(self.damage, self.repeat, self.damageType)
		
		# Return if damage is now 0
		if self.damage <= 0:
			self.isDone = True
			return

		# Execute the next steps for each repeat stack
		for _ in range(self.repeat):
			# Use Block, if any
			if self.damageType != "PIERCE":
				if self.target.block > 0:
					# Subtract Block and damage
					blockLost = min(self.damage, self.target.block)
					self.target.block, self.damage = max(self.target.block - self.damage, 0), max(self.damage - self.target.block, 0)
					# Displays result accordingly
					if self.target.block > 0:
						print(f"{self.target.name} lost {blockLost} Block. They have {self.target.block} Block left.")
					else:
						print(f"{self.target.name} lost {blockLost} Block. Their Block was broken.")

				# Return if damage is now 0
				if self.damage <= 0:
					self.isDone = True
					return

			# Apply defensives damage modifiers, if any
			for st in self.target.status:
				self.damage = st.onLoseHP(self.damage)

			# Return if damage is now 0
			if self.damage <= 0:
				self.isDone = True
				return

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

class ApplyStatusEvent(Event):
	def __init__(self, target: Actor, status: Status) -> None:
		super().__init__()
		self.target = target
		self.status = status

	def update(self) -> None:
		# Search for an eventual already existing identical status
		original = self.target.getStatus(self.status.name)

		# If it exists, simply revert to status addition
		if original is not None:
			original += self.status
		# If not, simply add it to the status list
		else:
			self.target.status.append(self.status)

		# Tell the event manager that it can continue
		self.isDone = True

class GainBlockEvent(Event):
	def __init__(self, source: Actor, target: Actor, amount: int) -> None:
		super().__init__()
		self.source = source
		self.target = target
		self.amount = amount
	
	def update(self) -> None:
		# Apply block modifiers, if any
		for st in self.source.status:
			self.amount = st.onDefend(self.amount)

		# Return if block is zero
		if self.amount <= 0:
			self.isDone = True
			return
		
		# Add block
		self.target.block += self.amount

		# Display block increase
		print(f"{self.target.name} gained {self.amount} Block. They now have {self.target.block} Block")

		# Tell the event maanger that it can continue
		self.isDone = True


""" Statuses """

class StrengthStatus(PermanentStatus):
	def __init__(self, owner: Actor, potency: int) -> None:
		super().__init__("Strength", owner, potency, True, True)

	def onAttack(self, damage: int, repeat: int, damageType: DamageType) -> Tuple[int, int]:
		if damageType != "MAGIC":
			return damage + self.potency, repeat
		else:
			return damage, repeat

class TemporaryStrengthStatus(PermanentStatus):
	def __init__(self, owner: Actor, potency: int) -> None:
		super().__init__("Temporary Strength", owner, potency, True, True)
	
	def onAttack(self, damage: int, repeat: int, damageType: DamageType) -> Tuple[int, int]:
		if damageType != "MAGIC":
			return damage + self.potency, repeat
		else:
			return damage, repeat

	def onTurnEnd(self) -> None:
		self.owner.status.remove(self)

class SurgeStatus(PermanentStatus):
	def __init__(self, owner: Actor, potency: int) -> None:
		super().__init__("Surge", owner, potency)

	def onAttack(self, damage: int, repeat: int, damageType: DamageType) -> Tuple[int, int]:
		if damageType == "MAGIC":
			GameManager.addToBot(ApplyStatusEvent(self.owner, SurgeStatus(self.owner, -1)))
			return damage * 2, repeat
		else:
			return damage, repeat

class OverchargeStatus(PermanentStatus):
	def __init__(self, owner: Actor, potency: int) -> None:
		super().__init__("Overcharge", owner, potency)
		self.counter = 0

	def onPlayCard(self, card: Card) -> None:
		# If the card played is a power, increase the counter
		if card.type == "POW":
			self.counter += 1
		
		# If the counter is now 3, reset the counter and add stacks of Surge
		if self.counter == 3:
			self.counter = 0
			GameManager.addToBot(ApplyStatusEvent(self.owner, SurgeStatus(self.owner, self.potency)))


""" Cards """

class Strike(Card):
	def __init__(self) -> None:
		name = "Strike"
		description = "Deal {self.damage} damage."
		cost = 1
		type = "ATK"
		target = "ONE"

		super().__init__(name, description, cost, type, target)

		self.damage = 6
	
	def onPlay(self, source: Actor, target: Actor) -> None:
		GameManager.addToBot(DamageEvent(source, target, self.damage, 1, "NORMAL"))

class LuckyShot(Card):
	def __init__(self) -> None:
		name = "Strike"
		description = "Deal {self.damage} damage. If the current turn is a multiple of 7, deal triple damage."
		cost = 2
		type = "ATK"
		target = "ONE"

		super().__init__(name, description, cost, type, target)

		self.damage = 11
	
	def onPlay(self, source: Actor, target: Actor) -> None:
		effectiveDamage = self.damage
		if 1 % 7 == 0: # A changer
			effectiveDamage *= 3
		
		GameManager.addToBot(DamageEvent(source, target, effectiveDamage, 1, "NORMAL"))
