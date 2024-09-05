from player import Player
import pygame
from constants import *

def main():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    clock = pygame.time.Clock()
    dt = 0
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    updatables.add(player)
    drawables.add(player)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        pygame.Surface.fill(screen, (0,0,0))
        dt = clock.tick(60) / 1000.0

        for drawable in drawables:
            drawable.draw(screen)

        for updatable in updatables:
            updatable.update(dt)

        pygame.display.flip()

if __name__ == "__main__":
    main()
