import arcade 
import random

SCREEN_WIDTH = 490
SCREEN_HEIGHT = 600

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


def on_draw(delta_time):
    """ Draw everything """
    arcade.start_render()

    draw_track(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    draw_fence(10,300)
    draw_fence(480,300)
    draw_dash_line(SCREEN_WIDTH/2,SCREEN_HEIGHT/2)
    draw_dash_line(95,SCREEN_HEIGHT/2)
    draw_dash_line(SCREEN_WIDTH - 95,SCREEN_HEIGHT/2)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.GRAY)

    # Call on_draw every 60th of a second.
    arcade.schedule(on_draw, 1/60)
    arcade.run()


# Call the main function to get the program started.
main()