

class plateau :

    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur
        self.plateau = [[0 for j in range(largeur)] for i in range(longueur)]

    def __str__(self):
        return "longueur:{}, largeur:{}".format(self.longueur, self.largeur)

class pion :

    def __init__(self, coords, orient):
        self.lis_orient = ["nord", "est", "sud", "ouest"]
        self.abscisse = coords[0]
        self.ordonnee = coords[1]
        self.orientation = orient
        self.gauche = orient
        self.droite = orient
        self.derriere = orient
        self.orienter(orient)


    def __str__(self):
        return "position({},{}), orientation:{}".format(self.abscisse, self.ordonnee, self.orientation)

    def deplacer(self, x, y, plateau):
        """
        permet de déplacer le pion sur le plateau
        :param x: l'abscisse du pion
        :param y: l'ordonnée du pion
        :param plateau: le plateau sur lequel on déplace le pion
        :return:rien du tout
        """
        if self.abscisse + x >= 0 and self.abscisse + x < plateau.largeur and self.ordonnee + y >= 0 and self.ordonnee + y < plateau.longueur :
            self.abscisse += x
            self.ordonnee += y
        else :
            print("pion hors du plateau")

    def orienter(self, orient):
        """
        permet d'orienter le pion
        :param orient: l'orientation qu'on souhaite donner
        :return: rien du tout
        """
        self.orientation = orient
        i = 0
        while i < 4 and self.lis_orient[i] != orient :
            i += 1
        self.droite = self.lis_orient[(i + 1) % 4]
        self.derriere = self.lis_orient[(i + 2) % 4]
        self.gauche = self.lis_orient[(i + 3) % 4]
