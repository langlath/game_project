import pygame as p
from pygame.locals import *
import sys
from carte import  *
from effet import *
from plateau import *
from paquets import *
from pile import *
p.init()
timer=p.time.Clock()
game_on=True

#fond

conf = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/conf.jpg")
acc = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/accueil1.jpg")

#images défausse, déplacement, orientation

depl = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/deplacement.png")
ori = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/orientation.png")
se_def = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/defausse.png")


#images rôles

chev = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/chevalier.png")
guer = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/guerrier.png")
moin = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/moine.png")
ass = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/assassin.png")


#images états

saig = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/saignement.png")


rev = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/Revers_devastateur.png")
high = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/High_kick.png")
upp = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/Uppercut.png")
tir = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/Tir_d_arbalete.png")
poing = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/Frappe_du_poing.png")
vel = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/Frappe_Veloce.png")
par_guer = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/parade_guerrier.png")
par_assa = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/parade_assassin.png")
par_chev = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/parade_chevalier.png")
par_moin = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/parade_moine.png")
bal = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/balayage.png")
poign = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/coup_de_poignard_leger.png")
avan = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/avancee_fulgurante.png")
sauva = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/charge_sauvage.png")
aban = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/abandon_du_fair_play.png")
face = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/dans_ta_face.png")
verti = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/frappe_verticale.png")
tourbi = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/tourbillon_de_lames.png")
embro = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/embrocher.png")
elan = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/prendre_son_elan.png")
foi = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/foi_renouvelee.png")
bers = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/berserker.png")
egor = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/egorgement.png")
trans = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/transe_du_combattant.png")
destru = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/parade_destructrice.png")
eclair = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/frappe_eclair.png")
estoc = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/frappe_d_estoc.png")
exec = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/executer.png")

#images pions

fish = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/fish.png")
fish2 = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/fish2.jpg")
deuxfish = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/deuxfish.png")
deuxfish = p.transform.scale(deuxfish, (100, 100))

#joueurs
lis_joueurs = []
def autre_joueur(joueur) :
    for j in lis_joueurs :
        if j != joueur :
            return j

effet_vide = effet("rien", "rien", "n'a pas d'effet")
pion1 = pion([0, 1], "sud", fish)
pion2 = pion([0,0],"nord",fish2 )

main_guer = main()
deck_guer = deck([])
defausse_guer = defausse()
guerrier = joueur(40, effet_vide, "guerrier", main_guer, deck_guer, defausse_guer, pion1)

main_assa = main()
deck_assa = deck([])
defausse_assar = defausse()
assassin = joueur(40, effet_vide, "assassin", main_assa, deck_assa, defausse_assar, pion1)

main_chev = main()
deck_chev = deck([])
defausse_chev = defausse()
chevalier = joueur(40, effet_vide, "chevalier", main_chev, deck_chev, defausse_chev, pion2)

main_moin = main()
deck_moin = deck([])
defausse_moin = defausse()
moine = joueur(40, effet_vide, "moine", main_moin, deck_moin, defausse_moin, pion2)

lis_joueurs = [assassin, moine]
pile = pile()

#effets


effet_vide = effet("rien", "rien", "n'a pas d'effet")
effet_parade = effet("rien", "rien", "met fin à l'échange")
effet_balayage = modificateur([guerrier.droit_orientation], "carte_jouee", "Orientez-vous. Votre prochaine carte joué perd 1 de vitesse", [attaque, action], 0, 0, -1)
effet_poignard = effet([autre_joueur(assassin).saigner], "rien", "l'adversaire gagne une carte saignement")
effet_avancee = effet([moine.droit_deplacement], "rien", "vous vous déplacez d'une case")
effet_sauvage = effet([assassin.droit_deplacement, assassin.droit_deplacement], "rien", "vous vous déplacez de deux cases")
effet_abandon = effet([autre_joueur(moine).saigner], "rien", "l'adversaire gagne une carte saignement")
effet_tourbillon = effet([assassin.droit_orientation], "rien", "vous vous orientez")
effet_embrocher = effet([autre_joueur(chevalier).saigner, autre_joueur(chevalier).saigner], "rien", "l'adversaire gagne deux cartes saignement")
effet_elan = modificateur("rien", "carte_jouee", "Votre prochaine attaque inflige 2 dégâts supplémentaires et sa vitesse augmente de 2", [attaque], 2, 0, 2)
effet_foi = effet([chevalier.soin, chevalier.soin, chevalier.soin, chevalier.soin, chevalier.soin, chevalier.pioche], "rien", "Vous gangez 5 PV. Piochez une carte")
effet_berserker = modificateur([guerrier.pioche], "fin_tour", "jusqu'à la fin du tour, vos cartes attaque infligent 2 dégâts supplémentaires et leur vitesse augmente de 1. Piochez une carte", [attaque], 2, 0, 1)
effet_egorgement = effet([autre_joueur(assassin).saigner, autre_joueur(assassin).saigner], "rien", "l'adversaire gagne deux cartes saignement")
effet_transe = modificateur([moine.pioche], "fin_tour", "jusqu'à la fin du tour, vos attaques infligent 2 dégâts supplémentaires. Piochez une carte", [attaque], 2, 0, 0)
effet_destructrice = effet([autre_joueur(moine).degats, autre_joueur(moine).degats, autre_joueur(moine).degats], "rien", "met fin à l'échange. L'adversaire subit 3 dégâts")
effet_eclair = effet([chevalier.orientation], "rien", "orientez-vous")

#cartes

Revers_devastateur = attaque("Revers devastateur", 2, 6, 1, ["devant", "gauche", "droite"], effet_vide, guerrier, rev)
Frappe_veloce = attaque("Frappe véloce", 4, 2, 1, ["devant", "gauche", "droite"], effet_vide, guerrier, vel)
Parade_guer = action("Parade", 4, effet_parade, guerrier, par_guer)
Balayage = attaque("Balayage", 4, 4, 1, ["devant", "gauche", "droite"], effet_balayage, guerrier, bal)
Dans_ta_face = attaque("Dans ta face", 5, 1, 1, ["devant", "gauche", "droite"], effet_vide, guerrier, face)
Berserker = action("Berserker", 5, effet_berserker, guerrier, bers)
Executer = attaque("Executer", 1, 8, 1, ["devant"], effet_vide, guerrier, exec)

