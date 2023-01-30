
from plateau import plateau, pion
from carte import *


class joueur:
    def __init__(self, pv, effet, name, main, deck, defausse, pion):
        self.pv = pv
        self.effet = effet
        self.nom = name
        self.main = main
        self.deck = deck
        self.defausse = defausse
        self.pion = pion
        self.saignement = 0
        self.poison = 0

    def __str__(self):
        return "nom: {}, pv: {}".format(self.nom, self.pv)

    def degats(self, nb = 1):
        """
        permet au joueur de prendre des dégâts
        :param nb: nombre de dégâts à infliger
        :return: rien du tout
        """
        self.pv -= nb

    def soin(self, n = 1):
        self.pv += n

    def saigner(self, n = 1):
        self.saignement += n

    def empoisonner(self, n):
        self.poison += n

    def orientation(self):
        a = input("vers où voulez-vous vous orienter ?")
        if a == "north" or a == "nord" :
            self.pion.orienter("nord")
        elif a == "est" or a == "east" :
            self.pion.orienter("est")
        elif a == "ouest" or a == "west" :
            self.pion.orienter("ouest")
        elif a == "south" or a == "sud" :
            self.pion.orienter("sud")

    def deplacement(self):
        a = input("veuillez indiquer comment vous souhaitez modifier votre abscisse")
        if a == 1 :
            self.pion.abscisse += 1
        elif a == -1 :
            self.pion.abscisse -= 1
        elif self.nom == "assassin" :
            if a == 2 :
                self.pion.abscisse += 2
            elif a == -2 :
                self.pion.abscisse -= 2
        b = input("veuillez indiquer comment vous souhaitez modifier votre ordonnée")
        if b == 1:
            self.pion.ordonnee += 1
        elif b == -1:
            self.pion.ordonnee -= 1
        elif self.nom == "assassin":
            if b == 2:
                self.pion.ordonnee += 2
            elif b == -2:
                self.pion.ordonnee -= 2

    def actions_possibles(self, pile, adversaire) :
        possibles = []
        if pile.vitesse < 1 :
            possibles.append(deplacement(self))
            possibles.append(se_defausser(self, adversaire))
        if pile.vitesse < 3 :
            possibles.append(orientation(self))
        vitesse =  pile.vitesse
        derniere_carte = pile[-1]
        for carte in self.main.cartes :
            if carte.vitesse > vitesse :
                possibles.append(carte)
            elif carte.vitesse == vitesse and type(carte) == action and type(derniere_carte) != action :
                possibles.append(carte)
            elif carte.vitesse == vitesse and type(carte) == attaque and type(derniere_carte) != attaque and type(derniere_carte) != action :
                possibles.append(carte)
        return possibles

    def pioche(self, n = 1):
        for i in range(n) :
            if self.deck.taille == 0 :
                self.defausse.vers_deck(self.deck)
                self.deck.melanger()
            car = self.deck[0]
            self.main.append(car)
            self.deck.remove(car)