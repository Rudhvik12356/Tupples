import pgzrun
import random

WIDTH = 1000
HEIGHT = 1000

score = 0
gameOver = False

ash = Actor("ashketchum.png")
pikachu = Actor("pikachu.png")

ash.pos = WIDTH/2, HEIGHT/2
pikachu.pos = 100, 300

def draw():
    screen.blit("background.png", (0,0))
    
    ash.draw()
    pikachu.draw()
    
    screen.draw.text("Score:" + str(score), color = "black", topleft = (10, 10))
    
    if gameOver:
        screen.fill(color = "red")
        screen.draw.text("Game Over! Your final score is "+str(score), color = "blue", fontsize = 40, center = (WIDTH/2, HEIGHT/2)) 
       
def gameState():
    global gameOver
    gameOver = True            
        
def update():
    global score
    global gameOver
    if not gameOver:
        if keyboard.left:
            ash.x -= 5
        elif keyboard.right:
            ash.x += 5
        elif keyboard.up:
            ash.y -= 5
        elif keyboard.down:
            ash.y += 5    
      
    if ash.colliderect(pikachu):
        score += 10
        pikachu.x = random.randint(50, WIDTH - 50)
        pikachu.y = random.randint(50, HEIGHT-50)
        
        
clock.schedule(gameState, 30.0)                    
    
pgzrun.go()    