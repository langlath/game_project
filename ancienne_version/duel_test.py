

import unittest
from paquets import paquet, deck, defausse, main
from plateau import plateau, pion
from effet import effet
from carte import carte, attaque, action, etat, personnage
from joueur import joueur

class test_duel(unittest.TestCase):

    def setUp(self):
        self.deck = deck([])
        self.defausse = defausse()
        self.pion = pion([0, 1], "nord")
        self.joueur = joueur(40, "rien")
        self.carte = attaque(2, 6, 1, ["devant"], effet("rien", "rien", True), self.joueur)

    def test_carte(self):
        self.assertIsInstance(self.carte, carte)
        self.assertNotIsInstance(carte, action)
        self.assertNotIsInstance(carte, attaque)

    def test_pion(self):
        self.assertEqual(self.pion.abscisse, 0)
        self.assertEqual(self.pion.ordonnee, 1)

    def test_deck(self):
        self.assertIsInstance(self.deck, paquet)
        self.assertEqual(self.deck.taille, 0)
        self.assertEqual(self.defausse.cartes, [])
        self.assertEqual(self.deck.cartes, self.defausse.cartes)
        self.assertIsNot(self.deck.cartes, self.defausse.cartes)

if __name__ == "__main__":
    unittest.main()