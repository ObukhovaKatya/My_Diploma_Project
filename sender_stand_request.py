import requests
import configuration
import data

def post_new_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER,
        json=body,
        headers=data.headers
    )

def get_track_order(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.TRACK_ORDER + str(track),
        headers=data.headers
    )
