from random import randint, choice
from gc import get_referrers

def damageCalculation(attacker, target, skill):

    if skill.effect == "Physical":
        hitProbability = attacker.physical[2] - target.physical[3]
        hit = randint(1, 100)
        
        if hit <= attacker.critical[0]:
            return "Critical"
            
        elif hit <= hitProbability:
            return round((1 + (randint(-20, 20) / 100)) * (attacker.physical[0] * (100 / (100 + target.physical[1])) * (2 + skill.power / 100)))

        return "Miss"

    elif skill.effect == "Magical":
        hitProbability = attacker.magical[2]
        hit = randint(1, 100)
        
        if hit <= attacker.critical[0]:
            return "Critical"
            
        elif hit <= hitProbability:
            return round((1 + (randint(-10, 10) / 100)) * (attacker.magical[0] * (100 / (100 + target.physical[1])) * (2 + skill.power / 100)))

        return "Miss"

    elif skill.effect == "HP Recover":
        hitProbability = attacker.magical[2]

        if randint(1, 100) <= hitProbability:
            return round((1 + (randint(-10, 10) / 100)) * (attacker.magical[0] * (2 + skill.power / 100)))

        return "Miss"

    elif skill.effect == "MP Recover":
        hitProbability = attacker.magical[2]

        if randint(1, 100) <= hitProbability:
            return round((1 + (randint(-10, 10) / 100)) * (attacker.magical[0] * (2 + skill.power / 100)))

        return "Miss"

def damageFormula(attacker, target, skill):

    if skill.effect == "Physical":
        return round((1 + (randint(-20, 20) / 100)) * (attacker.physical[0] * (100 / (100 + target.physical[1])) * (2 + skill.power / 100)))

    elif skill.effect == "Magical":
        return round((1 + (randint(-20, 20) / 100)) * (attacker.physical[0] * (100 / (100 + target.physical[1])) * (2 + skill.power / 100)))


