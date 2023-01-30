import numpy as np
from paquets import paquet, deck, defausse, main
from plateau import plateau, pion
from effet import effet
from carte import carte, attaque, action, etat, personnage
from joueur import joueur


deck = deck([])
defausse = defausse()
main = main()
pion = pion([0, 1], "north")
joueur = joueur(40, "nothing", "Guirlande d'Irlande", main, deck, defausse)
carte1 = attaque(2, 6, 1, ["front"], effet("nothing", "nothing", True), joueur)
print(main, pion, joueur,carte1)

#Cartes attaques

Revers_devastateur=attaque("Revers devastateur",2,6,1,["front", "left", "right"], effet("nothing", "nothing", True, None), joueur )
High_kick=attaque("High Kick",3,4,1,["front", "left", "right"], effet("nothing", "nothing", True, None), joueur )
Tir_d_arbalete=attaque("Tir d'arbalète",1,6,100,["front", "left", "right"], effet("nothing", "nothing", True, None), joueur )
Uppercut=attaque("Uppercut",4,6,0,["front", "left", "right"], effet("nothing", "nothing", True, None), joueur )
Frappe_du_poing=attaque("Frappe du poing",4,2,1,["front", "left", "right"], effet("nothing", "nothing", True, None), joueur )
Frappe_veloce=attaque("Frappe véloce",4,2,1,["front", "left", "right"], effet("nothing", "nothing", True, None), joueur )
Dans_ta_face=attaque("Dans ta face",5,1,1,["front", "left", "right"], effet("nothing", "nothing", True, None), joueur )
Frappe_verticale=attaque("Frappe verticale",4,5,1,["front"], effet("nothing", "nothing", True, None), joueur )

Balayage=attaque("Balayage",4,4,1,["front"], effet("nothing", "nothing", True, "Vous pouvez vous orienter. Votre prochaine carte jouée perd 1 de vitesse"), joueur )