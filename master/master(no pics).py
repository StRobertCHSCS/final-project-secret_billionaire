import arcade 
import random
import os

SCREEN_WIDTH = 490
SCREEN_HEIGHT = 600
current_screen = "menu"
fence_y = 300
dash_y = 300
car_x = 245
rock1_y = random.randrange(650,700)
rock1_x = random.choice([95,245,395])
rock2_y = random.randrange(800,850)
rock2_x = random.choice([95,245,395])
score = 0

def draw_track(x,y):
    """ Draw the Track"""
    # Seperation Lines
    arcade.draw_rectangle_filled(170,300, 10, 600,arcade.color.BLACK)
    arcade.draw_rectangle_filled(320,300, 10, 600,arcade.color.BLACK)

def draw_fence(x,y):
    """ Draw the Fence"""
    # Fence
    arcade.draw_rectangle_filled(x,y-250,20,100,arcade.color.RED)
    arcade.draw_rectangle_filled(x,y-150,20,100,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x,y-50,20,100,arcade.color.RED)
    arcade.draw_rectangle_filled(x,y+50,20,100,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x,y+150,20,100,arcade.color.RED)
    arcade.draw_rectangle_filled(x,y+250,20,100,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x,y+350,20,100,arcade.color.RED)
    arcade.draw_rectangle_filled(x,y+450,20,100,arcade.color.WHITE)

def draw_car(x,y):
    """ Draw the Car """
    arcade.draw_rectangle_filled(x,y,30,60,arcade.color.BLACK)

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
    arcade.draw_circle_filled(x,y,50,arcade.color.BLACK)

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
        arcade.draw_rectangle_filled(SCREEN_WIDTH/2,SCREEN_HEIGHT/2,200,70,arcade.color.LIGHT_GRAY)
        arcade.draw_text("PLAY",SCREEN_WIDTH/2,265,arcade.color.BLACK,60,anchor_x="center")

        arcade.draw_text("FAST AND FURIOUS",25,465,arcade.color.BLACK,37)
        arcade.draw_text("By: Harry & Frank",270,425,arcade.color.BLACK,20)

        arcade.draw_rectangle_filled(SCREEN_WIDTH/2,180,400,70,arcade.color.LIGHT_GRAY)
        arcade.draw_text("Instructions", SCREEN_WIDTH / 2, 145, arcade.color.BLACK,60, anchor_x="center")

    elif current_screen == "play":
        draw_track(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        draw_fence(10,fence_y)
        draw_fence(480,fence_y)
        draw_dash_line(SCREEN_WIDTH/2,dash_y)
        draw_dash_line(95,dash_y)
        draw_dash_line(SCREEN_WIDTH - 95,dash_y)
        draw_car(car_x, 50)
        arcade.draw_text(f"Score: {score}",10,570,arcade.color.BLACK,20)
        draw_rocks(rock1_x, rock1_y)
        draw_rocks(rock2_x, rock2_y)

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
        if mouse_x >=145 and mouse_x <= 345 and mouse_y >= 255 and mouse_y <= 345:
            current_screen = "play"
        if mouse_x >= 45 and mouse_x <= 445 and mouse_y >= 145 and mouse_y <= 215:
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
    speed = 10

    if current_screen == "play":
        fence_y -= speed
        rock1_y -= speed
        dash_y -= speed
        if score >= 5:
            rock2_y -= speed
        if fence_y <= 100:
            fence_y = 300
        if dash_y <= 240:
            dash_y = 300
        if rock1_y <= -55:
            rock1_x = random.choice([95,245,395])   
            rock1_y = random.randrange(650,700)
            speed += 5 
            score += 1   
        if rock2_y <= -55:
            rock2_x = random.choice([95,245,395])   
            rock2_y = random.randrange(800,850)
            speed += 5
            score += 1   
        if car_x == rock1_x and rock1_y <= 120 and rock1_y >= -20:
            current_screen = "gameover"        
        if car_x == rock2_x and rock2_y <= 120 and rock2_y >= -20:
            current_screen = "gameover"

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
