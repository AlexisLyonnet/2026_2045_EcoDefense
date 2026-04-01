#Projet : EcoDefense - Sauver la Terre !
#Auteurs : Adam Hzeg, Alexis Lyonnet, Martin Mechin

import pygame as pg
from ennemis import Ennemis
from world import World
import constante as c
from bouton import Bouton
from tour import Tour
from ennemies_data import ENNEMIES_SPAWN_DATA
from niveau_data import NIVEAU_DATA
from tour_data import TYPES_TOURS
from projectile import Projectile
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Initialisation de Pygame
pg.init()   

clock = pg.time.Clock()

# Création de la fenêtre
screen = pg.display.set_mode((c.SCREEN_WIDTH + c.PANNEAU_LARGEUR, c.SCREEN_HEIGHT))
pg.display.set_caption("EcoDefense - Sauver la Terre !")

# Variables de jeu
game_state = "accueil"
game_over = False
game_outcome = 0 # -1 est perdu, 0 est en cours, 1 est gagné
dernier_ennemies_spawn = pg.time.get_ticks()
placement_tour = False
selected_tour = None
niveau_commence = False
tour_type_choisi = None
image_deblocage = None
image_deblocage_timer = 0
image_deblocage_alpha = 255
IMAGE_DEBLOCAGE_DUREE = 1000
accueil_transition_timer = 0
ACCUEIL_TRANSITION_DUREE = 200
biome_timer = 0
biome_duree = 7000 
biome_actif = False


# Chargement des images
#ennemies
ennemies_images = {
    "faible" : pg.image.load("actif/ennemis/Ennemis_1.png").convert_alpha(),
    "moyen" : pg.image.load("actif/ennemis/Ennemis_2.png").convert_alpha(),
    "fort" : pg.image.load("actif/ennemis/Ennemis_3.png").convert_alpha(),
    "boss" : pg.image.load("actif/ennemis/Ennemis_4.png").convert_alpha(),
    "faible_rouge" : pg.image.load("actif/ennemis/Ennemis_1_Rouge.png").convert_alpha(),
    "moyen_rouge" : pg.image.load("actif/ennemis/Ennemis_2_Rouge.png").convert_alpha(),
    "fort_rouge" : pg.image.load("actif/ennemis/Ennemis_3_Rouge.png").convert_alpha(),
    "boss_rouge" : pg.image.load("actif/ennemis/Ennemis_4_Rouge.png").convert_alpha()
}
#tours indivuelles pour curseur
tour_curseur = pg.image.load(TYPES_TOURS["eolienne"]["images"][1][0]).convert_alpha()

#bouton
acheter_tour_image = pg.image.load("actif/bouton/acheter_tour_bouton.png").convert_alpha()
annuler_image = pg.image.load("actif/bouton/annuler_bouton.png").convert_alpha()
ameliorer_image = pg.image.load("actif/bouton/amelioration_bouton.png").convert_alpha()
commencer_image = pg.image.load("actif/bouton/commencer_bouton.png").convert_alpha()
recommencer_image = pg.image.load("actif/bouton/recommencer_bouton.png").convert_alpha()
accelerer_1x_image = pg.image.load("actif/bouton/vitesse_x1_bouton.png").convert_alpha()
accelerer_2x_image = pg.image.load("actif/bouton/vitesse_x2_bouton.png").convert_alpha()
img_3_debloque = pg.image.load("actif/gui/3debloque.png").convert_alpha()
img_6_debloque = pg.image.load("actif/gui/6debloque.png").convert_alpha()
# Affiche les polices pour les textes 
police_texte = pg.font.SysFont("Arial", 24, bold=True)
police_large = pg.font.SysFont("Arial", 36)
police_vague = pg.font.SysFont("Arial", 27, bold=True)
images_niveau = {
    1: pg.image.load("actif/gui/niveau_1.png").convert_alpha(),
    2: pg.image.load("actif/gui/niveau_2.png").convert_alpha(),
    3: pg.image.load("actif/gui/niveau_3.png").convert_alpha(),
}
perdu_image = pg.image.load("actif/gui/perdu.png").convert_alpha()
regles_fond_img = pg.image.load("actif/gui/regles_fond.png").convert_alpha()
retour_img = pg.image.load("actif/bouton/retour.png").convert_alpha()
retour_bouton = Bouton(104.9, 318.3, retour_img, False)

