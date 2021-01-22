from random import choice, randint
from item_chest.ItemChestData import stats, materials, types, attributes, qualities

print("Dans le coffre se trouve ...\n")

while True:
    # On prend des paramètres aléatoires dans les listes.
    iType, iAttr, iMat = choice(types), choice(attributes), choice(materials)
    title = iType.name + " " + iMat.name # On commence à former le nom de l'objet

    # On change le nom du matériau suivant masculin/féminin/pluriel
    if (iType.gender, iMat.feminine) == (1, 1): title += "e"
    elif (iType.gender, iMat.feminine) == (1, 2): title = title[:-1] + "se"
    elif (iType.gender, iMat.feminine) == (1, 3): title = title[:-3] + "rice"
    elif (iType.gender, iMat.feminine) == (1, 4): title += "le"
    elif (iType.gender, iMat.feminine) == (3, 1): title = title[:-1] + "es"
    elif (iType.gender, iMat.feminine) == (3, 2): title = title[:-3] + "ses"
    elif (iType.gender, iMat.feminine) == (3, 3): title = title[:-3] + "rices"
    elif (iType.gender, iMat.feminine) == (3, 4): title += "les"
    elif iType.gender >= 2 and iMat.plural == 1: title += "s"

    title += " " + iAttr.name # On ajoute le nom de l'attribut

    # On change le nom de l'attribut suivant masculin/féminin/pluriel
    if (iType.gender, iAttr.feminine) == (1, 1): title += "e"
    elif (iType.gender, iAttr.feminine) == (1, 2): title = title[:-1] + "se"
    elif (iType.gender, iAttr.feminine) == (1, 3): title = title[:-3] + "rice"
    elif (iType.gender, iAttr.feminine) == (1, 4): title += "le"
    elif (iType.gender, iAttr.feminine) == (3, 1): title = title[:-1] + "es"
    elif (iType.gender, iAttr.feminine) == (3, 2): title = title[:-3] + "ses"
    elif (iType.gender, iAttr.feminine) == (3, 3): title = title[:-3] + "rices"
    elif (iType.gender, iAttr.feminine) == (3, 4): title += "les"
    elif iType.gender >= 2 and iAttr.plural == 1: title += "s"

    # On gère l'ajout de la qualité de l'objet
    if iAttr.name == "aléatoire": qualNum = min(max(iMat.quality + iAttr.qualMod + randint(-5, 5), 0), 12) # Cas special pour "aléatoire"
    else: qualNum = min(max(iMat.quality + iAttr.qualMod + randint(-1, 1), 0), 12)

    quality = choice(qualities[qualNum]) # On prend une qualité aléatoire correspondant au rang de l'objet
    item = quality.name # On l'ajoute au nom

    # On calcule les 3 premières stats
    for i in range(3):
        stat, relative = [iType.stat, iMat.stat, iAttr.stat][i], False # On prend la stat

        # Gestion des cas "Copy", "Random" et "Null"
        if stat.name == "Copy": stat = iType.stat
        if stat.name == "Random": stat = stats[randint(0, 2)]
        elif stat.name == "Null": continue

        # On choisit si la stat est relative (%) ou flat
        statMagn = round(randint(3, 10) * quality.multiplier *  stat.modifier * [iType.statMod, iMat.statMod, iAttr.statMod][i] + randint(-4, 6))
        if (stat.type == "Dual" and randint(0, 1)) or stat.type in ("Relative", "FixedRelative"):
            statMagn *= 2
            relative = True
        if "Fixed" in stat.type: statMagn = stat.modifier # Et si sa valeur est fixe
        
        # On rajoute la stat au message
        if statMagn != 0: item += "\n " + ("+ " if statMagn > 0 else "- ") + str(abs(statMagn)) + ("%" if relative else "") + " " + stat.name


    qualMul = quality.multiplier
    if quality.name == "Démoniaque": qualMul = -6 # On gère le cas spécial de la qualité "Démoniaque"

    for i in range(quality.totalStats): # On calcule toutes les autres stats
        stat = choice(stats)
        relative = False

        # On choisit si la stat est relative (%) ou flat
        statMagn = round(randint(3, 10) * qualMul * stat.modifier + randint(-2, 3))
        if (stat.type == "Dual" and randint(0, 1)) or stat.type == "Relative":
            statMagn *= 2
            relative = True

        # On rajoute la stat au message
        if not(statMagn == 0): item += "\n " + ("+ " if statMagn > 0 else "- ") + str(abs(statMagn)) + ("%" if relative else "") + " " + stat.name

    print("{} :\n{}".format(title, item)) # On affiche l'objet
    input()