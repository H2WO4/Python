from random import randint
from ItemChestData import stats, materials, types, attributes, qualities

print("Dans le coffre se trouve ...\n")

while True:
    # Chooses Ressources
    itemType = types[randint(0, len(types) - 1)]
    itemAttribute = attributes[randint(0, len(attributes) - 1)]
    itemMaterial = materials[randint(0, len(materials) - 1)]
    item = itemType.name + " " + itemMaterial.name

    # Applies Male/Female/Plural -> Type
    if itemType.gender == 1 and itemMaterial.feminine == 1:
        item += "e"
    elif itemType.gender == 1 and itemMaterial.feminine == 2:
        item = item[:-1] + "se"
    elif itemType.gender == 1 and itemMaterial.feminine == 3:
        item = item[:-3] + "rice"
    elif itemType.gender == 1 and itemMaterial.feminine == 4:
        item += "le"
    elif itemType.gender == 3 and itemMaterial.feminine == 1:
        item = item[:-1] + "es"
    elif itemType.gender == 3 and itemMaterial.feminine == 2:
        item = item[:-3] + "ses"
    elif itemType.gender == 3 and itemMaterial.feminine == 3:
        item = item[:-3] + "rices"
    elif itemType.gender == 3 and itemMaterial.feminine == 4:
        item += "les"
    elif itemType.gender >= 2 and itemMaterial.feminine == -1:
        item += "s"

    item += " " + itemAttribute.name

    # Applies Male/Female/Plural -> Attribute
    if itemType.gender == 1 and itemAttribute.feminine == 1:
        item += "e"
    elif itemType.gender == 1 and itemAttribute.feminine == 2: 
        item = item[:-1] + "se"
    elif itemType.gender == 1 and itemAttribute.feminine == 3: 
        item = item[:-3] + "rice"
    elif itemType.gender == 1 and itemAttribute.feminine == 4: 
        item += "le"
    elif itemType.gender == 3 and itemAttribute.feminine == 1: 
        item = item[:-1] + "es"
    elif itemType.gender == 3 and itemAttribute.feminine == 2: 
        item = item[:-3] + "ses"
    elif itemType.gender == 3 and itemAttribute.feminine == 3: 
        item = item[:-3] + "rices"
    elif itemType.gender == 3 and itemAttribute.feminine == 4: 
        item += "les"
    elif itemType.gender >= 2 and itemAttribute.plural == 1:
        item += "s"

    # Finishes the name of the item and add quality
    if itemAttribute.name == "aléatoire": # Special "aléatoire" case
        qualityNumber = itemMaterial.quality + itemAttribute.qualityModifier + randint(-5, 5)
        qualityNumber = max({qualityNumber, 0})
        qualityNumber = min({qualityNumber, 12})
    else:
        qualityNumber = itemMaterial.quality + itemAttribute.qualityModifier + randint(-1, 1)
        qualityNumber = max({qualityNumber, 0})
        qualityNumber = min({qualityNumber, 12})

    quality = qualities[qualityNumber][randint(0, len(qualities[qualityNumber]) - 1)]

    item += "\n" + quality.name

    # Calculate the 1st stat
    stat1 = itemType.stat
    stat1type = -1
    if stat1.name == "Random":
        stat1 = stats[randint(0, 2)]

    if stat1.type == "Dual":
        if randint(0,1):
            statMagnitude1 = round(randint(3, 10) * quality.multiplier * stat1.modifier * itemType.statModifier + randint(-2, 3))
        else:
            stat1type = 1
            statMagnitude1 = round(randint(3, 10) * quality.multiplier *  stat1.modifier * itemType.statModifier * 2 + randint(-4, 6))
    if stat1.type == "Flat":
        statMagnitude1 = round(randint(3, 10) * quality.multiplier * stat1.modifier * itemType.statModifier + randint(-2, 3))
    if stat1.type == "Relative":
        stat1type = 1
        statMagnitude1 = round(randint(3, 10) * quality.multiplier *  stat1.modifier * itemType.statModifier * 2 + randint(-4, 6))
    if stat1.type == "FixedFlat":
        statMagnitude1 = stat1.modifier
    if stat1.type == "FixedRelative":
        stat1type = 1
        statMagnitude1 = stat1.modifier

    # Applies the +/-
    if statMagnitude1 > 0:
        statMagnitude1 = "+ " + str(statMagnitude1)
    else:
        statMagnitude1 = "- " + str(statMagnitude1 * -1)

    # Applies the stat in the message
    if stat1.name == "Null":
        statMagnitude1 = 0
    if not(statMagnitude1 == 0):
        if stat1type == 1:
            item += " \n" + statMagnitude1 + "%" + " " + stat1.name
        else:
            item += " \n" + statMagnitude1 + " " + stat1.name

    # Calculate the 2nd stat
    stat2 = itemMaterial.stat
    stat2type = -1
    if stat2.name == "Copy":
        stat2 = itemType.stat
    if stat2.name == "Random":
        stat2 = stats[randint(0, 2)]
    
    if stat2.type == "Dual":
        if randint(0,1):
            statMagnitude2 = round(randint(3, 10) * quality.multiplier * stat2.modifier * itemMaterial.statModifier + randint(-2, 3))
        else:
            stat2type = 1
            statMagnitude2 = round(randint(3, 10) * quality.multiplier *  stat2.modifier * itemMaterial.statModifier * 2 + randint(-4, 6))
    if stat2.type == "Flat":
        statMagnitude2 = round(randint(3, 10) * quality.multiplier * stat2.modifier * itemMaterial.statModifier + randint(-2, 3))
    if stat2.type == "Relative":
        stat2type = 1
        statMagnitude2 = round(randint(3, 10) * quality.multiplier *  stat2.modifier * itemMaterial.statModifier * 2 + randint(-4, 6))
    if stat2.type == "FixedFlat":
        statMagnitude2 = stat2.modifier
    if stat2.type == "FixedRelative":
        stat2type = 1
        statMagnitude2 = stat2.modifier

    # Applies the +/-
    if statMagnitude2 > 0:
        statMagnitude2 = "+ " + str(statMagnitude2)
    else:
        statMagnitude2 = "- " + str(statMagnitude2 * -1)

    # Applies the stat in the message
    if stat2.name == "Null":
        statMagnitude2 = 0
    if not(statMagnitude2 == 0):
        if stat2type == 1:
            item += " \n" + statMagnitude2 + "%" + " " + stat2.name
        else:
            item += " \n" + statMagnitude2 + " " + stat2.name

    # Calculate the 3rd stat
    stat3 = itemAttribute.stat
    stat3type = -1
    if stat3.name == "Copy":
        stat3 = itemType.stat
    if stat3.name == "Random":
        stat3 = stats[randint(0, 2)]

    if stat3.type == "Dual":
        if randint(0,1):
            statMagnitude3 = round(randint(3, 10) * quality.multiplier * stat3.modifier * itemAttribute.statModifier + randint(-2, 3))
        else:
            stat3type = 1
            statMagnitude3 = round(randint(3, 10) * quality.multiplier *  stat3.modifier * itemAttribute.statModifier * 2 + randint(-4, 6))
    if stat3.type == "Flat":
        statMagnitude3 = round(randint(3, 10) * quality.multiplier * stat3.modifier * itemAttribute.statModifier + randint(-2, 3))
    if stat3.type == "Relative":
        stat3type = 1
        statMagnitude3 = round(randint(3, 10) * quality.multiplier *  stat3.modifier * itemAttribute.statModifier * 2 + randint(-4, 6))
    if stat3.type == "FixedFlat":
        statMagnitude3 = stat3.modifier
    if stat3.type == "FixedRelative":
        stat3type = 1
        statMagnitude3 = stat3.modifier

    # Applies the +/-
    if statMagnitude3 > 0:
        statMagnitude3 = "+ " + str(statMagnitude3)
    else:
        statMagnitude3 = "- " + str(statMagnitude3 * -1)

    # Applies the stat in the message
    if stat3.name == "Null":
        statMagnitude3 = 0
    if not(statMagnitude3 == 0):
        if stat3type == 1:
            item += " \n" + statMagnitude3 + "%" + " " + stat3.name
        else:
            item += " \n" + statMagnitude3 + " " + stat3.name

    # Calculate the other stats
    if quality.name == "Démoniaque":
        quality.multiplier = -6 # "Démoniaque" case

    for i in range(quality.totalStats):
        statN = stats[randint(0, len(stats) - 1)]
        statNtype = 0
        if statN.type == "Dual":
            if randint(0,1):
                statMagnitudeN = round(randint(3, 10) * quality.multiplier * statN.modifier + randint(-2, 3))
            else:
                statNtype = 1
                statMagnitudeN = round(randint(3, 10) * quality.multiplier *  statN.modifier * 2 + randint(-4, 6))
        if statN.type == "Flat":
            statMagnitudeN = round(randint(3, 10) * quality.multiplier * statN.modifier + randint(-2, 3))
        if statN.type == "Relative":
            statNtype = 1
            statMagnitudeN = round(randint(3, 10) * quality.multiplier *  statN.modifier * 2 + randint(-4, 6))
        if statN.type == "FixedFlat":
            statMagnitudeN = statN.modifier
        if statN.type == "FixedRelative":
            statNtype = 1
            statMagnitudeN = statN.modifier

        # Applies the +/-
        if statMagnitudeN > 0:
            statMagnitudeN = "+ " + str(statMagnitudeN)
        else:
            statMagnitudeN = "- " + str(statMagnitudeN * -1)

        # Applies the stat in the message
        if not(statMagnitudeN == 0):
            if statNtype == 1:
                item += " \n" + statMagnitudeN + "%" + " " + statN.name
            else:
                item += " \n" + statMagnitudeN + " " + statN.name

    if quality.name == "Démoniaque":
        quality.multiplier = 16

    print(item)
    input()