class Entity:

    def __init__(self, name, maxHP, maxMP, maxTP, pAtk, pDef, mAtk, mDef, pDex, pEva, mMtr, cLuk, cMlt):
        self.name = name
        self.maxHMTP = [maxHP, maxMP, maxTP]
        self.HMTP = [maxHP, maxMP, maxTP]
        self.physical = [pAtk, pDef, pDex, pEva]
        self.magical = [mAtk, mDef, mMtr]
        self.critical = [cLuk, cMlt]
        self.skillList = {}
        self.alive = True

    def learnSkill(self, skill):
        self.skillList[skill.name] = skill

    def useSkillOne(self, skill, target):
    
        print("")
        if self.skillList[skill].effect == "Physical":
            actualDamage = damageCalculation(self, target, self.skillList[skill])

            if actualDamage == "Miss":
                print("The attack missed !")

            else:
                critical = False
                if actualDamage == "Critical":
                    actualDamage = damageFormula(self, target, self.skillList[skill]) * 3
                    critical = True
                    
                target.HMTP[0] -= actualDamage
                
                if critical:
                    print("Critical Hit !")
     
                print("{} did a {} and dealt {} damage to {}".format(self.name, skill, actualDamage, target.name))
                if target.HMTP[0] <= 0:
                    target.alive = False
                    print("{} is dead !".format(target.name))

        elif self.skillList[skill].effect == "Magical":
            actualDamage = damageCalculation(self, target, self.skillList[skill])

            if actualDamage == "Miss":
                print("The spell failed !")
                
            else:
                critical = False
                if actualDamage == "Critical":
                    actualDamage = damageFormula(self, target, self.skillList[skill]) * 3
                    critical = True
                    
                target.HMTP[0] -= actualDamage
                
                if critical:
                    print("Critical Hit !")
                    
                print("{} casted {} and dealt {} damage to {}".format(self.name, skill, actualDamage, target.name))
                if target.HMTP[0] <= 0:
                    target.alive = False
                    print("{} is dead !".format(target.name))

        elif self.skillList[skill].effect == "HP Recover":
            actualDamage = damageCalculation(self, target, self.skillList[skill])

            if actualDamage == "Miss":
                print("The spell failed !")

            else:
                target.HMTP[0] += actualDamage
                if target.HMTP[0] > target.maxHMTP[0]:
                        target.HMTP[0] = target.maxHMTP[0]
                print("{} casted {} and healed {} {} HP".format(self.name, skill, target.name, actualDamage))

        elif self.skillList[skill].effect == "MP Recover":
            actualDamage = damageCalculation(self, target, self.skillList[skill])

            if actualDamage == "Miss":
                print("The spell failed !")

            else:
                target.HMTP[1] += actualDamage
                if target.HMTP[1] > target.maxHMTP[1]:
                        target.HMTP[1] = target.maxHMTP[1]
                print("{} casted {} and recovered {} {} MP".format(self.name, skill, target.name, actualDamage))

        self.HMTP[1] -= self.skillList[skill].mtpCost[0]
        self.HMTP[2] -= self.skillList[skill].mtpCost[1]

    def useSkillAll(self, skill, scope):
    
        print("")
        targets = {}
        if scope == "Ennemies":
            for i in get_referrers(Hero):
                if i.__class__ is Hero:
                    targets[i] = i

        elif scope == "Allies":
            for i in get_referrers(Entity):
                if i.__class__ is Entity:
                    targets[i] = i

        if self.skillList[skill].effect == "Physical":
            for target in targets:
                actualDamage = damageCalculation(self, target, self.skillList[skill])

                if actualDamage == "Miss":
                    print("The attack missed !")

                else:
                    critical = False
                    if actualDamage == "Critical":
                        actualDamage = damageFormula(self, target, self.skillList[skill]) * 3
                        critical = True
                    
                    target.HMTP[0] -= actualDamage
                
                    if critical:
                        print("Critical Hit !")

                    print("{} did a {} and dealt {} damage to {}".format(self.name, skill, actualDamage, target.name))
                    if target.HMTP[0] <= 0:
                        target.alive = False
                        print("{} is dead !".format(target.name))

        elif self.skillList[skill].effect == "Magical":
            for target in targets:
                actualDamage = damageCalculation(self, target, self.skillList[skill])

                if actualDamage == "Miss":
                    print("The spell failed !")

                else:
                    critical = False
                    if actualDamage == "Critical":
                        actualDamage = damageFormula(self, target, self.skillList[skill]) * 3
                        critical = True
                    
                    target.HMTP[0] -= actualDamage
                
                    if critical:
                        print("Critical Hit !")

                    print("{} casted {} and dealt {} damage to {}".format(self.name, skill, actualDamage, target.name))
                    if target.HMTP[0] <= 0:
                        target.alive = False
                        print("{} is dead !".format(target.name))

        elif self.skillList[skill].effect == "HP Recover":
            for target in targets:
                actualDamage = damageCalculation(self, target, self.skillList[skill])

                if actualDamage == "Miss":
                    print("The spell failed !")

                else:
                    target.HMTP[0] += actualDamage
                    if target.HMTP[0] > target.maxHMTP[0]:
                        target.HMTP[0] = target.maxHMTP[0]
                    print("{} casted {} and healed {} {} HP".format(self.name, skill, target.name, actualDamage))

        elif self.skillList[skill].effect == "MP Recover":
            for target in targets:
                actualDamage = damageCalculation(self, target, self.skillList[skill])

                if actualDamage == "Miss":
                    print("The spell failed !")

                else:
                    target.HMTP[1] += actualDamage
                    if target.HMTP[1] > target.maxHMTP[1]:
                        target.HMTP[1] = target.maxHMTP[1]
                    print("{} casted {} and recovered {} {} MP".format(self.name, skill, target.name, actualDamage))

        self.HMTP[1] -= self.skillList[skill].mtpCost[0]
        self.HMTP[2] -= self.skillList[skill].mtpCost[1]

    def useSkillSelf(self, skill):
        
        print("")
        if self.skillList[skill].effect == "Physical":
            actualDamage = damageCalculation(self, self, self.skillList[skill])

            if actualDamage == "Miss":
                print("The attack missed !")

            else:
                critical = False
                if actualDamage == "Critical":
                    actualDamage = damageFormula(self, target, self.skillList[skill]) * 3
                    critical = True
                    
                target.HMTP[0] -= actualDamage
                
                if critical:
                    print("Critical Hit !")

                print("{} did a {} and dealt {} damage to themself".format(self.name, skill, actualDamage))
                if self.HMTP[0] <= 0:
                    self.alive = False
                    print("{} is dead !".format(self.name))

        elif self.skillList[skill].effect == "Magical":
            actualDamage = damageCalculation(self, self, self.skillList[skill])

            if actualDamage == "Miss":
                print("The spell failed !")

            else:
                critical = False
                if actualDamage == "Critical":
                    actualDamage = damageFormula(self, target, self.skillList[skill]) * 3
                    critical = True
                    
                target.HMTP[0] -= actualDamage
                
                if critical:
                    print("Critical Hit !")

                print("{} casted {} and dealt {} damage to themself".format(self.name, skill, actualDamage))
                if self.HMTP[0] <= 0:
                    self.alive = False
                    print("{} is dead !".format(target.name))

        elif self.skillList[skill].effect == "HP Recover":
            actualDamage = damageCalculation(self, self, self.skillList[skill])

            if actualDamage == "Miss":
                print("The spell failed !")

            else:
                self.HMTP[0] += actualDamage
                if target.HMTP[0] > target.maxHMTP[0]:
                    target.HMTP[0] = target.maxHMTP[0]
                print("{} casted {} and healed themself {} HP".format(self.name, skill, actualDamage))

        elif self.skillList[skill].effect == "MP Recover":
            actualDamage = damageCalculation(self, self, self.skillList[skill])

            if actualDamage == "Miss":
                print("The spell failed !")

            else:
                self.HMTP[1] += actualDamage
                if target.HMTP[1] > target.maxHMTP[1]:
                    target.HMTP[1] = target.maxHMTP[1]
                print("{} casted {} and recovered themself {} MP".format(self.name, skill, actualDamage))

        self.HMTP[1] -= self.skillList[skill].mtpCost[0]
        self.HMTP[2] -= self.skillList[skill].mtpCost[1]

    def __str__(self):
        hpPC = round(self.HMTP[0] / self.maxHMTP[0] * 100)
        return "\n{}:\nHP: {}%".format(self.name, hpPC)

