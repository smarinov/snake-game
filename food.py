import config

x = (random(config.WINDOW_WIDTH - config.SCALE) // config.SCALE) * config.SCALE 
y = (random(config.WINDOW_HEIGHT - config.SCALE) // config.SCALE) * config.SCALE

food_pos = [x, y]

def show():
    fill(0, 255, 0)
    rect(food_pos[0], food_pos[1], config.SCALE, config.SCALE)
    
    
def reset():
    x = (random(config.WINDOW_WIDTH - config.SCALE) // config.SCALE) * config.SCALE 
    y = (random(config.WINDOW_HEIGHT - config.SCALE) // config.SCALE) * config.SCALE

    food_pos[0] = x
    food_pos[1] = y
