from clients import SpaceXClient
from datetime import datetime, timedelta
import json
from .model import Model
from heapq import nlargest, nsmallest


class Ships(Model):

    def __init__(self, reload_day_schedule: int = None):
        super().__init__("ships.json", reload_day_schedule)

    def fetch_data(self):
        with open(self.LATEST_FILE, 'w') as f:
            new_data = {}
            new_data['data'] = self.client.get_ships_data()
            new_data['last_fetch'] = datetime.now().isoformat()
            self.data = new_data
            json.dump(new_data, f)

    def get_heaviest_live(self, n: int):
        """
        Requests the n heaviest ships from API

        Args:
            n (int): specified number of ships

        Returns:
            list
        """
        shipsQuery = {
            "query": {
                'mass_kg': {'$ne': None}  # Filters out ships without mass
            },
            "options": {
                "sort": {
                    "mass_kg": "desc"  # Sort by weight in descending order
                }
            }
        }
        ships = self.client.get_ships_data(shipsQuery)
        top_n_ships = ships[:n]
        return top_n_ships

    def get_heaviest_cached(self, n: int):
        """
        Gets the n heaviest ships from cached data
        Args:
            n (int): specified number of ships

        Returns:
            list
        """
        # Filter out ships without mass
        ships = list(
            filter(lambda x: x['mass_kg'] is not None, self.data['data']))
        ships = sorted(ships,
                       key=lambda x: x['mass_kg'] if x['mass_kg'] else 0, reverse=True)
        top_n_ships = ships[:n]
        return top_n_ships

    def get_lightest_live(self, n: int):
        """
        Requests the n lightest ships from the API

        Args:
            n (int): the specified number of ships

        Returns:
            list
        """
        shipsQuery = {
            "query": {
                'mass_kg': {'$ne': None}  # Filter out ships without mass
            },
            "options": {
                "sort": {
                    "mass_kg": "asc"  # Sort by weight in ascending order
                }
            }
        }
        ships = self.client.get_ships_data(shipsQuery)
        top_n_ships = ships[:n]
        return top_n_ships

    def get_lightest_cached(self, n: int):
        """
        Gets the n lightest number of ships from cached data

        Args:
            n (int): specified number of ships

        Returns:
            list
        """
        # Filter out ships without mass
        ships = list(
            filter(lambda x: x['mass_kg'] is not None, self.data['data']))
        ships = sorted(ships,
                       key=lambda x: x['mass_kg'] if x['mass_kg'] else 0)
        top_n_ships = ships[:n]
        return top_n_ships
