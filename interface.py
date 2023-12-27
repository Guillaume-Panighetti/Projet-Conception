import os
import pygame
import textwrap

pygame.init()
pygame.font.init()

class Fenetre:
    """
    @class Fenetre
    @brief Fenêtre graphique.

    @param largeur (int) La largeur de la fenêtre.
    @param hauteur (int) La hauteur de la fenêtre.
    @param fenetre (pygame.Surface) La surface de la fenêtre.
    """

    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur
        self.fenetre = pygame.display.set_mode((self.largeur, self.hauteur))

        chemin_script = os.path.dirname(__file__)


    def set_titre(self, titre):
        """
        @brief Définit le titre de la fenêtre.

        @param titre (str): Le titre de la fenêtre.
        """
        pygame.display.set_caption(titre)

    def set_couleur_fond(self, couleur):
        """
        @brief Définit la couleur de fond de la fenêtre.

        @param couleur (tuple): Un tuple représentant la couleur au format RGB.
        """
        self.fenetre.fill(couleur)

    def afficher(self):

        pygame.display.flip()

    def fermer(self):
 
        pygame.display.quit()

class Rectangle:
    """
    @class Rectangle 
    
    @brief représente un rectangle qui sert à cacher certains texte (pas le plus optimal).

    @param x (int): La coordonnée x du coin supérieur gauche du rectangle.
    @param y (int): La coordonnée y du coin supérieur gauche du rectangle.
    @param largeur (int): La largeur du rectangle.
    @param hauteur (int): La hauteur du rectangle.
    @param couleur_fond (tuple): La couleur de fond du rectangle au format RGB.
    @param couleur_bord (tuple): La couleur du bord du rectangle au format RGB.
    @param fenetre (pygame.Surface): La surface sur laquelle le rectangle sera dessiné.
    """

    def __init__(self, x, y, largeur, hauteur, couleur_fond, couleur_bord, fenetre):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.couleur_fond = couleur_fond
        self.couleur_bord = couleur_bord
        self.fenetre = fenetre

    def dessiner(self):
        """
        @brief Dessine le rectangle sur la surface spécifiée.
        """
        pygame.draw.rect(self.fenetre, self.couleur_fond, (self.x, self.y, self.largeur, self.hauteur), border_radius=20)
        pygame.draw.rect(self.fenetre, self.couleur_bord, (self.x, self.y, self.largeur, self.hauteur), width=2, border_radius=20)

class Bouton:
    """
    @class Bouton
    @brief représente un bouton dans une interface graphique.

    @param x (int): La coordonnée x du coin supérieur gauche du bouton.
    @param y (int): La coordonnée y du coin supérieur gauche du bouton.
    @param largeur (int): La largeur du bouton.
    @param hauteur (int): La hauteur du bouton.
    @param texte (str): Le texte affiché sur le bouton.
    @param taille_police (int): La taille de la police du texte.
    @param couleur_texte (tuple): La couleur du texte (format RGB).
    @param couleur_bouton (tuple): La couleur du bouton (format RGB).
    @param fenetre (pygame.Surface): La surface de la fenêtre sur laquelle le bouton est dessiné.
    """

    def __init__(self, x, y, largeur, hauteur, texte, taille_police, couleur_texte, couleur_bouton, fenetre):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.texte = texte
        self.taille_police = taille_police
        self.couleur_texte = couleur_texte
        self.couleur_bouton = couleur_bouton
        self.fenetre = fenetre

    def dessiner(self):
        """
        Dessine le bouton sur la fenêtre.
        """
        rayon = self.hauteur / 2
        pygame.draw.ellipse(self.fenetre, self.couleur_bouton, (self.x, self.y, 2*rayon, 2*rayon))
        pygame.draw.ellipse(self.fenetre, self.couleur_bouton, (self.x + self.largeur - 2*rayon, self.y, 2*rayon, 2*rayon))
        pygame.draw.ellipse(self.fenetre, self.couleur_bouton, (self.x, self.y + self.hauteur - 2*rayon, 2*rayon, 2*rayon))
        pygame.draw.ellipse(self.fenetre, self.couleur_bouton, (self.x + self.largeur - 2*rayon, self.y + self.hauteur - 2*rayon, 2*rayon, 2*rayon))
        pygame.draw.rect(self.fenetre, self.couleur_bouton, (self.x, self.y + rayon, self.largeur, self.hauteur - 2*rayon))
        pygame.draw.rect(self.fenetre, self.couleur_bouton, (self.x + rayon, self.y, self.largeur - 2*rayon, self.hauteur))

        police = pygame.font.Font(None, self.taille_police)
        texte = police.render(self.texte, True, self.couleur_texte)
        self.fenetre.blit(texte, (self.x + (self.largeur - texte.get_width()) / 2, self.y + (self.hauteur - texte.get_height()) / 2))

    def est_survole(self, souris_x, souris_y):
        """
        @brief Vérifie si le bouton est survolé par la souris.

        @param souris_x (int): La coordonnée x de la position de la souris.
        @param souris_y (int): La coordonnée y de la position de la souris.

        @return bool: True si le bouton est survolé, False sinon.
        """
        if self.x <= souris_x <= self.x + self.largeur and self.y <= souris_y <= self.y + self.hauteur:
            return True
        else:
            return False

    def est_clique(self, x, y):
        """
        @brief Vérifie si le bouton est cliqué.

        @param x (int): La coordonnée x du clic.
        @param y (int): La coordonnée y du clic.

        @return bool: True si le bouton est cliqué, False sinon.
        """
        return self.x <= x <= self.x + self.largeur and self.y <= y <= self.y + self.hauteur
    
