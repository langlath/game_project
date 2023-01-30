class joueur:
    def __init__(self, pv, effet,nom, main, deck, defausse):
        self.pv= pv
        self.effet = effet
        self.nom= nom
        self.main=main
        self.deck=deck
        self.defausse= defausse

    def __str__(self):
        return "nom: {}, pv: {}".format(self.nom, self.pv)

    def degats(self, nb):
        """
        permet au joueur de prendre des dégâts
        :param nb: nombre de dégâts à infliger
        :return: rien du tout
        """
        self.pv -= nb