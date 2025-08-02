import pygame
from constants import *
from circleshape import Shot
from player import Player
from asteroid import Asteroid
from asteroidfield import *
import sys

def main():
    pygame.init()
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots,updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)
    asteroid_field = AsteroidField() 
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    is_running = True
    while(is_running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        screen.fill("black")
        updatable.update(dt)
        for each_asteroid in asteroids:
            if player.collision_check(each_asteroid) == True:
                print("Game Over!")
                sys.exit()
            for each_shot in shots:
                if each_shot.collision_check(each_asteroid) == True:
                    each_shot.kill()
                    each_asteroid.split(asteroids)

        for each_thing in drawable:
            each_thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) /1000

        
    pygame.quit()


if __name__ == "__main__":
    main()
