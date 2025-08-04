from circleshape import*
from constants import*
import random
from weapons import*

player_picture = pygame.image.load("images/spaceship.png")
player_picture = pygame.transform.rotate(player_picture, 180)

class Player(CircleShape):
    def __init__(self,x,y):
        super().__init__(x,y,PLAYER_RADIUS)
        self.rotation = 0
        self.radius = PLAYER_RADIUS
        self.timer = 0
        self.weapon = Weapon(self,x,y,"")
        self.gatling_firing = False
        self.attackspeed_buff_timer = BUFF_LENGTH
        self.attackspeed_buff_active = False
        self.gatling_buff_length = GATLING_BUFF_LENGTH
        self.gatling_buff_active = False
        self.doublepoints_buff_active = False
        self.doublepoints_buff_length = BUFF_LENGTH
 
        self.base_picture = pygame.transform.scale(player_picture, (self.radius *3,self.radius *3))

    # in the player class
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]
    
    def draw(self,screen):
        #pygame.draw.polygon(screen,"green",self.triangle(),width=0)
        #pygame.draw.polygon(screen,"black",self.triangle(),width=4)
        rotated_image = pygame.transform.rotate(self.base_picture, -self.rotation)
        rect = rotated_image.get_rect(center=(self.position.x,self.position.y))
        screen.blit(rotated_image, rect)

    def rotate(self,dt):
        self.rotation += PLAYER_TURN_SPEED * dt
        self.player_picture = pygame.transform.rotate(player_picture, -self.rotation)

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.rotate(-dt)
            self.weapon.update()
        if keys[pygame.K_d]:
            self.rotate(dt)
            self.weapon.update()
        if keys[pygame.K_w]:
            self.move(dt)
            self.weapon.update()
        if keys[pygame.K_s]:
            self.move(-dt)
            self.weapon.update()
        if keys[pygame.K_SPACE]:
            self.shoot("gatling_gun",dt)
        

        self.weapon.timer -= dt
        
        # gatling cooldown
        if self.weapon.gatling_on_cooldown == True:
            self.weapon.gatling_cooldown_timer -= dt
            if self.weapon.gatling_cooldown_timer <= 0:
                self.weapon.gatling_on_cooldown = False
                self.weapon.gatling_use_time = GATLING_USE_TIME
        
        # attack speed buff
        if self.attackspeed_buff_active == True:
            self.attackspeed_buff_timer -= dt
            self.weapon.single_shot_firerate = SINGLE_SHOT_FIRERATE / 2
            self.weapon.triple_shot_firerate = TRIPLE_SHOT_FIRERATE / 2
            if self.attackspeed_buff_timer <= 0:
                self.attackspeed_buff_active = False
                self.attackspeed_buff_timer = BUFF_LENGTH
        else:
            self.weapon.single_shot_firerate = SINGLE_SHOT_FIRERATE
            self.weapon.triple_shot_firerate = TRIPLE_SHOT_FIRERATE
        
        #gatling buff timer
        if self.gatling_buff_active == True:
            self.weapon.gatling_on_cooldown = False   
            self.gatling_buff_length -= dt    
            if self.gatling_buff_length <= 0:
                self.gatling_buff_active = False
                self.gatling_buff_length = GATLING_BUFF_LENGTH
        
        #double points buff timer
        if self.doublepoints_buff_active == True:
            self.doublepoints_buff_length -= dt
            if self.doublepoints_buff_length <= 0:
                self.doublepoints_buff_active = False


    def move(self,dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        possible_move = self.position + forward * PLAYER_SPEED * dt
        
        if (0 <= possible_move.x <= SCREEN_WIDTH and
            0 <= possible_move.y <= SCREEN_HEIGHT):
            self.position = possible_move
        
    def shoot(self,weapon,dt):
        self.weapon.type = weapon
        if self.weapon.type == "single_shot":
            if self.weapon.timer <= 0:
                self.weapon.single_shot(dt)
        if self.weapon.type == "triple_shot":
            if self.weapon.timer <= 0:
                self.weapon.triple_shot(dt)
        if self.weapon.type == "gatling_gun":
            if self.weapon.gatling_on_cooldown == False:
                if self.weapon.timer <= 0:
                    self.weapon.gatling_gun(dt)
                    if self.gatling_buff_active == False:
                        self.weapon.gatling_use_time -= dt
                    if self.weapon.gatling_use_time <= 0:
                        self.weapon.gatling_on_cooldown = True
                        self.weapon.gatling_cooldown_timer = GATLING_COOLDOWN
                        self.gatling_firing = False
        

