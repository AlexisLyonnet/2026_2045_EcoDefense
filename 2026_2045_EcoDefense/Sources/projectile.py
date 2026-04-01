#Projet : EcoDefense - Sauver la Terre !
#Auteurs : Adam Hzeg, Alexis Lyonnet, Martin Mechin

import pygame as pg
from pygame.math import Vector2
import math

# Vitesse du projectile en pixels par frame (indépendante du cooldown)
PROJECTILE_VITESSE = 8

class Projectile(pg.sprite.Sprite):
    def __init__(self, start_pos, target_pos, projectile_img):
        super().__init__()
        self.original_image = projectile_img
        self.pos   = Vector2(start_pos)
        self.target_pos = Vector2(target_pos)   # position figée au moment du tir

        direction = self.target_pos - self.pos
        dist = direction.length()
        if dist > 0:
            self.velocity = direction.normalize() * PROJECTILE_VITESSE
            # atan2 attend (y, x), on inverse y car l'axe Y est vers le bas en pygame
            angle = math.degrees(math.atan2(-direction.y, direction.x))
        else:
            self.velocity = Vector2(0, 0)
            angle = 0

        # Rotation unique calculée à la création (le projectile ne courbe pas)
        self.image = pg.transform.rotate(self.original_image, angle)
        self.rect = self.image.get_rect(center=self.pos)

    def update(self, world):
        # Avance vers la cible à vitesse constante
        self.pos += self.velocity * world.game_speed

        # Tue le projectile dès qu'il atteint (ou dépasse) la cible
        restant = self.target_pos - self.pos
        if restant.length() <= (self.velocity * world.game_speed).length():
            self.kill()
            return

        self.rect.center = self.pos