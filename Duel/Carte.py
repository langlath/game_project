import pygame as p


class carte:
    def __init__(self, nom, effet, joueur, image):
        self.effet=effet
        self.joueur= joueur
        self.modifiee_par = []
        self.nom = nom
        self.image = image

    def resoudre(self):
        """
        permet de résoudre l'effet de la carte
        :return: rien du tout
        Auteur: Thibault Langlard
        """
        self.effet.resoudre(self.joueur)

    def dessiner(self):
        """
        permet de redimensionner et retourner l'image de la carte
        :return a: image, image de la carte
        Auteur: Léa Vilasi
        """
        a = p.transform.scale(self.image, (150, 210))
        a = a.convert()
        return a

class action(carte):
    def __init__(self,nom, vitesse, effet, joueur,image):
        super().__init__(nom, effet, joueur, image)
        self.vitesse = vitesse

    def __str__(self):
        return "joueur:{0}, effet:{1}, vitesse:{2}".format(self.joueur.nom, self.effet, self.vitesse)


class attaque(carte):
    def __init__(self, nom, vitesse, degats, portee, direction, effet, joueur,image):
        super().__init__(nom, effet, joueur, image)
        self.vitesse = vitesse
        self.degats = degats
        self.portee= portee
        self.directions = direction

    def __str__(self):
        return "joueur:{0}, effet:{1}, vitesse:{2}, portée:{3}, direction: {4}, dégats: {5}".format(self.joueur.nom, self.effet, self.vitesse, self.portee, self.directions, self.degats)

    def infliger_degats(self, joueur, adversaire, plateau):
        """
        permet d'infliger des dégâts à un joueur grâce à une carte attaque
        :param joueur: joueur, joueur qui a joué la carte
        :param adversaire: joueur, adversaire qui reçoit les dégâts
        :param plateau: plateau, plateau de jeu
        :return: rien du tout
        Auteur: Thibault Langlard
        """
        lis_cases_touchees = [[joueur.pion.x - 600, joueur.pion.y - 100]]
        for n in range(self.portee + 1) :
            for i in range(len(self.directions)) :
                direc_i = "rien"
                elt_i = self.directions[i]
                if elt_i == "devant" :
                    direc_i = joueur.pion.orientation
                elif elt_i == "gauche" :
                    direc_i = joueur.pion.gauche
                elif elt_i == "droite" :
                    direc_i = joueur.pion.droite
                elif elt_i == "derriere" :
                    direc_i = joueur.pion.derriere
                for n in range(self.portee + 1):
                    for j in range(i, len(self.directions)) :
                        elt_j = self.directions[j]
                        direc_j = "rien"
                        if j > i :
                            if elt_j == "devant":
                                direc_j = joueur.pion.orientation
                            elif elt_j == "gauche":
                                direc_j = joueur.pion.gauche
                            elif elt_j == "droite":
                                direc_j = joueur.pion.droite
                            elif elt_j == "derriere":
                                direc_j = joueur.pion.derriere
                        directions = [direc_i, direc_j]
                        coords_a_toucher = [joueur.pion.x - 600, joueur.pion.y - 100]
                        if "nord" in directions :
                            coords_a_toucher[1] -= 100
                        if "sud" in directions :
                            coords_a_toucher[1] += 100
                        if "est" in directions :
                            coords_a_toucher[0] += 100
                        if "ouest" in directions :
                            coords_a_toucher[0] -= 100
                        if coords_a_toucher[0] >= 0 and coords_a_toucher[0] < plateau.largeur and coords_a_toucher[1] >= 0 and coords_a_toucher[1] < plateau.longueur and not coords_a_toucher in lis_cases_touchees :
                            lis_cases_touchees.append(coords_a_toucher)
        print(lis_cases_touchees, [joueur.pion.x, joueur.pion.y], [adversaire.pion.x, adversaire.pion.y])
        for case in lis_cases_touchees :
            if case == [adversaire.pion.x - 600, adversaire.pion.y - 100]:
                dir_portees = [case[0] - joueur.pion.x, case[1] - joueur.pion.y]
                orient_adv = adversaire.pion.orientation
                if (dir_portees[0] == 1 and orient_adv == "ouest") or (dir_portees[0] == -1 and orient_adv == "est") or (dir_portees[1] == 1 and orient_adv == "nord") or (dir_portees[1] == -1 and orient_adv == "sud") or (dir_portees == [0, 0] and orient_adv == joueur.pion.orientation) :
                    adversaire.degats(self.degats + 3)
                else :
                    adversaire.degats(self.degats)