class Hero(Entity):

    def useSkillAll(self, skill, scope):
        
        print("")
        targets = {}
        if scope == "Allies":
            for i in get_referrers(Hero):
                if i.__class__ is Hero:
                    targets[i] = i

        elif scope == "Ennemies":
            for i in get_referrers(Entity):
                if i.__class__ is Entity:
                    targets[i] = i

        if self.skillList[skill].effect == "Physical":
            for target in targets:
                actualDamage = damageCalculation(self, target, self.skillList[skill])

                if actualDamage == "Miss":
                    print("The attack missed !")

                else:
                    critical = False
                    if actualDamage == "Critical":
                        actualDamage = damageFormula(self, target, self.skillList[skill]) * 3
                        critical = True
                    
                    target.HMTP[0] -= actualDamage
                
                    if critical:
                        print("Critical Hit !")

                    print("{} did a {} and dealt {} damage to {}".format(self.name, skill, actualDamage, target.name))
                    if target.HMTP[0] <= 0:
                        target.alive = False
                        print("{} is dead !".format(target.name))

        elif self.skillList[skill].effect == "Magical":
            for target in targets:
                actualDamage = damageCalculation(self, target, self.skillList[skill])

                if actualDamage == "Miss":
                    print("The spell failed !")

                else:
                    critical = False
                    if actualDamage == "Critical":
                        actualDamage = damageFormula(self, target, self.skillList[skill]) * 3
                        critical = True
                    
                    target.HMTP[0] -= actualDamage
                
                    if critical:
                        print("Critical Hit !")

                    print("{} casted {} and dealt {} damage to {}".format(self.name, skill, actualDamage, target.name))
                    if target.HMTP[0] <= 0:
                        target.alive = False
                        print("{} is dead !".format(target.name))

        elif self.skillList[skill].effect == "HP Recover":
            for target in targets:
                actualDamage = damageCalculation(self, target, self.skillList[skill])

                if actualDamage == "Miss":
                    print("The spell failed !")

                else:
                    target.HMTP[0] += actualDamage
                    if target.HMTP[0] > target.maxHMTP[0]:
                        target.HMTP[0] = target.maxHMTP[0]
                    print("{} casted {} and healed {} {} HP".format(self.name, skill, target.name, actualDamage))

        elif self.skillList[skill].effect == "MP Recover":
            for target in targets:
                actualDamage = damageCalculation(self, target, self.skillList[skill])

                if actualDamage == "Miss":
                    print("The spell failed !")

                else:
                    target.HMTP[1] += actualDamage
                    if target.HMTP[1] > target.maxHMTP[1]:
                        target.HMTP[1] = target.maxHMTP[1]
                    print("{} casted {} and recovered {} {} MP".format(self.name, skill, target.name, actualDamage))

        self.HMTP[1] -= self.skillList[skill].mtpCost[0]
        self.HMTP[2] -= self.skillList[skill].mtpCost[1]

    def useItem(self, item, target):
        pass

    def __str__(self):
        return "\n{}:\nHP: {}/{} MP: {}/{} TP: {}/{}\nAtk: {} Def: {}\nDex: {}% Eva: {}%\nMat: {} Mdf: {}\nMastery: {}%\nCritical Chance: {}%\nCritical Multiplier: x{}".format(self.name, self.HMTP[0], self.maxHMTP[0], self.HMTP[1], self.maxHMTP[1], self.HMTP[2], self.maxHMTP[2], self.physical[0], self.physical[1], self.physical[2], self.physical[3], self.magical[0], self.magical[1], self.magical[2], self.critical[0], self.critical[1])

