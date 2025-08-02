from circleshape import*
import random

class Asteroid(CircleShape):
    def __init__(self,x,y,radius):
        super().__init__(x,y,radius)

    def draw(self, screen):
        pygame.draw.circle(screen,"white",self.position,self.radius,width=2)

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
