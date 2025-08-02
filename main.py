import pygame
from constants import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    is_running = True
    while(is_running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        screen.fill("black")
        pygame.display.flip()
    pygame.quit()


if __name__ == "__main__":
    main()
