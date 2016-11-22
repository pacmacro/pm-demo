#!/usr/bin/python3

import time

# Custom modules
import pacmacro

LOCAL_URL = "http://localhost:8080"
HEROKU_URL = "http://pacmacro.herokuapp.com"

# CONFIGURATIONS:

# Select the server to demo on
BASE_URL = HEROKU_URL

# Player's name (i.e. Pacman/Pinky/Inky/Blinky/Clyde)
PLAYER_NAME = "Pacman"

# The start and end coordinates between which the player should travel
# See the Pac Macro Server Wiki for Pacdot locations within the game map
COORDINATE_1_LATITUDE  = 49.286575  # North
COORDINATE_1_LONGITUDE = -123.115834
COORDINATE_2_LATITUDE  = 49.284038  # East
COORDINATE_2_LONGITUDE = -123.111918
COORDINATE_3_LATITUDE  = 49.280098  # South
COORDINATE_3_LONGITUDE = -123.117852
COORDINATE_4_LATITUDE  = 49.282639
COORDINATE_4_LONGITUDE = -123.121772

# The amount of seconds between each location update (not including
# request/response times)
DELAY_TIME = 0.7

if __name__ == "__main__":
    pacmacro.select_player(
            BASE_URL, PLAYER_NAME,
            COORDINATE_1_LATITUDE, COORDINATE_1_LONGITUDE
    )

    step_1 = 6
    latitude_1_step = (COORDINATE_2_LATITUDE - COORDINATE_1_LATITUDE) / step_1
    longitude_1_step = (COORDINATE_2_LONGITUDE - COORDINATE_1_LONGITUDE) / step_1

    step_2 = 15
    latitude_2_step = (COORDINATE_3_LATITUDE - COORDINATE_2_LATITUDE) / step_2
    longitude_2_step = (COORDINATE_3_LONGITUDE - COORDINATE_2_LONGITUDE) / step_2

    step_3 = step_1
    latitude_3_step = (COORDINATE_4_LATITUDE - COORDINATE_3_LATITUDE) / step_3
    longitude_3_step = (COORDINATE_4_LONGITUDE - COORDINATE_3_LONGITUDE) / step_3

    step_4 = step_2
    latitude_4_step = (COORDINATE_1_LATITUDE - COORDINATE_4_LATITUDE) / step_4
    longitude_4_step = (COORDINATE_1_LONGITUDE - COORDINATE_4_LONGITUDE) / step_4

    while True:
        for i in range(step_1):
            pacmacro.set_player_location(
                    BASE_URL,
                    PLAYER_NAME,
                    COORDINATE_1_LATITUDE + i*latitude_1_step,
                    COORDINATE_1_LONGITUDE + i*longitude_1_step
            )
            time.sleep(DELAY_TIME)

        for i in range(step_2):
            pacmacro.set_player_location(
                    BASE_URL,
                    PLAYER_NAME,
                    COORDINATE_2_LATITUDE + i*latitude_2_step,
                    COORDINATE_2_LONGITUDE + i*longitude_2_step
            )
            time.sleep(DELAY_TIME)

        for i in range(step_3):
            pacmacro.set_player_location(
                    BASE_URL,
                    PLAYER_NAME,
                    COORDINATE_3_LATITUDE + i*latitude_3_step,
                    COORDINATE_3_LONGITUDE + i*longitude_3_step
            )
            time.sleep(DELAY_TIME)

        for i in range(step_4):
            pacmacro.set_player_location(
                    BASE_URL,
                    PLAYER_NAME,
                    COORDINATE_4_LATITUDE + i*latitude_4_step,
                    COORDINATE_4_LONGITUDE + i*longitude_4_step
            )
            time.sleep(DELAY_TIME)
