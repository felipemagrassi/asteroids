from constants import ASTEROID_MIN_RADIUS
import pygame
import random
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            'white',
            self.position,
            self.radius,
            2
        )

        return

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        angle = random.uniform(20, 50)

        first = Asteroid(self.position.x, 
                         self.position.y, 
                         self.radius - ASTEROID_MIN_RADIUS)

        extra_speed = random.uniform(1, 2)
        first.velocity = self.velocity.rotate(angle) * extra_speed

        second = Asteroid(self.position.x, 
                          self.position.y, 
                          self.radius - ASTEROID_MIN_RADIUS)

        second.velocity = self.velocity.rotate(-angle)