class BoiteTexte:
    """
    @class BoiteTexte
    @brief une boîte de texte.

    @param x (int): La position horizontale de la boîte de texte.
    @param y (int): La position verticale de la boîte de texte.
    @param texte (str): Le texte contenu dans la boîte de texte.
    @param taille_police (int): La taille de la police du texte.
    @param couleur (tuple): La couleur du texte.
    @param texte_centre (bool): Indique si le texte est centré horizontalement.
    @param longueur_ligne (int): La longueur maximale d'une ligne de texte.
    @param fenetre (pygame.Surface): La surface de la fenêtre où la boîte de texte est affichée.
    """

    def __init__(self, x, y, texte, taille_police, couleur, texte_centre, longueur_ligne, fenetre):
        self.x = x
        self.y = y
        self.texte = texte
        self.taille_police = taille_police
        self.police = pygame.font.Font(None, self.taille_police)
        self.texte_surface = self.police.render(texte, True, couleur)
        self.couleur = couleur
        self.texte_centre = texte_centre
        self.longueur_ligne = longueur_ligne
        self.derniere_taille = (0, 0)
        self.fenetre = fenetre

    def dessiner(self):
        """
        @brief Méthode pour dessiner une boîte de texte.
        """
        # Dessiner un rectangle blanc sur l'ancienne boîte de texte
        if self.derniere_taille != (0, 0):
            pygame.draw.rect(self.fenetre, (255, 255, 255), (self.x, self.y, self.derniere_taille[0], self.derniere_taille[1]))

        lines = self.texte.split('\n')
        for line in lines:
            self.wrapped_lines = textwrap.wrap(line, self.longueur_ligne)
            for self.wrapped_line in self.wrapped_lines:
                texte_surface = self.police.render(self.wrapped_line, True, self.couleur)
                if self.texte_centre:
                    self.x_centre = self.x - texte_surface.get_width() / 2
                else:
                    self.x_centre = self.x
                pygame.draw.rect(self.fenetre, (255, 255, 255), (self.x_centre, self.y, self.police.size(self.wrapped_line)[0], self.police.size(self.wrapped_line)[1]))
                self.fenetre.blit(texte_surface, (self.x_centre, self.y))
                self.y += self.police.get_height()

        # Mémoriser la taille et la position de la boîte de texte
        self.derniere_taille = self.get_taille()

    def get_taille(self):
        """
        @brief Méthode pour obtenir la taille de la boîte de texte.

        @return tuple: La taille de la boîte de texte (largeur, hauteur).
        """
        return self.texte_surface.get_size()

    def set_texte(self, texte):
        """
        @brief Méthode pour définir le texte d'une boîte de texte.

        @param texte (str): Le nouveau texte à définir.
        """
        self.texte = texte
        self.dessiner()

    def reset_texte(self):
        """
        @brief Méthode pour réinitialiser le texte d'une boîte de texte.
        """
        self.texte = ""
        self.dessiner()
    
