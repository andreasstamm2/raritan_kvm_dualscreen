#!/usr/bin/env python3
import time
import struct
import mouse_move_absolute

def alternate_left_right():
    # overall virtual desktop that represents a dual-screen setup with 1920x1280 for each screen
    screen_width = 1920
    screen_height = 1280

    # offset so that the pixels of the cursor are not hidden on another screen
    offset_x = 15
    offset_y = 15

    # time that the cursor stands still before moving to the next screen position
    sleep_duration = 3

    virtualdesktop_width = screen_width*2 
    virtualdesktop_height = screen_height

    # calculation of coordinates to be looped through below
    screen_1_upper_left = (0+offset_x,0+offset_y)
    screen_1_upper_right = (screen_width-offset_x,0+offset_y)
    screen_1_lower_right = (screen_width-offset_x,screen_height-offset_y)
    screen_1_lower_left = (0+offset_x,screen_height-offset_y)

    screen_2_upper_left = (screen_width+offset_x,0+offset_y)
    screen_2_upper_right = (virtualdesktop_width-offset_x,0+offset_y)
    screen_2_lower_right = (virtualdesktop_width-offset_x,screen_height-offset_y)
    screen_2_lower_left = (screen_width+offset_x,screen_height-offset_y)

    # this will move the cursor to different points on the screen assuming a 2-screen-setup
    while 1:
        mouse_move_absolute.point(screen_1_upper_left, virtualdesktop_width, virtualdesktop_height)
        time.sleep(sleep_duration)
        mouse_move_absolute.point(screen_1_upper_right, virtualdesktop_width, virtualdesktop_height)
        time.sleep(sleep_duration)
        mouse_move_absolute.point(screen_1_lower_right, virtualdesktop_width, virtualdesktop_height)
        time.sleep(sleep_duration)
        mouse_move_absolute.point(screen_1_lower_left, virtualdesktop_width, virtualdesktop_height)
        time.sleep(sleep_duration)
        mouse_move_absolute.point(screen_1_upper_left, virtualdesktop_width, virtualdesktop_height)
        time.sleep(sleep_duration)
        mouse_move_absolute.point(screen_1_upper_right, virtualdesktop_width, virtualdesktop_height)
        time.sleep(sleep_duration)

        mouse_move_absolute.point(screen_2_upper_left, virtualdesktop_width, virtualdesktop_height)
        time.sleep(sleep_duration)
        mouse_move_absolute.point(screen_2_upper_right, virtualdesktop_width, virtualdesktop_height)
        time.sleep(sleep_duration)
        mouse_move_absolute.point(screen_2_lower_right, virtualdesktop_width, virtualdesktop_height)
        time.sleep(sleep_duration)
        mouse_move_absolute.point(screen_2_lower_left, virtualdesktop_width, virtualdesktop_height)
        time.sleep(sleep_duration)

        mouse_move_absolute.point(screen_1_lower_right, virtualdesktop_width, virtualdesktop_height)
        time.sleep(sleep_duration)
        mouse_move_absolute.point(screen_1_lower_left, virtualdesktop_width, virtualdesktop_height)
        time.sleep(sleep_duration)

if __name__ == '__main__':
    alternate_left_right()
