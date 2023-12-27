import os
import pygame
import json
import tkinter as tk
from tkinter import messagebox
from statistics import mean, median
from collections import Counter

class Joueurs:
    """
    @class Joueurs
    @brief Représente un joueur.
    
    @param joueurs (list) Liste de classe pour stocker tous les joueurs.
    @param numero (int) Le numéro du joueur.
    @param nom (str) Le nom du joueur.
    """
    
    joueurs = []

    def __init__(self, numero, nom):
        self.numero = numero
        self.nom = nom


    def __repr__(self):
        return f"   Joueur {self.numero} : {self.nom}"
    
class Taches:
    """
    @class Taches
    @brief représente une tache.

    @param taches (list) Liste de classe pour stocker tous les cas d'utilisation.
    @param numero (int) Le numéro du cas d'utilisation.
    @param titre (str) Le titre du cas d'utilisation.
    @param description (str) La description du cas d'utilisation.
    @param difficulte (int) La difficulté du cas d'utilisation.
    """
    taches = []

    def __init__(self, numero, titre, description, difficulte):
        self.numero = numero
        self.titre = titre
        self.description = description
        self.difficulte = difficulte

    def __repr__(self):
        return f"Cas {self.numero} :\n   Titre : {self.titre}\n   Description : {self.description}\n   Difficulté : {self.difficulte}"

class Cartes:
    """
    @Class Cartes
    @brief représente une carte du jeu.
    
    @param nom_carte (str) Le nom de la carte.
    @param position (tuple) La position de la carte sur la fenêtre.
    @param fenetre (pygame.Surface) La fenêtre d'affichage du jeu.
    @param taille (tuple, optional) La taille de la carte (par défaut None).
    """

    def __init__(self, nom_carte, position, fenetre, taille=None):
        chemin_script = os.path.dirname(__file__)
        self.nom_carte = nom_carte
        chemin_carte = os.path.join(chemin_script, 'ressources', 'cartes', self.nom_carte + '.png')
        self.image = pygame.image.load(chemin_carte)

        if taille is not None:
            self.image = pygame.transform.scale(self.image, taille)

        self.position = position
        self.fenetre = fenetre    

    def afficher(self):
        """
        @brief Affiche l'image de la carte sur la fenêtre.
        """
        self.fenetre.blit(self.image, self.position)
    
    def est_survole(self, souris_x, souris_y):
        """
        @brief Vérifie si la carte est survolée par la souris.

        
        @param souris_x (int) La position en x de la souris.
        @param souris_y (int) La position en y de la souris.

        
        @return bool True si la carte est survolée, False sinon.
        """
        largeur, hauteur = self.image.get_size()
        if self.position[0] <= souris_x <= self.position[0] + largeur and self.position[1] <= souris_y <= self.position[1] + hauteur:
            return True
        return False

    def est_clique(self, x, y):
        """
        @brief Vérifie si la carte est cliquée.

        @param x (int) La position en x du clic.
        @param y (int) La position en y du clic.

        @return bool True si la carte est cliquée, False sinon.
        """
        largeur, hauteur = self.image.get_size()
        return self.position[0] <= x <= self.position[0] + largeur and self.position[1] <= y <= self.position[1] + hauteur

class CartesFactory:
    @staticmethod
    def creer_carte(nom_carte, position, fenetre, taille=None):
        """
        
        @brief Factory Method pour créer une instance de la classe Cartes. 
        """
        chemin_script = os.path.dirname(__file__)
        chemin_carte = os.path.join(chemin_script, 'ressources', 'cartes', nom_carte + '.png')
        image = pygame.image.load(chemin_carte)

        if taille is not None:
            image = pygame.transform.scale(image, taille)

        return Cartes(nom_carte, position, fenetre, image)
    
class PartieObserver:
    def mettre_en_pause(self):
        """
        @brief Met la partie en pause lorsque tous les joueurs ont choisi la carte café.
        """
        print("[INFO] : Tous les joueurs ont choisi la carte café. La partie est mise en pause et enregistrée.")
        messagebox.showinfo("Infos", "Tous les joueurs ont choisi la carte café. La partie est finie")


