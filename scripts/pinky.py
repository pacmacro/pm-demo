#!/usr/bin/python3

import configparser
import os

# Custom modules
import pacmacro.api

# CONFIGURATIONS:

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

def main(config):
    server_config = config["Server"]
    url = server_config.get("url") + ":" + str(server_config.getint("port"))
    
    pacmacro.api.select_player(url, PLAYER_NAME, COORDINATE_START)

    while True:
        pacmacro.api.move_player(
                url, PLAYER_NAME,
                COORDINATE_START, COORDINATE_END,
                STEPS, DELAY_SECS
        )
        pacmacro.api.move_player(
                url, PLAYER_NAME,
                COORDINATE_END, COORDINATE_START,
                STEPS, DELAY_SECS
        )

if __name__ == "__main__":
    location = os.path.realpath(
        os.path.join(os.getcwd(), os.path.dirname(__file__)))
    config_filename = os.path.join(location, "cfg/target-server.cfg")
    config = configparser.ConfigParser()
    config.read(config_filename)
    
    try:
        main(config)
    except Exception as e:
        raise