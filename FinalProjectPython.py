import pygame
pygame.init()
import time
import random

# Background music #
def Backgroundmusic():
    music = "./Final-Battle.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.12)

# Line Collision sound #
def LineCollisionSound():  
    music = "./Collision.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.12)

# Covid Collision sound #
def CovidSound():
    music = "./Cough.mp3"
    pygame.mixer.init()
    pygame.mixer.music.load(music)
    pygame.mixer.music.play(1)
    pygame.mixer.music.set_volume(0.12)


Highscorefile = open("Highscores.txt","r")
High_score = [line.rstrip() for line in Highscorefile]

width = 800
height = 600

virus_width = 80
virus_height = 80

F1carwidth = 90
F1carheight = 200



screen = pygame.display.set_mode((width,height)) # Window Size #

pygame.display.set_caption("Covid Racing") # Caption on top #

# virus Function #
def virusFunction(virus_x,virus_y,virus):
    if virus == 0:
        viruspic = pygame.image.load("covid1.png")
        virus_pic = pygame.transform.scale(viruspic,(virus_width,virus_height))
    elif virus == 1:
        viruspic = pygame.image.load("covid2.png") 
        virus_pic = pygame.transform.scale(viruspic,(virus_width,virus_height))
    elif virus == 2:
        viruspic = pygame.image.load("covid3.png") 
        virus_pic = pygame.transform.scale(viruspic,(virus_width,virus_height))
    elif virus == 3:
        viruspic = pygame.image.load("covid4.png") 
        virus_pic = pygame.transform.scale(viruspic,(virus_width,virus_height))


    screen.blit(virus_pic,(virus_x,virus_y))



# Load the Images #
F1Car = pygame.image.load("F1Car.png")
MainCar = pygame.transform.scale(F1Car, (F1carwidth,F1carheight))
grass = pygame.image.load("grass.jpg")
yellow_strip = pygame.image.load("yellow_strip.jpg")
strip = pygame.image.load("strip.jpg")

# Messages #
GameFont = pygame.font.SysFont("None",100)
crash_text = GameFont.render("Your Car Crashed",1,(188, 36, 60))
infected_text = GameFont.render("You are Infected",1,(188,36,60))
NewFont = pygame.font.SysFont("None",50)
HSFont = pygame.font.SysFont("comicsansms",30)
highScoreF = HSFont.render("Highscore: " + str(High_score[0]), True, (188,36,60))




# Time module #
clock = pygame.time.Clock()

# Background Appearing #
def Background():
    screen.blit(grass,(0,0))
    screen.blit(grass,(700,0))
    screen.blit(yellow_strip,(375,0))
    screen.blit(yellow_strip,(375,100))
    screen.blit(yellow_strip,(375,200))
    screen.blit(yellow_strip,(375,300))
    screen.blit(yellow_strip,(375,400))
    screen.blit(yellow_strip,(375,500))
    screen.blit(strip,(130,0))
    screen.blit(strip,(670,0))


# Function for the score #
def scoreFunction(viruses_passed,score):
    font = pygame.font.SysFont("None",35)
    passed = font.render("Passed: " + str(viruses_passed), True, (188,36,60))
    score = font.render("Score: " + str(score), True, (0,0,0))
    screen.blit(passed, (0,50))
    screen.blit(score, (0,100))
   



# Function for the highscore #
def HighScore(score):
    if score >= int(High_score[0]):
        file = open("Highscores.txt","w")
        file.write(str(score) + "\n")
        
        


    


# Image Appearing #
def car(x,y):
    screen.blit(MainCar,(x,y))


# Game Loop #
def game_loop():
    clicked = False
    x_change = 0
    x = 350
    y = 410
    virus = random.randint(0,3)
    virus_speed = 5
    y_change = 0
    virus_x = random.randrange(200,650)
    virus_y = -750
    viruses_passed = 0
    score = 0
    level = 1
    Backgroundmusic()
    

    
    # Make the window close when clicking at the top right #
    while not clicked:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                clicked = True
             # Moving the car #
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -6
                if event.key == pygame.K_RIGHT:
                    x_change = 6           
              
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
    
           

        screen.fill((119,119,119)) # Change Background color and update the display #

        Background() # Call the function to complete the Background #

        virus_y -= (virus_speed/4)
        virusFunction(virus_x,virus_y,virus)
        virus_y += virus_speed

        scoreFunction(viruses_passed,score)
        screen.blit(highScoreF, (150, 550))
        

        car(x,y) # Call the car Function with the coordinates #
        if x > 670 - 75 or x < 125:
            LineCollisionSound()
            screen.blit(crash_text,(110,200))
            pygame.display.update()
            time.sleep(3)
            HighScore(score)
            game_loop()

        if virus_y > height:
            virus_y = 0 - virus_height
            virus_x = random.randrange(170,width - 170)
            virus = random.randrange(0,4)
            viruses_passed += 1
            score = viruses_passed * 10

            if int(viruses_passed) % 10 ==0:
                level +=1
                virus_speed += 2
                level_text = NewFont.render("Level: " + str(level), 1, (0,0,0))
                screen.blit(level_text,(0,300))
                pygame.display.update()
                time.sleep(2)


            
        if y + 35 < virus_y + virus_height:
            if x - 70 < virus_x < x + 70:
                CovidSound()
                screen.blit(infected_text,(130,200))
                pygame.display.update()
                time.sleep(2)
                HighScore(score)
                game_loop()




        

        pygame.display.update() # Update the Display #

        clock.tick(100)
        
        
game_loop()
        
        

          

            
           

            


    