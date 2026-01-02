import pygame
from circleshape import *
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event
import random

class Asteroid(CircleShape):
    def __init__(self,x, y, radius):
        super().__init__(x,y, radius)
        super().collides_with

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def split(self):
        self.kill()
        if self.radius < ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            split_angle = random.uniform(20, 50)
            current_vector = self.velocity
            vectora = current_vector.rotate(split_angle)
            vectorb = current_vector.rotate(-split_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            roid_a = Asteroid(self.position.x, self.position.y, new_radius)
            roid_b = Asteroid(self.position.x, self.position.y, new_radius)
            roid_a.velocity = vectora * 1.2
            roid_b.velocity = vectorb * 1.2


    def update(self, dt):
        self.position += self.velocity * dt