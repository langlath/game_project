

from pile import pile
import numpy.random as rd


def echange(joueur1, joueur2, pil, lis_effets) :
    pil.jouer(joueur1, joueur2)
    fin_effet("fin_echange", lis_effets)

def faire_un_echange(joueur1, joueur2, joueur_init, lis_effets):
    pil = pile()
    joueur_qui_doit_jouer = 0
    if joueur1.main.taille > joueur2.main.taille :
        joueur_qui_doit_jouer = joueur1
    elif joueur2.main.taille > joueur1.main.taille :
        joueur_qui_doit_jouer = joueur2
    else :
        joueur_qui_doit_jouer = joueur_init
    if joueur1 == joueur_qui_doit_jouer :
        joueur_qui_ne_doit_pas_jouer = joueur2
    else :
        joueur_qui_ne_doit_pas_jouer = joueur1

    if pil.veut_jouer(joueur_qui_doit_jouer):
        echange(joueur_qui_ne_doit_pas_jouer, joueur_qui_doit_jouer, pil, lis_effets)
    elif pil.veut_jouer(joueur_qui_ne_doit_pas_jouer) :
        echange(joueur_qui_ne_doit_pas_jouer, joueur_qui_doit_jouer, pil, lis_effets)
    else :
        print("vous devez jouer {0} !".format(joueur_qui_doit_jouer))
        a = pil.veut_jouer(joueur_qui_doit_jouer)
        while not a :
            print("vous devez jouer {0} !".format(joueur_qui_doit_jouer))
            a= pil.veut_jouer(joueur_qui_doit_jouer)
        echange(joueur_qui_ne_doit_pas_jouer, joueur_qui_doit_jouer, pil, lis_effets)

def un_tour(joueur1, joueur2, joueur_init, lis_effets):
    while joueur1.main.taille > 0 or joueur2.main.taille > 0 :
        faire_un_echange(joueur1, joueur2, joueur_init)
    fin_effet("fin_tour", lis_effets)
    joueur1.pioche(6)
    joueur2.pioche(6)

def fin_effet(cond, lis_effets):
    a_enlever = []
    for eff in lis_effets :
        if eff.fin == cond :
            a_enlever.append(eff)
    for elt in a_enlever :
        lis_effets.remove(elt)

def partie(joueur1, joueur2, lis_effets):
    n = rd.randint(1, 2)
    if n == 1:
        joueur_init = joueur1
        joueur_pas_init = joueur2
    else :
        joueur_init = joueur2
        joueur_pas_init = joueur1
    while joueur1.pv > 0 and joueur2.pv > 0 :
        un_tour(joueur1, joueur2, joueur_init)
        if joueur1.pv > 0 and joueur2.pv > 0 :
            un_tour(joueur1, joueur2, joueur_pas_init)
    if joueur1.pv > 0 :
        print("{} a gagné, félicitations !".format(joueur1))
    elif joueur2.pv > 0 :
        print("{} a gagné, félicitations !".format(joueur2))
    else :
        print("tout le monde est mort... quel carnage!")

def commencer_une_partie():
    lis_classes = ["assassin", "moine", "guerrier", "chevalier"]
    a = input("veuillez choisir la classe du premier joueur. Les classes disponibles sont {}".format(lis_classes))
    lis_classes.remove(a)
    b = input("veuillez choisir la classe du deuxième joueur. Les classes disponibles sont {}".format(lis_classes))
    if a == "assassin" :
        joueur1.deck = deck(lis_cartes_assassin_1)
        joueur1.nom = "assassin"
    elif a == "guerrier" :
        joueur1.deck = deck(lis_cartes_guerrier_1)
        joueur1.nom = "guerrier"
    elif a == "moine" :
        joueur1.deck = deck(lis_cartes_moine_1)
        joueur1.nom = "moine"
    elif a == "chevalier" :
        joueur1.deck = deck(lis_cartes_chevalier_1)
        joueur1.nom = "chevalier"
    else :
        print("c'est pas cool, maintenant ça va bugger")
    if b == "assassin":
        joueur2.deck = deck(lis_cartes_assassin_2)
        joueur2.nom = "assassin"
    elif b == "guerrier":
        joueur2.deck = deck(lis_cartes_guerrier_2)
        joueur2.nom = "guerrier"
    elif b == "moine":
        joueur2.deck = deck(lis_cartes_moine_2)
        joueur2.nom = "moine"
    elif b == "chevalier":
        joueur2.deck = deck(lis_cartes_chevalier_2)
        joueur2.nom = "chevalier"
    else:
        print("c'est pas cool, maintenant ça va bugger")
    lis_effets = []
    joueur1.pioche(6)
    joueur2.pioche(6)
    partie(joueur1, joueur2, lis_effets)