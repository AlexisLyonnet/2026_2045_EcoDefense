#Projet : EcoDefense - Sauver la Terre !
#Auteurs : Adam Hzeg, Alexis Lyonnet, Martin Mechin

import pygame as pg
import math
import constante as c
from tour_data import TYPES_TOURS
from projectile import Projectile


class Tour(pg.sprite.Sprite):
    def __init__(self, images, souris_grille_x, souris_grille_y, type_tour="eolienne", projectile_img=None):
        pg.sprite.Sprite.__init__(self)
        self.upgrade_level = 1
        self.type_tour = type_tour
        self.images = images
        self.image = self.images[self.upgrade_level - 1]
        stats = TYPES_TOURS[self.type_tour]["stats"][self.upgrade_level - 1]
        self.range    = stats["range"]
        self.cooldown = stats["cooldown"]
        self.degats   = stats["degats"]
        self.last_shot = pg.time.get_ticks()
        self.selected = False
        self.target = None

        # Image du projectile chargée une seule fois à la création de la tour
        self.projectile_img = projectile_img or pg.image.load("actif/tours/projectile1.png").convert_alpha()

        self.souris_grille_x = souris_grille_x
        self.souris_grille_y = souris_grille_y
        # Calculer le centre de la grille
        self.x = (self.souris_grille_x + 0.5) * c.GRILLE
        self.y = (self.souris_grille_y + 0.5) * c.GRILLE
        self.rect = self.image.get_rect()
        self.rect.center = (self.x, self.y)

        self.creer_range_image()

    def creer_range_image(self):
        size = max(1, int(math.ceil(self.range * 2)))
        radius = max(1, int(round(self.range)))
        self.range_image = pg.Surface((size, size))
        self.range_image.fill((0, 0, 0))
        self.range_image.set_colorkey((0, 0, 0))
        pg.draw.circle(self.range_image, "grey100", (size // 2, size // 2), radius)
        self.range_image.set_alpha(100)
        self.range_rect = self.range_image.get_rect()
        self.range_rect.center = self.rect.center

    def update(self, ennemis_groupe, world, projectiles_groupe):
        if pg.time.get_ticks() - self.last_shot > (self.cooldown / world.game_speed):
            self.choisi_cible(ennemis_groupe, world, projectiles_groupe)

    def choisi_cible(self, ennemis_groupe, world, projectiles_groupe):
        for ennemi in ennemis_groupe:
            if ennemi.health > 0:
                x_dist = ennemi.pos[0] - self.x
                y_dist = ennemi.pos[1] - self.y
                dist = math.sqrt(x_dist ** 2 + y_dist ** 2)
                if dist <= self.range:
                    self.target = ennemi

                    # --- Dégâts instantanés (logique inchangée) ---
                    self.target.health -= self.degats
                    self.target.flash_hit()   # déclenche le flash rouge visuel
                    self.last_shot = pg.time.get_ticks()
                    projectile = Projectile(
                        start_pos=(self.x, self.y),
                        target_pos=pg.math.Vector2(self.target.pos),
                        projectile_img=self.projectile_img,
                    )
                    projectiles_groupe.add(projectile)
                    break

    def cout_amelioration(self):
        if self.upgrade_level < c.NIVEAU_MAX:
            return TYPES_TOURS[self.type_tour]["stats"][self.upgrade_level]["cout_amelioration"]
        return 0

    def upgrade(self):
        if self.upgrade_level < c.NIVEAU_MAX:
            self.upgrade_level += 1
            stats = TYPES_TOURS[self.type_tour]["stats"][self.upgrade_level - 1]
            self.range = stats["range"]
            self.cooldown = stats["cooldown"]
            self.degats = stats["degats"]
            self.image = self.images[self.upgrade_level - 1]
            self.creer_range_image()
    
    

    def draw(self, surface):
        surface.blit(self.image, self.rect)
        if self.selected:
            surface.blit(self.range_image, self.range_rect)