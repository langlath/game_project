class carte:
    def __init__(self, effet, joueur, nom):
        self.effet=effet
        self.joueur= joueur
        self.nom=nom

    def resoudre(self):
        self.effet.resoudre()

class action(carte):
    def __init__(self, vitesse, effet, joueur,nom):
        super().__init__(effet, joueur,nom)
        self.vitesse = vitesse
    def __str__(self):
        return "joueur:{0}, effet:{1}, vitesse:{2}".format(self.joueur, self.effet, self.vitesse)


class attaque(carte):
    def __init__(self, vitesse, degats, portee, direction, effet, joueur,nom):
        super().__init__(effet, joueur,nom)
        self.vitesse = vitesse
        self.degats = degats
        self.portee= portee
        self.direction = direction
    def __str__(self):
        return "joueur:{0}, effet:{1}, vitesse:{2}, portée:{3}, direction: {4}, dégats: {5}".format(self.joueur, self.effet, self.vitesse, self.portee, self.direction, self.degats)


class etat(carte):
    def __init__(self, effet, joueur,nom):
        super().__init__(effet, joueur,nom)
    def __str__(self):
        return "joueur:{0}, effet:{1}".format(self.joueur, self.effet)

class personnage(carte):
    def __init__(self, effet, joueur,nom):
        super().__init__(effet, joueur,nom)
    def __str__(self):
        return "joueur:{0}, effet:{1}".format(self.joueur, self.effet)
