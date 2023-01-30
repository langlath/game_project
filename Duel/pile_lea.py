class pile(list):
    def __init__(self):
        super().__init__()
        self.nb= len(self)

    def vider(self):
        """
        permet de vider la liste
        :return: rien du tout
        """
        L=[carte for carte in self]
        for carte in L:
            carte.joueur.defausse.append(carte)
        self.clear()

    def jouer(self, joueur):
        """
        permet de remplir la liste avec les cartes jouées
        :param joueur: le joueur qui a la possibilité d'interrompre
        :return: rien du tout
        """
        a = input("Voulez vous interrompre?")
        if a == "Oui":
            None
            # joueur.main.jouer(carte_à_jouer, self)  #carte à jouer à compléter
            # self.jouer(self, joueur_adverse)        #joueur adverse à compléter
        else:
            for carte in pile:
                carte.resoudre()
            pile.vider()
