#
# Python 3 module with simple HTTP utilities specifically for the Pac Macro
# demonstration scripts.
#

import json
import requests

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

def start_game(base_url):
    log_response(requests.put(
            base_url + "/admin/gamestate",
            headers = HEADERS,
            data = create_json_state_body("IN_PROGRESS")
    ))

def select_player(base_url, name, coordinate):
    log_response(requests.post(
            base_url + "/player/" + name,
            headers = HEADERS,
            data = create_json_coordinate_body(coordinate)
    ))

def set_player_location(base_url, name, coordinate):
    log_response(requests.put(
            base_url + "/player/" + name + "/location",
            headers = HEADERS,
            data = create_json_coordinate_body(coordinate)
    ))
