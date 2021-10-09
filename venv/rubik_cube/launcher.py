import pygame
import os
from rubik_cube import Cube


def main():
    pygame.init()
    screen = pygame.display.set_mode((600, 600))
    pygame.display.set_caption('Rubik solver')

    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill((250, 250, 250))
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

if __name__ == "__main__":
    main()