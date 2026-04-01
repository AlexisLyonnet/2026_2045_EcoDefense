# Structure du projet

## Fichiers principaux

- `main.py` : point d'entrée du jeu, contient la boucle principale, 
la gestion des états (accueil, jeu, victoire) et les interactions joueur

- `constante.py` : toutes les valeurs configurables du jeu 
(taille de la grille, argent, vie, cooldowns...)

- `world.py` : gère l'état global de la partie (niveau, vie, monnaie, 
spawn des ennemis)

## Ennemis

- `ennemis.py` : classe Ennemis, gère le déplacement le long des waypoints,
la rotation, le flash rouge au hit et la mort

- `ennemies_data.py` : données des ennemis (vie, vitesse, récompense) 
et composition des vagues par niveau

## Tours

- `tour.py` : classe Tour, gère la détection des ennemis, le tir,
les améliorations et l'affichage de la portée

- `tour_data.py` : données des tours (portée, dégâts, cooldown, 
images) pour chaque type et chaque niveau d'amélioration

## Autres

- `projectile.py` : classe Projectile, gère le déplacement visuel 
du projectile de la tour vers l'ennemi

- `bouton.py` : classe Bouton, gère l'affichage et la détection 
de clic pour tous les boutons du jeu

- `niveau_data.py` : données des cartes (image, waypoints, cases 
interdites) pour chaque monde

## Dossier actif/
Contient toutes les images du jeu organisées en sous-dossiers :
- `actif/ennemis/` : sprites des ennemis
- `actif/tours/` : sprites des tours et projectiles
- `actif/bouton/` : images des boutons
- `actif/gui/` : interfaces, fonds d'écran et éléments graphiques
- `actif/Map/` : images des cartes