class BoiteSaisie:
    """
    @class BoiteSaisie
    @brief boîte de saisie.

    @param x (int): La coordonnée x de la boîte de saisie.
    @param y (int): La coordonnée y de la boîte de saisie.
    @param largeur (int): La largeur de la boîte de saisie.
    @param hauteur (int): La hauteur de la boîte de saisie.
    @param taille_police (int): La taille de la police du texte.
    @param couleur (tuple): La couleur de la boîte de saisie au format RGB.
    @param max_caracteres (int): Le nombre maximum de caractères autorisés dans la boîte de saisie.
    @param longueur_ligne (int): La longueur maximale d'une ligne de texte dans la boîte de saisie.
    @param fenetre (pygame.Surface): La surface de la fenêtre sur laquelle la boîte de saisie est dessinée.
    @param texte (str): Le texte saisi dans la boîte de saisie.
    """

    def __init__(self, x, y, largeur, hauteur, taille_police, couleur, max_caracteres, longueur_ligne, fenetre):
        self.x = x
        self.y = y
        self.largeur = largeur
        self.hauteur = hauteur
        self.rect = pygame.Rect(x, y, largeur, hauteur)
        self.couleur = couleur
        self.police = pygame.font.Font(None, taille_police)
        self.texte = ""
        self.max_caracteres = max_caracteres
        self.longueur_ligne = longueur_ligne
        self.fenetre = fenetre

    def dessiner(self):
        """
        @brief Dessine la boîte de saisie sur la fenêtre.
        """
        pygame.draw.rect(self.fenetre, self.couleur, (self.x, self.y, self.largeur, self.hauteur), 2, border_radius=20)
        pygame.draw.rect(self.fenetre, (255, 255, 255), (self.x + 10, self.y + 5, self.largeur - 20, self.hauteur - 10))

        lines = textwrap.wrap(self.texte, self.longueur_ligne)
        y = self.y + 5
        for line in lines:
            texte_surface = self.police.render(line, True, (0, 0, 0))
            self.fenetre.blit(texte_surface, (self.x + 10, y))
            y += self.police.get_height()

    def evenement(self, event):
        """
        @brief Gère les événements liés à la boîte de saisie.

        @param event (pygame.event.Event): L'événement à gérer.
        """
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.texte = self.texte[:-1]
            else:
                if len(self.texte) < self.max_caracteres:
                    self.texte += event.unicode
        self.dessiner()

    def est_survole(self, souris_x, souris_y):
        """
        @brief Vérifie si la boîte de saisie est survolée par la souris.

        @param souris_x (int): La coordonnée x de la souris.
        @paramsouris_y (int): La coordonnée y de la souris.

        @return bool: True si la boîte de saisie est survolée, False sinon.
        """
        if self.x <= souris_x <= self.x + self.largeur and self.y <= souris_y <= self.y + self.hauteur:
            return True
        else:
            return False

    def est_clique(self, x, y):
        """
        @brief Vérifie si la boîte de saisie est cliquée.

        @param x (int): La coordonnée x du clic.
        @param y (int): La coordonnée y du clic.

        @return bool: True si la boîte de saisie est cliquée, False sinon.
        """
        return self.x <= x <= self.x + self.largeur and self.y <= y <= self.y + self.hauteur

    def get_texte(self):
        """
        @brief Récupère le texte saisi dans la boîte de saisie.

        @return str: Le texte saisi dans la boîte de saisie.
        """
        return self.texte

    def reset_texte(self):
        """
        @brief Réinitialise le texte de la boîte de saisie.
        """
        self.texte = ""
        self.dessiner()