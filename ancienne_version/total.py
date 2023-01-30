

class effet :

    def __init__(self, effet, activ, passif):
        self.resolution = effet
        self.activation = activ
        self.est_passif = passif

    def resoudre(self):
        lis_effets.append(effet)
        self.resolution()

class plateau :

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.plateau = [[0 for j in range(largeur)] for i in range(longueur)]


class pion :

    def __init__(self, coords, orient):
        self.abscisse = coords[0]
        self.ordonnee = coords[1]
        self.orientation = orient

    def deplacer(self, x, y, plateau):
        if self.abscisse + x >= 0 and self.abscisse + x < plateau.largeur and self.ordonnee + y >= 0 and self.ordonnee + y < plateau.longueur :
            self.abscisse += x
            self.ordonnee += y
        else :
            print("pion hors du plateau")

    def orienter(self, orient):
        self.orientation = orient

class paquet :

    def __init__(self, lis_cartes):
        self.cartes = lis_cartes
        self.taille = len(lis_cartes)

class deck(paquet):

    def __init__(self, lis_cartes):
        super().__init__(lis_cartes)

    def melanger(self):
        rd.shuffle(self.cartes)


class defausse(paquet) :

    def __init__(self):
        super().__init__([])

    def vers_deck(self, deck):
        for carte in self.cartes :
            deck.cartes.append(carte)
        self.cartes = []
        self.taille = 0
        deck.taille = len(deck.cartes)



class main(paquet) :

    def __init__(self):
        super().__init__([])

    def jouer(self, carte, pile):
        i = 0
        while i < len(self.cartes) and self.cartes[i] != carte :
            i += 1
        pile.append(carte)
        pile.vitesse = carte.vitesse
        self.cartes.del(i)
        self.taille -= 1

class carte:
    def __init__(self, effet, joueur):
        self.effet=effet
        self.joueur= joueur

    def resoudre(self):
        self.effet.resoudre()

class action(carte):
    def __init__(self, vitesse, effet):
        super().__init__()
        self.vitesse = vitesse

class attaque(carte):
    def __init__(self, vitesse, degats, portee, direction, effet):
        super().__init__()
        self.vitesse = vitesse
        self.degats = degats
        self.portee= portee
        self.direction = direction


class etat(carte):
    def __init__(self, effet):
        super().__init__()

class personnage(carte):
    def __init__(self, effet):
        super().__init__()

class joueur:
    def __init__(self, pv, effet):
        self.pv= pv
    def degats(self, nb):
        self.pv -= nb

class pile(list):
    def __init__(self, nb):
        super().__init__()
        self.nb= len(self)
    def vider(self):
        L=[carte for carte in self]
        for carte in L:
            carte.joueur.defausse.append(carte)
         self=[]
    def jouer(self, joueur):
        a=input("Voulez vous interrompre?")
        if a=="Oui":
            joueur.main.jouer(carte_à_jouer, self)  #carte à jouer à compléter
            self.jouer(self, joueur_adverse)        #joueur adverse à compléter
        else:
            for carte in pile:
                carte.resoudre()
            pile.vider()