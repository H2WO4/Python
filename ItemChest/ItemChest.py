from random import randint
from ItemChest.ItemChestData import stats, materials, types, attributes, qualities

print("Dans le coffre se trouve ...\n")

while True:
    # On prend des paramètres aléatoires dans les listes.
    itemType = types[randint(0, len(types) - 1)]
    itemAttribute = attributes[randint(0, len(attributes) - 1)]
    itemMaterial = materials[randint(0, len(materials) - 1)]

    # On commence à former le nom de l'objet
    title = itemType.name + " " + itemMaterial.name

    # On change le nom du matériau suivant masculin/féminin/pluriel
    if itemType.gender == 1 and itemMaterial.feminine == 1:
        title += "e"
    elif itemType.gender == 1 and itemMaterial.feminine == 2:
        title = title[:-1] + "se"
    elif itemType.gender == 1 and itemMaterial.feminine == 3:
        title = title[:-3] + "rice"
    elif itemType.gender == 1 and itemMaterial.feminine == 4:
        title += "le"
    elif itemType.gender == 3 and itemMaterial.feminine == 1:
        title = title[:-1] + "es"
    elif itemType.gender == 3 and itemMaterial.feminine == 2:
        title = title[:-3] + "ses"
    elif itemType.gender == 3 and itemMaterial.feminine == 3:
        title = title[:-3] + "rices"
    elif itemType.gender == 3 and itemMaterial.feminine == 4:
        title += "les"
    elif itemType.gender >= 2 and itemMaterial.feminine == -1:
        title += "s"

    # On ajoute le nom de l'attribut
    title += " " + itemAttribute.name

    # On change le nom de l'attribut suivant masculin/féminin/pluriel
    if itemType.gender == 1 and itemAttribute.feminine == 1:
        title += "e"
    elif itemType.gender == 1 and itemAttribute.feminine == 2: 
        title = title[:-1] + "se"
    elif itemType.gender == 1 and itemAttribute.feminine == 3: 
        title = title[:-3] + "rice"
    elif itemType.gender == 1 and itemAttribute.feminine == 4: 
        title += "le"
    elif itemType.gender == 3 and itemAttribute.feminine == 1: 
        title = title[:-1] + "es"
    elif itemType.gender == 3 and itemAttribute.feminine == 2: 
        title = title[:-3] + "ses"
    elif itemType.gender == 3 and itemAttribute.feminine == 3: 
        title = title[:-3] + "rices"
    elif itemType.gender == 3 and itemAttribute.feminine == 4: 
        title += "les"
    elif itemType.gender >= 2 and itemAttribute.plural == 1:
        title += "s"

    # On gère l'ajout de la qualité de l'objet
    if itemAttribute.name == "aléatoire": # Cas special pour "aléatoire"
        qualityNumber = itemMaterial.quality + itemAttribute.qualityModifier + randint(-5, 5)
        qualityNumber = max({qualityNumber, 0})
        qualityNumber = min({qualityNumber, 12})
    else:
        qualityNumber = itemMaterial.quality + itemAttribute.qualityModifier + randint(-1, 1)
        qualityNumber = max({qualityNumber, 0})
        qualityNumber = min({qualityNumber, 12})

    quality = qualities[qualityNumber][randint(0, len(qualities[qualityNumber]) - 1)]

    # On l'ajoute au nom
    item = quality.name

    # On calcule les 3 premières stats
    for i in range(3):
        # On prend la stat
        stat = [itemType.stat, itemMaterial.stat, itemAttribute.stat][i]
        statType = -1

        # Gestion des cas "Copy" et "Random"
        if stat.name == "Copy":
            stat = itemType.stat
        if stat.name == "Random":
            stat = stats[randint(0, 2)]

        # On choisit si la stat est relative (%) ou flat
        statMagnitude = round(randint(3, 10) * quality.multiplier *  stat.modifier * [itemType.statModifier, itemMaterial.statModifier, itemAttribute.statModifier][i] + randint(-4, 6))
        if stat.type == "Dual":
            if randint(0,1):
                statMagnitude *= 2
                statType = 1  
        if stat.type == "Relative":
            statMagnitude *= 2
            statType = 1
        if stat.type == "FixedFlat":
            statMagnitude = stat.modifier
        if stat.type == "FixedRelative":
            statType = 1
            statMagnitude = stat.modifier

        # On applique le signe
        if statMagnitude > 0:
            statMagnitude = "+ " + str(statMagnitude)
        else:
            statMagnitude = "- " + str(statMagnitude * -1)

        # On gère le cas spécial "Null"
        if stat.name == "Null":
            statMagnitude = 0
        
        # On rajoute la stat au message
        if not(statMagnitude == 0):
            if statType == 1:
                item += " \n" + statMagnitude + "%" + " " + stat.name
            else:
                item += " \n" + statMagnitude + " " + stat.name

    # On calcule toutes les autres stats
    if quality.name == "Démoniaque":
        quality.multiplier = -6 # On gère le cas spécial de la qualité "Démoniaque"

    for i in range(quality.totalStats):
        stat = stats[randint(0, len(stats) - 1)]
        statType = 0

        # On choisit si la stat est relative (%) ou flat
        statMagnitude = round(randint(3, 10) * quality.multiplier * stat.modifier + randint(-2, 3))
        if stat.type == "Dual":
            if randint(0,1):
                statType = 1
                statMagnitude *= 2
        if stat.type == "Relative":
            statType = 1
            statMagnitude *= 2
        if stat.type == "FixedFlat":
            statMagnitude = stat.modifier
        if stat.type == "FixedRelative":
            statType = 1
            statMagnitude = stat.modifier

        # On applique le signe
        if statMagnitude > 0:
            statMagnitude = "+ " + str(statMagnitude)
        else:
            statMagnitude = "- " + str(statMagnitude * -1)

        # On rajoute la stat au message
        if not(statMagnitude == 0):
            if statType == 1:
                item += " \n" + statMagnitude + "%" + " " + stat.name
            else:
                item += " \n" + statMagnitude + " " + stat.name

    # On remet "Démoniaque" à la normale
    if quality.name == "Démoniaque":
        quality.multiplier = 16

    print("{}:\n{}".format(title, item))
    input()