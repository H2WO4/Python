from __future__ import annotations
from typing import Generic, List, TypeVar

T = TypeVar("T")

class Queue(Generic[T]):
	def __init__(self) -> None:
		self.values: List[T] = []

	def __len__(self) -> int:
		return len(self.values)
	
	def get(self) -> T | None:
		if len(self) == 0:
			return None
		output = self.values[0]
		self.values = self.values[1:]
		return output

	def addToBottom(self, other: T) -> None:
		self.values.append(other)
	
	def addToTop(self, other: T) -> None:
		self.values = [other] + self.values


class EventManager:
	def __init__(self) -> None:
		self.queue: Queue[Event] = Queue()
	
	def execQueue(self) -> None:
		while (event := self.queue.get()) != None:
			while not event.isDone:
				event.update()
	
	def addToBot(self, event: Event) -> None:
		self.queue.addToBottom(event)

	def addToTop(self, event: Event) -> None:
		self.queue.addToTop(event)


class Event:
	def __init__(self) -> None:
		self.isDone = False

	def update(self) -> None:
		pass
