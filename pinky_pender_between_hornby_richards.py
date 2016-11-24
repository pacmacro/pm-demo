#!/usr/bin/python3

# Custom modules
import pacmacro

LOCAL_URL = "http://localhost:8080"
HEROKU_URL = "http://pacmacro.herokuapp.com"

# CONFIGURATIONS:

# Select the server to demo on
BASE_URL = LOCAL_URL

# Player's name (i.e. Pacman/Pinky/Inky/Blinky/Clyde)
PLAYER_NAME = "Pinky"

# The start and end coordinates between which the player should travel
# See the Pac Macro Server Wiki for Pacdot locations within the game map

# Pender and Hornby
COORDINATE_START = {"latitude": 49.285931, "longitude": -123.116808}
# Pender and Richards
COORDINATE_END = {"latitude": 49.283387, "longitude": -123.112884}

# The number of steps taken between the two coordinates
STEPS = 8

# The amount of seconds between each location update (not including
# request/response times)
DELAY_SECS = 0.7

if __name__ == "__main__":
    pacmacro.select_player(BASE_URL, PLAYER_NAME, COORDINATE_START)

    while True:
        pacmacro.move_player(
                BASE_URL, PLAYER_NAME,
                COORDINATE_START, COORDINATE_END,
                STEPS, DELAY_SECS
        )
        pacmacro.move_player(
                BASE_URL, PLAYER_NAME,
                COORDINATE_END, COORDINATE_START,
                STEPS, DELAY_SECS
        )
