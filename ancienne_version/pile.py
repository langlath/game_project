from carte import *
from plateau import *

plateau = plateau(3, 4)

class pile(list):
    def __init__(self):
        super().__init__()
        self.nb= len(self)
        self.vitesse = 0

    def vider(self):
        """
        permet de vider la liste
        :return: rien du tout
        """
        L=[carte for carte in self]
        for carte in L:
            if type(carte) == action or type(carte) == attaque :
                carte.joueur.defausse.append(carte)
        self.clear()
        self.vitesse = 0

    def veut_jouer(self, joueur):
        a = input("Voulez-vous jouer ?")
        if a == "Oui" :
            #joueur.main.jouer(carte_a_jouer)
            return True
        else :
            return False

    def jouer(self, joueur1, joueur2, plateau = plateau):
        """
        permet de remplir la liste avec les cartes jouées
        :param joueur: le joueur qui a la possibilité d'interrompre
        :return: rien du tout
        """
        a = input("Voulez-vous interrompre {0} ?".format(joueur1))
        if a == "Oui":
            possibles = joueur1.actions_possibles(self, joueur2)
            a_jouer = 0
            while a_jouer == 0 :
                e = input("quelle carte voulez-vous jouer ? Les cartes que vous pouvez jouer sont {}.".format([i.nom for i in possibles]))
                for carte in possibles :
                    if carte.nom == e :
                        a_jouer = carte
                if a_jouer == 0 :
                    print("Vous ne pouvez pas jouer cette carte!")
                elif type(a_jouer) == action or type(a_jouer) == attaque :
                    joueur1.main.jouer(a_jouer, self)
                else :
                    self.append(a_jouer)
                    self.vitesse = a_jouer.vitesse
                self.jouer(joueur2, joueur1, plateau)
        else:
            while self.nb > 0:
                carte = self[-1]
                carte.resoudre()
                if type(carte) == attaque :
                    if carte.joueur == joueur1 :
                        joueur, adversaire = joueur1, joueur2
                    else :
                        joueur, adversaire = joueur2, joueur1
                    carte.infliger_degats(joueur, adversaire, plateau)
                    self.vider()
                elif carte.nom == "Parade" or carte.nom == "Parade destructrice":
                    self.vider()
                self.nb = len(self)
                fin_effet("carte_jouee", lis_effets)