victoire_img = pg.image.load("actif/gui/victoire.png").convert_alpha()
retour_accueil_img = pg.image.load("actif/bouton/rejouer_fin.png").convert_alpha()
retour_accueil_bouton = Bouton(839.5, 628.3, retour_accueil_img, False)

vague_image = pg.image.load("actif/gui/vague.png").convert_alpha()

projectiles_images = {
    type_tour: pg.image.load(TYPES_TOURS[type_tour]["projectile"]).convert_alpha()
    for type_tour in TYPES_TOURS
}

biome_images = {
    1: pg.image.load("actif/gui/plaine.png").convert_alpha(),
    2: pg.image.load("actif/gui/sable.png").convert_alpha(),
    3: pg.image.load("actif/gui/glace.png").convert_alpha(),
}



#Ecran d'accueil
try:
    accueil = pg.image.load("actif/gui/accueil.png").convert_alpha()
    accueil = pg.transform.scale(accueil, (c.SCREEN_WIDTH + c.PANNEAU_LARGEUR, c.SCREEN_HEIGHT))
except:
    accueil = pg.Surface((c.SCREEN_WIDTH + c.PANNEAU_LARGEUR, c.SCREEN_HEIGHT))
    accueil.fill((20, 40, 20))

commencer_jeu_img = pg.image.load("actif/bouton/commencer_jeu.png").convert_alpha()
regles_img = pg.image.load("actif/bouton/regles.png").convert_alpha()

accueil_commencer_bouton = Bouton(268.6, 480.9, commencer_jeu_img, True)
accueil_regles_bouton    = Bouton(364.6, 630.4, regles_img, True)

# Interface de jeu

try:
    panel_bg = pg.image.load("Actif/Gui/interface.png").convert_alpha()
    panel_bg = pg.transform.scale(panel_bg, (c.PANNEAU_LARGEUR, c.SCREEN_HEIGHT))
except Exception:
    panel_bg = pg.Surface((c.PANNEAU_LARGEUR, c.SCREEN_HEIGHT))
    panel_bg.fill((200, 200, 200))

# Menu pour selectionner les tours
class MenuSelectionTour:
    def __init__(self, screen):
        self.screen = screen
        self.visible = False

        # Chargement des 3 images de boutons
        icone_1 = pg.image.load("actif/bouton/icone_1.png").convert_alpha()
        icone_2 = pg.image.load("actif/bouton/icone_2.png").convert_alpha()
        icone_3 = pg.image.load("actif/bouton/icone_3.png").convert_alpha()

        # Chargement des images grisées
        icone_2_gris = pg.image.load("actif/bouton/icone_2_gris.png").convert_alpha()
        icone_3_gris = pg.image.load("actif/bouton/icone_3_gris.png").convert_alpha()

        # On associe chaque image à un type de tour
        self.boutons = [
        {"cle": "eolienne", "bouton": Bouton(c.SCREEN_WIDTH + 30.8,  325.9, icone_1, True), "bouton_gris": None, "vague_deblocage": 0},
        {"cle": "solaire", "bouton": Bouton(c.SCREEN_WIDTH + 116.4, 325.9, icone_2, True), "bouton_gris": Bouton(c.SCREEN_WIDTH + 116.4, 325.9, icone_2_gris, True), "vague_deblocage": 3},
        {"cle": "recyclage", "bouton": Bouton(c.SCREEN_WIDTH + 202,   325.9, icone_3, True), "bouton_gris": Bouton(c.SCREEN_WIDTH + 202,   325.9, icone_3_gris, True), "vague_deblocage": 6},
        ]

    def afficher(self, vague_actuelle):
        if not self.visible:
            return
        for btn in self.boutons:
            # Affiche la version grisée si pas encore débloqué
            if btn["vague_deblocage"] > vague_actuelle and btn["bouton_gris"] is not None:
                btn["bouton_gris"].draw(self.screen)
            else:
                btn["bouton"].draw(self.screen)

