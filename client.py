import json
import requests

from track import Track
from playlist import Playlist

class SpotifyClient:
    def __init__(self, user_id, authorization_token):
        self.authorization_token = authorization_token
        self.user_id = user_id

    def get_last_played_tracks(self, limit = 10):
        url = f"https://api.spotify.com/v1/me/player/recently-played?limit={limit}"
        response = self._place_get_api_request(url)
        response_json = json()
        