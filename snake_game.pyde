import config
import snake
import food
import score
import os


def end_screen():
    background(150)
    fill(128, 0, 0)
    textSize(64)
    text("G A M E  O V E R", 130, 400)
    
def setup():
    size(config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    frameRate(10)
    if os.path.exists(config.HIGHSCORE_FILE_PATH):
        with open(config.HIGHSCORE_FILE_PATH, "r") as file:
            score.highscore = int(file.read())
    else:
        highscore = 0
        
        
def draw():
    background(0)
    snake.show()
    snake.move()
    food.show()
    score.show()
    
    if snake.touches_food():
        snake.eat_food()
        food.reset()
        score.score += 10
        
    if snake.eats_self():
        end_screen()
        score.update_highscore()
        noLoop()
        
                
def keyPressed():
    if keyCode == UP or key == "w":
        if config.CURRENT_DIR != "down":
            config.CURRENT_DIR = "up"
    elif keyCode == RIGHT or key == "d":
        if config.CURRENT_DIR != "left":
            config.CURRENT_DIR = "right"
    elif keyCode == DOWN or key == "s":
        if config.CURRENT_DIR != "up":
            config.CURRENT_DIR = "down"
    elif keyCode == LEFT or key == "a":
        if config.CURRENT_DIR != "right":
            config.CURRENT_DIR = "left"