Parade_assa = action("Parade", 4, effet_parade, assassin, par_assa)
Coup_de_poignard_leger = attaque("Coup de poignard léger", 4, 1, 1, ["devant", "gauche", "droite"], effet_poignard, assassin, poign)
Charge_sauvage = action("Charge sauvage", 4, effet_sauvage, assassin, sauva)
Frappe_verticale = attaque("Frappe verticaale", 2, 5, 1, ["devant"], effet_vide, assassin, verti)
Tourbillon_de_lames = attaque("Tourbillon de lames", 4, 2, 1, ["devant", "gauche", "droite", "derrière"], effet_tourbillon, assassin, tourbi)
Egorgement = attaque("Egorgement", 1, 5, 1, ["devant", "gauche", "droite"], effet_egorgement, assassin, egor)

Frappe_d_estoc = attaque("Frappe d'estoc", 2, 4, 2, ["devant", "gauche", "droite"], effet_vide, chevalier, estoc)
Parade_chev = action("Parade", 4, effet_parade, chevalier, par_chev)
Embrocher = attaque("Embrocher", 2, 5, 1, ["devant"], effet_embrocher, chevalier, embro)
Prendre_son_elan = action("Prendre son élan", 3, effet_elan, chevalier, elan)
Foi_renouvelee = action("Foi renouvelée", 4, effet_foi, chevalier, foi)
Frappe_eclair = attaque("Frappe éclair", 4, 4, 1, ["gauche", "droite", "derrière"], effet_eclair, chevalier, eclair)

High_kick = attaque("High Kick", 3, 4, 1, ["devant", "gauche", "droite"], effet_vide, moine, high)
Uppercut = attaque("Uppercut", 4, 6, 0, ["devant", "gauche", "droite"], effet_vide, moine, upp)
Frappe_du_poing = attaque("Frappe du poing", 4, 2, 1, ["devant", "gauche", "droite"], effet_vide, moine, poing)
Parade_moin = action("Parade", 4, effet_parade, moine, par_moin)
Avancee_fulgurante = action("Avancée fulgurante", 5, effet_avancee, moine, avan)
Abandon_du_fair_play = attaque("Abandon du fair-play", 3, 3, 1, ["devant", "gauche", "droite"], effet_abandon, moine, aban)
Transe_du_combattant = action("Transe du combattant", 4, effet_transe, moine, trans)
Parade_destructrice = action("Parade destructrice", 5, effet_destructrice, moine, destru)


deck_guer.cartes = 3 * [Revers_devastateur] + 4 * [Frappe_veloce] + 4 * [Parade_guer] + 3 * [Balayage] + 3 * [Dans_ta_face] + 2 * [Berserker] + 1 * [Executer]
deck_assa.cartes = 4 * [Parade_assa] + 4 * [Coup_de_poignard_leger] + 2 * [Charge_sauvage] + 3 * [Frappe_verticale] + 2 * [Tourbillon_de_lames] + 3 * [Egorgement]
deck_chev.cartes = 3 * [Frappe_d_estoc] + 4 * [Parade_chev] + 3 * [Embrocher] + 3 * [Prendre_son_elan] + 2 * [Foi_renouvelee] + 3 * [Frappe_eclair]
deck_moin.cartes = 3 * [High_kick] + 2 * [Uppercut] + 3 * [Frappe_du_poing] + 3 * [Parade_moin] + 2 * [Parade_destructrice]+ 2 * [Avancee_fulgurante] + 3 * [Abandon_du_fair_play] + 2 * [Transe_du_combattant]

deck_guer.melanger()
deck_assa.melanger()
deck_chev.melanger()
deck_moin.melanger()

#définition des joueurs

joueur1 = assassin
joueur2 = moine

#test précédent


"""main1 = main()
main2 = main()
deck1 = deck([])
deck2 = deck([])
defausse1 = defausse()
defausse2 = defausse()
pile = pile()

pion1 = pion([0, 1], "sud", fish)
pion2 = pion([0,0],"nord",fish2 )
lpion = [pion1,pion2]
j1 = joueur(40, "rien", "Guirlande", main1, deck1, defausse1, pion1)
j2 = joueur(40, "rien", "Irlande", main2, deck2, defausse2, pion2)

Revers_devastateur = attaque("Revers devastateur",2,6,1,["front", "left", "right"], effet("nothing", "nothing",  None), j1,rev )
High_kick = attaque("High Kick",3,4,1,["front", "left", "right"], effet("nothing", "nothing",  None), j1,high )
Tir_d_arbalete = attaque("Tir d'arbalète",1,6,100,["front", "left", "right"], effet("nothing", "nothing",  None), j2,tir )
Uppercut = attaque("Uppercut",4,6,0,["front", "left", "right"], effet("nothing", "nothing",  None), j2,upp )
Frappe_du_poing = attaque("Frappe du poing",4,2,1,["front", "left", "right"], effet("nothing", "nothing",  None), j1,poing )
Frappe_veloce = attaque("Frappe véloce",4,2,1,["front", "left", "right"], effet("nothing", "nothing",  None), j2,vel )


lismain1 = [Revers_devastateur, High_kick]
lismain2 = [Tir_d_arbalete,Uppercut]
main1.cartes = lismain1
main2.cartes = lismain2
deck1.cartes = [Frappe_veloce]
deck2.cartes = [Frappe_du_poing]
lisdefausse1 = []
defausse1.cartes = lisdefausse1


lisdefausse2 = []
defausse2.cartes = lisdefausse2"""



#rôles


