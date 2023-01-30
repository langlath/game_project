from joueur import joueur

class effet :

    def __init__(self, a_resoudre, cond_fin, enonce):
        self.a_resoudre = a_resoudre
        self.fin = cond_fin
        self.enonce = enonce

    def __str__(self):
        return self.enonce

    def resoudre(self):
        """
        résoud l'effet et le place dans la liste des effets en action"
        :return: rien du tout
        """
        if self.a_resoudre != "rien" :
            lis_effets.append(effet)
            for eff in self.a_resoudre :
                eff()

class modificateur(effet):

    def __init__(self, a_resoudre, cond_fin, enonce, lis_types, force, portee, vitesse):
        super.__init__(a_resoudre, cond_fin, enonce)
        self.a_modifier = lis_types
        self.force = force
        self.portee = portee
        self.vitesse = vitesse

    def modifier(self, joueur):
        for paquet in [joueur.deck, joueur.main, joueur.defausse]:
            for carte in paquet :
                for ty in self.a_modifier :
                    if type(carte) == ty :
                        if type(carte) == attaque :
                            carte.degats += self.force
                            carte.vitesse += self.vitesse
                            carte.portee += self.portee
                        else :
                            carte.vitesse += self.vitesse
                        carte.modifiee_par.append(self)
        self.resoudre()

    def demodifier(self, joueur):
        for paquet in [joueur.deck, joueur.main, joueur.defausse]:
            for carte in paquet:
                if appartient(self, carte.modifiee_par):
                    if type(carte) == attaque :
                        carte.degats -= self.force
                        carte.vitesse -= self.vitesse
                        carte.portee -= self.portee
                    else :
                        carte.vitesse -= self.vitesse
                    carte.modifiee_par.remove(self)
                    lis_effets.remove(self)



def appartient(elt, lis):
    for i in lis :
        if i == elt :
            return True
    return False

# def poison():
#     adversaire gagne poison

# effet(poison, "rien", False, "fait gagner un poison à l'adversaire")