class Partie:
    """
    @class Partie 
    @brief représente la partie, le mode de jeu.

    @param self.mode Le mode de jeu.
    @param joueur_actuel Le nombre de joueur en train de jouer.
    @param cartes_choisies les cartes choisies dans un tableau.
    @param log_cartes_choisies les cartes qui sont choisies
    @param tache_actuelle le nombre de taches.
    """
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self, mode, fenetre):
        self.mode = mode
        self.joueur_actuel = 0
        self.cartes_choisies = []
        self.log_cartes_choisies = []
        self.tache_actuelle = 1
        self.fenetre = fenetre
        self.observer = PartieObserver()

    def jouer(self, carte):
        """
        @brief Fonction qui permet de jouer une carte.
        
        @param carte (Cartes): La carte à jouer.
        """
        if self.tache_actuelle <= len(Taches.taches):
            if self.joueur_actuel < len(Joueurs.joueurs) - 1:
                print(f"[EVENT] : Carte '{carte.nom_carte}' cliquée") 
                if carte.nom_carte != "interro" and carte.nom_carte != "cafe":
                    self.cartes_choisies.append(carte)
                self.log_cartes_choisies.append(carte)
                self.joueur_actuel += 1
                self.fenetre.affichage_joueur(Joueurs.joueurs[self.joueur_actuel])
            elif self.joueur_actuel == len(Joueurs.joueurs) - 1:
                print(f"[EVENT] : Carte '{carte.nom_carte}' cliquée")
                if carte.nom_carte != "interro" and carte.nom_carte != "cafe":
                    self.cartes_choisies.append(carte)
                self.log_cartes_choisies.append(carte)
                self.joueur_actuel += 1
                if all(carte.nom_carte == "cafe" for carte in self.log_cartes_choisies):
                        self.observer.mettre_en_pause()
                        self.enregistrer_resultats()
                        
                else:
                    self.fin_tour()
        elif self.tache_actuelle > len(Taches.taches):
            print("[INFO] : Tous les cas ont été traités!") 
            messagebox.showinfo("Infos", "Tous les cas ont été traités, la partie est terminée.")


    def fin_tour(self):
        """
        @brief Fonction qui détermine l'issue du tour en fonction du mode de jeu.
        """
        if self.mode == "strict":
            if not len(set(self.cartes_choisies)) <= 1:
                print("Toutes les cartes choisies ne sont pas identiques !")
                messagebox.showinfo("Attention", "Les cartes choisies doivent être identiques")
                self.rejouer_tour()
            else:
                print("[INFO] : Toutes les cartes choisies sont identiques !")
                messagebox.showinfo("Infos", "Toutes les cartes choisies sont identiques !")
                strict = mean([int(carte.nom_carte) for carte in self.cartes_choisies])
                Taches.taches[self.tache_actuelle - 1].difficulte = strict
                self.tache_suivante()
        elif self.mode == "moyenne":
            moyenne = mean([int(carte.nom_carte) for carte in self.cartes_choisies])
            print(f"[INFO] : La moyenne de difficulté est de {moyenne}")
            fmoyenne = f"La moyenne de difficulté est de {moyenne}"
            messagebox.showinfo("Infos", fmoyenne)
            Taches.taches[self.tache_actuelle - 1].difficulte = moyenne
            self.tache_suivante()

        if self.tache_actuelle > len(Taches.taches):
            self.enregistrer_resultats()

    def enregistrer_resultats(self):
        """
        @brief Fonction qui enregistre les résultats de la partie dans un fichier JSON.
        """
        resultats = []
        for tache in Taches.taches:
            resultat_tache = {
                "tache": tache.numero,
                "titre": tache.titre,
                "description": tache.description,
                "difficulte": tache.difficulte
            }
            resultats.append(resultat_tache)

        # Spécifiez le chemin pour sauvegarder le fichier JSON
        chemin_script = os.path.dirname(__file__)
        chemin_json = os.path.join(chemin_script, 'resultats_partie.json')

        # Écriture des données JSON dans le fichier
        with open(chemin_json, 'w') as fichier_json:
            json.dump(resultats, fichier_json, indent=2)

        print("[INFO] : Résultats de la partie enregistrés dans 'resultats_partie.json'")
        messagebox.showinfo("Infos", "Résultats de la partie enregistrés dans 'resultats_partie.json'")

        

    def rejouer_tour(self):
        """
        @brief Fonction qui permet de rejouer le tour.
        """
        print("[INFO] : Le tour doit être rejoué !") 
        self.joueur_actuel = 0
        self.cartes_choisies = []
        self.fenetre.affichage_joueur(Joueurs.joueurs[self.joueur_actuel])
    
    def tache_suivante(self):
        """
        @brief Fonction qui permet de passer au cas suivant.
        """
        print(f"[INFO] : Résultat du cas d'utilisation :\n", Taches.taches[self.tache_actuelle - 1])
        self.tache_actuelle += 1
        self.joueur_actuel = 0
        self.cartes_choisies = []
        if self.tache_actuelle <= len(Taches.taches):
            print(f"[INFO] : Cas suivant à traiter :\n", Taches.taches[self.tache_actuelle - 1])
            self.fenetre.affichage_tache(Taches.taches[self.tache_actuelle - 1])
            self.fenetre.affichage_joueur(Joueurs.joueurs[self.joueur_actuel])

