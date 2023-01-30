import pygame as p

class plateau :

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.plateau = [[0 for j in range(largeur)] for i in range(longueur)]

    def __str__(self):
        return "longueur:{}, largeur:{}".format(self.longueur, self.largeur)

class pion :

    def __init__(self, coords, orient, image):
        self.lis_orient = ["nord", "est", "sud", "ouest"]
        self.x = coords[0]
        self.y = coords[1]
        self.orientation = orient
        self.gauche = orient
        self.droite = orient
        self.derriere = orient
        self.image=image
        self.orienter(orient)


    def __str__(self):
        return "position({},{}), orientation:{}".format(self.x, self.y, self.orientation)

    def deplacer(self, a, b, plateau, joueur):
        """
        permet de déplacer le pion sur le plateau
        :param x: l'abscisse du pion
        :param y: l'ordonnée du pion
        :param plateau: le plateau sur lequel on déplace le pion
        :return:rien du tout
        Auteur: Thibault Langlard
        """
        if self.x - 600 + a >= 0 and self.x - 600 + a < plateau.largeur and self.y -100 + b >= 0 and self.y - 100 + b < plateau.longueur :
            self.x += a
            self.y += b
            joueur.nb_actions=0

        else :
            print("pion hors du plateau")


    def orienter(self, orient):
        """
        permet d'orienter le pion
        :param orient: l'orientation qu'on souhaite donner
        :return: rien du tout
        Auteur: Thibault Langlard
        """
        self.orientation = orient
        i = 0
        while i < 4 and self.lis_orient[i] != orient :
            i += 1
        self.droite = self.lis_orient[(i + 1) % 4]
        self.derriere = self.lis_orient[(i + 2) % 4]
        self.gauche = self.lis_orient[(i + 3) % 4]

    def dessiner(self):
        """
        permet de redimensionner et retourner l'image du pion
        :return a: image, image du pion
        Auteur: Léa Vilasi
        """
        a = p.transform.scale(self.image, (100, 100))
        a = a.convert()
        return a

    def deplacement_possible(self,a,b, plateau):
        """
        permet d'accéder aux déplacements possibles du pion sur le plateau
        :return : booléen, True ou False si le déplacement est possible ou non
        Auteur: Léa Vilasi
        """
        return self.x - 600 + a >= 0 and self.x - 600 + a < plateau.largeur and self.y - 100 + b >= 0 and self.y - 100 + b < plateau.longueur