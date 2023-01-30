import pygame as p
import sys
from carte import  attaque
from effet import *
from plateau import *
from paquets import *
from pile import *
p.init()
timer = p.time.Clock()
game_on = True

#deck

blanc = p.Surface((150, 210))
blanc.fill((255, 255, 255))

rev = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/revers_devastateur.png")
high = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/high_kick.png")
upp = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/uppercut.png")
tir = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/tir_d_arbalete.png")
poing = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/frappe_du_poing.png")
vel = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/frappe_veloce.png")
par_guer = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/parade_guerrier.png")
par_assa = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/parade_assassin.png")
par_chev = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/parade_chevalier.png")
par_moin = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/parade_moine.png")
bal = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/balayage.png")
poign = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/coup_de_poignard_leger.png")
avan = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/avancee_fulgurante.png")
sauva = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/charge_sauvage.png")
aban = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/abandon_du_fair_play.png")
face = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/dans_ta_face.png")
verti = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/frappe_verticale.png")
tourbi = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/tourbillon_de_lames.png")
embro = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/embrocher.png")
elan = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/prendre_son_elan.png")
foi = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/foi_renouvelee.png")
bers = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/berserker.png")
egor = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/egorgement.png")
trans = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/transe_du_combattant.png")
destru = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/parade_destructrice.png")
eclair = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/frappe_eclair.png")
estoc = p.image.load("D:/projets_pycharm/UE2.4_projet_info/images/frappe_d_estoc.png")


#joueurs
lis_joueurs = []
def autre_joueur(joueur) :
    for j in lis_joueurs :
        if j != joueur :
            return j

effet_vide = effet("rien", "rien", "n'a pas d'effet")
pion = pion([0, 1], "nord")

main_guer = main()
deck_guer = deck([])
defausse_guer = defausse()
guerrier = joueur(40, effet_vide, "guerrier", main_guer, deck_guer, defausse_guer, pion)

main_assa = main()
deck_assa = deck([])
defausse_assar = defausse()
assassin = joueur(40, effet_vide, "assassin", main_assa, deck_assa, defausse_assar, pion)

main_chev = main()
deck_chev = deck([])
defausse_chev = defausse()
chevalier = joueur(40, effet_vide, "chevalier", main_chev, deck_chev, defausse_chev, pion)

main_moin = main()
deck_moin = deck([])
defausse_moin = defausse()
moine = joueur(40, effet_vide, "moine", main_moin, deck_moin, defausse_moin, pion)


#effets

effet_vide = effet("rien", "rien", "n'a pas d'effet")
effet_parade = effet("rien", "rien", "met fin à l'échange")
effet_balayage = modificateur([guerrier.orientation], "carte_jouee", "Orientez-vous. Votre prochaine carte joué perd 1 de vitesse", [attaque, action], 0, 0, -1)
effet_poignard = effet([autre_joueur(assassin).saigner], "rien", "l'adversaire gagne une carte saignement")
effet_avancee = effet([moine.deplacement], "rien", "vous vous déplacez d'une case")
effet_sauvage = effet([assassin.deplacement, assassin.deplacement], "rien", "vous vous déplacez de deux cases")
effet_abandon = effet([autre_joueur(moine).saigner], "rien", "l'adversaire gagne une carte saignement")
effet_tourbillon = effet([assassin.orientation], "rien", "vous vous orientez")
effet_embrocher = effet([autre_joueur(chevalier).saigner, autre_joueur(chevalier).saigner], "rien", "l'adversaire gagne deux cartes saignement")
effet_elan = modificateur("rien", "carte_jouee", [attaque], 2, 0, 2)
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
Frappe_eclair = attaque("Frappe éclair", 4, 4, 1, ["gauche", "droite", "derrière"], chevalier, eclair)

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



main=main()
lismain = [Revers_devastateur, High_kick, Balayage, Uppercut]
main.cartes = lismain
deck = deck([Frappe_veloce,Frappe_du_poing])
defausse = defausse()
lisdefausse = []
defausse.cartes = lisdefausse
pile = pile()
pion = pion([0, 1], "nord")
joueur = joueur(40, "rien", "Guirlande d'Irlande", main, deck, defausse, pion)


#écran

col=3
li=4
size=100
screen=p.display.set_mode(size=(1535,830))
my_surface=p.Surface((col*size,li*size))

#points de vie

#pv=p.Rect(100,100,150,50)
pv_im=p.image.load("/Users/leavl/Documents/Cours 2020-2021/Duel/Cartes/coeur.png")
pv_im=p.transform.scale(pv_im, (118,41))
pv_im=pv_im.convert()

police = p.font.Font(None,34)
texte = police.render(str(joueur.pv),True,"black")

#Bouton pioche
pioche=p.Rect(1165,85,150,50)
police = p.font.Font(None,34)
textepioche = police.render("Piocher",True,"black")

#image poisson

fish=p.image.load("/Users/leavl/Desktop/fish.png")
fish=p.transform.scale(fish, (100,100))
fish=fish.convert()
fish_rect=fish.get_rect()
x=0
y=0
posi=0

#quadrillage

def show_grid():
    for i in range (6,col+6):
        for j in range(1,li+1):
            rect=p.Rect(i*size,j*size,size,size)
            p.draw.rect(screen, p.Color("black"), rect, width=1)

#interface

while game_on:

    timer.tick(60)

    for event in p.event.get():
        if event.type==p.QUIT:
            p.quit()
            sys.exit()
        if event.type==p.MOUSEBUTTONDOWN:
            print(event.button)
            if event.button==1:
                print("a")
                X=p.mouse.get_pos()
                L=[]
                position=0
                for k in range(len(main.cartes)):
                    L.append(p.Rect(180 + position, 550, 150, 210))
                    position+=200
                for k in range(len(L)):
                    Rectplace=L[k]
                    if Rectplace.collidepoint(X):
                        carte=main.cartes[k]
                        main.jouer(carte,pile)
                if pioche.collidepoint(X):
                    main.cartes.append(deck.cartes[0])
                    deck.cartes.pop(0)
            elif event.button==3:
                X = p.mouse.get_pos()
                L = []
                position = 0
                for k in range(len(main.cartes)):
                    L.append(p.Rect(180 + position, 550, 150, 210))
                    position += 200
                for k in range(len(L)):
                    Rectplace = L[k]
                    if Rectplace.collidepoint(X):
                        main.cartes.pop(k)


    #plateau
    screen.fill(p.Color("white"))
    my_surface.fill(p.Color("white"))
    my_surface.blit(fish, (x, y))
    screen.blit(my_surface, (600, 100))
    show_grid()

    #cartes initiales
    for carte in main.cartes:
        screen.blit(carte.dessiner(), (180 + posi,550))
        posi += 200
    posi=0

    #pile
    for carte in pile:
        screen.blit(carte.dessiner(), (300, 150))

    #pv
    screen.blit(pv_im, (90, 90))
    screen.blit(texte, (180,100))

    #bouton pioche
    p.draw.rect(screen, (0,0,0), pioche,width=1)
    screen.blit(textepioche, (1200,100))

    p.display.update()