chevalier_role = personnage("chevalier", effet("nothing", "nothing", "Les attaques adverses vous infligent 1 dégât de moins.Vos déplacements et orientations ont 1 de vitesse en moins"), chevalier, chev)
moine_role = personnage("chevalier", effet("nothing", "nothing", "Les attaques adverses vous infligent 1 dégât supplémentaire. La vitesse de vos déplacements et orientations augmente de 1."), moine, moin)
guerrier_role= personnage("chevalier", effet("nothing", "nothing", "Vos attaques infligent 1 dégât supplémentaire. Vous ne subissez pas de dégâts de fatigue"), guerrier, guer)
assassin_role = personnage("chevalier", effet("nothing", "nothing", "Vos attaques dans le dos de vos adversaires infligent 3 dégâts supplémentaires."), assassin, ass)

L_role = [chevalier_role, moine_role, guerrier_role, assassin_role]

#états

saignement = etat("saignement", effet([joueur1.degats], "nothing", "A la fin de chaque tour, vous subissez 1 de dégât."), joueur1, saig)

#fonctions


def actions_possibles(joueur, pile):
    possibles = []
    if pile.vitesse < 1:
        possibles.append("deplacement")
        possibles.append("se_defausser")
    if pile.vitesse < 3:
        possibles.append("orientation")
    vitesse = pile.vitesse
    if pile != []:
        derniere_carte = pile[-1]
        for carte in joueur.main.cartes:
            if carte.vitesse > vitesse:
                possibles.append(carte)
            elif carte.vitesse == vitesse and type(carte) == action and type(derniere_carte) != action:
                possibles.append(carte)
            elif carte.vitesse == vitesse and type(carte) == attaque and type(derniere_carte) != attaque and type(
                    derniere_carte) != action:
                possibles.append(carte)
    elif pile == []:
        for carte in joueur.main.cartes:
            possibles.append(carte)
    return possibles

carte_init= action("rien", 7, "rien", joueur, None)

def choix(joueur, adversaire, possible, pile):
    choix = carte_init
    bouge = 0
    for carte in possible:
        if carte == "deplacement" and joueur.nb_actions == 1:
            if joueur.pion.x - adversaire.pion.x < -100 :
                joueur.futur_deplacementx = 100
                joueur.futur_deplacement = "droite"
                joueur.futur_deplacementy = 0
                joueur.nb_actions = 0
                pile.append(deplacement(joueur, depl))
                pile.vitesse = 1
                bouge = 1
            elif joueur.pion.x - adversaire.pion.x > 100 :
                joueur.futur_deplacementx = - 100
                joueur.futur_deplacement = "gauche"
                joueur.futur_deplacementy = 0
                joueur.nb_actions = 0
                pile.append(deplacement(joueur, depl))
                pile.vitesse = 1
                bouge = 1
                print("se déplace")
            elif joueur.pion.y - adversaire.pion.y > 100 and abs(joueur.pion.x - adversaire.pion.x) <= 100:
                joueur.futur_deplacementy = -100
                joueur.futur_deplacement = "haut"
                joueur.futur_deplacementx = 0
                joueur.nb_actions = 0
                pile.append(deplacement(joueur, depl))
                pile.vitesse = 1
                bouge = 1
            elif joueur.pion.y - adversaire.pion.y < -100 and abs(joueur.pion.x - adversaire.pion.x) <= 100:
                joueur.futur_deplacementy = 100
                joueur.futur_deplacement = "bas"
                joueur.futur_deplacementx = 0
                joueur.nb_actions = 0
                pile.append(deplacement(joueur, depl))
                pile.vitesse = 1
                bouge = 1
        if type(carte) == action or type(carte) == attaque and bouge == 0:
            if choix.vitesse > carte.vitesse:
                    choix = carte
    if choix != carte_init and bouge == 0 and joueur.nb_actions == 1 and (type(choix) == action or type(choix) == attaque):
        print("choix", choix, "bouge", bouge)
        joueur.main.jouer(choix, pile)
        joueur.nb_actions = 0





#écran

col = 3
li = 4
size = 100
screen = p.display.set_mode(size=(1535,830))
my_surface = p.Surface((col*size,li*size))

#points de vie

pv_im = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/coeur.png")
pv_im = p.transform.scale(pv_im, (118,41))
pv_im = pv_im.convert()

police = p.font.Font(None,28)
policewin = p.font.Font(None,80)

#Bouton défausse

defa = p.Rect(1165,85,170,50)
textedef = police.render("Se défausser",True,"black")

#Bouton Fin du tour (un joueur interrompt)

tour = p.Rect(1165,150,170,50)
textetour = police.render("Finir mon tour",True,"black")

#Bouton Dépiler

dep = p.Rect(1165,215,170,50)
textedep = police.render("Dépiler",True,"black")

#initialisation variables


plateau = plateau(400,300)

joueur1.pion.x = 600
joueur1.pion.y = 100
joueur2.pion.x = 800
joueur2.pion.y = 400
posi = 0
couleur1 = (255,255,255)
couleur2 = (255,255,255)
couleur3 = (255,255,255)
couleur4 = (255,255,255)


orientbas = ((joueur1.pion.x, joueur1.pion.y + 100), (joueur1.pion.x + 50, joueur1.pion.y + 150), (joueur1.pion.x + 100, joueur1.pion.y + 100))
orient=orientbas

orient2 = ((joueur2.pion.x, joueur2.pion.y + 100), (joueur2.pion.x + 50, joueur2.pion.y + 150), (joueur2.pion.x + 100, joueur2.pion.y + 100))

chevalier.plateau = plateau
assassin.plateau = plateau
moine.plateau = plateau
guerrier.plateau = plateau


lis_effets = []
#
# if joueur1.main.cartes == []:
#     joueur1.pioche(6)
#
# if joueur2.main.cartes ==[]:
#     joueur2.pioche(6)



#quadrillage

def show_grid():
    for i in range (6,col+6):
        for j in range(1,li+1):
            rect = p.Rect(i*size,j*size,size,size)
            p.draw.rect(screen, p.Color("black"), rect, width=1)


#interface

joueur1_choisi = False
joueur2_choisi = False