menu_selection_tour = MenuSelectionTour(screen)


# Fonction pour montrer le texte à l'écran
def draw_texte(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

def charger_niveau(niveau):
    data = NIVEAU_DATA[niveau]
    map_0 = pg.image.load(data["map_0"]).convert_alpha()
    map_100 = pg.image.load(data["map_100"]).convert_alpha()
    waypoints = data["waypoints"]
    placement_interdit = data["placement_interdit"]
    return map_0, map_100, waypoints, placement_interdit

#map
# map (two versions: with grid and without)
map_image_grille_0, map_image_grille_100, waypoints, placement_interdit = charger_niveau(1)


def creer_tour(pos_souris, type_tour="eolienne"):
    souris_grille_x = pos_souris[0] // c.GRILLE
    souris_grille_y = pos_souris[1] // c.GRILLE
    images_tour = []
    for chemin in TYPES_TOURS[type_tour]["images"][world.monde]:
        images_tour.append(pg.image.load(chemin).convert_alpha())
    tour = Tour(images_tour, souris_grille_x, souris_grille_y, type_tour, projectiles_images[type_tour])
    tour_groupe.add(tour)
    #print(tour_groupe)
    

def selectionner_tour(pos_souris):
    souris_grille_x = pos_souris[0] // c.GRILLE
    souris_grille_y = pos_souris[1] // c.GRILLE
    for tour in tour_groupe:
        if (souris_grille_x, souris_grille_y) == (tour.souris_grille_x, tour.souris_grille_y):
            return tour
        
def deselectionner_tour():
    for tour in tour_groupe:
        tour.selected = False
    

#create world
world = World(ENNEMIES_SPAWN_DATA, map_image_grille_100)
world.process_ennemies()


# Création de groupe
ennemies_groupe = pg.sprite.Group()
tour_groupe = pg.sprite.Group()
projectiles_groupe = pg.sprite.Group()

# Création des boutons (centrés dans le panneau de droite)

tour_bouton = Bouton((c.SCREEN_WIDTH + 30), 237.5, acheter_tour_image, True)
annuler_bouton = Bouton((c.SCREEN_WIDTH + 30), 427.9, annuler_image, True)
ameliorer_bouton = Bouton((c.SCREEN_WIDTH + 30), 237.5, ameliorer_image, True)
commencer_bouton = Bouton((c.SCREEN_WIDTH + 30), 133.8, commencer_image, True)
recommencer_bouton = Bouton(
    (c.SCREEN_WIDTH + c.PANNEAU_LARGEUR) // 2 - recommencer_image.get_width() // 2,
    370.6,
    recommencer_image, True
)
accelerer_1x_bouton = Bouton((c.SCREEN_WIDTH + 31.6), 635.4, accelerer_1x_image, True)
accelerer_2x_bouton = Bouton((c.SCREEN_WIDTH + 169.7) , 635.4, accelerer_2x_image, True)

#-----------------------------------------------------------------------------------------------------------------------#

# Boucle de jeu
run = True
while run:

    clock.tick(c.FPS)

    if game_state == "accueil":
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        screen.blit(accueil, (0, 0))

        if accueil_commencer_bouton.draw(screen):
            if accueil_transition_timer == 0:
                accueil_transition_timer = pg.time.get_ticks()
                biome_actif = True
                biome_timer = pg.time.get_ticks()

        if accueil_transition_timer > 0:
            if pg.time.get_ticks() - accueil_transition_timer >= ACCUEIL_TRANSITION_DUREE:
                game_state = "jeu"

        if accueil_regles_bouton.draw(screen):
            game_state = "regles"

        pg.display.flip()
        continue

    if game_state == "regles":
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        screen.blit(regles_fond_img, (-27.7, 212))

        if retour_bouton.draw(screen):
            game_state = "accueil"

        pg.display.flip()
        continue 

    if game_state == "victoire":
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False

        screen.blit(victoire_img, (0, 0))

        if retour_accueil_bouton.draw(screen):
            game_state = "accueil"
            # Reset complet
            game_over = False
            game_outcome = 0
            niveau_commence = False
            placement_tour = False
            selected_tour = None
            accueil_transition_timer = 0
            ennemies_groupe.empty()
            tour_groupe.empty()
            map_image_grille_0, map_image_grille_100, waypoints, placement_interdit = charger_niveau(1)
            world = World(ENNEMIES_SPAWN_DATA, map_image_grille_100)
            world.process_ennemies()

        pg.display.flip()
        continue

    #-----------------------------------------------------------#
    #-------------------------Update----------------------------#
    #-----------------------------------------------------------#

    if game_over == False:
        #verifie si le joueur a perdu
        if world.niveau_vie <= 0:
            game_over = True
            game_outcome = -1
        #verifie si le joueur a gagner
        if world.level > c.NOMBRE_NIVEAU:
            game_over = True
            game_outcome = 1


        #Mise à jour des ennemis
        ennemies_groupe.update(world)
        tour_groupe.update(ennemies_groupe, world, projectiles_groupe)
        projectiles_groupe.update(world)


        #Surligner la tour sélectionnée
        if selected_tour:
            selected_tour.selected = True

    #-----------------------------------------------------------#
    #-------------------------Dessin----------------------------#
    #-----------------------------------------------------------#

    screen.fill("grey")

    # Dessiner le monde
    # Change la carte selon si on place une tour ou non
    if placement_tour or selected_tour:
        world.image = map_image_grille_0
    else:
        world.image = map_image_grille_100
    world.draw(screen)
    # Dessiner le chemin 
    #for i in range(len(waypoints)-1):
        #pg.draw.line(screen, "red", waypoints[i], waypoints[i+1], 5)

    barre_info_image = pg.image.load("actif//gui/barre_info.png").convert_alpha()
    screen.blit(barre_info_image, (10, 10))



    # Dessiner les ennemis
    ennemies_groupe.draw(screen)
    for tour in tour_groupe:
        tour.draw(screen)

    projectiles_groupe.draw(screen)
    screen.blit(panel_bg, (c.SCREEN_WIDTH, 0))


    police_petit = pg.font.SysFont("Arial", 15, bold=True)

    img_niveau_vie = police_petit.render(f"{world.niveau_vie}/{c.NIVEAU_VIE}", True, "grey100")
    rect_niveau_vie = img_niveau_vie.get_rect(bottomright=(114, 54))
    screen.blit(img_niveau_vie, rect_niveau_vie)

    img_monnaie = police_petit.render(str(world.monnaie), True, "grey100")
    rect_monnaie = img_monnaie.get_rect(bottomright=(196, 54))
    screen.blit(img_monnaie, rect_monnaie)

    if game_over == False:
        screen.blit(vague_image, (c.SCREEN_WIDTH + 30, 133.8))
        draw_texte(f"{world.level}", police_vague, "grey100", c.SCREEN_WIDTH + 189.5, 158.7)
        #Verifie si la partie a commencé
        if niveau_commence == False:
            if commencer_bouton.draw(screen):
                    niveau_commence = True
        #Spawn les ennemis
        else:
            # Accelere le jeu
            if accelerer_2x_bouton.draw(screen):
                world.game_speed = 2
            if accelerer_1x_bouton.draw(screen):
                world.game_speed = 1
            if pg.time.get_ticks() - dernier_ennemies_spawn > c.SPAWN_COOLDOWN / world.game_speed:
                if world.spawned_ennemies < len(world.ennemies_liste):
                    ennemies_type = world.ennemies_liste[world.spawned_ennemies]
                    ennemis = Ennemis(ennemies_type, (waypoints), ennemies_images)
                    ennemies_groupe.add(ennemis)
                    world.spawned_ennemies += 1
                    dernier_ennemies_spawn = pg.time.get_ticks()



        #Verifie si la vague est terminé
        if world.verifie_niveau_fini() == True:
            world.monnaie += c.NIVEAU_FINI
            world.level += 1
            niveau_commence = False
            last_ennemies_spawn = pg.time.get_ticks()
            world.reset_niveau()
            world.process_ennemies()
            placement_tour = False
            menu_selection_tour.visible = False
            selected_tour = None
            deselectionner_tour()
             # Si toutes les vagues du monde sont finies
            if world.level > c.NOMBRE_NIVEAU:
                if world.monde < 3:
                    world.monde += 1
                    biome_actif = True
                    biome_timer = pg.time.get_ticks()
                    world.monnaie = c.MONNAIE
                    world.niveau_vie = c.NIVEAU_VIE
                    world.level = 1
                    world.reset_niveau()
                    world.process_ennemies()
                    map_image_grille_0, map_image_grille_100, waypoints, placement_interdit = charger_niveau(world.monde)
                    # Réinitialiser les tours
                    tour_groupe.empty()
                else:
                    game_over = True
                    game_outcome = 1


        # Dessiner les boutons
        # Bouton pour placer une tour (caché si une tour est sélectionnée)
        if not selected_tour:
            if tour_bouton.draw(screen):
                menu_selection_tour.visible = True
                placement_tour = True
                tour_type_choisi = None


            menu_selection_tour.afficher(world.level)
        # Si le bouton de placement de tour est actif montre le bouton annuler 
        if placement_tour == True:
            #Affiche le curseur de la tour
            curseur_rect = tour_curseur.get_rect()
            curseur_pos = pg.mouse.get_pos()
            curseur_rect.center = curseur_pos
            if curseur_pos[0] < c.SCREEN_WIDTH and curseur_pos[1] < c.SCREEN_HEIGHT:
                if tour_type_choisi is not None:
                    range_tour = TYPES_TOURS[tour_type_choisi]["stats"][0]["range"]
                    size = max(1, int(range_tour * 2))
                    range_surface = pg.Surface((size, size), pg.SRCALPHA)
                    pg.draw.circle(range_surface, (255, 255, 255, 80), (size // 2, size // 2), int(range_tour))
                    range_rect = range_surface.get_rect(center=curseur_pos)
                    screen.blit(range_surface, range_rect)
                    screen.blit(tour_curseur, curseur_rect)
            if annuler_bouton.draw(screen):
                placement_tour = False
                menu_selection_tour.visible = False
        #si une tour est sélectionné affiche le bouton ameliorer
        if selected_tour:
            screen.blit(images_niveau[selected_tour.upgrade_level], (c.SCREEN_WIDTH + 31.6, 324.1))
            #si une tour peut etre amélioré affiche le bouton ameliorer
            if selected_tour.upgrade_level < c.NIVEAU_MAX:
                if ameliorer_bouton.draw(screen):
                    cout = selected_tour.cout_amelioration()
                    if world.monnaie >= cout:
                        world.monnaie -= cout
                        selected_tour.upgrade()
            # Bouton annuler pour désélectionner la tour
            if annuler_bouton.draw(screen):
                selected_tour = None
                deselectionner_tour()
    else:
        if game_outcome == -1:
            screen.blit(perdu_image, (
                (c.SCREEN_WIDTH + c.PANNEAU_LARGEUR) // 2 - perdu_image.get_width() // 2,
                275.6
            ))
        else:
            game_state = "victoire" 
            
        # Recommence le niveau
        if recommencer_bouton.draw(screen):
            game_over = False
            game_outcome = 0
            niveau_commence = False
            placement_tour = False
            selected_tour = None    
            menu_selection_tour.visible = False
            tour_type_choisi = None
            dernier_ennemies_spawn = pg.time.get_ticks()
            monde_actuel = world.monde
            map_image_grille_0, map_image_grille_100, waypoints, placement_interdit = charger_niveau(monde_actuel)
            world = World(ENNEMIES_SPAWN_DATA, map_image_grille_100)
            world.monde = monde_actuel
            world.process_ennemies()
            ennemies_groupe.empty()
            tour_groupe.empty()




    # Gestion des événements
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        # CLick de la souris
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # Clic gauche
            pos_souris = pg.mouse.get_pos()

            # Clic sur un bouton du menu de sélection de tour
            if not selected_tour:
                for btn in menu_selection_tour.boutons:
                    if btn["bouton"].rect.collidepoint(pos_souris):
                        # Vérifier si le bouton est débloqué
                        if world.level >= btn["vague_deblocage"]:
                            tour_type_choisi = btn["cle"]
                            placement_tour = True
                            tour_curseur = pg.image.load(TYPES_TOURS[tour_type_choisi]["images"][world.monde][0]).convert_alpha()
                        else:
                            tour_curseur = pg.Surface((c.GRILLE, c.GRILLE), pg.SRCALPHA)
                            # Afficher l'image de déblocage correspondante
                            if btn["vague_deblocage"] == 3:
                                image_deblocage = img_3_debloque.copy()
                            elif btn["vague_deblocage"] == 6:
                                image_deblocage = img_6_debloque.copy()
                            image_deblocage_timer = pg.time.get_ticks()
                            image_deblocage_alpha = 255

            # Vérifier si la position de la souris est sur une case de la grille
            if pos_souris[0] < c.SCREEN_WIDTH and pos_souris[1] < c.SCREEN_HEIGHT:
                # Desélectionner la tour précédemment sélectionnée
                selected_tour = None
                deselectionner_tour()
                # Vérifier si la case est un emplacement interdit pour les tours
                if placement_tour == True:
                    if placement_interdit[pos_souris[1] // c.GRILLE][pos_souris[0] // c.GRILLE] == 1:
                        # Vérifier s'il n'y a pas déjà une tour à cet emplacement
                        emplacement_libre = True
                        for tour in tour_groupe:
                            if tour.rect.collidepoint(pos_souris):
                                emplacement_libre = False
                                break
                        # Si l'emplacement est libre, créer une tour
                        if emplacement_libre == True:
                            if tour_type_choisi is not None:
                                # Verifier si le joueur a assez de monnaie pour acheter la tour
                                if world.monnaie >= TYPES_TOURS[tour_type_choisi]["cout"]:
                                    creer_tour(pos_souris, tour_type_choisi)
                                    # Enleve de la monnaie si le joueur clique pour placer la tour
                                    world.monnaie -= TYPES_TOURS[tour_type_choisi]["cout"]
                                    placement_tour = False
                                    menu_selection_tour.visible = False 
                else:
                    selected_tour = selectionner_tour(pos_souris)
#mise à jour des ennemis

    # Affichage de l'image de déblocage avec fade out
    if image_deblocage is not None:
        temps_ecoule = pg.time.get_ticks() - image_deblocage_timer
        if temps_ecoule < IMAGE_DEBLOCAGE_DUREE:
            # Fade out progressif sur la dernière moitié de la durée
            if temps_ecoule > IMAGE_DEBLOCAGE_DUREE // 2:
                image_deblocage_alpha = int(255 * (1 - (temps_ecoule - IMAGE_DEBLOCAGE_DUREE // 2) / (IMAGE_DEBLOCAGE_DUREE // 2)))
            image_deblocage.set_alpha(image_deblocage_alpha)
            screen.blit(image_deblocage, (205.2, 665.5))
        else:
            image_deblocage = None

    if biome_actif:
        temps_ecoule = pg.time.get_ticks() - biome_timer
        if temps_ecoule < biome_duree:
            screen.blit(biome_images[world.monde], (0, 0))
        else:
            biome_actif = False
    pg.display.flip()
pg.quit()