# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


from duel_lea import *
from deroulement import *


plateau = plateau(4, 3)
pion1 = pion(0, 0, "sud")
pion2 = pion(2, 3, "nord")


joueur1 = joueur(40, "rien", "Guirlande d'Irlande", main(), deck([]), defausse(), pion1)
joueur2 = joueur(40, "rien", "Mollo l'abricot", main(), deck([]), defausse(), pion2)


