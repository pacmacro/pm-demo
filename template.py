#!/usr/bin/python3
#
# This Python 3 file is a template for creating a demonstration script
# for a Pac Macro player. Fill in and modify the configurations below
# before executing the script.
#

import time

# Custom modules
import pacmacro

LOCAL_URL = "http://localhost:8080"
HEROKU_URL = "http://pacmacro.herokuapp.com"

# CONFIGURATIONS:

# Select the server to demo on
BASE_URL = LOCAL_URL

# Player's name (i.e. Pacman/Pinky/Inky/Blinky/Clyde)
PLAYER_NAME = "Pacman"

# The start and end coordinates between which the player should travel
# See the Pac Macro Server Wiki for Pacdot locations within the game map
LATITUDE_START  = 0
LONGITUDE_START = 0
LATITUDE_END    = 50
LONGITUDE_END   = -50

# The number of steps taken between the two coordinates
STEPS = 15

# The amount of seconds between each location update (not including
# request/response times)
DELAY_TIME = 0.7

if __name__ == "__main__":
    pacmacro.select_player(BASE_URL, PLAYER_NAME, LATITUDE_START, LONGITUDE_START)

    latitude_step = (LATITUDE_END - LATITUDE_START) / STEPS
    longitude_step = (LONGITUDE_END - LONGITUDE_START) / STEPS

    while True:
        for i in range(STEPS):
            pacmacro.set_player_location(
                    BASE_URL,
                    PLAYER_NAME,
                    LATITUDE_START + i*latitude_step,
                    LONGITUDE_START + i*longitude_step
            )
            time.sleep(DELAY_TIME)
        for i in range(STEPS, 0, -1):
            pacmacro.set_player_location(
                    BASE_URL,
                    PLAYER_NAME,
                    LATITUDE_START + i*latitude_step,
                    LONGITUDE_START + i*longitude_step
            )
            time.sleep(DELAY_TIME)