while game_on:

    timer.tick(60)
    if not joueur1_choisi :
        L_roles = [p.Rect(200, 200, 150, 210), p.Rect(1000, 200, 150, 210), p.Rect(200, 500, 150, 210), p.Rect(1000, 500, 150, 210)]
        for event in p.event.get():

            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:

                if event.button == 1:
                    print(joueur1.nb_actions)
                    X = p.mouse.get_pos()
                    L = []
                    position = 0
                    if L_roles[0].collidepoint(X):
                        lis_joueurs = [chevalier]
                        print("chevalier")
                        joueur1 = chevalier
                        chevalier.pion = pion1
                    elif L_roles[1].collidepoint(X):
                        print("moine")
                        lis_joueurs = [moine]
                        moine.pion = pion1
                        joueur1 = moine
                    elif L_roles[2].collidepoint(X):
                        print("guerrier")
                        lis_joueurs = [guerrier]
                        guerrier.pion = pion1
                        joueur1 = guerrier
                    elif L_roles[3].collidepoint(X):
                        print("assassin")
                        lis_joueurs = [assassin]
                        joueur1 = assassin
                        assassin.pion = pion1
                    print(lis_joueurs)
                    joueur1_choisi = (len(lis_joueurs) == 1)
                    possibles = actions_possibles(joueur1, pile)
        screen.blit(acc, (0,0))
        screen.blit(chevalier_role.dessiner(), (200, 200))
        screen.blit(moine_role.dessiner(), (1150, 200))
        screen.blit(guerrier_role.dessiner(), (200, 500))
        screen.blit(assassin_role.dessiner(), (1150, 500))
    elif not joueur2_choisi :
        L_roles = [p.Rect(200, 200, 150, 210), p.Rect(1000, 200, 150, 210), p.Rect(200, 500, 150, 210), p.Rect(1000, 500, 150, 210)]
        for event in p.event.get():
            if event.type == p.QUIT:
                p.quit()
                sys.exit()
            if event.type == p.MOUSEBUTTONDOWN:
                if event.button == 1:
                    print(joueur1.nb_actions)
                    X = p.mouse.get_pos()
                    L = []
                    position = 0
                    if L_roles[0].collidepoint(X) and lis_joueurs[0] != chevalier:
                        lis_joueurs.append(chevalier)
                        joueur2 = chevalier
                        chevalier.pion = pion2
                    elif L_roles[1].collidepoint(X) and lis_joueurs != [moine]:
                        lis_joueurs.append(moine)
                        joueur2 = moine
                        moine.pion = pion2
                    elif L_roles[2].collidepoint(X) and lis_joueurs != [guerrier]:
                        lis_joueurs.append(guerrier)
                        joueur2 = guerrier
                        guerrier.pion = pion2
                    elif L_roles[3].collidepoint(X) and lis_joueurs != [assassin]:
                        lis_joueurs.append(assassin)
                        joueur2 = assassin
                        assassin.pion = pion2
                    joueur2_choisi = len(lis_joueurs) == 2
                    print(lis_joueurs)
                    if joueur2_choisi :
                        effet_vide = effet("rien", "rien", "n'a pas d'effet")
                        effet_parade = effet("rien", "rien", "met fin à l'échange")
                        effet_balayage = modificateur([guerrier.droit_orientation], "carte_jouee", "Orientez-vous. Votre prochaine carte joué perd 1 de vitesse",[attaque, action], 0, 0, -1)
                        effet_poignard = effet([autre_joueur(assassin).saigner], "rien", "l'adversaire gagne une carte saignement")
                        effet_avancee = effet([moine.droit_deplacement], "rien", "vous vous déplacez d'une case")
                        effet_sauvage = effet([assassin.droit_deplacement, assassin.droit_deplacement], "rien", "vous vous déplacez de deux cases")
                        effet_abandon = effet([autre_joueur(moine).saigner], "rien","l'adversaire gagne une carte saignement")
                        effet_tourbillon = effet([assassin.droit_orientation], "rien", "vous vous orientez")
                        effet_embrocher = effet([autre_joueur(chevalier).saigner, autre_joueur(chevalier).saigner], "rien","l'adversaire gagne deux cartes saignement")
                        effet_elan = modificateur("rien", "carte_jouee","Votre prochaine attaque inflige 2 dégâts supplémentaires et sa vitesse augmente de 2",[attaque], 2, 0, 2)
                        effet_foi = effet([chevalier.soin, chevalier.soin, chevalier.soin, chevalier.soin, chevalier.soin, chevalier.pioche], "rien", "Vous gangez 5 PV. Piochez une carte")
                        effet_berserker = modificateur([guerrier.pioche], "fin_tour", "jusqu'à la fin du tour, vos cartes attaque infligent 2 dégâts supplémentaires et leur vitesse augmente de 1. Piochez une carte",  [attaque], 2, 0, 1)
                        effet_egorgement = effet([autre_joueur(assassin).saigner, autre_joueur(assassin).saigner], "rien", "l'adversaire gagne deux cartes saignement")
                        effet_transe = modificateur([moine.pioche], "fin_tour", "jusqu'à la fin du tour, vos attaques infligent 2 dégâts supplémentaires. Piochez une carte", [attaque], 2, 0, 0)
                        effet_destructrice = effet( [autre_joueur(moine).degats, autre_joueur(moine).degats, autre_joueur(moine).degats], "rien","met fin à l'échange. L'adversaire subit 3 dégâts")
                        effet_eclair = effet([chevalier.orientation], "rien", "orientez-vous")

                        Revers_devastateur = attaque("Revers devastateur", 2, 6, 1, ["devant", "gauche", "droite"], effet_vide, guerrier, rev)
                        Frappe_veloce = attaque("Frappe véloce", 4, 2, 1, ["devant", "gauche", "droite"], effet_vide, guerrier, vel)
                        Parade_guer = action("Parade", 4, effet_parade, guerrier, par_guer)
                        Balayage = attaque("Balayage", 4, 4, 1, ["devant", "gauche", "droite"], effet_balayage, guerrier, bal)
                        Dans_ta_face = attaque("Dans ta face", 5, 1, 1, ["devant", "gauche", "droite"], effet_vide,guerrier, face)
                        Berserker = action("Berserker", 5, effet_berserker, guerrier, bers)
                        Executer = attaque("Executer", 1, 8, 1, ["devant"], effet_vide, guerrier, exec)
                        Parade_assa = action("Parade", 4, effet_parade, assassin, par_assa)
                        Coup_de_poignard_leger = attaque("Coup de poignard léger", 4, 1, 1, ["devant", "gauche", "droite"], effet_poignard, assassin, poign)
                        Charge_sauvage = action("Charge sauvage", 4, effet_sauvage, assassin, sauva)
                        Frappe_verticale = attaque("Frappe verticaale", 2, 5, 1, ["devant"], effet_vide, assassin, verti)
                        Tourbillon_de_lames = attaque("Tourbillon de lames", 4, 2, 1, ["devant", "gauche", "droite", "derrière"], effet_tourbillon, assassin, tourbi)
                        Egorgement = attaque("Egorgement", 1, 5, 1, ["devant", "gauche", "droite"], effet_egorgement, assassin, egor)
                        Frappe_d_estoc = attaque("Frappe d'estoc", 2, 4, 2, ["devant", "gauche", "droite"], effet_vide, chevalier, estoc)
                        Parade_chev = action("Parade", 4, effet_parade, chevalier, par_chev)
                        Embrocher = attaque("Embrocher", 2, 5, 1, ["devant"], effet_embrocher, chevalier, embro)
                        Prendre_son_elan = action("Prendre son élan", 3, effet_elan, chevalier, elan)
                        Foi_renouvelee = action("Foi renouvelée", 4, effet_foi, chevalier, foi)
                        Frappe_eclair = attaque("Frappe éclair", 4, 4, 1, ["gauche", "droite", "derrière"], effet_eclair, chevalier, eclair)
                        High_kick = attaque("High Kick", 3, 4, 1, ["devant", "gauche", "droite"], effet_vide, moine, high)
                        Uppercut = attaque("Uppercut", 4, 6, 0, ["devant", "gauche", "droite"], effet_vide, moine, upp)
                        Frappe_du_poing = attaque("Frappe du poing", 4, 2, 1, ["devant", "gauche", "droite"], effet_vide, moine, poing)
                        Parade_moin = action("Parade", 4, effet_parade, moine, par_moin)
                        Avancee_fulgurante = action("Avancée fulgurante", 5, effet_avancee, moine, avan)
                        Abandon_du_fair_play = attaque("Abandon du fair-play", 3, 3, 1, ["devant", "gauche", "droite"], effet_abandon, moine, aban)
                        Transe_du_combattant = action("Transe du combattant", 4, effet_transe, moine, trans)
                        Parade_destructrice = action("Parade destructrice", 5, effet_destructrice, moine, destru)

                        deck_guer.cartes = 3 * [Revers_devastateur] + 4 * [Frappe_veloce] + 4 * [Parade_guer] + 3 * [Balayage] + 3 * [Dans_ta_face] + 2 * [Berserker] + 1 * [Executer]
                        deck_assa.cartes = 4 * [Parade_assa] + 4 * [Coup_de_poignard_leger] + 2 * [Charge_sauvage] + 3 * [Frappe_verticale] + 2 * [Tourbillon_de_lames] + 3 * [Egorgement]
                        deck_chev.cartes = 3 * [Frappe_d_estoc] + 4 * [Parade_chev] + 3 * [Embrocher] + 3 * [Prendre_son_elan] + 2 * [Foi_renouvelee] + 3 * [Frappe_eclair]
                        deck_moin.cartes = 3 * [High_kick] + 2 * [Uppercut] + 3 * [Frappe_du_poing] + 3 * [Parade_moin] + 2 * [Parade_destructrice] + 2 * [Avancee_fulgurante] + 3 * [Abandon_du_fair_play] + 2 * [Transe_du_combattant]

                        deck_guer.melanger()
                        deck_assa.melanger()
                        deck_chev.melanger()
                        deck_moin.melanger()
        # screen.blit(acc, (0, 0))
        screen.blit(chevalier_role.dessiner(), (200, 200))
        screen.blit(moine_role.dessiner(), (1150, 200))
        screen.blit(guerrier_role.dessiner(), (200, 500))
        screen.blit(assassin_role.dessiner(), (1150, 500))
        joueur2.ia = True
    else :
        for event in p.event.get():

            if event.type == p.QUIT:
                p.quit()
                sys.exit()

            if event.type == p.MOUSEBUTTONDOWN:

                if event.button == 1:
                    print("nb_actions",joueur1.nb_actions)
                    X = p.mouse.get_pos()
                    L = []
                    position = 0

                    #jouer une carte:

                    for k in range(len(joueur1.main.cartes)):
                        L.append(p.Rect(180 + position, 550, 150, 210))
                        position += 200
                    for k in range(len(L)):
                        Rectplace = L[k]
                        if Rectplace.collidepoint(X) and joueur1.nb_actions == 1:
                            carte = joueur1.main.cartes[k]
                            if carte in possibles:
                                joueur1.main.jouer(carte,pile)
                                joueur1.nb_actions = 0
                                print(pile, "main",joueur1.main)

                    #se défausser de ses cartes et en piocher des nouvelles:

                    if defa.collidepoint(X) and joueur1.nb_actions == 1:
                        pile.append(se_defausser(joueur1,joueur2, se_def))

                        joueur1.nb_actions = 0

                    #un joueur finit son tour:

                    if tour.collidepoint(X):
                        couleur2 = (255, 255, 255)
                        couleur1 = (255, 255, 255)
                        couleur3 = (255, 255, 255)
                        couleur4 = (255, 255, 255)
                        stock_joueur=joueur1
                        joueur1=joueur2
                        joueur2=stock_joueur

                        joueur1.nb_actions = 1
                        possibles = actions_possibles(joueur1, pile)
                        print("vitesse de la pile",pile.vitesse)
                        print("actions possibles", possibles)
                        print(joueur1.main.cartes)

                    #dépiler lorsque plus aucun joueur ne souhaite interrompre:

                    if dep.collidepoint(X):
                        pile.depiler(joueur1,joueur2,plateau)
                        pile.vitesse = 0
                        joueur1.nb_actions = 1

                    #afficher les directions possibles:

                    rectpion = p.Rect(joueur1.pion.x, joueur1.pion.y, 100, 100)

                    if rectpion.collidepoint(X):
                        x1 = joueur1.pion.x-600
                        y1 = joueur1.pion.y-100

                        if 0<x1<200 and 0<y1<300:
                            couleur1 = (100,100,100)
                            couleur4 = (100,100,100)
                            couleur3 = (100,100,100)
                            couleur2 = (100,100,100)
                        elif x1>=200 and 0<y1<300:
                            couleur4 = (100,100,100)
                            couleur1 = (255,255,255)
                            couleur3 = (100,100,100)
                            couleur2 = (100,100,100)
                        elif x1<=0 and 0<y1<300:
                            couleur1 = (100,100,100)
                            couleur4 = (255,255,255)
                            couleur3 = (100,100,100)
                            couleur2 = (100,100,100)
                        elif x1>=200 and y1>=300:
                            couleur3 = (100,100,100)
                            couleur4 = (100,100,100)
                            couleur1 = (255,255,255)
                            couleur2 = (255,255,255)
                        elif x1<=0 and y1<=0:
                            couleur3 = (255,255,255)
                            couleur4 = (255,255,255)
                            couleur1 = (100,100,100)
                            couleur2 = (100,100,100)
                        elif x1>=200 and y1<=0:
                            couleur3 = (255,255,255)
                            couleur4 = (100,100,100)
                            couleur1 = (255,255,255)
                            couleur2 = (100,100,100)
                        elif x1<=0 and y1>=200:
                            couleur3 = (100,100,100)
                            couleur4 = (255,255,255)
                            couleur1 = (100,100,100)
                            couleur2 = (255,255,255)
                        elif y1>=200 and 0<x1<200:
                            couleur3 = (100,100,100)
                            couleur1 = (100,100,100)
                            couleur4 = (100,100,100)
                            couleur2 = (255,255,255)
                        elif y1<=0 and 0<x1<200:
                            couleur2 = (100,100,100)
                            couleur1 = (100,100,100)
                            couleur3 = (255,255,255)
                            couleur4 = (100,100,100)

                    #déplacer son pion:

                    rectgauche = p.Rect(joueur1.pion.x - 100, joueur1.pion.y, 100, 100)
                    rectdroite = p.Rect(joueur1.pion.x + 100, joueur1.pion.y, 100, 100)
                    rectbas = p.Rect(joueur1.pion.x, joueur1.pion.y + 100, 100, 100)
                    recthaut = p.Rect(joueur1.pion.x, joueur1.pion.y - 100, 100, 100)


                    if "deplacement" in possibles:

                        if rectgauche.collidepoint(X) and joueur1.nb_actions==1 and joueur1.pion.deplacement_possible(-100,0,plateau) and joueur1.peut_deplacer==0:

                            couleur2 = (255, 255, 255)
                            couleur1 = (255, 255, 255)
                            couleur3 = (255, 255, 255)
                            couleur4 = (255, 255, 255)
                            joueur1.futur_deplacement = "gauche"
                            joueur1.futur_deplacementx = -100
                            joueur1.futur_deplacementy = 0
                            joueur1.nb_actions = 0
                            pile.append(deplacement(joueur1, depl))
                            pile.vitesse=1

                        elif rectdroite.collidepoint(X) and joueur1.nb_actions==1 and joueur1.pion.deplacement_possible(100,0,plateau) and joueur1.peut_deplacer==0:

                            couleur2 = (255, 255, 255)
                            couleur1 = (255, 255, 255)
                            couleur3 = (255, 255, 255)
                            couleur4 = (255, 255, 255)
                            joueur1.futur_deplacement = "droite"
                            joueur1.futur_deplacementx = 100
                            joueur1.futur_deplacementy = 0
                            joueur1.nb_actions = 0
                            pile.append(deplacement(joueur1, depl))
                            pile.vitesse = 1


                        elif recthaut.collidepoint(X) and joueur1.nb_actions==1 and joueur1.pion.deplacement_possible(0,-100,plateau) and joueur1.peut_deplacer==0:

                            couleur2 = (255, 255, 255)
                            couleur1 = (255, 255, 255)
                            couleur3 = (255, 255, 255)
                            couleur4 = (255, 255, 255)
                            joueur1.futur_deplacement = "haut"
                            joueur1.futur_deplacementx = 0
                            joueur1.futur_deplacementy = -100
                            joueur1.nb_actions = 0
                            pile.append(deplacement(joueur1, depl))
                            pile.vitesse = 1

                        elif rectbas.collidepoint(X)and joueur1.nb_actions==1 and joueur1.pion.deplacement_possible(0,100,plateau) and joueur1.peut_deplacer==0:

                            couleur2 = (255, 255, 255)
                            couleur1 = (255, 255, 255)
                            couleur3 = (255, 255, 255)
                            couleur4 = (255, 255, 255)
                            joueur1.futur_deplacement = "bas"
                            joueur1.futur_deplacementx = 0
                            joueur1.futur_deplacementy = 100
                            joueur1.nb_actions = 0
                            pile.append(deplacement(joueur1, depl))
                            pile.vitesse = 1

                    #si carte permet de déplacer

                    if joueur1.peut_deplacer==1 and rectgauche.collidepoint(X) and joueur1.pion.deplacement_possible(-100,0,plateau):
                        joueur1.pion.deplacer(-100,0,plateau, joueur1)
                        joueur1.peut_deplacer = 0
                    elif joueur1.peut_deplacer==1 and rectdroite.collidepoint(X) and joueur1.pion.deplacement_possible(100,0,plateau):
                        joueur1.pion.deplacer(100,0,plateau, joueur1)
                        joueur1.peut_deplacer = 0
                    elif joueur1.peut_deplacer==1 and recthaut.collidepoint(X) and joueur1.pion.deplacement_possible(0,-100,plateau):
                        joueur1.pion.deplacer(0,-100,plateau, joueur1)
                        joueur1.peut_deplacer = 0
                    elif joueur1.peut_deplacer==1 and rectbas.collidepoint(X) and joueur1.pion.deplacement_possible(0,100,plateau):
                        joueur1.pion.deplacer(0,100,plateau, joueur1)
                        joueur1.peut_deplacer = 0

                    #conserver l'orientation lors de déplacements:

                    orientdroite = ((joueur1.pion.x + 100, joueur1.pion.y), (joueur1.pion.x + 150, joueur1.pion.y + 50), (joueur1.pion.x + 100, joueur1.pion.y + 100))
                    orientgauche = ((joueur1.pion.x, joueur1.pion.y), (joueur1.pion.x - 50, joueur1.pion.y + 50), (joueur1.pion.x, joueur1.pion.y + 100))
                    orienthaut = ((joueur1.pion.x, joueur1.pion.y), (joueur1.pion.x + 50, joueur1.pion.y - 50), (joueur1.pion.x + 100, joueur1.pion.y))
                    orientbas = ((joueur1.pion.x, joueur1.pion.y + 100), (joueur1.pion.x + 50, joueur1.pion.y + 150), (joueur1.pion.x + 100, joueur1.pion.y + 100))


            if event.type == p.KEYDOWN :
                print(joueur1.nb_actions)

                #s'orienter:

                if "orientation" in possibles:

                    if event.key==p.K_UP and joueur1.nb_actions==1 and joueur1.peut_orienter==0:
                        joueur1.future_orientation = "nord"
                        pile.append(orientation(joueur1, ori))
                        pile.vitesse = 3
                        joueur1.nb_actions = 0
                    elif event.key==p.K_DOWN and joueur1.nb_actions==1 and joueur1.peut_orienter==0:
                        joueur1.future_orientation = "sud"
                        pile.append(orientation(joueur1, ori))
                        pile.vitesse = 3
                        joueur1.nb_actions = 0
                    elif event.key==p.K_LEFT and joueur1.nb_actions==1 and joueur1.peut_orienter==0:
                        joueur1.future_orientation = "ouest"
                        pile.append(orientation(joueur1, ori))
                        pile.vitesse = 3
                        joueur1.nb_actions = 0
                    elif event.key==p.K_RIGHT and joueur1.nb_actions==1 and joueur1.peut_orienter==0:
                        joueur1.future_orientation = "est"
                        pile.append(orientation(joueur1, ori))
                        pile.vitesse = 3
                        joueur1.nb_actions = 0

                #carte permet d'orienter:

                elif event.key==p.K_UP and joueur1.peut_orienter==1:
                    joueur1.pion.orienter("nord")
                    joueur1.peut_orienter = 0
                if event.key==p.K_DOWN and joueur1.peut_orienter==1:
                    joueur1.pion.orienter("sud")
                    joueur1.peut_orienter = 0
                if event.key==p.K_LEFT and joueur1.peut_orienter==1:
                    joueur1.pion.orienter("ouest")
                    joueur1.peut_orienter = 0
                if event.key==p.K_RIGHT and joueur1.peut_orienter==1:
                    joueur1.pion.orienter("est")
                    joueur1.peut_orienter = 0


        #plateau
        screen.fill(p.Color("white"))
        my_surface.fill(p.Color("white"))

        possibles = actions_possibles(joueur1, pile)

        if joueur1.pion.x==joueur2.pion.x  and joueur1.pion.y==joueur2.pion.y:
            my_surface.blit(deuxfish, (joueur1.pion.x -600, joueur1.pion.y -100))
        else:
            my_surface.blit(joueur1.pion.dessiner(), (joueur1.pion.x-600, joueur1.pion.y-100))
            my_surface.blit(joueur2.pion.dessiner(), (joueur2.pion.x-600,joueur2.pion.y -100))
        screen.blit(my_surface, (600, 100))
        show_grid()


        p.draw.circle(screen, couleur1, (joueur1.pion.x +150, joueur1.pion.y + 50), 30) #droite
        p.draw.circle(screen, couleur2, (joueur1.pion.x + 50, joueur1.pion.y + 150), 30) #bas

        p.draw.circle(screen, couleur3, (joueur1.pion.x +50, joueur1.pion.y - 50), 30) #haut
        p.draw.circle(screen, couleur4, (joueur1.pion.x - 50, joueur1.pion.y + 50), 30)   #gauche


        #orientation joueur 1

        orientdroite = ((joueur1.pion.x + 100, joueur1.pion.y), (joueur1.pion.x + 150, joueur1.pion.y + 50), (joueur1.pion.x + 100, joueur1.pion.y + 100))
        orientgauche = ((joueur1.pion.x, joueur1.pion.y), (joueur1.pion.x - 50, joueur1.pion.y + 50), (joueur1.pion.x, joueur1.pion.y + 100))
        orienthaut = ((joueur1.pion.x, joueur1.pion.y), (joueur1.pion.x + 50, joueur1.pion.y - 50), (joueur1.pion.x + 100, joueur1.pion.y))
        orientbas = ((joueur1.pion.x, joueur1.pion.y + 100), (joueur1.pion.x + 50, joueur1.pion.y + 150), (joueur1.pion.x + 100, joueur1.pion.y + 100))

        if joueur1.pion.orientation=="nord":
            orient = orienthaut
        elif joueur1.pion.orientation=="sud":
            orient = orientbas
        elif joueur1.pion.orientation=="est":
            orient = orientdroite
        elif joueur1.pion.orientation=="ouest":
            orient = orientgauche

        p.draw.polygon(screen, (150,150,150), orient)


        #orientation joueur 2


        orientdroite2 = ((joueur2.pion.x + 100, joueur2.pion.y), (joueur2.pion.x + 150, joueur2.pion.y + 50), (joueur2.pion.x + 100, joueur2.pion.y + 100))
        orientgauche2 = ((joueur2.pion.x, joueur2.pion.y), (joueur2.pion.x - 50, joueur2.pion.y + 50), (joueur2.pion.x, joueur2.pion.y + 100))
        orienthaut2 = ((joueur2.pion.x, joueur2.pion.y), (joueur2.pion.x + 50, joueur2.pion.y - 50), (joueur2.pion.x + 100, joueur2.pion.y))
        orientbas2 = ((joueur2.pion.x, joueur2.pion.y + 100), (joueur2.pion.x + 50, joueur2.pion.y + 150), (joueur2.pion.x + 100, joueur2.pion.y + 100))

        if joueur2.pion.orientation=="nord":
            orient2 = orienthaut2
        elif joueur2.pion.orientation=="sud":
            orient2 = orientbas2
        elif joueur2.pion.orientation=="est":
            orient2 = orientdroite2
        elif joueur2.pion.orientation=="ouest":
            orient2 = orientgauche2

        p.draw.polygon(screen, (100,200,200), orient2)

        # action future: orientation

        if joueur1.future_orientation == "nord":
            p.draw.polygon(screen, (100, 50, 100), orienthaut)
        elif joueur1.future_orientation == "sud":
            p.draw.polygon(screen, (100, 50, 100), orientbas)
        elif joueur1.future_orientation == "est":
            p.draw.polygon(screen, (100, 50, 100), orientdroite)
        elif joueur1.future_orientation == "ouest":
            p.draw.polygon(screen, (100, 50, 100), orientgauche)

        if joueur2.future_orientation == "nord":
            p.draw.polygon(screen, (100, 50, 100), orienthaut2)
        elif joueur2.future_orientation == "sud":
            p.draw.polygon(screen, (100, 50, 100), orientbas2)
        elif joueur2.future_orientation == "est":
            p.draw.polygon(screen, (100, 50, 100), orientdroite2)
        elif joueur2.future_orientation == "ouest":
            p.draw.polygon(screen, (100, 50, 100), orientgauche2)

        #action future: déplacement

        if joueur1.futur_deplacement=="droite":
            p.draw.circle(screen, (100,50,100), (joueur1.pion.x +150, joueur1.pion.y + 50), 50)
        elif joueur1.futur_deplacement=="gauche":
            p.draw.circle(screen, (100,50,100), (joueur1.pion.x - 50, joueur1.pion.y + 50), 50)
        elif joueur1.futur_deplacement=="haut":
            p.draw.circle(screen, (100,50,100), (joueur1.pion.x +50, joueur1.pion.y - 50), 50)
        elif joueur1.futur_deplacement=="bas":
            p.draw.circle(screen, (100,50,100), (joueur1.pion.x + 50, joueur1.pion.y + 150), 50)

        if joueur2.futur_deplacement=="droite":
            p.draw.circle(screen, (100,50,100), (joueur2.pion.x +150, joueur2.pion.y + 50), 50)
        elif joueur2.futur_deplacement=="gauche":
            p.draw.circle(screen, (100,50,100), (joueur2.pion.x - 50, joueur2.pion.y + 50), 50)
        elif joueur2.futur_deplacement=="haut":
            p.draw.circle(screen, (100,50,100), (joueur2.pion.x +50, joueur2.pion.y - 50), 50)
        elif joueur2.futur_deplacement=="bas":
            p.draw.circle(screen, (100,50,100), (joueur2.pion.x + 50, joueur2.pion.y + 150), 50)

        # IA
        if joueur1.ia == True:
            choix(joueur1, joueur2, possibles, pile)

        #cartes initiales

        for carte in joueur1.main.cartes:
            screen.blit(carte.dessiner(), (180 + posi,550))
            posi += 200
        posi=0

        #pile
        for carte in pile:
            if carte.joueur == joueur1 :
                screen.blit(carte.dessiner(), (1175 - 5, 300 + posi))
            else :
                screen.blit(carte.dessiner(), (1175 + 5, 300 + posi))
            posi += 25
        posi = 0

        #pv

        textepv = police.render(str(joueur1.pv), True, "black")
        screen.blit(pv_im, (300, 90))
        screen.blit(textepv, (380,100))

        #orientation et déplacement possibles

        texteor = police.render("Orientations : " + str(joueur1.peut_orienter), True, "black")
        screen.blit(texteor, (300, 180))

        textedepi = police.render("Déplacements : " + str(joueur1.peut_deplacer), True, "black")
        screen.blit(textedepi, (300, 220))

        #carte de rôle

        for carte in L_role:
            if carte.joueur==joueur1:
                screen.blit(carte.dessiner(), (130,90))

        #cartes d'état

        textesaig = police.render( "Saignements : " + str(joueur1.saignement), True, "black")
        screen.blit(textesaig, (300, 140))

        #bouton défausse

        p.draw.rect(screen, (0,0,0), defa,width=1)
        screen.blit(textedef, (1190,100))

        if joueur1.main.cartes ==[] and joueur2.main.cartes == []:
            joueur1.pioche(6)
            joueur2.pioche(6)

        #bouton fin du tour
        p.draw.rect(screen, (0, 0, 0), tour, width=1)
        screen.blit(textetour, (1190, 165))

        #bouton dépiler
        p.draw.rect(screen, (0, 0, 0), dep, width=1)
        screen.blit(textedep, (1220, 230))

        #mort d'un joueur
        if joueur1.pv <= 0:
            game_on = False
            game_over = True
            gagnant = joueur2
        elif joueur2.pv <= 0:
            game_on = False
            game_over = True
            gagnant  = joueur1

    p.display.update()

while game_over:
    for event in p.event.get():
        if event.type == p.QUIT:
            game_over = 0

    screen.blit(conf, (0,0))
    textefin = policewin.render("Le joueur " + str(gagnant.nom) + " a gagné !" , True, "black")
    textefin_rect = textefin.get_rect(center=(1535 / 2, 830 / 2))
    screen.blit(textefin, textefin_rect)
    p.display.flip()