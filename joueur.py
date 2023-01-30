
from plateau import plateau, pion
from Carte import *


class joueur:
    def __init__(self, pv, effet, nom, main, deck, defausse, pion):
        self.pv = pv
        self.effet = effet
        self.nom = nom
        self.main = main
        self.deck = deck
        self.defausse = defausse
        self.pion = pion
        self.saignement = 0
        self.poison = 0
        self.nb_actions = 1
        self.peut_deplacer = 0
        self.peut_orienter = 0
        self.future_orientation = ""
        self.futur_deplacement = ""
        self.futur_deplacementx=0
        self.futur_deplacementy=0
        self.plateau=plateau
        self.ia = False


    def __str__(self):
        return "nom: {}, pv: {}".format(self.nom, self.pv)

    def degats(self, nb=1):
        """
        permet au joueur de prendre des dégâts
        :param nb: int, nombre de dégâts à infliger
        :return: rien du tout
        Auteur: Thibault Langlard
        """
        self.pv -= nb

    def soin(self, n = 1):
        """
        permet au joueur de se soigner
        :param n: int, nombre de points de vie à récupérer
        :return: rien du tout
        Auteur: Thibault Langlard
        """
        self.pv += n

    def saigner(self, n = 1):
        """
        permet au joueur de gagner des saignements
        :param n: int, nombre de saignements à récupérer
        :return: rien du tout
        Auteur: Thibault Langlard
        """
        self.saignement += n

    def empoisonner(self, n):
        """
        permet au joueur de gagner des poisons
        :param n: int, nombre de poisons à récupérer
        :return: rien du tout
        Auteur: Thibault Langlard
        """
        self.poison += n


    def orientation(self):
        """
        permet au joueur de s'orienter (suite à la résolution de l'effet d'une carte orientation)
        :return: rien du tout
        Auteur: Léa Vilasi
        """
        self.pion.orienter(self.future_orientation)
        self.future_orientation = ""

    def deplacement(self):
        """
        permet au joueur de se déplacer (suite à la résolution de l'effet d'une carte déplacement)
        :return: rien du tout
        Auteur: Léa Vilasi
        """
        self.pion.deplacer(self.futur_deplacementx, self.futur_deplacementy, self.plateau, self)
        self.futur_deplacementx=0
        self.futur_deplacementy=0
        self.futur_deplacement=""


    def droit_orientation(self):
        """
        permet au joueur de s'orienter (s'il a gagné cet effet grâce à une carte action/attaque)
        :return: rien du tout
        Auteur: Léa Vilasi
        """
        self.peut_orienter+=1

    def droit_deplacement(self):
        """
        permet au joueur de se déplacer (s'il a gagné cet effet grâce à une carte action/attaque)
        :return: rien du tout
        Auteur: Léa Vilasi
        """
        self.peut_deplacer+=1


    def pioche(self, n=1):
        """
        permet au joueur de piocher
        :param n: int, nombre de cartes piochées
        :return: rien du tout
        Auteur: Thibault Langlard
        """
        for i in range(n) :
            if len(self.deck.cartes) == 0 :
                self.defausse.vers_deck(self.deck)
                self.deck.melanger()
            car = self.deck.cartes[0]
            self.main.cartes.append(car)
            self.deck.cartes.remove(car)