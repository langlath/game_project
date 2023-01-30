from carte import carte, attaque, action, etat, personnage
from joueur import joueur
from effet import effet, modificateur


#Cartes attaques

Revers_devastateur=attaque("Revers devastateur",2,6,1,["front", "left", "right"], effet("nothing", "nothing",  None, "ne fait rien"), joueur )
High_kick=attaque("High Kick",3,4,1,["front", "left", "right"], effet("nothing", "nothing",  None, "ne fait rien"), joueur )
Tir_d_arbalete=attaque("Tir d'arbalète",1,6,100,["front", "left", "right"], effet("nothing", "nothing",  None, "ne fait rien"), joueur )
Uppercut=attaque("Uppercut",4,6,0,["front", "left", "right"], effet("nothing", "nothing",  None, "ne fait rien"), joueur )
Frappe_du_poing=attaque("Frappe du poing",4,2,1,["front", "left", "right"], effet("nothing", "nothing",  None, "ne fait rien"), joueur )
Frappe_veloce=attaque("Frappe véloce",4,2,1,["front", "left", "right"], effet("nothing", "nothing",  None, "ne fait rien"), joueur )
Dans_ta_face=attaque("Dans ta face",5,1,1,["front", "left", "right"], effet("nothing", "nothing",  None, "ne fait rien"), joueur )
Frappe_verticale=attaque("Frappe verticale",4,5,1,["front"], effet("nothing", "nothing",  None, "ne fait rien"), joueur )


#Fonctions effets

def f_enduire_poison(joueur1):#Ajoute une carte poison au joueur1
    Poison.joueur = joueur1
    joueur1.main.cartes.append(Poison)

def f_balayage(joueur1):
    a=input("Voulez vous vous orienter?")
    if a=="Oui":
        joueur1.deplacement()

def f_parade():
    pass

def f_arbalete():
    pass

def f_fulgurante():
    pass

def f_elan():
    pass

Balayage=attaque("Balayage", 4, 4, 1, ["front"], effet(f_balayage, "carte_jouee", False, "Vous pouvez vous orienter. Votre prochaine carte jouée perd 1 de vitesse."), joueur )

#Cartes actions

Enduire_de_poison=action("Enduire de poison", 4, effet(f_enduire_poison, "rien", False, "Votre adversaire gagne une carte poison."), joueur)
Parade= action("Parade", 4, effet(f_parade, "rien", False, "Annulez l'attaque de votre adversaire. Met fin à l'échange."), joueur)
# Charger_l_arbalete=action("Charger l'arbalète", 1, effet(f_arbalete, "rien", "Votre prochain tir d'arbalète aura 4 de vitesse. Piochez une carte."))
# Avancee_fugurante=action("Avancée fulgurante", 5, effet(f_fulgurante, "rien", "Vous vous déplacez d'une case dans la direction de votre choix."))
# Prendre_son_elan=action("Prendre son élan", 3, effet(f_elan, "rien", "Vote prochaine attaque inflige 2 dégâts supplémentaires et sa vitesse augmente de 2."))

#Cartes états
# Poison=etat("Poison", effet("rien", "rien", "Au début de chaque tour, vous subissez 1 de dégât"), joueur)

print(type(Balayage) == carte)
