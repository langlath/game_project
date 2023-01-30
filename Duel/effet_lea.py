

class effet :

    def __init__(self, effet, activ, passif, enonce):
        self.resolution = effet
        self.activation = activ
        self.est_passif = passif
        self.enonce=enonce

    def __str__(self):
        return self.enonce

    def resoudre(self):
        """
        résoud l'effet et le place dans la liste des effets en action"
        :return: rien du tout
        """
        lis_effets.append(effet)
        self.resolution()

lis_effets = []