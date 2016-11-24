#
# Python 3 module with simple HTTP utilities specifically for the Pac Macro
# demonstration scripts.
#

import json
import requests
import time

HEADERS = {"Content-Type":"application/json"}

def create_json_coordinate_body(coordinate):
    return json.dumps({
            "latitude": coordinate.get("latitude"),
            "longitude": coordinate.get("longitude")
    })

def create_json_state_body(state):
    return json.dumps({"state":state})

def log_response(response):
    print(
            "[REQUEST ] " + response.request.method + " " +
            response.url + " | " +
            "JSON body: " + response.request.body
    )
    print(
            "[RESPONSE] HTTP " + str(response.status_code) + " | " +
            "JSON body: " + response.text
    )
    print()

def select_player(base_url, player_name, coordinate):
    log_response(requests.post(
            base_url + "/player/" + player_name,
            headers = HEADERS,
            data = create_json_coordinate_body(coordinate)
    ))

def set_player_location(base_url, player_name, coordinate):
    log_response(requests.put(
            base_url + "/player/" + player_name + "/location",
            headers = HEADERS,
            data = create_json_coordinate_body(coordinate)
    ))

def move_player(
        base_url, player_name,
        coordinate_start, coordinate_end,
        steps, delay_secs):

    latitude_step = (
            (coordinate_end.get("latitude") - coordinate_start.get("latitude"))
            / steps
    )
    longitude_step = (
            (coordinate_start.get("longitude") -
            coordinate_start.get("longitude"))
            / steps
    )

    new_coordinate = coordinate_start.copy()
    for i in range(steps):
        new_coordinate["latitude"] = \
                coordinate_start.get("latitude") + i*latitude_step
        new_coordinate["longitude"] = \
                coordinate_start.get("longitude") + i*longitude_step

        set_player_location(
                base_url, player_name, new_coordinate
        )
        time.sleep(delay_secs)
