from clients import Client, SpaceXClient
from custom_types import SpaceXQuery
import json
from models import Company, Ships, Landpads


# The following call the Models directly, returns data based off of cached
# or live data from the API:


refresh_data_time = 1  # Number of days between data pulls from the API

# Company data:
company = Company(refresh_data_time)
# company.fetch_data() # forces a fresh fetch from the API
# print(company.get_data())
# print(company.get_employees())
# print(company.get_location())
# print(company.get_valuation())

# Ships data:
ships = Ships(refresh_data_time)
# ships.fetch_data() # forces a fresh fetch from the API
# print(ships.get_heaviest_cached(5))
# print(ships.get_heaviest_live(5))

# print(ships.get_lightest_cached(5))
# print(ships.get_lightest_live(5))


# Landpads data:
landpads = Landpads(refresh_data_time)
# landpads.fetch_data()  # forces a fresh fetch from the API
# print(landpads.get_location_cached())
# print(landpads.get_location_live())


# Custom queries that one can use when calling the SpaceXClient directly
shipsQuery = {
    "query": {},  # No filter, fetch all ships
    "options": {
        "limit": 1,
        "sort": {
            "mass_kg": "desc"  # Sort by weight in descending order
        },
        "select": {
            "name": 1,
            "mass_kg": 1
        }
    }
}

landpadsQuery = {
    "query": {},  # No filter, fetch all ships
    "options": {
        "select": {
            "name": 1,
            "latitude": 1,
            "longitude": 1
        }
    }
}

spaceXClient = SpaceXClient()
# print(spaceXClient.get_company_data())
# print(spaceXClient.get_ships_data())
# print(spaceXClient.get_ships_data(shipsQuery))
# print(spaceXClient.get_ships_data(id="5ea6ed2d080df4000697c903"))

# print(spaceXClient.get_landpads_data())
# print(spaceXClient.get_landpads_data(landpadsQuery))
# print(spaceXClient.get_landpads_data(id="5e9e3033383ecbb9e534e7cc"))


# IGNORE BELOW: (TODO: DELETE)
# print(sorted(ships.get_heaviest_cached(5), key=lambda x: x["id"])
#       == sorted(ships.get_heaviest_live(5), key=lambda x: x["id"]))
# print(sorted(ships.get_lightest_cached(5), key=lambda x: x["id"])
#       == sorted(ships.get_lightest_live(5), key=lambda x: x["id"]))
# print(sorted(landpads.get_location_cached(), key=lambda x: x["id"])
#       == sorted(landpads.get_location_live(), key=lambda x: x["id"]))

# TO REMOVE PYCACHE FOLDERS: (TODO: DELETE)
# find . | grep -E "(/__pycache__$|\.pyc$|\.pyo$)" | xargs rm -rf
