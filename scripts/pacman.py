#!/usr/bin/python3

import configparser
import os

# Custom modules
import pacmacro.api

# Player's name (i.e. Pacman/Pinky/Inky/Blinky/Clyde)
PLAYER_NAME = "Pacman"

# The start and end coordinates between which the player should travel
# See the Pac Macro Server Wiki for Pacdot locations within the game map

# Hastings and Hornby
COORDINATE_NORTH = {"latitude": 49.286575, "longitude": -123.115834}
# Hastings and Richards
COORDINATE_EAST  = {"latitude": 49.284038, "longitude": -123.111918}
# Robson and Richards
COORDINATE_SOUTH = {"latitude": 49.280098, "longitude": -123.117852}
# Robson and Hornby
COORDINATE_WEST  = {"latitude": 49.282639, "longitude": -123.121772}

# The number of steps taken between the coordinates
STEPS_NORTH_EAST = 7
STEPS_EAST_SOUTH = 12
STEPS_SOUTH_WEST = STEPS_NORTH_EAST
STEPS_WEST_NORTH = STEPS_EAST_SOUTH

# The amount of seconds between each location update (not including
# request/response times)
DELAY_SECS = 0.5

def main(config):
    server_config = config["Server"]
    url = server_config.get("url") + ":" + str(server_config.getint("port"))

    pacmacro.api.select_player(url, PLAYER_NAME, COORDINATE_NORTH)

    while True:
        pacmacro.api.move_player(
                url, PLAYER_NAME,
                COORDINATE_NORTH, COORDINATE_EAST,
                STEPS_NORTH_EAST, DELAY_SECS
        )
        pacmacro.api.move_player(
                url, PLAYER_NAME,
                COORDINATE_EAST, COORDINATE_SOUTH,
                STEPS_EAST_SOUTH, DELAY_SECS
        )
        pacmacro.api.move_player(
                url, PLAYER_NAME,
                COORDINATE_SOUTH, COORDINATE_WEST,
                STEPS_SOUTH_WEST, DELAY_SECS
        )
        pacmacro.api.move_player(
                url, PLAYER_NAME,
                COORDINATE_WEST, COORDINATE_NORTH,
                STEPS_WEST_NORTH, DELAY_SECS
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