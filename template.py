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
COORDINATE_START = {"latitude": 0, "longitude": 0}
COORDINATE_END = {"latitude": 50, "longitude": -50}

# The number of steps taken between the two coordinates
STEPS = 15

# The amount of seconds between each location update (not including
# request/response times)
DELAY_TIME = 0.7

if __name__ == "__main__":
    pacmacro.select_player(BASE_URL, PLAYER_NAME, COORDINATE_START)

    while True:
        pacmacro.move_player(
                BASE_URL, PLAYER_NAME,
                COORDINATE_START, COORDINATE_END,
                STEPS, DELAY_TIME
        )
        pacmacro.move_player(
                BASE_URL, PLAYER_NAME,
                COORDINATE_END, COORDINATE_START,
                STEPS, DELAY_TIME
        )
