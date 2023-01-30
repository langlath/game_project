from Carte import *
from plateau import *

class pile(list):
    def __init__(self):
        super().__init__()
        self.nb= len(self)
        self.vitesse = 0
        self.lis_effets=[]

    def vider(self):
        """
        permet de vider la liste
        :return: rien du tout
        Auteur: Thibault Langlard
        """
        L=[carte for carte in self]
        for carte in L:
            if type(carte) == action or type(carte) == attaque :
                carte.joueur.defausse.cartes.append(carte)
        self.clear()
        self.vitesse = 0

    def depiler(self,joueur1, joueur2, plateau):

        """
        permet de résoudre les effets de chaque carte présente dans la pile, une par une, et de vider la pile au fur et à mesure
        :param joueur1: joueur, l'un des joueurs
        :param joueur2: joueur, l'un des joueurs
        :param plateau: plateau, plateau de jeu
        :return: rien du tout
        Auteur: Léa Vilasi
        """
        carte = self[-1]
        carte.resoudre()
        print(carte.nom)
        if type(carte) == attaque:
            if carte.joueur == joueur1:
                joueur, adversaire = joueur1, joueur2
            else:
                joueur, adversaire = joueur2, joueur1
            carte.infliger_degats(joueur, adversaire, plateau)
            self.vider()
            joueur.futur_deplacementx = 0
            joueur.futur_deplacementy = 0
            joueur.future_orientation = ""
            joueur.futur_deplacement = ""
            adversaire.futur_deplacementx = 0
            adversaire.futur_deplacementy = 0
            adversaire.future_orientation = ""
            adversaire.futur_deplacement = ""
        elif carte.nom == "Parade" or carte.nom == "Parade destructrice":
            self.vider()
            print("vider")
        elif type(carte) == action :
            self.remove(carte)
            carte.joueur.defausse.cartes.append(carte)
        else :
            self.remove(carte)
        if len(self)>0:
            self.depiler(joueur1, joueur2, plateau)