class Skill:

    def __init__(self, name, power, effect, mpCost, tpCost, scope):

        self.name = name
        self.effect = effect
        self.power = power
        self.mtpCost = [mpCost, tpCost]
        self.scope = scope

    def __str__(self):

        return "\n{}:\n{} Power: {}\nMP Cost: {} TP Cost: {}\nScope: {}\n".format(self.name, self.effect, self.power, self.mtpCost[0], self.mtpCost[1], self.scope)

class Inventory:

    def __init__(self):
        self.items = {}

    def addItem(self, item, number):
        item.number += number
        self.items[item.name] = item

    def view(self):
        for item in self.items.values():
            if item.number >= 1:
                print("{} x{}".format(item.name, item.number))

class Item:

    def __init__(self, name, power, effect, scope):
        self.name = name
        self.effect = effect
        self.power = power
        self.scope = scope
        self.number = 0

    

link = Hero("Link", 100, 30, 80, 18, 10, 10, 8, 95, 5, 85, 10, 2)
zelda = Hero("Zelda", 80, 100, 20, 10, 15, 12, 15, 85, 10, 100, 5, 3)

inv = Inventory()
healingPotion = Item("Healing Potion", 50, "HP Recover", "One")
manaPotion = Item("Mana Potion", 50, "MP Recover", "One")

inv.addItem(healingPotion, 10)
inv.addItem(manaPotion, 5)

bash = Skill("Bash", 10, "Physical", 0, 0, "One")
fireball = Skill("Fireball", 50, "Magical", 10, 0, "One")
spinAttack = Skill("Spin Attack", 50, "Physical", 0, 20, "All Ennemies")
mindMissile = Skill("Mind Missile", 20, "Magical", 0, 0, "One")
heal = Skill("Heal", 100, "HP Recover", 20, 0, "One")
concentrate = Skill("Concentrate", 50, "MP Recover", 0, 0, "Self")
heroStrike = Skill("Hero Strike", 150, "Physical", 20, 50, "One")
healingChant = Skill("Healing Chant", 50, "HP Recover", 50, 0, "All Allies")

link.learnSkill(bash)
link.learnSkill(spinAttack)
link.learnSkill(heroStrike)

