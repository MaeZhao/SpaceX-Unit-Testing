from clients import SpaceXClient
from datetime import datetime, timedelta
import json
from .model import Model


class Landpads(Model):

    def __init__(self, reload_day_schedule: int = None):
        super().__init__("landpads.json", reload_day_schedule)

    def fetch_data(self):
        with open(self.LATEST_FILE, 'w') as f:
            new_data = {}
            new_data['data'] = self.client.get_landpads_data()
            new_data['last_fetch'] = datetime.now().isoformat()
            self.data = new_data
            json.dump(new_data, f)

    def get_location_live(self):
        """
        Requests location of all landpads from API

        Returns:
            list
        """
        landpadsQuery = {
            "query": {},  # No filter, fetch all ships
            "options": {
                "select": {
                    "name": 1,
                    "latitude": 1,
                    "longitude": 1,
                    "id": 1
                }
            }
        }
        locations = self.client.get_landpads_data(landpadsQuery)
        return locations

    def get_location_cached(self):
        """
        Gets locations of all landpads from cached data

        Returns:
            list
        """
        landpads = self.data['data']
        locations = list(map(lambda x: {
            "name": x['name'],
            'latitude': x['latitude'],
            'longitude': x['longitude'],
            'id': x['id']
        }, landpads))
        return locations
