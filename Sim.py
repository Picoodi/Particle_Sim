# all the necessary imports 
import pygame, string, random, math


#init pygame to work
pygame.init()
#Creating the Screen
Screen_Height = 750
Screen_Width = 1500
Screen = pygame.display.set_mode((Screen_Width,Screen_Height))
#giving the window a title
pygame.display.set_caption("Particle Simulation")





#this is the class for creating a Round Particle in the Simulation
class ParticleRound():
    def __init__(self, radius, colour, speed_x, speed_y, position_x, postition_y):
        self.radius = radius
        self.colour = colour
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.position_x = position_x
        self.position_y = postition_y

    def draw_to_screen(self, Screen):
        pygame.draw.circle(Screen, self.colour, (self.position_x, self.position_y), self.radius)

    def movement(self, border_right, border_down):
        #overall movement on the axes
        self.position_x += self.speed_x
        self.position_y += self.speed_y

        #movement collision with the borders
        if self.position_x <= 0 or self.position_x + self.radius >= border_right:
            self.speed_x *= -1
        if self.position_y <= 0 or self.position_y + self.radius >= border_down:
            self.speed_y *= -1


#This class is that we can create random particles in our simulation 
#All the random particles will have the color white so we can identify them easily
class RandomParticle():
    def __init__(self):
        self.radius = random.randint(3,30)
        self.colour = (255,255,255)
        self.speed_x = random.uniform(-0.5,0.5)
        self.speed_y = random.uniform(-0.5,0.5)
        self.position_x = random.randint(0, Screen_Width)
        self.position_y = random.randint(0, Screen_Height)

    def draw_to_screen(self, Screen):
        pygame.draw.circle(Screen, self.colour, (self.position_x, self.position_y), self.radius)

    def movement(self, border_right, border_down):
        #overall movement on the axes
        self.position_x += self.speed_x
        self.position_y += self.speed_y
        #movement collision with the borders
        if self.position_x <= 0 or self.position_x + self.radius >= border_right:
            self.speed_x *= -1
        if self.position_y <= 0 or self.position_y + self.radius >= border_down:
            self.speed_y *= -1



#For the random Particles you can go and enter names in this list if you want to 
#Leave it empyt so no random particles are getting created
RandomParticleNames = ["p1","p2","p3","p4","p5","p6","p7","p8","p9","p10","p11","p12","p13","p14","p15","p16","p17","p18","p19","p20"]

#In this list we store the Random Particle elements which are getting created in the for loop
RandomParticles = []
for element in RandomParticleNames:
    element = RandomParticle()
    RandomParticles.append(element)



#Here we create some custom balls 
kreis = ParticleRound(20, (255,0,0), 0.1, 0.1, 50, 50)
kreis2 = ParticleRound(10,(0,0,250), -0.2, 0.3, 700, 50)



#The loop for the game
run = True
while run == True:
    #make the screen black so its a fresh canvas
    Screen.fill((0,0,0))
    #looking for all events and if the x is clicked exit the simulation
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #this for loop creates the random particles
    for element in RandomParticles:
        element.draw_to_screen(Screen)
        element.movement(Screen_Width,Screen_Height)


    #draw the balls to the screen
    kreis.draw_to_screen(Screen)
    kreis2.draw_to_screen(Screen)
   
    #make the balls move
    kreis.movement(Screen_Width,Screen_Height)
    kreis2.movement(Screen_Width,Screen_Height)
    
   
    pygame.display.update()

pygame.quit
print("The Window has been closed")
