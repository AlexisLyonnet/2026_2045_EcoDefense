#Projet : EcoDefense - Sauver la Terre !
#Auteurs : Adam Hzeg, Alexis Lyonnet, Martin Mechin

import pygame as pg
from pygame.math import Vector2
import math
from ennemies_data import ENNEMIES_DATA
import constante as c

# Durée du flash rouge en millisecondes
HIT_FLASH_DURATION = 120

class Ennemis(pg.sprite.Sprite):
    def __init__(self, ennemies_type, waypoints, images):
        pg.sprite.Sprite.__init__(self)
        self.ennemies_type = ennemies_type
        self.waypoints = waypoints
        self.pos = Vector2(self.waypoints[0])
        self.target_waypoint = 1
        self.health = ENNEMIES_DATA[self.ennemies_type].get("health")
        self.speed = ENNEMIES_DATA[self.ennemies_type].get("speed")
        self.angle = 0

        # Image normale et image rouge (flash au hit)
        self.original_image = images.get(ennemies_type)
        self.hit_image      = images.get(ennemies_type + "_rouge")  # ex: "faible_rouge"

        self.image = pg.transform.rotate(self.original_image, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

        # Timer du flash (0 = pas de flash actif)
        self.hit_flash_timer = 0

    def flash_hit(self):
        """Appelé par la tour au moment de l'impact."""
        self.hit_flash_timer = HIT_FLASH_DURATION

    def update(self, world):
        self.move(world)
        self.rotate()
        self.verifie_mort(world)

        # Décrémenter le timer du flash
        if self.hit_flash_timer > 0:
            self.hit_flash_timer -= world.game_speed * (1000 / c.FPS)

    def move(self, world):
        if self.target_waypoint < len(self.waypoints):
            self.target = Vector2(self.waypoints[self.target_waypoint])
            self.movement = self.target - self.pos
        else:
            self.kill()
            world.niveau_vie -= 5
            world.ennemies_rates += 1

        dist = self.movement.length()

        if dist >= (self.speed * world.game_speed):
            self.pos += self.movement.normalize() * (self.speed * world.game_speed)
        else:
            if dist != 0:
                self.pos += self.movement.normalize() * dist
            self.target_waypoint += 1

    def rotate(self):
        dist = self.target - self.pos
        self.angle = math.degrees(math.atan2(-dist[1], dist[0]))

        # Choisir l'image source selon l'état du flash
        if self.hit_flash_timer > 0 and self.hit_image:
            source = self.hit_image
        else:
            source = self.original_image

        self.image = pg.transform.rotate(source, self.angle)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos

    def verifie_mort(self, world):
        if self.health <= 0:
            world.ennemies_tues += 1
            world.monnaie += ENNEMIES_DATA[self.ennemies_type]["reward"]  # ← au lieu de c.RECOMPENSE_TUE
            self.kill()