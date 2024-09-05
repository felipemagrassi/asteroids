from asteroid import Asteroid
from asteroidfield import AsteroidField
from player import Player
import pygame
from constants import *
from shot import Shot

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        dt = clock.tick(60) / 1000.0

        for obj in drawable:
            obj.draw(screen)

        for obj in updatable:
            obj.update(dt)

        for obj in asteroids:
            if obj.collides_with(player):
                print("Game over!")
                return
            for shot in shots:
                if obj.collides_with(shot):
                    obj.split()
                    shot.kill()
                


        pygame.display.flip()

if __name__ == "__main__":
    main()
