'''
@file main.py
Fichier principal
@author Guillaume Panighetti
@author Arthur Perret
@date 12/2023

'''
import pygame
from interface import BoiteSaisie
from fenetres import FntAccueil, FntConfigJoueurs, FntConfigTaches, FntJeu
from jeu import Joueurs, Taches, Partie

if __name__ == "__main__":

    # Affichage de la fenêtre Accueil
    fnt_accueil = FntAccueil()
    fnt_accueil.afficher()

    # Initialisation des autres fenêtres
    fnt_config_joueurs = None
    fnt_config_taches = None
    fnt_jeu = None

    # Boucle d'événements de l'application
    running = True
    while running:
        # Définition des variables globales
        souris_x, souris_y = pygame.mouse.get_pos() # Récupération des coordonnées de la souris

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # Evénements si la souris est déplacée
            elif event.type == pygame.MOUSEMOTION:

                # Création d'une liste de tous les éléments interactifs (boutons et boîtes de saisie)
                elements = []
                if fnt_accueil is not None:
                    elements.append(fnt_accueil.get_btn_strict())
                    elements.append(fnt_accueil.get_btn_moyenne())
                if fnt_config_joueurs is not None:
                    elements.extend(fnt_config_joueurs.get_bs_joueurs())
                    elements.append(fnt_config_joueurs.get_btn_ajouter_joueur())
                    elements.append(fnt_config_joueurs.get_btn_supprimer_joueur())
                    elements.append(fnt_config_joueurs.get_btn_valider())
                    elements.append(fnt_config_joueurs.get_btn_retour())
                if fnt_config_taches is not None:
                    elements.append(fnt_config_taches.get_bs_titre())
                    elements.append(fnt_config_taches.get_bs_description())
                    elements.append(fnt_config_taches.get_btn_enregistrer())
                    elements.append(fnt_config_taches.get_btn_valider())
                    elements.append(fnt_config_taches.get_btn_retour())
                if fnt_jeu is not None:
                    elements.extend(fnt_jeu.get_cartes())
                    elements.append(fnt_jeu.get_btn_quitter())

                # Vérification si le curseur de la souris est sur un élément interactif
                cursor = pygame.SYSTEM_CURSOR_ARROW  # Initialisation du curseur en mode normal
                for element in elements:
                    if element.est_survole(souris_x, souris_y):
                        if isinstance(element, BoiteSaisie):
                            cursor = pygame.SYSTEM_CURSOR_IBEAM  # Mode texte pour les boîtes de saisie
                        else:
                            cursor = pygame.SYSTEM_CURSOR_HAND  # Mode main pour les boutons
                        break

                # Changement du curseur de la souris
                pygame.mouse.set_cursor(cursor)

            # Evénements si un bouton de la souris est cliqué
            elif event.type == pygame.MOUSEBUTTONDOWN:

                if fnt_accueil is not None:
                    if fnt_accueil.get_btn_strict().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Mode strict' cliqué")
                        fnt_accueil.fermer()
                        fnt_accueil = None
                        fnt_config_joueurs = FntConfigJoueurs()
                        fnt_config_joueurs.afficher()
                        fnt_config_joueurs.desactiver_btn_supprimer_joueur()
                        mode_jeu = "strict"
                        nb_joueurs = 2
                    
                    elif fnt_accueil.get_btn_moyenne().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Mode moyenne' cliqué") 
                        fnt_accueil.fermer()
                        fnt_accueil = None
                        fnt_config_joueurs = FntConfigJoueurs()
                        fnt_config_joueurs.afficher()
                        fnt_config_joueurs.desactiver_btn_supprimer_joueur()
                        mode_jeu = "moyenne"
                        nb_joueurs = 2
                
                elif fnt_config_joueurs is not None:
                    if fnt_config_joueurs.get_btn_ajouter_joueur().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Ajouter un joueur' cliqué") 
                        if nb_joueurs < 4:
                            nb_joueurs += 1
                            print("[UPDATE] : Nombre de joueurs : " + str(nb_joueurs)) 
                            fnt_config_joueurs.ajouter_bs_joueur()
                        elif nb_joueurs == 4:
                            nb_joueurs += 1
                            print("[UDPATE] : Nombre de joueurs : " + str(nb_joueurs))
                            fnt_config_joueurs.ajouter_bs_joueur()
                            fnt_config_joueurs.desactiver_btn_ajouter_joueur()
                        else:
                            print("[WARNING] : Nombre de joueurs maximum atteint")
                    
                    elif fnt_config_joueurs.get_btn_supprimer_joueur().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Supprimer un joueur' cliqué")
                        if nb_joueurs > 3:
                            nb_joueurs -= 1
                            print("[UPDATE] : Nombre de joueurs : " + str(nb_joueurs)) 
                            fnt_config_joueurs.supprimer_bs_joueur()
                        elif nb_joueurs == 3:
                            nb_joueurs -= 1
                            print("[UDPATE] : Nombre de joueurs : " + str(nb_joueurs)) 
                            fnt_config_joueurs.supprimer_bs_joueur()
                            fnt_config_joueurs.desactiver_btn_supprimer_joueur()
                        else:
                            print("[WARNING] : Nombre de joueurs minimum atteint")
                

                    elif fnt_config_joueurs.get_btn_valider().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Valider' cliqué") # [DEBUG]
                        
                        Joueurs.joueurs = []
                        # Parcourir toutes les boîtes de saisie
                        for i, boite_saisie in enumerate(fnt_config_joueurs.get_bs_joueurs()):
                            # Créer un nouveau joueur avec le numéro et le texte de la boîte de saisie comme nom
                            joueur = Joueurs(i+1, boite_saisie.get_texte())

                            # Ajouter le joueur à la liste des joueurs
                            Joueurs.joueurs.append(joueur)

                        # Vérifier si tous les joueurs ont un nom non vide
                        if all(joueur.nom for joueur in Joueurs.joueurs):
                            # Afficher la liste des joueurs 
                            print("[INFO] : Liste des joueurs :")
                            for joueur in Joueurs.joueurs:
                                print(joueur)
                            
                            fnt_config_joueurs.fermer()
                            fnt_config_joueurs = None
                            fnt_config_taches = FntConfigTaches()
                            fnt_config_taches.afficher()
                            Taches.taches = []
                            nb_taches = 0
                        else:
                            print("[WARNING] : Tous les joueurs doivent avoir un nom") 
                            fnt_config_joueurs.afficher_msg_erreur("Tous les joueurs doivent avoir un nom !")
                
                    elif fnt_config_joueurs.get_btn_retour().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Retour' cliqué") 
                        fnt_config_joueurs.fermer()
                        fnt_config_joueurs = None
                        fnt_accueil = FntAccueil()
                        fnt_accueil.afficher()

                elif fnt_config_taches is not None:
                    if fnt_config_taches.get_btn_enregistrer().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Enregistrer cette tache' cliqué") 

                        titre = fnt_config_taches.get_bs_titre().get_texte()
                        description = fnt_config_taches.get_bs_description().get_texte()

                        if titre:  # Vérifier si le titre n'est pas vide
                            if not description:  # Si la description est vide
                                description = " "  # Définir la description par défaut

                            # Enregistrer le cas d'utilisation
                            numero = len(Taches.taches) + 1
                            difficulte = None
                            tache = Taches(numero, titre, description, difficulte)
                            Taches.taches.append(tache)

                            # Incrémenter le nombre de cas
                            nb_taches += 1

                            # Actualisation de l'affichage
                            fnt_config_taches.actualiser_bt_titre(nb_taches+1)
                            fnt_config_taches.actualiser_bt_description(nb_taches+1)
                            fnt_config_taches.reset_bs()
                            print(f"[INFO] : Le cas d'utilisation '{titre}' enregistrée avec succès") 
                            # Afficher la liste des cas d'utilisation 
                            print("[INFO] : Liste des cas d'utilisation :")
                            for tache in Taches.taches:
                                print(tache)
                        else:
                            print("[WARNING] : Le titre du cas d'utilisation ne peut pas être vide") 
                            fnt_config_taches.afficher_msg_erreur("Attention : le titre du cas d'utilisation ne peut pas être vide !")

                    elif fnt_config_taches.get_btn_valider().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Valider' cliqué") 
                        if nb_taches == 0:
                            fnt_config_taches.afficher_msg_erreur("Attention : aucun cas d'utilisation n'a été enregistré !")
                            print("[WARNING] : Aucun cas d'utilisation enregistré") 
                        else:
                            fnt_config_taches.fermer()
                            fnt_config_taches = None
                            joueur_actuel = 0
                            nb_taches_traitees = 0
                            tache_actuelle = Taches.taches[nb_taches_traitees]
                            fnt_jeu = FntJeu(mode_jeu, tache_actuelle, Joueurs.joueurs[joueur_actuel])
                            partie = Partie(mode_jeu, fnt_jeu)
                            fnt_jeu.afficher()
                
                    elif fnt_config_taches.get_btn_retour().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Retour' cliqué") # [DEBUG]
                        fnt_config_taches.fermer()
                        fnt_config_taches = None
                        fnt_config_joueurs = FntConfigJoueurs()
                        fnt_config_joueurs.afficher()
                        nb_joueurs = 2
                        fnt_config_joueurs.desactiver_btn_supprimer_joueur()
                    
                elif fnt_jeu is not None:
                    for carte in fnt_jeu.liste_cartes:
                        if carte.est_clique(souris_x, souris_y):
                            partie.jouer(carte)

                    if fnt_jeu.get_btn_quitter().est_clique(souris_x, souris_y):
                        print("[EVENT] : Bouton 'Quitter la partie' cliqué") 
                        fnt_jeu.fermer()
                        fnt_jeu = None
                        fnt_accueil = FntAccueil()
                        fnt_accueil.afficher()
            
            # Evénements si une touche du clavier est pressée
            elif event.type == pygame.KEYDOWN:

                if fnt_config_joueurs is not None:
                    # Parcourir toutes les boîtes de saisie
                    for i, boite_saisie in enumerate(fnt_config_joueurs.get_bs_joueurs()):
                        if boite_saisie.est_clique(souris_x, souris_y):
                            boite_saisie.evenement(event)
                            print("[UPDATE] Boite de saisie {} : ".format(i+1) + boite_saisie.get_texte()) 
                
                elif fnt_config_taches is not None:
                    if fnt_config_taches.get_bs_titre().est_clique(souris_x, souris_y):
                        fnt_config_taches.get_bs_titre().evenement(event)
                        print("[UPDATE] Boite de saisie 'Titre' : " + fnt_config_taches.get_bs_titre().get_texte()) 
                        
                    elif fnt_config_taches.get_bs_description().est_clique(souris_x, souris_y):
                        fnt_config_taches.get_bs_description().evenement(event)
                        print("[UPDATE] Boite de saisie 'Description' : " + fnt_config_taches.get_bs_description().get_texte()) 

        pygame.display.flip()
    pygame.quit()
