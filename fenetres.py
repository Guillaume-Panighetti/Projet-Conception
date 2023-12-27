import os
import pygame
from interface import Fenetre, Rectangle, Bouton, BoiteTexte, BoiteSaisie
from jeu import Cartes

class FntAccueil(Fenetre, Bouton):
    """
    @class FntAccueil
    @brief fenêtre d'accueil du jeu.

    """

    def __init__(self):
        # Paramètres de la fenêtre du menu
        fnt_accueil_l = 450
        fnt_accueil_h = 500
        super().__init__(fnt_accueil_l, fnt_accueil_h)
        self.set_titre("Menu")
        self.set_couleur_fond((255, 255, 255))
        btn_l = 200
        btn_h = 40
        # Mettre bouton au milieu
        btn_x = (fnt_accueil_l - btn_l) / 2
        btn_espacement = 75
        btn_taille_police = 25
        btn_couleur_texte = (255, 255, 255)
        btn_couleur = (0, 0, 0)
        # Texte
        bt_pp = BoiteTexte(fnt_accueil_l / 2, 100, "Planning Poker", 50, (0, 0, 0), True, 100, self.fenetre)
        bt_pp.dessiner()
        bt_mode_jeu = BoiteTexte(fnt_accueil_l / 2, 200, "Choississez un mode de jeu :", 30, (0, 0, 0), True, 100, self.fenetre)
        bt_mode_jeu.dessiner()

        # Création du bouton "Mode strict"
        btn_strict_y = 250
        self.btn_strict = Bouton(btn_x, btn_strict_y, btn_l, btn_h,  "Strict", btn_taille_police, btn_couleur_texte, btn_couleur, self.fenetre)
        self.btn_strict.dessiner()

        # Création du bouton "Mode moyenne"
        btn_moyenne_y = btn_strict_y + btn_espacement
        self.btn_moyenne = Bouton(btn_x, btn_moyenne_y, btn_l, btn_h,  "Moyenne", btn_taille_police, btn_couleur_texte, btn_couleur, self.fenetre)
        self.btn_moyenne.dessiner()


    def get_btn_strict(self):
        """
        @brief Renvoie le bouton "Mode strict" de la fenêtre d'accueil.

        
        @return Bouton: Le bouton "Mode strict".
        """
        return self.btn_strict
    
    def get_btn_moyenne(self):
        """
        @brief Renvoie le bouton "Mode moyenne" de la fenêtre d'accueil.

        
        @return Bouton: Le bouton "Mode moyenne".
        """
        return self.btn_moyenne
    
    
    def afficher(self):
        super().afficher()
    
    def fermer(self):
        super().fermer()