class etat(carte):
    def __init__(self, nom, effet, joueur, image):
        super().__init__(nom, effet, joueur, image)

    def __str__(self):
        return "effet:{}".format(self.effet)

class personnage(carte):
    def __init__(self, nom, effet, joueur, image):
        super().__init__(nom, effet, joueur, image)

    def __str__(self):
        return "joueur:{0}, effet:{1}".format(self.joueur.nom, self.effet)

class deplacement(carte) :

    def __init__(self, joueur, image):
        super().__init__("deplacement", effet([joueur.deplacement], "rien", "permet au joueur de se déplacer"), joueur, image)
        self.vitesse = 1

class orientation(carte) :

    def __init__(self, joueur,image):
        super().__init__("orientation", effet([joueur.orientation], "rien", "permet au joueur de s'orienter"), joueur,  image)
        self.vitesse = 3

class se_defausser(carte):

    def __init__(self, joueur, adversaire, image):

        def defausse():
            """
            permet au joueur de se défausser de toutes ses cartes
            :return: rien du tout
            Auteur: Thibault Langlard
            """
            n = len(joueur.main.cartes)
            for carte in joueur.main.cartes :
                 joueur.defausse.cartes.append(carte)
            adversaire.degats(n)
            joueur.main.cartes = []
            joueur.main.taille = 0
        super().__init__("Défausse",effet([defausse], "rien", "permet au joueur de se défausser de ses cartes"), joueur,image)
        self.vitesse = 1


class effet :

    def __init__(self, a_resoudre, cond_fin, enonce):
        self.a_resoudre = a_resoudre
        self.cond_fin = cond_fin
        self.enonce = enonce

    def __str__(self):
        return self.enonce

    def resoudre(self, joueur):
        """
        résoud l'effet et le place dans la liste des effets en action"
        :return: rien du tout
        Auteur: Thibault Langlard
        """
        if self.a_resoudre != "rien" and self.a_resoudre != "nothing" :
            for effet_a in self.a_resoudre:
               effet_a()

class modificateur(effet):

    def __init__(self, a_resoudre, cond_fin, enonce, lis_types, force, portee, vitesse):
        super().__init__(a_resoudre, cond_fin, enonce)
        self.a_modifier = lis_types
        self.force = force
        self.portee = portee
        self.vitesse = vitesse

    def resoudre(self, joueur):
        """
        résoud l'effet et le place dans la liste des effets en action"
        :return: rien du tout
        Auteur: Thibault Langlard
        """
        if self.a_resoudre != "rien" and self.a_resoudre != "nothing" :
            for effet_a in self.a_resoudre:
               effet_a()
        self.modifier(joueur)


    def modifier(self, joueur):
        """
        permet d'augmenter les attributs d'une carte, grâce à l'effet d'une autre carte
        :param joueur: joueur, joueur dont les cartes bénéficient de l'effet
        :return: rien du tout
        Auteur: Thibault Langlard
        """
        for paquet in [joueur.deck, joueur.main, joueur.defausse]:
            for carte in paquet.cartes :
                for ty in self.a_modifier :
                    if type(carte) == ty :
                        if type(carte) == attaque :
                            carte.degats += self.force
                            carte.vitesse += self.vitesse
                            carte.portee += self.portee
                        else :
                            carte.vitesse += self.vitesse
                    carte.modifiee_par.append(self)

    def demodifier(self, joueur):
        """
        permet d'annuler les modifications d'une carte
        :param joueur: joueur, joueur dont les cartes ont été précédemment modifiées
        :return: rien du tout
        Auteur: Thibault Langlard
        """
        for paquet in [joueur.deck, joueur.main, joueur.defausse]:
            for carte in paquet:
                if appartient(self, carte.modfiee_par):
                    if type(carte) == attaque :
                        carte.degats -= self.force
                        carte.vitesse -= self.vitesse
                        carte.portee -= self.portee
                    else :
                        carte.vitesse -= self.vitesse
                    carte.modifiee_par.remove(self)
                    lis_effets.remove(self)

