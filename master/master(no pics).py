import arcade 
import random
import os

SCREEN_WIDTH = 490
SCREEN_HEIGHT = 600
current_screen = "menu"
road_y = 300
fence_y = 400
car_x = 245
speed = 5
rock1_y = random.randrange(650,700)
rock1_x = random.choice([95,245,395])
rock2_y = random.randrange(800,850)
rock2_x = random.choice([95,245,395])
score = 0
car = arcade.load_texture('car.jpg')
rocks = arcade.load_texture('rocks.jpg')
menu_background = arcade.load_texture('menu_background.jpg')
road = arcade.load_texture('road.jpg')
fence = arcade.load_texture('fence.jpg')
ins_pic = arcade.load_texture('ins_pic.jpg')
gg_pic = arcade.load_texture('gg.jpg')

def draw_car(x,y):
    """ Draw the Car """
    arcade.draw_texture_rectangle(x,y,50,70,car)

def draw_rocks(x,y):
    """ Draw rocks """
    arcade.draw_texture_rectangle(x,y,90,90,rocks)

def on_draw():
    """ Draw everything """
    global current_screen
    global car_x
    global rock1_x
    global rock1_y
    global rock2_x
    global rock2_y
    global road_y
    global score
    global fence_y
    arcade.start_render()

    if current_screen == "menu":
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,menu_background)
        arcade.draw_text("PLAY",SCREEN_WIDTH/2,305,arcade.color.BLACK,60,anchor_x="center")
        arcade.draw_text("By: Harry & Frank",270,405,arcade.color.BLACK,20)
        arcade.draw_text("Instructions", SCREEN_WIDTH / 2, 225, arcade.color.BLACK,60, anchor_x="center")

    elif current_screen == "play":
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,road_y,480,720,road)
        arcade.draw_texture_rectangle(10,fence_y,25,805,fence)        
        arcade.draw_texture_rectangle(480,fence_y,25,805,fence)        
        draw_car(car_x, 50)
        arcade.draw_text(f"Score: {score}",10,570,arcade.color.BLACK,20)
        draw_rocks(rock1_x, rock1_y)
        draw_rocks(rock2_x, rock2_y)

    elif current_screen == "ins":
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,ins_pic)
        arcade.draw_text("Instructions", SCREEN_WIDTH / 2, 450,
                             arcade.color.WHITE, 60, anchor_x="center")
        arcade.draw_text("You are the new 007,",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 90 ,arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("you are now driving",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 60,arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("a car trying to escape.",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 + 30,arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("Your job is to dodge",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 ,arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("the rocks that are on",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 30,arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("the road, you can press",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60,arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("'a' key to move your car",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 90,arcade.color.WHITE, 20, anchor_x="center")                           
        arcade.draw_text("left, and press 'd' key",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 120,arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("to move your car right.",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,arcade.color.WHITE, 20, anchor_x="center")
        arcade.draw_text("If you hit the rock, the",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 180,arcade.color.WHITE, 20, anchor_x="center") 
        arcade.draw_text("game is over. Now good",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 210,arcade.color.WHITE, 20, anchor_x="center") 
        arcade.draw_text("luck and have fun! Press",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 240,arcade.color.WHITE, 20, anchor_x="center") 
        arcade.draw_text("'Escape' to go back.",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 270,arcade.color.WHITE, 20, anchor_x="center") 
                     
                     

    elif current_screen == "gameover":
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,gg_pic)
        arcade.draw_text(f"You dodged {score} rocks!", 245, 230, arcade.color.BURNT_ORANGE, 28, anchor_x="center")
        arcade.draw_text("Press 'esc' to go back.", 355, 50, arcade.color.BLACK, 20, anchor_x="center")

def on_mouse_press(mouse_x: float, mouse_y: float, button: int, modifiers: int):
    global current_screen
    if current_screen == "menu":
        if mouse_x >=145 and mouse_x <= 345 and mouse_y >= 305 and mouse_y <= 365:
            current_screen = "play"
        if mouse_x >= 45 and mouse_x <= 445 and mouse_y >= 225 and mouse_y <= 295:
            current_screen = "ins"

def on_key_press(key,modifiers):
    global current_screen
    global car_x

    if key == arcade.key.ESCAPE:
            current_screen = "menu"
    if current_screen == "play":
        if key == arcade.key.A and car_x > 95:
            car_x -= 150
        if key == arcade.key.D and car_x < 395:
            car_x += 150

def update(dalta_time):
    global current_screen
    global car_x
    global rock1_x
    global rock1_y
    global rock2_x
    global rock2_y
    global road_y
    global score
    global fence_y
    global speed

    if current_screen == "play":
        rock1_y -= speed
        road_y -= speed
        fence_y -= speed
        if score >= 5:
            rock2_y -= speed
        if road_y <= 290:
            road_y = 350
        if fence_y <= 200:
            fence_y = 400
        if rock1_y <= -55:
            rock1_x = random.choice([95,245,395])   
            rock1_y = random.randrange(650,700)
            speed += 0.25
            score += 1   
        if rock2_y <= -55:
            rock2_x = random.choice([95,245,395])   
            rock2_y = random.randrange(800,850)
            speed += 0.25
            score += 1   
        if car_x == rock1_x and rock1_y <= 120 and rock1_y >= -20:
            current_screen = "gameover"        
        if car_x == rock2_x and rock2_y <= 120 and rock2_y >= -20:
            current_screen = "gameover"

    if current_screen == "menu":
        road_y = 350
        car_x = 245
        rock1_y = random.randrange(650,700)
        rock1_x = random.choice([95,245,395])     
        rock2_y = random.randrange(800,850)
        rock2_x = random.choice([95,245,395])
        speed = 5
        score = 0



def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")

    # Override arcade window methods
    window = arcade.get_window()
    window.on_draw = on_draw
    window.on_key_press = on_key_press
    window.on_mouse_press = on_mouse_press
    
    arcade.set_background_color(arcade.color.GRAY)

    # Call on_draw every 60th of a second.
    arcade.schedule(update, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()
