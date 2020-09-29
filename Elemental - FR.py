""" Definition des objets """

class Élément:
    """
    L'objet Élément sert à représenter un seu élement
    Il contient des attributs représentant son nom, à quel Groupe il appartient, son état et la liste de ses recettes
    """

    def __init__(self, nom, recettes, Groupe = None, révélé = False):
        # Initialisation - Assignement des attributs
        self.nom = nom
        self.recettes = recettes
        self.Groupe = Groupe
        self.révélé = révélé

        # Initialisation - S'ajoute au listes pour l'indexation
        Éléments.append(self)
        if Groupe != None:
            Groupe.Éléments.append(self)
        
        if révélé:
            ÉlémentsCrées.append(self)
        else:
            ÉlémentsNonCrées.append(self)
    
    def __str__(self):
        # Surcharge l'opérateur 'str()' et renvoie le nom de l'élément
        return self.nom

    def __contains__(self, other):
        # Surcharge l'opérateur 'in' pour effectuer des opérations logiques d'inclusion lors de la fusion d'éléments
        if type(other) != set:
            raise TypeError

        # Cherche le set dans la liste des recettes de l'élément, et retourne un booléan
        if other in self.recettes:
            return True
        return False
    
    def __add__(self, other):
        # Surcharge l'opérateur '+' pour pouvoir créer des sets lors de la fusion d'éléments
        if type(other) != Élément:
            raise TypeError

        # Renvoie un set contenant les deux éléments
        return {self, other}
    
    def __lt__(self, other):
        # Surcharge l'opérateur '<' pour permettre le tri de listes d'éléments
        if type(other) != Élément:
            raise TypeError
        
        # Compare leurs deux noms et renvoie un booléan
        if self.nom < other.nom:
            return True
        return False
    
    def révéler(self):
        # Gére les listes quand un nouvel élément et révélé
        if not self.révélé:
            self.révélé = True
            ÉlémentsCrées.append(self)
            ÉlémentsCrées.sort()
            ÉlémentsNonCrées.pop(ÉlémentsNonCrées.index(self))
        
        return None


class Groupe:
    """
    L'objet Groupe est utilisé pour représenter une liste d'éléments
    Il contient des attributs représentant son nom ainsi qu'une liste ordonnée de ses membres
    """

    def __init__(self, nom):
        # Initialisation - Assignement des attributs
        self.nom = nom
        self.Éléments = []

        # Initialisation - S'ajoute au listes pour l'indexation
        Groupes.append(self)
    
    def __str__(self):
        # Surcharge l'opérateur 'str()' et renvoie le nom du groupe
        return self.nom


# Définition de listes permettant de lister facilement les éléments et groupes
Éléments = []
ÉlémentsCrées = []
ÉlémentsNonCrées = []
Groupes = []



""" Création des instances de chaque objets, pour permettre de créer le jeu """

# Groupes
Ignis = Groupe("Ignis")
Aqua = Groupe("Aqua")
Terra = Groupe("Terra")
Aer = Groupe("Aer")
Fulgur = Groupe("Fulgur")
Vitae = Groupe("Vitae")
Primus = Groupe("Primus")
Locus = Groupe("Locus")


# Éléments de base
Feu = Élément("Feu", [], Ignis, True)
Air = Élément("Air", [], Aer, True)
Eau = Élément("Eau", [], Aqua, True)
Terre = Élément("Terre", [], Terra, True)
Énergie = Élément("Énergie", [], Primus, True)
Vide = Élément("Vide", [], Primus, True)

# Composés de niveau 1
Plasma = Élément("Plasma", [Feu + Énergie], Ignis)
Électricité = Élément("Électricité", [Air + Énergie], Fulgur)
Lave = Élément("Lave", [Feu + Terre], Ignis)
Vapeur = Élément("Vapeur", [Air + Eau], Aer)
Chaleur = Élément("Chaleur", [Feu + Feu], Primus)
Pression = Élément("Pression", [Terre + Énergie], Primus)
Pierre = Élément("Pierre", [Terre + Terre], Terra)
Mer = Élément("Mer", [Eau + Eau], Aqua)
Vague = Élément("Vague", [Eau + Énergie], Primus)
Vent = Élément("Vent", [Air + Énergie], Aer)

# Composés de niveau 2+ généraux
Son = Élément("Son", [Air + Vague], Aer)
Océan = Élément("Océan", [Mer + Mer], Aqua)
Sel = Élément("Sel", [Mer + Chaleur], Terra)
Tsunami = Élément("Tsunami", [Mer + Vague], Aqua)

# Série Céléste
Nuage = Élément("Nuage", [Vapeur + Vapeur], Aer)
Tornade = Élément("Tornade", [Vent + Vent], Aer)
Pluie = Élément("Pluie", [Nuage + Eau], Aqua)
Éclair = Élément("Éclair", [Nuage + Électricité], Fulgur)
Cyclone = Élément("Cyclone", [Tornade + Tornade], Aer)

