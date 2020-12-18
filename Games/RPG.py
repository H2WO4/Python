class Actor:
    def __init__(self, name, **stats):
        self.name = name
        self.stats = stats


class Hero(Actor):
    def __init__(self, name, **stats):
        Actor.__init__(self, name, **stats)

        Heroes.append(self)
    
    def __str__(self):
        output = "{}:\n".format(self.name)
        for i in self.stats:
            output += "{}: {}\n".format(eval(i), self.stats[i])
        
        return output


class Stat:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name


class Skill:
    def __init__(self, name, effect):
        self.name = name
        self.effect = effect


Heroes = []

mhp = Stat("Max HP")
mmp = Stat("Max MP")
patk = Stat("Physical Atk")
pdef = Stat("Physical Def")
matk = Stat("Magical Atk")
mdef = Stat("Magical Def")
cct = Stat("Concentration")

bash = Skill("Bash", lambda atk: 2 * atk)

Link = Hero("Link", mhp = 100, mmp = 30, patk = 15, pdef = 10, matk = 12, mdef = 12)
Zelda = Hero("Zelda", mhp = 100, mmp = 30, patk = 15, pdef = 10, matk = 12, mdef = 12, cct = 10)

print(Link)
print(Zelda)

print(bash)