import config

score = 0
highscore = 0

def show():
    fill(255)
    textSize(24)
    text("Score: " + str(score), 20, 40)
    text("Highscore: " + str(highscore), 20, 70)
    

def update_highscore():
    if score > highscore:
        with open(config.HIGHSCORE_FILE_PATH, "w") as file:
             file.write(str(score))