class FntConfigJoueurs(Fenetre, Bouton, BoiteTexte, BoiteSaisie):
    """
    @class FntConfigJoueurs 
    @brief fenêtre de configuration des joueurs.

    Cette classe hérite des classes Fenetre, Bouton, BoiteTexte et BoiteSaisie.
    
    @param fnt_config_joueurs_l (int): Largeur de la fenêtre.
    @param fnt_config_joueurs_h (int): Hauteur de la fenêtre.
    @param bs_joueurs (list): Liste des boîtes de saisie des noms de joueurs.
    @param bt_joueurs (list): Liste des étiquettes des noms de joueurs.
    @param bt_couleur (tuple): Couleur du texte des étiquettes.
    @param bs_couleur (tuple): Couleur du texte des boîtes de saisie.
    @param bt_taille_police (int): Taille de la police des étiquettes.
    @param bs_taille_police (int): Taille de la police des boîtes de saisie.
    @param bs_joueur_l (int): Largeur des boîtes de saisie des noms de joueurs.
    @param bs_joueur_h (int): Hauteur des boîtes de saisie des noms de joueurs.
    @param bs_joueur_x (float): Position en x des boîtes de saisie des noms de joueurs.
    @param bs_joueur_y (int): Position en y des boîtes de saisie des noms de joueurs.
    @param bs_joueur_max_caracteres (int): Nombre maximum de caractères dans les boîtes de saisie des noms de joueurs.
    @param btn_joueur_l (int): Largeur des boutons "Ajouter un joueur" et "Supprimer un joueur".
    @param btn_joueur_h (int): Hauteur des boutons "Ajouter un joueur" et "Supprimer un joueur".
    @param btn_ajouter_joueur_x (float): Position en x du bouton "Ajouter un joueur".
    @param btn_supprimer_joueur_x (float): Position en x du bouton "Supprimer un joueur".
    @param btn_joueur_y (int): Position en y des boutons "Ajouter un joueur" et "Supprimer un joueur".
    @param btn_valider (Bouton): Bouton "Valider".
    @param btn_retour (Bouton): Bouton "Retour".
    """

    def __init__(self):
        # Paramètres de la fenêtre
        self.fnt_config_joueurs_l = 450
        self.fnt_config_joueurs_h = 500
        super().__init__(self.fnt_config_joueurs_l, self.fnt_config_joueurs_h)
        self.set_titre("Configuration des joueurs")
        self.set_couleur_fond((255, 255, 255))
        self.bs_joueurs = []
        self.bt_joueurs = []
        self.bt_couleur = (0, 0, 220)
        self.bs_couleur = (0, 0, 0)
        self.bt_taille_police = 25
        self.bs_taille_police = 30

        # Création des boîtes de saisie des noms de joueurs
        self.bs_joueur_l = 300
        self.bs_joueur_h = 30
        self.bs_joueur_x = (self.fnt_config_joueurs_l - self.bs_joueur_l) / 2
        self.bs_joueur_y = 50
        self.bs_joueur_max_caracteres = 15
        self.bs_joueurs = [BoiteSaisie(self.bs_joueur_x, self.bs_joueur_y, self.bs_joueur_l, self.bs_joueur_h, self.bs_taille_police, self.bs_couleur, self.bs_joueur_max_caracteres, 15, self.fenetre)]

        # Création d'un texte au-dessus de la boîte de saisie des noms de joueurs
        self.bt_joueur = BoiteTexte(self.bs_joueur_x + 10, self.bs_joueur_y - 20, "J1", self.bt_taille_police, self.bt_couleur, False, 17, self.fenetre)
        self.bt_joueur.dessiner()

        # Création du bouton "Ajouter un joueur" et "Supprimer un joueur"
        self.btn_joueur_l = 170
        self.btn_joueur_h = 30
        self.btn_ajouter_joueur_x = self.fnt_config_joueurs_l * 1.2 / 4 - self.btn_joueur_l / 2
        self.btn_supprimer_joueur_x = self.fnt_config_joueurs_l * 2.8 / 4 - self.btn_joueur_l / 2
        self.btn_joueur_y = 150

        # Création du bouton "Valider"
        btn_valider_l = 100
        btn_valider_h = 40
        btn_valider_x = (self.fnt_config_joueurs_l - btn_valider_l) / 2
        btn_valider_y = self.fnt_config_joueurs_h - 50
        self.btn_valider = Bouton(btn_valider_x, btn_valider_y, btn_valider_l, btn_valider_h, "Valider", 25, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_valider.dessiner()

        # Création du bouton "Retour"
        btn_retour_l = 70
        btn_retour_h = 30
        btn_retour_x = 10
        btn_retour_y = 10
        self.btn_retour = Bouton(btn_retour_x, btn_retour_y, btn_retour_l, btn_retour_h, "Menu", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_retour.dessiner()

        # Création de la boîte de saisie 2
        self.ajouter_bs_joueur()
    
    def ajouter_bs_joueur(self):
        """
        @brief Ajoute un champ de saisie pour un nouveau joueur.

        """
        # Créer une nouvelle boîte de saisie en dessous de la dernière
        derniere_bs_joueur = self.bs_joueurs[-1]
        nouvelle_bs_joueur = BoiteSaisie(derniere_bs_joueur.x, derniere_bs_joueur.y + 60, self.bs_joueur_l, self.bs_joueur_h, self.bs_taille_police, self.bs_couleur, self.bs_joueur_max_caracteres, 15, self.fenetre)
        self.bs_joueurs.append(nouvelle_bs_joueur)

        # Création de la nouvelle étiquette
        nouvelle_bt_joueur = BoiteTexte(self.bs_joueur_x + 10, derniere_bs_joueur.y + 40, f"J{len(self.bs_joueurs)}", self.bt_taille_police, self.bt_couleur, False, 17, self.fenetre)
        self.bt_joueurs.append(nouvelle_bt_joueur)

        # Faire descendre les boutons "Ajouter un joueur" et "Supprimer un joueur" de 60 pixels
        ancien_y = self.btn_joueur_y
        self.btn_joueur_y += 60

        # Effacer l'ancien bouton en dessinant un rectangle de la couleur de fond sur son ancienne position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_ajouter_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))

        # Effacer l'ancien bouton en dessinant un rectangle de la couleur de fond sur son ancienne position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_supprimer_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))

        nouvelle_bt_joueur.dessiner()

        # Redessiner toutes les boîtes de saisie
        for bs_joueur in self.bs_joueurs:
            bs_joueur.dessiner()

        # Redessiner le bouton "Ajouter un joueur"
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Ajouter un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_ajouter_joueur.dessiner()

        # Redessiner le bouton "Supprimer un joueur"
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Supprimer un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_supprimer_joueur.dessiner()

        # Mettre à jour l'affichage
        pygame.display.flip()

    def supprimer_bs_joueur(self):
        """
        @brief Supprime la dernière boîte de saisie et son étiquette correspondante.

        """
        # Supprimer la dernière boîte de saisie
        derniere_bs_joueur = self.bs_joueurs.pop()

        # Supprimer la dernière étiquette
        derniere_bt_joueur = self.bt_joueurs.pop()

        # Faire monter le bouton "Ajouter un joueur" et "Supprimer un joueur" de 60 pixels
        ancien_y = self.btn_joueur_y
        self.btn_joueur_y -= 60

        # Effacer l'ancienne boîte de saisie en dessinant un rectangle de la couleur de fond sur sa position
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(derniere_bs_joueur.x, derniere_bs_joueur.y, self.bs_joueur_l, self.bs_joueur_h))

        # Effacer l'ancienne étiquette en dessinant un rectangle de la couleur de fond sur sa position
        bt_joueur_largeur, bt_joueur_hauteur = derniere_bt_joueur.get_taille()
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(derniere_bt_joueur.x, derniere_bt_joueur.y - 17, bt_joueur_largeur, bt_joueur_hauteur))

        # Effacer l'ancien bouton en dessinant un rectangle de la couleur de fond sur son ancienne position (pas le plus optimal)
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_ajouter_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))

        # Effacer l'ancien bouton en dessinant un rectangle de la couleur de fond sur son ancienne position (pas le plus optimal)
        pygame.draw.rect(self.fenetre, (255, 255, 255), pygame.Rect(self.btn_supprimer_joueur_x, ancien_y, self.btn_joueur_l, self.btn_joueur_h))

        # Redessiner le bouton "Ajouter un joueur"
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Ajouter un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_ajouter_joueur.dessiner()

        # Redessiner le bouton "Supprimer un joueur"
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Supprimer un joueur", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_supprimer_joueur.dessiner()

        # Mettre à jour l'affichage
        pygame.display.flip()

    
    def get_btn_ajouter_joueur(self):
        """

        @return Bouton: Bouton "Ajouter un joueur".
        """
        return self.btn_ajouter_joueur
    
    def get_btn_supprimer_joueur(self):
        """

        Renvoie:
            Bouton: Bouton "Supprimer un joueur".
        """
        return self.btn_supprimer_joueur
    
    def get_bs_joueurs(self):
        """
        @return list: Liste des boîtes de saisie des noms de joueurs.
        """
        return self.bs_joueurs
    
    def desactiver_btn_supprimer_joueur(self):
        """
        @brief Désactive le bouton "Supprimer un joueur".

        """
        self.btn_supprimer_joueur = Bouton(self.btn_supprimer_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Supprimer un joueur", 20, (255, 255, 255), (125, 125, 125), self.fenetre)
        self.btn_supprimer_joueur.dessiner()

    def desactiver_btn_ajouter_joueur(self):
        """
        @brief Désactive le bouton "Ajouter un joueur".

        """
        self.btn_ajouter_joueur = Bouton(self.btn_ajouter_joueur_x, self.btn_joueur_y, self.btn_joueur_l, self.btn_joueur_h, "Ajouter un joueur", 20, (255, 255, 255), (125, 125, 125), self.fenetre)
        self.btn_ajouter_joueur.dessiner() 
    
    def get_btn_retour(self):
        """ 
        @return Bouton: Bouton "Retour".
        
        """
        return self.btn_retour
    
    def get_btn_valider(self):
        """
        @return Bouton: Bouton "Valider".
        """
        return self.btn_valider
    
    def afficher_msg_erreur(self, message):
        """
        @brief Affiche un message d'erreur.

        @param message (str): Message d'erreur à afficher.
        """
        bt_msg_erreur = BoiteTexte(self.fnt_config_joueurs_l / 2, self.get_btn_valider().y - 25, message, 20, (150, 0, 0), True, 51, self.fenetre)
        bt_msg_erreur.dessiner()

    def afficher(self):

        super().afficher()

    def fermer(self):

        super().fermer()

class FntConfigTaches(Fenetre, Bouton, BoiteTexte, BoiteSaisie):
    """
    @class FntConfigTaches
    @brief fenêtre de configuration des cas d'utilisations.

    Cette fenêtre permet de configurer les différents cas d'utilisations du planning poker.
    Elle contient des boîtes de saisie pour le titre et la description de chaque cas,
    ainsi que des boutons pour enregistrer, valider et retourner à la fenêtre précédente.
    """

    def __init__(self):
        # Paramètres généraux de la fenêtre
        self.fnt_config_taches_l = 450
        self.fnt_config_taches_h = 500
        super().__init__(self.fnt_config_taches_l, self.fnt_config_taches_h)
        self.set_titre("Configuration des cas d'utilisations")
        self.set_couleur_fond((255, 255, 255))
        self.bt_couleur = (0, 0, 0)
        bs_couleur = (0, 0, 0)
        self.bt_taille_police = 25
        bs_taille_police = 25

        # Création de la boite de saisie du titre du cas d'utilisation
        bs_titre_l = 350
        bs_titre_h = 30
        self.bs_titre_x = (self.fnt_config_taches_l - bs_titre_l) / 2
        self.bs_titre_y = 100
        bs_titre_max_caracteres = 20
        self.bs_titre = BoiteSaisie(self.bs_titre_x, self.bs_titre_y, bs_titre_l, bs_titre_h, bs_taille_police, bs_couleur, bs_titre_max_caracteres, 20, self.fenetre)
        self.bs_titre.dessiner()

        # Création d'un texte au-dessus de la boîte de saisie du titre
        self.bt_titre = BoiteTexte(self.bs_titre_x + 10, self.bs_titre_y - 20, "Cas n°1", self.bt_taille_police, self.bt_couleur, False, 23, self.fenetre)
        self.bt_titre.dessiner()

        # Création de la boite de saisie de la description du cas d'utilisation
        bs_description_l = 350
        bs_description_h = 170
        self.bs_description_x = (self.fnt_config_taches_l - bs_description_l) / 2
        self.bs_description_y = 175
        bs_desription_max_caracteres = 160
        self.bs_description = BoiteSaisie(self.bs_description_x, self.bs_description_y, bs_description_l, bs_description_h, bs_taille_police, bs_couleur, bs_desription_max_caracteres, 20, self.fenetre)
        self.bs_description.dessiner()

        # Création d'un texte au-dessus de la description du cas d'utilisation
        self.bt_description = BoiteTexte(self.bs_description_x + 10, self.bs_description_y - 20, "Description du cas n°1", self.bt_taille_police, self.bt_couleur, False, 29, self.fenetre)
        self.bt_description.dessiner()

        # Création du bouton "Enregistrer"
        btn_enregistrer_l = 170
        btn_enregistrer_h = 40
        btn_enregistrer_x = (self.fnt_config_taches_l - btn_enregistrer_l) / 2
        btn_enregistrer_y = self.fnt_config_taches_h - 140
        self.btn_enregistrer = Bouton(btn_enregistrer_x, btn_enregistrer_y, btn_enregistrer_l, btn_enregistrer_h, "Enregistrer", 25, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_enregistrer.dessiner()

        # Création du bouton "Valider"
        btn_valider_l = 100
        btn_valider_h = 40
        btn_valider_x = (self.fnt_config_taches_l - btn_valider_l) / 2
        btn_valider_y = self.fnt_config_taches_h - 50
        self.btn_valider = Bouton(btn_valider_x, btn_valider_y, btn_valider_l, btn_valider_h, "Valider", 30, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_valider.dessiner()

        # Création du bouton "Retour"
        btn_retour_l = 70
        btn_retour_h = 40
        btn_retour_x = 10
        btn_retour_y = 10
        self.btn_retour = Bouton(btn_retour_x, btn_retour_y, btn_retour_l, btn_retour_h, "Joueurs", 20, (255, 255, 255), (0, 0, 0), self.fenetre)
        self.btn_retour.dessiner()

    def get_bs_titre(self):
        """
        @brief Méthode pour récupérer la boîte de saisie du titre du cas d'utilisation .

        
        @return BoiteSaisie: La boîte de saisie du titre du cas d'utilisation.
        """
        return self.bs_titre
    
    def get_bs_description(self):
        """
        @brief Méthode pour récupérer la boîte de saisie de la description du cas d'utilisation.

        @return BoiteSaisie: La boîte de saisie de la description du cas d'utilisation.
        """
        return self.bs_description

    def get_btn_enregistrer(self):
        """
        @brief Méthode pour récupérer le bouton "Enregistrer".

        @return Bouton: Le bouton "Enregistrer".
        """
        return self.btn_enregistrer

    def get_btn_valider(self):
        """
        @brief Méthode pour récupérer le bouton "Valider".

        @return Bouton: Le bouton "Valider".
        """
        return self.btn_valider
    
    def get_btn_retour(self):
        """
        @brief Méthode pour récupérer le bouton "Retour".

        @return Bouton: Le bouton "Retour".
        """
        return self.btn_retour
    
    def actualiser_bt_titre(self, nb_taches):
        """
        @brief Méthode pour actualiser le texte de la boîte de saisie du titre.

        @param nb_taches (int): Le numéro du cas d'utilisation.
        """
        self.bt_titre.reset_texte()
        self.bt_titre = BoiteTexte(self.bs_titre_x + 10, self.bs_titre_y - 20, f"Cas n°{nb_taches}", self.bt_taille_police, self.bt_couleur, False, 23, self.fenetre)
        self.bt_titre.dessiner()

    def actualiser_bt_description(self, nb_taches):
        """
        Méthode pour actualiser le texte du champ de saisie de la description.

        @param nb_taches (int): Le numéro du cas d'utilisation.
        """
        self.bt_description.reset_texte()
        self.bt_description = BoiteTexte(self.bs_description_x + 10, self.bs_description_y - 20, f"Description", self.bt_taille_police, self.bt_couleur, False, 29, self.fenetre)
        self.bt_description.dessiner()
    
    def reset_bs(self):
        """
        @brief éthode pour réinitialiser les champs de saisie.
        """
        self.bs_titre.reset_texte()
        self.bs_description.reset_texte()
        pygame.display.flip()

    def afficher_msg_erreur(self, message):
        """
        @brief Méthode pour afficher un message d'erreur.

        @param message (str): Le message d'erreur à afficher.
        """
        Rectangle(30, self.get_btn_valider().y - 30, 400, 25, (255, 255, 255), (255, 255, 255), self.fenetre).dessiner()
        bt_msg_erreur = BoiteTexte(self.fnt_config_taches_l / 2, self.get_btn_valider().y - 25, message, 20, (150, 0, 0), True, 60, self.fenetre)
        bt_msg_erreur.dessiner()

    def afficher(self):
 
        super().afficher()

    def fermer(self):

        super().fermer()
        
class FntJeu(Fenetre, Rectangle, Bouton, BoiteTexte, BoiteSaisie, Cartes):
    """
    @class FntJeu
    
    @brief représentant la fenêtre de jeu.
    
    Affiche les différentes cartes du planning poker.
    
    @param ecran (pygame.Surface): L'écran sur lequel s'affiche la fenêtre.
    @param ecran_l (int): Largeur de l'écran.
    @param ecran_h (int): Hauteur de l'écran.
    @param rect_marge (int): Marge entre les rectangles.
    @param rect_l (int): Largeur des rectangles.
    @param rect_h (int): Hauteur des rectangles.
    @param noms_cartes (list): Liste des noms des cartes.
    @param liste_cartes (list): Liste des cartes.
    @param btn_quitter (Bouton): Bouton pour quitter la partie.
    """
    def __init__(self, mode_jeu, tache, joueur):
        # Paramètres de la fenêtre
        super().__init__(0, 0)
        self.ecran = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.ecran_l, self.ecran_h = self.ecran.get_size()
        self.set_titre("Jeu")
        self.set_couleur_fond((255, 255, 255))
        self.mode_jeu = mode_jeu
        

        # Affichage du mode de jeu
        bt_mode_jeu = BoiteTexte(self.ecran_l / 2, self.ecran_h / 10, f"Mode de jeu : {self.mode_jeu}", 30, (0, 0, 0), True, 100, self.ecran)
        bt_mode_jeu.dessiner()

        # Afffichage des éléments de la fenêtre de jeu
        self.affichage_tache(tache)
        self.affichage_joueur(joueur)
        self.plateau_cartes()
        

        # Création du bouton "Quitter la partie"
        btn_quitter_l = 180
        btn_quitter_h = 40
        btn_quitter_x = 20
        btn_quitter_y = 10
        self.btn_quitter = Bouton(btn_quitter_x, btn_quitter_y, btn_quitter_l, btn_quitter_h, "Quitter la partie", 25, (255, 255, 255), (200, 0, 0), self.fenetre)
        self.btn_quitter.dessiner()
    
    
        


    def affichage_tache(self, tache):
        """
        @brief Affiche le cas d'utilisation en cours.
    
        @param tache (Tache): Le cas d'utilisation en cours.
            
        @return Tache: Le cas d'utilisation en cours.
        """
        # Calculer les coordonnées pour l'affichage des cas d'utilisation
        x = self.ecran_l / 2
        y = self.ecran_h / 5

        # Rectangle blanc pour cacher le texte de la tache 1 (pas le plus optimal)
        Rectangle(self.ecran_l / 5 * 1.95, y - 10, 800, 260, (255, 255, 255), (255, 255, 255), self.fenetre).dessiner()

        # Créer une boîte de texte pour le titre
        bt_titre_tache = BoiteTexte(x, y, f"Cas n°{tache.numero} : {tache.titre}", 40, (0, 0, 0), True, 46, self.ecran)

        # Créer une boîte de texte pour la description
        bt_description_tache = BoiteTexte(x, y + 50, f"{tache.description}", 40, (0, 0, 0), True, 30, self.ecran)

        # Dessiner les boîtes de texte
        bt_titre_tache.dessiner()
        bt_description_tache.dessiner()

        # Mettre à jour l'affichage
        pygame.display.flip()

    def affichage_joueur(self, joueur):
        """
        @brief Affiche le joueur en cours.
        
        @param joueur (Joueur): Le joueur en cours.
            
        @return Joueur: Le joueur en cours.
        """
        # Calculer les coordonnées pour l'affichage du joueur
        x = self.ecran_l / 2
        y = self.ecran_h / 2

        # Rectangle blanc pour cacher le texte du joueur 1 (pas le plus optimal)
        Rectangle(self.ecran_l / 5, y - 10, 800, 45, (255, 255, 255), (255, 255, 255), self.fenetre).dessiner()

        # Créer une boîte de texte pour le nom du joueur
        bt_nom_joueur = BoiteTexte(x, y, f"C'est au tour de {joueur.nom} de jouer", 40, (0, 0, 0), True, 46, self.ecran)

        # Dessiner la boîte de texte
        bt_nom_joueur.dessiner()

        # Mettre à jour l'affichage
        pygame.display.flip()

    def plateau_cartes(self):
        """
        @brief Affiche le plateau de cartes.
        
        @return list: Liste des cartes.
        """
        # Définir la taille et l'espacement des cartes
        taille_carte = (self.ecran_l // 11, self.ecran_h // 5)
        espacement = 20
        marge = 20

        # Calculer la position de départ du plateau de cartes
        x_debut = self.ecran_l / 5
        y_debut = self.ecran_h - (2 * taille_carte[1] + espacement) - marge

        self.noms_cartes = ['0', '1', '2', '3', '5', '8', '13', '20', '40', '100', 'interro', 'cafe']

        self.liste_cartes = []
        for i, nom_carte in enumerate(self.noms_cartes):
            x = x_debut + (i % 6) * (taille_carte[0] + espacement)
            y = y_debut + (i // 6) * (taille_carte[1] + espacement)

            carte = Cartes(nom_carte, (x, y), self.fenetre, taille_carte)
            self.liste_cartes.append(carte)
        
        for carte in self.liste_cartes:
            carte.afficher()

        # Mettre à jour l'affichage
        pygame.display.flip()

    def get_cartes(self):
        """
        @brief Renvoie la liste des cartes.

        @return list: Liste des cartes.
        """
        return self.liste_cartes
    
    def get_btn_quitter(self):
        """
       @brief Renvoie le bouton "Quitter la partie".
        
        @return Bouton: Le bouton "Quitter la partie".
        """
        return self.btn_quitter

    def afficher(self):

        super().afficher()

    def fermer(self):

        super().fermer()