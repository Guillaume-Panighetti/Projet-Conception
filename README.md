# Projet de Planning Poker

## Installation

Tout d'abord, il faut avoir ces librairies python installées :

    - pygame
    - tkinter
    - json
    - textwrap
    - statistics
    - collections

Il faut ensuite installé le fichier du projet dans un dossier local.

## Exécution

Pour exécuter le projet, il faut ouvrir un terminal, se placer dans le dossier du projet puis exécuter le fichier main avec python en écrivant "python ./main.py"

## Déroulement

Un paquet contient 12 cartes :
- 10 cartes valeurs (0,1,2,3,5,8,13,20,40,100)
- 1 carte interrogation
- 1 carte café (qui est là pour demander une pause pendant la partie).
Chaque joueur possède 1 paquet de cartes.
On donne un cas d’utilisation au joueur, le but du jeu est de déterminer une difficulté pour ce cas d’utilisation. Les joueurs doivent argumentés pour parvenir à un consensus sur la valeur à attribuer.
On écrit des cas d'utilisations au début du jeu.

Tour de jeu :
- on présente le cas d’utilisation
- les joueurs débattent
- à la fin des débats, les joueurs votent un à un en prenant une carte. Les joueurs doivent voter avec une carte représentant, selon eux, la valeur de difficulté du cas d’utilisation. Une carte avec une valeur élevée représente une difficulté élevée et inversement.
- Si le joueur n’a aucune idée de la difficulté du cas d’utilisation, il peut jouer la carte interrogation.
- Dans le mode de jeu strict : Si toutes les cartes sont identiques alors le cas d'utilisation est achevé et on passe au suivant, sinon on débat une nouvelle fois jusqu'à avoir une valeur identique.
- Dans le mode de jeu moyenne : Le jeu calcule la moyenne de toutes les valeurs et passent à la suivantes (l'interrogation ne compte pas).
- Une fois tous les cas d'utilisations achevés, la partie se finit et créer un fichier json avec tous les cas ainsi que leur difficulté (stricte ou en moyenne).

 ## Doc

La doc faite avec Doxygen est accessible via le fichier index.html situé dans le dossier "Doc".
