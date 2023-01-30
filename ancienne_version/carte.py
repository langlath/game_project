from effet import effet
import pygame as p

class carte:
    def __init__(self, nom, effet, joueur, image):
        self.effet = effet
        self.joueur = joueur
        self.modifiee_par = []
        self.nom = nom
        self.image = image

    def resoudre(self):
        self.effet.resoudre()

    def dessiner(self):
        a = p.transform.scale(self.image, (150, 210))
        a = a.convert()
        return a

class action(carte):
    def __init__(self, nom, vitesse, effet, joueur, image):
        super().__init__(effet, joueur, nom, image)
        self.vitesse = vitesse

    def __str__(self):
        return "joueur:{0}, effet:{1}, vitesse:{2}".format(self.joueur.nom, self.effet, self.vitesse)


class attaque(carte):
    def __init__(self, nom, vitesse, degats, portee, direction, effet, joueur,image):
        super().__init__(effet, joueur, nom,image)
        self.vitesse = vitesse
        self.degats = degats
        self.portee= portee
        self.directions = direction

    def __str__(self):
        return "joueur:{0}, effet:{1}, vitesse:{2}, portée:{3}, direction: {4}, dégats: {5}".format(self.joueur.nom, self.effet, self.vitesse, self.portee, self.directions, self.degats)

    def infliger_degats(self, joueur, adversaire, plateau):
        lis_cases_touchees = [[joueur.pion.abscisse, joueur.pion.ordonnee]]
        for n in range(self.portee + 1) :
            for i in range(len(self.directions)) :
                direc_i = "rien"
                if i == "devant" :
                    direc_i = joueur.pion.orient
                elif i == "gauche" :
                    direc_i = joueur.pion.gauche
                elif i == "droite" :
                    direc_i = joueur.pion.droite
                elif i == "derriere" :
                    direc_i = joueur.pion.derriere
                for n in range(self.portee + 1):
                    for j in range(i, len(self.directions)) :
                        direc_j = "rien"
                        if j > i :
                            if j == "devant":
                                direc_j = joueur.pion.orient
                            elif j == "gauche":
                                direc_j = joueur.pion.gauche
                            elif j == "droite":
                                direc_j = joueur.pion.droite
                            elif j == "derriere":
                                direc_j = joueur.pion.derriere
                        directions = [direc_i, direc_j]
                        coords_a_toucher = [joueur.pion.abscisse, joueur.pion.ordonnee]
                        if appartient("nord", directions) :
                            coords_a_toucher[1] += 1
                        if appartient("sud", directions) :
                            coords_a_toucher[1] -= 1
                        if appartient("est", directions) :
                            coords_a_toucher[0] += 1
                        if appartient("ouest", directions) :
                            coords_a_toucher[0] -= 1
                        if coords_a_toucher[0] >= 0 and coords_a_toucher[0] < plateau.largeur and coords_a_toucher[1] >= 0 and coords_a_toucher[1] < plateau.longueur and not appartient(coords_a_toucher, lis_cases_touchees) :
                            lis_cases_touchees.append(coords_a_toucher)
        for case in lis_cases_touchees :
            if case == [adversaire.pion.abscisse, adversaire.pion.ordonnee]:
                dir_portees = [case[0] - joueur.pion.abscisse, case[1] - joueur.pion.ordonnee]
                orient_adv = adversaire.pion.orient
                if (dir_portees[0] == 1 and orient_adv == "ouest") or (dir_portees[0] == -1 and orient_adv == "est") or (dir_portees[1] == 1 and orient_adv == "nord") or (dir_portees[1] == -1 and orient_adv == "sud") or (dir_portees == [0, 0] and orient_adv == joueur.pion.orient) :
                    if joueur.nom == "assassin" :
                        adversaire.degats(self.degats + 5)
                    else :
                        adversaire.degats(self.degats + 3)
                else :
                    adversaire.degats(self.degats)


class etat(carte):
    def __init__(self, nom, effet, joueur,image):
        super().__init__(effet, joueur, nom,image)

    def __str__(self):
        return "joueur:{0}, effet:{1}".format(self.joueur.nom, self.effet)

class personnage(carte):
    def __init__(self, nom, effet, joueur,image):
        super().__init__(effet, joueur, nom,image)

    def __str__(self):
        return "joueur:{0}, effet:{1}".format(self.joueur.nom, self.effet)

class deplacement(carte) :

    def __init__(self, joueur):
        super.__init__(effet(joueur.deplacement, "rien", False, "permet au joueur de se déplacer"), joueur, "deplacement")
        self.vitesse = 1

class orientation(carte) :

    def __init__(self, effet, joueur):
        super.__init__(effet(joueur.orientation, "rien", False, "permet au joueur de s'orienter"), joueur, "orientation")
        self.vitesse = 3

class se_defausser(carte):

    def __init__(self, joueur, adversaire):
        def defausse():
            n = joueur.main.taille
            for carte in joueur.main.cartes :
                joueur.defausse.cartes.append(carte)
            adversaire.degats(n)
            joueur.main.cartes = []
            Joueur.main.taille = 0
        super.__init__(effet(defausse, "rien", False, "permet au joueur de se défausser de ses cartes"), joueur, "défausse")
        self.vitesse = 1