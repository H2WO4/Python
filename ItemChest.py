from random import choice, randint
from typing import Union
from item_chest.ItemChestData import Attribute, Material, Type, stats, materials, types, attributes, qualities

print("Dans le coffre se trouve ...\n")
while True:
    # On prend des paramètres aléatoires dans les listes
    iType, iAttr, iMat = choice(types), choice(attributes), choice(materials)
    title = iType.name + " " + iMat.name # On commence à former le nom de l'objet
    # On change le nom du matériau suivant masculin/féminin/pluriel
    if iType.gender in (1, 3) and iMat.feminine == 1: title += "e"
    elif iType.gender in (1, 3) and iMat.feminine == 2: title = title[:-1] + "se"
    elif iType.gender in (1, 3) and iMat.feminine == 3: title = title[:-3] + "rice"
    elif iType.gender in (1, 3) and iMat.feminine == 4: title += "le"
    if iType.gender >= 2 and iMat.plural: title += "s"
    title += " " + iAttr.name # On ajoute le nom de l'attribut
    # On change le nom de l'attribut suivant masculin/féminin/pluriel
    if iType.gender in (1, 3) and iAttr.feminine == 1: title += "e"
    elif iType.gender in (1, 3) and iAttr.feminine == 2: title = title[:-1] + "se"
    elif iType.gender in (1, 3) and iAttr.feminine == 3: title = title[:-3] + "rice"
    elif iType.gender in (1, 3) and iAttr.feminine == 4: title += "le"
    if iType.gender >= 2 and iAttr.plural: title += "s"
    if iAttr.name != "aléatoire": qualNum = min(max(iMat.quality + iAttr.qualMod + randint(-1, 1), 0), 12) # On gère l'ajout de la qualité de l'objet
    else: qualNum = min(max(iMat.quality + iAttr.qualMod + randint(-5, 5), 0), 12) # Cas special pour "aléatoire"
    quality = choice(qualities[qualNum]) # On prend une qualité aléatoire correspondant au rang de l'objet
    item = quality.name # On l'ajoute au nom

    # On calcule les 3 premières stats
    for i in range(3):
        obj: Union[Type, Material, Attribute] = [iType, iMat, iAttr][i] # On prend l'objet, et setup relative
        stat, relative = obj.stat, False
        # Gestion des cas "Copy", "Random" et "Null"
        if stat.name == "Copy": stat = iType.stat
        if stat.name == "Random": stat = stats[randint(0, 2)]
        elif stat.name == "Null": continue
        # On choisit si la stat est relative (%) ou flat
        statMagn = round(randint(3, 10) * quality.multiplier *  stat.modifier * obj.statMod + randint(-4, 6))
        if (stat.type == "Dual" and randint(0, 1)) or stat.type in ("Relative", "FixedRelative"): statMagn, relative = statMagn * 2, True
        if "Fixed" in stat.type: statMagn = stat.modifier # Et si sa valeur est fixe
        # On rajoute la stat au message
        if statMagn != 0: item += "\n " + ("+ " if statMagn > 0 else "- ") + str(abs(statMagn)) + ("%" if relative else "") + " " + stat.name

    qualMul = -6 if quality.name == "Démoniaque" else quality.multiplier # On gère le cas spécial de la qualité "Démoniaque"
    for i in range(quality.totalStats): # On calcule toutes les autres stats
        stat, relative = choice(stats), False
        # On choisit si la stat est relative (%) ou flat
        statMagn = round(randint(3, 10) * qualMul * stat.modifier + randint(-2, 3))
        if (stat.type == "Dual" and randint(0, 1)) or stat.type == "Relative": statMagn, relative = statMagn * 2, True
        # On rajoute la stat au message
        if statMagn != 0: item += "\n " + ("+ " if statMagn > 0 else "- ") + str(abs(statMagn)) + ("%" if relative else "") + " " + stat.name

    print("{} :\n{}".format(title, item)) # On affiche l'objet
    if input() != "": break # On gère la sortie de programme