
import numpy as np
import numpy.random as rd
import pile

class paquet :

    def __init__(self, lis_cartes):
        self.cartes = lis_cartes
        self.taille = len(lis_cartes)


class deck(paquet):

    def __init__(self, lis_cartes):
        super().__init__(lis_cartes)

    def melanger(self):
        """
        Pour mélanger le deck
        :return: le deck mélangé
        """
        rd.shuffle(self.cartes)


    def __str__(self):
        return " Le deck contient {}".format(self.cartes)


class defausse(paquet) :

    def __init__(self):
        super().__init__([])

    def vers_deck(self, deck):
        """
        mélange les cartes de la défausse au deck
        :param deck: le deck vers lequel on envoie les cartes
        :return: rien du tout
        """
        for carte in self.cartes :
            deck.cartes.append(carte)
        self.cartes = []
        self.taille = 0
        deck.taille = len(deck.cartes)

    def __str__(self):
        return " La défausse contient {}".format(self.cartes)



class main(paquet) :

    def __init__(self):
        super().__init__([])

    def jouer(self, carte, pile):
        """
        Sélectionne la carte de la main à jouer
        :param carte: la carte qui est jouée
        :param pile: la pile dans laquelle va la carte
        :return: rien du tout
        """
        pile.append(carte)
        pile.vitesse = carte.vitesse
        self.cartes.remove(carte)
        self.taille -= 1

    def __str__(self):
        return " La main contient {}".format(self.cartes)