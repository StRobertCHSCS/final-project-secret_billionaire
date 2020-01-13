import arcade 
import random
import os

SCREEN_WIDTH = 900
SCREEN_HEIGHT = 400
current_screen = "play"
fence_y = 50
dash_y = 300
car_x = 245
rock1_y = random.randrange(650,700)
rock1_x = random.choice([95,245,395])
rock2_y = random.randrange(800,850)
rock2_x = random.choice([95,245,395])
score = 0
car = arcade.load_texture('car.jpg')
rocks = arcade.load_texture('rocks.jpg')
menu_background = arcade.load_texture('menu_background.jpg')

def draw_track(x,y):
    """ Draw the Track"""
    # Seperation Lines
    arcade.draw_rectangle_filled(170,300, 10, 800,arcade.color.BLACK)
    arcade.draw_rectangle_filled(320,300, 10, 800,arcade.color.BLACK)

def draw_fence(x,y):
    """ Draw the Fence"""
    # Fence
    arcade.draw_rectangle_filled(x-300,y,100,20,arcade.color.RED)
    arcade.draw_rectangle_filled(x-200,y,100,20,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x-100,y,100,20,arcade.color.RED)
    arcade.draw_rectangle_filled(x,y,100,20,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x+100,y,100,20,arcade.color.RED)
    arcade.draw_rectangle_filled(x+200,y,100,20,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x+300,y,100,20,arcade.color.RED)
    arcade.draw_rectangle_filled(x+400,y,100,20,arcade.color.WHITE)


def draw_car(x,y):
    """ Draw the Car """
    arcade.draw_texture_rectangle(x,y,50,70,car)

def draw_dash_line(x,y):
    """ Draw the Dash Line on the Track"""
    arcade.draw_rectangle_filled(x, y-270,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, y-210,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, y-150,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, y-90,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, y-30,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, y+30,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, y+90,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, y+150,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, y+210,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, y+270,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, y+330,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, y+390,10,40,arcade.color.LIGHT_GRAY)

def draw_rocks(x,y):
    arcade.draw_texture_rectangle(x,y,90,90,rocks)

def on_draw():
    """ Draw everything """
    global current_screen
    global fence_y
    global dash_y
    global car_x
    global rock1_x
    global rock1_y
    global rock2_x
    global rock2_y
    global score
    arcade.start_render()

    if current_screen == "menu":
        arcade.draw_texture_rectangle(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,SCREEN_WIDTH,SCREEN_HEIGHT,menu_background)

        arcade.draw_text("PLAY",SCREEN_WIDTH/2,305,arcade.color.BLACK,60,anchor_x="center")

        arcade.draw_text("By: Harry & Frank",270,405,arcade.color.BLACK,20)

        arcade.draw_text("Instructions", SCREEN_WIDTH / 2, 225, arcade.color.BLACK,60, anchor_x="center")

    elif current_screen == "play":
        draw_fence(400,fence_y)

    elif current_screen == "ins":
        arcade.draw_text("Instructions", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 * 2,
                             arcade.color.BLACK, font_size=60, anchor_x="center")
        arcade.draw_text("You are the new 007, you are now driving a",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,arcade.color.BLACK, 20, anchor_x="center")
        arcade.draw_text("car trying to escape. Your job is to dodge",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 30,arcade.color.BLACK, 20, anchor_x="center")
        arcade.draw_text("the rocks that are on the road, you can",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60,arcade.color.BLACK, 20, anchor_x="center")
        arcade.draw_text("press 'a' key to move your car left,",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 90,arcade.color.BLACK, 20, anchor_x="center")
        arcade.draw_text("and press 'd' key to move your car",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 120,arcade.color.BLACK, 20, anchor_x="center")
        arcade.draw_text("right. If you hit the rock, the game ",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,arcade.color.BLACK, 20, anchor_x="center")
        arcade.draw_text("is over. Now good luck and have fun! ",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 180,arcade.color.BLACK, 20, anchor_x="center")                           
        arcade.draw_text("Press 'Escape' to go back",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 210,arcade.color.BLACK, 20, anchor_x="center") 

    elif current_screen == "gameover":
        arcade.draw_text("GAME OVER!", 245, 300, arcade.color.RED, 50, anchor_x="center")
        arcade.draw_text(f"You dodged {score} rocks!", 245, 250, arcade.color.RED, 30, anchor_x="center")
        arcade.draw_text("Press 'esc' to go back.", 355, 50, arcade.color.RED, 20, anchor_x="center")

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
    global fence_y
    global dash_y
    global car_x
    global rock1_x
    global rock1_y
    global rock2_x
    global rock2_y
    global score
    speed = 20

    if current_screen == "play":
        rock1_y -= speed
        if score >= 5:
            rock2_y -= speed
        if fence_y <= 100:
            fence_y = 300

        if rock1_y <= -55:
            rock1_x = random.choice([95,245,395])   
            rock1_y = random.randrange(650,700)
            speed += 10
            score += 1   
        if rock2_y <= -55:
            rock2_x = random.choice([95,245,395])   
            rock2_y = random.randrange(800,850)
            speed += 10
            score += 1   

    else:
        fence_y = 300
        dash_y = 300
        car_x = 245
        rock1_y = random.randrange(650,700)
        rock1_x = random.choice([95,245,395])     
        rock2_y = random.randrange(800,850)
        rock2_x = random.choice([95,245,395])
        speed = 10


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
