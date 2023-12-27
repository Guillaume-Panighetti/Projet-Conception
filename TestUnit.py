import unittest
import _tkinter
import pytest
from jeu import *

class TestPartie(unittest.TestCase):

    def test_jouer_carte(self):
        # Initialisation
        joueurs = [Joueurs(1, "Joueur 1"), Joueurs(2, "Joueur 2")]
        fenetre = None
        mode = "strict"
        partie = Partie(mode, fenetre)

        # Cas 1 : Joueur joue une carte
        carte = Cartes("1", (0, 0), fenetre)
        partie.jouer(carte)
        self.assertEqual(partie.joueur_actuel, 2)

        # Cas 2 : Joueur joue une carte café
        carte = Cartes("cafe", (0, 0), fenetre)
        partie.jouer(carte)
        self.assertEqual(partie.joueur_actuel, 1)

    def test_fin_tour(self):
        # Initialisation
        joueurs = [Joueurs(1, "Joueur 1"), Joueurs(2, "Joueur 2")]
        fenetre = None
        mode = "strict"
        partie = Partie(mode, fenetre)

        # Cas 1 : Cartes choisies identiques
        cartes = [Cartes("1", (0, 0), fenetre), Cartes("1", (0, 0), fenetre)]
        partie.cartes_choisies = cartes
        partie.fin_tour()
        self.assertEqual(partie.tache_actuelle, 2)

        # Cas 2 : Cartes choisies différentes
        cartes = [Cartes("1", (0, 0), fenetre), Cartes("2", (0, 0), fenetre)]
        partie.cartes_choisies = cartes
        partie.fin_tour()
        self.assertEqual(partie.rejouer_tour, True)

    def test_enregistrer_resultats(self):
        # Initialisation
        joueurs = [Joueurs(1, "Joueur 1"), Joueurs(2, "Joueur 2")]
        fenetre = None
        mode = "strict"
        partie = Partie(mode, fenetre)

        # Cas 1 : Enregistrement des résultats
        cartes = [Cartes("1", (0, 0), fenetre), Cartes("1", (0, 0), fenetre)]
        partie.cartes_choisies = cartes
        partie.fin_tour()
        partie.enregistrer_resultats()

        # Vérification des résultats enregistrés
        with open("backlog.json", "r") as fichier_json:
            backlog = json.load(fichier_json)

        self.assertEqual(backlog[0]["tache"], 1)
        self.assertEqual(backlog[0]["titre"], "Tâche 1")
        self.assertEqual(backlog[0]["description"], "Description de la tâche 1")
        self.assertEqual(backlog[0]["difficulte"], 1)

if __name__ == "__main__":
    unittest.main()
