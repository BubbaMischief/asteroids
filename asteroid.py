from circleshape import*
import random
asteroid_picture = pygame.image.load("images/Asteroid-PNG-Transparent.png")
firerate_buff_picture = pygame.image.load("images/ammobox.png")
doublepoints_buff_picture = pygame.image.load("images/doublepoints.png")

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.asteroid_picture = pygame.transform.scale(asteroid_picture, (self.radius *2,self.radius *2))

    def draw(self, screen):
        #pygame.draw.circle(screen,"red",self.position,self.radius,width=0)
        #pygame.draw.circle(screen,"black",self.position,self.radius,width=4)
        screen.blit(self.asteroid_picture, (self.position.x-self.radius,self.position.y-self.radius))

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self,asteroids):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20,50)
            direction1 = self.velocity.rotate(random_angle)
            direction2 = self.velocity.rotate(-random_angle)
            new_radius = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x,self.position.y,new_radius,)
            asteroid2 = Asteroid(self.position.x,self.position.y,new_radius,)
            asteroid1.velocity = direction1 * 1.2
            asteroid2.velocity = direction2 * 1.2
            asteroids.add(asteroid1)
            asteroids.add(asteroid2)

class Buff_attackspeed_Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.firerate_buff_picture = pygame.transform.scale(firerate_buff_picture, (self.radius *2,self.radius *2))
        #print("Get the 2x attack speed buff!")

    def draw(self, screen):
        #pygame.draw.circle(screen,"blue",self.position,self.radius,width=0)
        #pygame.draw.circle(screen,"black",self.position,self.radius,width=4)
        screen.blit(self.firerate_buff_picture, (self.position.x-self.radius,self.position.y-self.radius))

    def update(self, dt):
        self.position += self.velocity * dt

class Buff_doublepoints_Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)
        self.doublepoints_buff_picture = pygame.transform.scale(doublepoints_buff_picture, (self.radius *2 ,self.radius *2))
        #print("Get the double points buff!")

    def draw(self, screen):
        #pygame.draw.circle(screen,"yellow",self.position,self.radius,width=0)
        #pygame.draw.circle(screen,"black",self.position,self.radius,width=4)
        screen.blit(self.doublepoints_buff_picture, (self.position.x-self.radius,self.position.y-self.radius))

    def update(self, dt):
        self.position += self.velocity * dt