# Série Minérale
Obsidienne = Élément("Obsidienne", [Lave + Eau], Terra)
Fer = Élément("Fer", [Pierre + Pression], Terra)
Acier = Élément("Acier", [Fer + Chaleur], Terra)
Charbon = Élément("Charbon", [Pierre + Feu], Terra)
Diamond = Élément("Diamond", [Charbon + Pression], Terra)
Rouille = Élément("Rouille", [Fer + Eau], Terra)
Cuivre = Élément("Cuivre", [Fer + Pierre], Terra)
Étain = Élément("Étain", [Fer + Feu], Terra)
Bronze = Élément("Bronze", [Cuivre + Étain], Terra)

# Série Biologique
Cellule = Élément("Cellule", [Énergie + Océan], Vitae)
Bactérie = Élément("Bactérie", [Cellule + Cellule], Vitae)
Vie = Élément("Vie", [Bactérie + Énergie], Primus)
Ver = Élément("Ver", [Bactérie + Terre], Vitae)
SolArable = Élément("Sol Arable", [Terre + Ver], Terra)
Poisson = Élément("Poisson", [Bactérie + Mer], Vitae)

# Série Spatiale
Étoile = Élément("Étoile", [Plasma + Vide], Locus)
TrouNoir = Élément("Trou Noir", [Vide + Étoile], Locus)
Pulsar = Élément("Pulsar", [Étoile + Électricité], Locus)
Planète = Élément("Planète", [Pierre + Vide], Locus)
PlanèteOcéan = Élément("Planète Océan", [Planète + Océan], Locus)
Magma = Élément("Magma", [Planète + Lave], Ignis)
SystèmeSolaire = Élément("Système Solaire", [Planète + Étoile], Locus)


# Trie tout les listes des groupes
for i in Groupes:
    i.Éléments.sort()



""" Système de sauvergarde """

# Gère l'ouverture du ficher de sauvergarde si présent
try:
    with open("ÉlémentSauvergarde.txt", "r") as f:
        # Lit le fichier et révèle tout les éléments qui y sont listés
        texteLu = f.read().split("\n")[:-1]
        for i in texteLu:
            eval(i.replace(" ", "")).révéler()
except FileNotFoundError:
    pass



""" Boucle de jeu principale """

print("Bienvenue dans Elemental !\n")
print("Le principe du jeu est très simple :\nUtilisez les éléments à votre disposition pour en créer de nouveaux.\n")
print("Pour plus d'informations, tapez \"aide\".\n")

quitter = False
while not quitter:

    instruction = input().lower()

    if instruction in {"groupe", "groupes"}:
        # Affiche tout les éléments d'un groupe choisi
        print("\nQuel groupe voulez vous voir ?")
        for i in Groupes:
            # Affiche tout les groupes
            print(i)
        
        instruction = eval(input("\n").title())

        if instruction in Groupes:
            print("\n{} Groupe:".format(str(instruction)))

            for i in instruction.Éléments:
                # Affiche tout les éléments révélés d'un groupe
                if i.révélé:
                    print(str(i))
                
    elif instruction in {"fusion", "mélange"}:
        # Gère la fusion de deux éléments
        try:
            # Prend deux entrées textes et vérifie leurs validités
            réactif1 = eval(input("\nChoisi un 1er élément : ").title())
            if not réactif1 in ÉlémentsCrées:
                raise IndexError
            réactif2 = eval(input("\nChoisi un 2ème élément : ").title())
            if not réactif2 in ÉlémentsCrées:
                raise IndexError

            # Réunit les deux valeurs en une et évalue le résulatat pour obenir un set
            instruction = eval("{} + {}".format(réactif1, réactif2))
            newÉlément = False

            # Parcours la liste des éléments afin de trouver un élément correspondant à la combinaison
            for i in ÉlémentsNonCrées:
                if instruction in i:
                    # Révèle l'élément crée
                    newÉlément = True
                    print("\nÉlément {} crée!".format(str(i)))
                    i.révéler()
            if not newÉlément:
                print("Pas de nouvel elément crée...")
        
        # Gère les érreurs lors de la saisie d'un nom incorrect
        except NameError:
            print("\nÉlément inéxistant!")
        except IndexError:
            print("\nÉlément pas encore découvert!")
    
    elif instruction in {"liste"}:
        # Affiche tout les éléments découverts
        print("\nListe des éléments :")
        for i in ÉlémentsCrées:
            print(i)
    
    elif instruction in {"aide"}:
        # Affiche la liste des commandes
        print("\nPour obtenir une liste des éléments, entrez \"liste\"\n")

    elif instruction in {"quitter", "fermer", "stopper"}:
        # Gère la fermeture du programme
        quitter = True
    
    elif instruction in {"révélé"}:
        # Fonction de debug, révèle tout les éléments
        ÉlémentsNonCréesCopie = ÉlémentsNonCrées.copy() 
        for i in ÉlémentsNonCréesCopie:
            print(i)
            i.révéler()
    
    print("\n")

# Sauvergarde les données dans un fichier de sauvergarde
with open("ÉlémentSave.txt", "w") as f:
    for i in ÉlémentsCrées:
        f.write(str(i) + "\n")