import pygame
from constants import *
from circleshape import Shot
from player import Player
from asteroid import*
from asteroidfield import *
import sys

high_score = float("-inf")

def main():
    pygame.init()
    global high_score
    
    # set up all my groups
    clock = pygame.time.Clock()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    buff_attackspeed_asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    Shot.containers = (shots,updatable,drawable)
    Asteroid.containers = (asteroids,updatable,drawable)
    Player.containers = (updatable,drawable)
    AsteroidField.containers = (updatable)
    Buff_attackspeed_Asteroid.containers = (buff_attackspeed_asteroids,updatable,drawable)
    asteroid_field = AsteroidField() 

    # set variables
    player = Player(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    dt = 0
    lives = MAX_LIVES
    score = 0
    print(" ")
    print(" ")
    print(f"LMB fires single shots, RMB fires 3 shots in a cone, Space fires rapid single shots (use sparingly, it has a cooldown)")
    print("Big asteroids = 100 points, Medium = 200 points, and Small = 300 points")
    print(f"You have {lives} lives")
    timer = GRACE_PERIOD
    invincible = False
    grace_period_was_printed = False
    buff = False

    # create screen variable
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    background_image = pygame.image.load("images/space_asteroids.png")
    background_image = pygame.transform.scale(background_image, (SCREEN_WIDTH, SCREEN_HEIGHT)).convert()
    is_running = True

    while(is_running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                is_running = False
        screen.blit(background_image, (0,0))    # actually "draw" screen
        updatable.update(dt)    # update everything in updatable group, player, asteroids, and shots

        buttons = pygame.mouse.get_pressed()
        if buttons[0]:
            player.shoot("single_shot",dt)
        if buttons[2]:
            player.shoot("triple_shot",dt)
        


        # make a grace period after getting hit
        if invincible == True:
            timer -= dt
               
            if timer <= 0:
                invincible = False
                print("You're Vulnerable")
                if delay_life_print == True:
                    
                    if lives == 1:
                        print("!!!This is your Last Life!!!")
                    elif lives > 1:
                        print(f"You have {lives} lives left!")
                    delay_life_print = False

                   
        # while out of grace period track if hit by asteroid        
        if invincible == False:
            for each_asteroid in asteroids:
                if player.collision_check(each_asteroid) == True:
                    each_asteroid.kill()
                    invincible = True 

                    timer = GRACE_PERIOD
                    lives -= 1
                    if lives == 0:
                        print("Game Over!")
                        if score > high_score:
                            high_score = score
                            print(f"You set a new High Score with a total of {score} points!")
                        elif score == high_score:
                            print(f"You tied the High Score with a total of {score} points! So Close :(")
                        else:
                            print(f"Your Score:{score}")
                            print(f"High Score:{high_score}")
                        sys.exit()

                    delay_life_print = True
                    print("Grace Period")

                    break

        # check if each shot hits an asteroid and split/destroy it                
        for each_asteroid in asteroids:
            for each_shot in shots:
                if each_shot.collision_check(each_asteroid) == True:
                    each_shot.kill()
                    if each_asteroid.radius == ASTEROID_MIN_RADIUS:
                        score += 300
                    elif each_asteroid.radius == ASTEROID_MIN_RADIUS * 2:
                        score += 200
                    else:
                        score += 100
                    each_asteroid.split(asteroids)

        for each_attackspeed_asteroid in buff_attackspeed_asteroids:
            if player.collision_check(each_attackspeed_asteroid) == True:
                    each_attackspeed_asteroid.kill()
                    print("2x Firerate for 5 Seconds!")
                    player.buff_timer = BUFF_ATTACKSPEED_LENGTH
            


                    
        # draw everything
        for each_thing in drawable:
            each_thing.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) /1000

        
    pygame.quit()


if __name__ == "__main__":
    main()
