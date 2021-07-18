from typing import Dict


class BattleManager:
	def __init__(self) -> None:
		pass



class Actor:
	def __init__(self, name: str, ressources: Dict[str, int],params: Dict[str, int]) -> None:
		self.name = name
		self.ressources = {i: (ressources[i], ressources[i]) for i in ressources}
		self.params = params

	def __str__(self) -> str:
		params = tuple(self.params.items())
		return "{}\n".format(self.name) + \
			"\t".join([f"{i}: {self.ressources[i][0]}/{self.ressources[i][1]}" for i in self.ressources]) + "\n" + \
			"\n".join([f"{params[2*i][0]}: {params[2*i][1]}" + (f"\t{params[2*i+1][0]}: {params[2*i+1][1]}" if i*2+1 != len(params) else "") for i in range((len(params)+1)//2)])


JeanClaude = Actor("Jean-Claude",
	{
		"HP": 100,  "MP": 50, "CCT" : 20
	},
	{
		"Attack": 10, "Defense": 20,
		"Faith": 0
	})

print(JeanClaude)