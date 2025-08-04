from circleshape import*
from constants import*
import random
from player import*

class Weapon(CircleShape):
    def __init__(self,player,x,y,type):
           super().__init__(x,y,PLAYER_RADIUS)
           self.player = player
           self.rotation = 0
           self.type = type
           self.timer = 0
           self.gatling_cooldown_timer = GATLING_COOLDOWN
           self.gatling_on_cooldown = False
           self.gatling_use_time = GATLING_USE_TIME
           self.single_shot_firerate = SINGLE_SHOT_FIRERATE
           self.triple_shot_firerate = TRIPLE_SHOT_FIRERATE
           self.gatling_firerate = GATLING_FIRERATE
           
        

    def single_shot(self,dt):
        direction = pygame.Vector2(0,1).rotate(self.player.rotation)
        velocity = PLAYER_SHOOT_SPEED * direction
        shot = Shot(self.position.x,self.position.y,velocity)
        self.timer = self.single_shot_firerate


    def triple_shot(self,dt):
        random_angle = random.uniform(20,50)
        direction1 = pygame.Vector2(0,1).rotate(self.rotation+random_angle)
        direction2 = pygame.Vector2(0,1).rotate(self.rotation-random_angle)
        direction3 = pygame.Vector2(0,1).rotate(self.rotation)
        velocity1 = PLAYER_SHOOT_SPEED * direction1
        velocity2 = PLAYER_SHOOT_SPEED * direction2
        velocity3 = PLAYER_SHOOT_SPEED * direction3
        shot1 = Shot(self.position.x,self.position.y,velocity1)
        shot2 = Shot(self.position.x,self.position.y,velocity2)
        shot3 = Shot(self.position.x,self.position.y,velocity3)
        self.timer = self.triple_shot_firerate
    
    def gatling_gun(self,dt):
        direction = pygame.Vector2(0,1).rotate(self.rotation)
        velocity = PLAYER_SHOOT_SPEED * direction
        shot = Shot(self.position.x,self.position.y,velocity)
        self.timer = self.gatling_firerate

    def update(self):
         self.rotation = self.player.rotation
         self.position = self.player.position
