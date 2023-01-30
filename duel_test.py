

import unittest
from paquets import *
from Carte import *
from pile import *
import pygame as p
from plateau import *
from joueur import *


class test_duel(unittest.TestCase):

    def setUp(self):
        self.main_guer = main()
        self.deck_guer = deck([])
        fish = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/fish.png")
        self.pion1 = pion([0, 1], "sud", fish)
        self.defausse_guer = defausse()
        self.effet_vide = effet("rien", "rien", "n'a pas d'effet")
        self.guerrier = joueur(40, self.effet_vide, "guerrier", self.main_guer, self.deck_guer, self.defausse_guer, self.pion1)
        self.rev = p.image.load("D:/projets_pycharm/UE2.4_projet_info/Cartes/Revers_devastateur.png")
        self.Revers_devastateur = attaque("Revers devastateur", 2, 6, 1, ["devant", "gauche", "droite"], self.effet_vide, self.guerrier, self.rev)
        self.effet_balayage = modificateur([self.guerrier.droit_orientation], "carte_jouee", "Orientez-vous. Votre prochaine carte joué perd 1 de vitesse", [attaque, action], 0, 0, -1)

    def test_carte(self):
        self.assertIsInstance(self.Revers_devastateur, carte)
        self.assertNotIsInstance(carte, action)
        self.assertNotIsInstance(carte, attaque)

    def test_pion(self):
        self.assertEqual(self.pion1.x, 0)
        self.assertEqual(self.pion1.y, 1)

    def test_deck(self):
        self.assertIsInstance(self.deck_guer, paquet)
        self.assertEqual(self.deck_guer.taille, 0)
        self.assertEqual(self.defausse_guer.cartes, [])
        self.assertEqual(self.deck_guer.cartes, self.defausse_guer.cartes)
        self.assertIsNot(self.deck_guer.cartes, self.defausse_guer.cartes)
        self.deck_guer.cartes = [self.Revers_devastateur]
        self.assertEqual(len(self.deck_guer.cartes), 1)
        self.guerrier.pioche(1)
        self.assertIn(self.Revers_devastateur, self.guerrier.main.cartes)
        self.assertIs(self.main_guer, self.guerrier.main)

    def test_effet(self):
        self.deck_guer.cartes = [self.Revers_devastateur]
        self.effet_balayage.resoudre(self.guerrier)
        self.assertEqual(self.guerrier.peut_orienter, 1)
        self.assertIn(self.effet_balayage, self.Revers_devastateur.modifiee_par)
        self.assertEqual(self.Revers_devastateur.vitesse, 1)



if __name__ == "__main__":
    unittest.main()