zelda.learnSkill(mindMissile)
zelda.learnSkill(fireball)
zelda.learnSkill(heal)
zelda.learnSkill(concentrate)
zelda.learnSkill(healingChant)

slime = Entity("Slime", 60, 50, 0, 10, 8, 10, 8, 95, 0, 60, 0, 0)
slime2 = Entity("Slime 2", 60, 50, 0, 10, 8, 10, 8, 95, 0, 60, 0, 0)

charge = Skill("Charge", 10, "Physical", 0, 0, "One")
poweredCharge = Skill("Powered Charge", 80, "Physical", 20, 0, "One")

slime.learnSkill(charge)
slime.learnSkill(poweredCharge)
slime2.learnSkill(charge)
slime2.learnSkill(poweredCharge)

while True:
    for i in get_referrers(Hero):
        turnEnded = False
        
        if i.__class__ is Hero:
            if i.alive == True:
                print("\nIt's {} turn".format(i.name))
                
                while not turnEnded:
                    action = input().title()

                    if action == "Skills":
                        print("\nWhich skill ?")
                        for j in i.skillList:
                            print(j)
                            
                        action = input().title()

                        if action in i.skillList:
                            print(i.skillList[action])

                        else:
                            print("\nSkill not found")

                    elif action == "Attack":
                        print("\nWhich skill ?")
                        for j in i.skillList:
                            print(j)
                        
                        action = input().title()
                                
                        if action in i.skillList:
                            skill = action
                            if i.skillList[skill].scope == "One":
                                print("\nWhich one ?")
                                targets = {}
             
                                for j in get_referrers(Entity) + get_referrers(Hero):
                                    if isinstance(j, Entity):
                                        if j.alive == True:
                                            print(j.name)
                                            targets[j.name] = j
            
                                action = input().title()
                                if action in targets:
                                    target = action
                                    i.useSkillOne(skill, targets[target])
                                    turnEnded = True
                            
                                else:
                                    print("\nTarget not found")

                            elif i.skillList[skill].scope == "All Ennemies":
                                i.useSkillAll(skill, "Ennemies")
                                turnEnded = True

                            elif i.skillList[skill].scope == "All Allies":
                                i.useSkillAll(skill, "Allies")
                                turnEnded = True
                                

                        else:
                            print("\nSkill not found")
                                
                        
                            
                    elif action == "Check":
                        print("\nWhich one ?")
                        targets = {}
                        
                        for j in get_referrers(Entity) + get_referrers(Hero):
                            if isinstance(j, Entity):
                                if j.alive == True:
                                    print(j.name)
                                    targets[j.name] = j

                        action = input().title()
                        if action in targets:
                            print(targets[action])

                        else:
                            print("\nTarget not found")

                    elif action == "Help":
                        print("\nAttack, Skills, Check, Inventory, Wait")

                    elif action == "Wait":
                        print("\n{} did nothing".format(i.name))
                        turnEnded = True

                    elif action == "Inventory":
                        print("\nWhat do you want ?")
                        print("View\nItem\nUse")
                        
                        action = input().title()
                        if action == "View":
                            print("")
                            inv.view()

                        else:
                            print("Command not found")

                            
    for i in get_referrers(Entity):
        if i.__class__ is Entity:
            turnEnded = False
            if i.alive and not turnEnded:
                skill = choice(list(i.skillList.keys()))
                targets = {}

                for j in get_referrers(Hero):
                    if j.__class__ is Hero:
                        if j.alive == True:
                            targets[j.name] = j

                if i.HMTP[1] >= i.skillList[skill].mtpCost[0] and i.HMTP[2] >= i.skillList[skill].mtpCost[1]:
                    if i.skillList[skill].scope == "One":
                        target = choice(list(targets.keys()))
                        i.useSkillOne(skill, targets[target])

                    elif i.skillList[skill].scope == "All Ennemies":
                        i.useSkillAll(skill, "Ennemies")

                    elif i.skillList[skill].scope == "All Allies":
                        i.useSkillAll(skill, "Allies")

                    turnEnded = True
