import arcade 
import random

SCREEN_WIDTH = 490
SCREEN_HEIGHT = 600
current_screen = "menu"

def draw_track(x,y):
    """ Draw the Track"""
    # Seperation Lines
    arcade.draw_rectangle_filled(170,300, 10, 600,arcade.color.BLACK)
    arcade.draw_rectangle_filled(320,300, 10, 600,arcade.color.BLACK)

def draw_fence(x,y):
    """ Draw the Fence"""
    # Fence
    arcade.draw_rectangle_filled(x,50,20,100,arcade.color.RED)
    arcade.draw_rectangle_filled(x,150,20,100,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x,250,20,100,arcade.color.RED)
    arcade.draw_rectangle_filled(x,350,20,100,arcade.color.WHITE)
    arcade.draw_rectangle_filled(x,450,20,100,arcade.color.RED)
    arcade.draw_rectangle_filled(x,550,20,100,arcade.color.WHITE)

def draw_dash_line(x,y):
    """ Draw the Dash Line on the Track"""
    arcade.draw_rectangle_filled(x, 30,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, 90,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, 150,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, 210,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, 270,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, 330,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, 390,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, 450,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, 510,10,40,arcade.color.LIGHT_GRAY)
    arcade.draw_rectangle_filled(x, 570,10,40,arcade.color.LIGHT_GRAY)

def on_draw():
    """ Draw everything """
    global current_screen
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
        draw_fence(10,300)
        draw_fence(480,300)
        draw_dash_line(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
        draw_dash_line(95,SCREEN_HEIGHT/2)
        draw_dash_line(SCREEN_WIDTH - 95,SCREEN_HEIGHT/2)

    elif current_screen == "ins":

        arcade.draw_text("Instructions", SCREEN_WIDTH / 2, SCREEN_HEIGHT / 3 * 2,
                             arcade.color.BLACK, font_size=60, anchor_x="center")
        arcade.draw_text("You are the new 007, you are now driving a",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2,arcade.color.BLACK, 20, anchor_x="center")
        arcade.draw_text("car trying to escape. Your job is to dodge",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 30,arcade.color.BLACK, 20, anchor_x="center")
        arcade.draw_text("the rocks that are on the road, you can",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 60,arcade.color.BLACK, 20, anchor_x="center")
        arcade.draw_text("press 'left arrow' key to move your car",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 90,arcade.color.BLACK, 20, anchor_x="center")
        arcade.draw_text("left, and press 'right arrow' key to move",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 120,arcade.color.BLACK, 20, anchor_x="center")
        arcade.draw_text("your car right. If you hit the rock, the game ",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 150,arcade.color.BLACK, 20, anchor_x="center")
        arcade.draw_text("is over. Now good luck and have fun! ",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 180,arcade.color.BLACK, 20, anchor_x="center")                           
        arcade.draw_text("Press 'Escape' to go back",
                    SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 210,arcade.color.BLACK, 20, anchor_x="center") 

    elif current_screen == "gameover":
        pass

def on_mouse_press(mouse_x: float, mouse_y: float, button: int, modifiers: int):
    global current_screen
    if current_screen == "menu":
        if mouse_x >=145 and mouse_x <= 345 and mouse_y >= 255 and mouse_y <= 345:
            current_screen = "play"
            print("clicked")
        if mouse_x >= 45 and mouse_x <= 445 and mouse_y >= 145 and mouse_y <= 215:
            current_screen = "ins"

def on_key_press(key,modifiers):
    global current_screen
    if key == arcade.key.ESCAPE:
            current_screen = "menu"

def update(dalta_time):
    pass

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