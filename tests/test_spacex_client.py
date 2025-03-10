import pytest
from unittest.mock import patch
from clients import SpaceXClient
import json


@pytest.fixture
def api_client():
    return SpaceXClient()


def test_simulate_get_company_data(api_client: SpaceXClient):
    """_summary_
    Does not hit the SpaceX API, tests get_company_data() response
    Args:
        api_client (SpaceXClient)
    """
    with patch("clients.SpaceXClient._fetch_data") as mock:
        mock.return_value.ok = True
        mock.return_value.json.return_value = {'headquarters': {'address': 'Rocket Road', 'city': 'Hawthorne', 'state': 'California'}, 'links': {'website': 'https://www.spacex.com/', 'flickr': 'https://www.flickr.com/photos/spacex/', 'twitter': 'https://twitter.com/SpaceX', 'elon_twitter': 'https://twitter.com/elonmusk'}, 'name': 'SpaceX', 'founder': 'Elon Musk', 'founded': 2002, 'employees': 9500, 'vehicles': 4,
                                               'launch_sites': 3, 'test_sites': 3, 'ceo': 'Elon Musk', 'cto': 'Elon Musk', 'coo': 'Gwynne Shotwell', 'cto_propulsion': 'Tom Mueller', 'valuation': 74000000000, 'summary': 'SpaceX designs, manufactures and launches advanced rockets and spacecraft. The company was founded in 2002 to revolutionize space technology, with the ultimate goal of enabling people to live on other planets.', 'id': '5eb75edc42fea42237d7f3ed'}
        result = api_client.get_company_data()
        assert result['name'] == "SpaceX"
        assert result['founder'] == "Elon Musk"
        assert result['founded'] == 2002


def test_simulate_get_ships_data(api_client: SpaceXClient):
    """_summary_
    Does not hit the SpaceX API, test get_ships_data with no query
    Args:
        api_client (SpaceXClient)
    """
    with patch("clients.SpaceXClient._fetch_data") as mock:
        mock.return_value.ok = True
        mock.return_value = [{"last_ais_update": None, "legacy_id": "AMERICANCHAMPION", "model": None, "type": "Tug", "roles": ["Support Ship", "Barge Tug"], "imo": 7434016, "mmsi": 367020820, "abs": 571252, "class": 7604342, "mass_kg": 266712, "mass_lbs": 588000, "year_built": 1976, "home_port": "Port of Los Angeles", "status": "", "speed_kn": None, "course_deg": None, "latitude": None, "longitude": None, "link": "https://www.marinetraffic.com/en/ais/details/ships/shipid:434663/mmsi:367020820/imo:7434016/vessel:AMERICAN_CHAMPION", "image": "https://i.imgur.com/woCxpkj.jpg", "name": "American Champion", "active": False, "launches": ["5eb87cdeffd86e000604b330", "5eb87cdfffd86e000604b331"], "id": "5ea6ed2d080df4000697c901"}, {"last_ais_update": None, "legacy_id": "AMERICANISLANDER", "model": None, "type": "Cargo", "roles": ["Dragon Recovery"], "imo": None, "mmsi": 367035570, "abs": None, "class": None, "mass_kg": None, "mass_lbs": None, "year_built": None, "home_port": "Port of Los Angeles",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              "status": "", "speed_kn": None, "course_deg": None, "latitude": None, "longitude": None, "link": "https://www.marinetraffic.com/en/ais/details/ships/shipid:435112/mmsi:367035570/imo:0/vessel:AMERICAN_ISLANDER", "image": "https://i.imgur.com/jmj8Sh2.jpg", "name": "American Islander", "active": False, "launches": ["5eb87ce0ffd86e000604b332", "5eb87ce1ffd86e000604b333", "5eb87ce4ffd86e000604b337", "5eb87ce7ffd86e000604b33b"], "id": "5ea6ed2d080df4000697c902"}, {"last_ais_update": None, "legacy_id": "AMERICANSPIRIT", "model": None, "type": "Cargo", "roles": ["Support Ship"], "imo": None, "mmsi": None, "abs": None, "class": None, "mass_kg": None, "mass_lbs": None, "year_built": None, "home_port": "Port of Los Angeles", "status": None, "speed_kn": None, "course_deg": None, "latitude": None, "longitude": None, "link": None, "image": None, "name": "American Spirit", "active": False, "launches": ["5eb87ce1ffd86e000604b334"], "id": "5ea6ed2d080df4000697c903"}]
        result = api_client.get_ships_data()
        assert isinstance(result, list)
        assert result[0]["mass_kg"] == 266712


def test_simulate_get_ships_data_query(api_client: SpaceXClient):
    """_summary_
    Does not hit the SpaceX API, test get_ships_data with query
    Args:
        api_client (SpaceXClient)
    """
    with patch("clients.SpaceXClient._fetch_data") as mock:
        mock.return_value.ok = True
        mock.return_value = [{"last_ais_update": None, "legacy_id": "AMERICANCHAMPION", "model": None, "type": "Tug", "roles": ["Support Ship", "Barge Tug"], "imo": 7434016, "mmsi": 367020820, "abs": 571252, "class": 7604342, "mass_kg": 266712, "mass_lbs": 588000, "year_built": 1976, "home_port": "Port of Los Angeles", "status": "", "speed_kn": None, "course_deg": None, "latitude": None, "longitude": None, "link": "https://www.marinetraffic.com/en/ais/details/ships/shipid:434663/mmsi:367020820/imo:7434016/vessel:AMERICAN_CHAMPION", "image": "https://i.imgur.com/woCxpkj.jpg", "name": "American Champion", "active": False, "launches": ["5eb87cdeffd86e000604b330", "5eb87cdfffd86e000604b331"], "id": "5ea6ed2d080df4000697c901"}, {"last_ais_update": None, "legacy_id": "AMERICANISLANDER", "model": None, "type": "Cargo", "roles": ["Dragon Recovery"], "imo": None, "mmsi": 367035570, "abs": None, "class": None, "mass_kg": None, "mass_lbs": None, "year_built": None, "home_port": "Port of Los Angeles",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              "status": "", "speed_kn": None, "course_deg": None, "latitude": None, "longitude": None, "link": "https://www.marinetraffic.com/en/ais/details/ships/shipid:435112/mmsi:367035570/imo:0/vessel:AMERICAN_ISLANDER", "image": "https://i.imgur.com/jmj8Sh2.jpg", "name": "American Islander", "active": False, "launches": ["5eb87ce0ffd86e000604b332", "5eb87ce1ffd86e000604b333", "5eb87ce4ffd86e000604b337", "5eb87ce7ffd86e000604b33b"], "id": "5ea6ed2d080df4000697c902"}, {"last_ais_update": None, "legacy_id": "AMERICANSPIRIT", "model": None, "type": "Cargo", "roles": ["Support Ship"], "imo": None, "mmsi": None, "abs": None, "class": None, "mass_kg": None, "mass_lbs": None, "year_built": None, "home_port": "Port of Los Angeles", "status": None, "speed_kn": None, "course_deg": None, "latitude": None, "longitude": None, "link": None, "image": None, "name": "American Spirit", "active": False, "launches": ["5eb87ce1ffd86e000604b334"], "id": "5ea6ed2d080df4000697c903"}]
        result = api_client.get_ships_data(query={"query": {}})
        assert isinstance(result, list)
        assert result[0]["mass_kg"] == 266712


def test_simulate_get_ships_data_id(api_client: SpaceXClient):
    """_summary_
    Does not hit the SpaceX API, test get_ships_data with id
    Args:
        api_client (SpaceXClient)
    """
    with patch("clients.SpaceXClient._fetch_data") as mock:
        mock.return_value.ok = True
        mock.return_value = {"last_ais_update": None, "legacy_id": "AMERICANCHAMPION", "model": None, "type": "Tug", "roles": ["Support Ship", "Barge Tug"], "imo": 7434016, "mmsi": 367020820, "abs": 571252, "class": 7604342, "mass_kg": 266712, "mass_lbs": 588000, "year_built": 1976, "home_port": "Port of Los Angeles", "status": "", "speed_kn": None, "course_deg": None,
                             "latitude": None, "longitude": None, "link": "https://www.marinetraffic.com/en/ais/details/ships/shipid:434663/mmsi:367020820/imo:7434016/vessel:AMERICAN_CHAMPION", "image": "https://i.imgur.com/woCxpkj.jpg", "name": "American Champion", "active": False, "launches": ["5eb87cdeffd86e000604b330", "5eb87cdfffd86e000604b331"], "id": "5ea6ed2d080df4000697c901"}
        result = api_client.get_ships_data(id="id_foo")
        assert isinstance(result, dict)
        assert result["mass_kg"] == 266712


def test_simulate_get_landpads_data(api_client: SpaceXClient):
    """_summary_
    Does not hit the SpaceX API, test get_landpads_data with no query
    Args:
        api_client (SpaceXClient)
    """
    with patch("clients.SpaceXClient._fetch_data") as mock:
        mock.return_value.ok = True
        mock.return_value = [{"last_ais_update": None, "legacy_id": "AMERICANCHAMPION", "model": None, "type": "Tug", "roles": ["Support Ship", "Barge Tug"], "imo": 7434016, "mmsi": 367020820, "abs": 571252, "class": 7604342, "mass_kg": 266712, "mass_lbs": 588000, "year_built": 1976, "home_port": "Port of Los Angeles", "status": "", "speed_kn": None, "course_deg": None, "latitude": None, "longitude": None, "link": "https://www.marinetraffic.com/en/ais/details/ships/shipid:434663/mmsi:367020820/imo:7434016/vessel:AMERICAN_CHAMPION", "image": "https://i.imgur.com/woCxpkj.jpg", "name": "American Champion", "active": False, "launches": ["5eb87cdeffd86e000604b330", "5eb87cdfffd86e000604b331"], "id": "5ea6ed2d080df4000697c901"}, {"last_ais_update": None, "legacy_id": "AMERICANISLANDER", "model": None, "type": "Cargo", "roles": ["Dragon Recovery"], "imo": None, "mmsi": 367035570, "abs": None, "class": None, "mass_kg": None, "mass_lbs": None, "year_built": None, "home_port": "Port of Los Angeles",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              "status": "", "speed_kn": None, "course_deg": None, "latitude": None, "longitude": None, "link": "https://www.marinetraffic.com/en/ais/details/ships/shipid:435112/mmsi:367035570/imo:0/vessel:AMERICAN_ISLANDER", "image": "https://i.imgur.com/jmj8Sh2.jpg", "name": "American Islander", "active": False, "launches": ["5eb87ce0ffd86e000604b332", "5eb87ce1ffd86e000604b333", "5eb87ce4ffd86e000604b337", "5eb87ce7ffd86e000604b33b"], "id": "5ea6ed2d080df4000697c902"}, {"last_ais_update": None, "legacy_id": "AMERICANSPIRIT", "model": None, "type": "Cargo", "roles": ["Support Ship"], "imo": None, "mmsi": None, "abs": None, "class": None, "mass_kg": None, "mass_lbs": None, "year_built": None, "home_port": "Port of Los Angeles", "status": None, "speed_kn": None, "course_deg": None, "latitude": None, "longitude": None, "link": None, "image": None, "name": "American Spirit", "active": False, "launches": ["5eb87ce1ffd86e000604b334"], "id": "5ea6ed2d080df4000697c903"}]
        result = api_client.get_landpads_data()
        assert isinstance(result, list)
        assert result[0]["mass_kg"] == 266712


def test_simulate_get_landpads_data_query(api_client: SpaceXClient):
    """_summary_
    Does not hit the SpaceX API, test get_landpads_data with query
    Args:
        api_client (SpaceXClient)
    """
    with patch("clients.SpaceXClient._fetch_data") as mock:
        mock.return_value.ok = True
        mock.return_value = [{"last_ais_update": None, "legacy_id": "AMERICANCHAMPION", "model": None, "type": "Tug", "roles": ["Support Ship", "Barge Tug"], "imo": 7434016, "mmsi": 367020820, "abs": 571252, "class": 7604342, "mass_kg": 266712, "mass_lbs": 588000, "year_built": 1976, "home_port": "Port of Los Angeles", "status": "", "speed_kn": None, "course_deg": None, "latitude": None, "longitude": None, "link": "https://www.marinetraffic.com/en/ais/details/ships/shipid:434663/mmsi:367020820/imo:7434016/vessel:AMERICAN_CHAMPION", "image": "https://i.imgur.com/woCxpkj.jpg", "name": "American Champion", "active": False, "launches": ["5eb87cdeffd86e000604b330", "5eb87cdfffd86e000604b331"], "id": "5ea6ed2d080df4000697c901"}, {"last_ais_update": None, "legacy_id": "AMERICANISLANDER", "model": None, "type": "Cargo", "roles": ["Dragon Recovery"], "imo": None, "mmsi": 367035570, "abs": None, "class": None, "mass_kg": None, "mass_lbs": None, "year_built": None, "home_port": "Port of Los Angeles",
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              "status": "", "speed_kn": None, "course_deg": None, "latitude": None, "longitude": None, "link": "https://www.marinetraffic.com/en/ais/details/ships/shipid:435112/mmsi:367035570/imo:0/vessel:AMERICAN_ISLANDER", "image": "https://i.imgur.com/jmj8Sh2.jpg", "name": "American Islander", "active": False, "launches": ["5eb87ce0ffd86e000604b332", "5eb87ce1ffd86e000604b333", "5eb87ce4ffd86e000604b337", "5eb87ce7ffd86e000604b33b"], "id": "5ea6ed2d080df4000697c902"}, {"last_ais_update": None, "legacy_id": "AMERICANSPIRIT", "model": None, "type": "Cargo", "roles": ["Support Ship"], "imo": None, "mmsi": None, "abs": None, "class": None, "mass_kg": None, "mass_lbs": None, "year_built": None, "home_port": "Port of Los Angeles", "status": None, "speed_kn": None, "course_deg": None, "latitude": None, "longitude": None, "link": None, "image": None, "name": "American Spirit", "active": False, "launches": ["5eb87ce1ffd86e000604b334"], "id": "5ea6ed2d080df4000697c903"}]
        result = api_client.get_landpads_data(query={"query": {}})
        assert isinstance(result, list)
        assert result[0]["mass_kg"] == 266712


def test_simulate_get_landpads_data_id(api_client: SpaceXClient):
    """_summary_
    Does not hit the SpaceX API, test get_landpads_data with id
    Args:
        api_client (SpaceXClient)
    """
    with patch("clients.SpaceXClient._fetch_data") as mock:
        mock.return_value.ok = True
        mock.return_value = {"last_ais_update": None, "legacy_id": "AMERICANCHAMPION", "model": None, "type": "Tug", "roles": ["Support Ship", "Barge Tug"], "imo": 7434016, "mmsi": 367020820, "abs": 571252, "class": 7604342, "mass_kg": 266712, "mass_lbs": 588000, "year_built": 1976, "home_port": "Port of Los Angeles", "status": "", "speed_kn": None, "course_deg": None,
                             "latitude": None, "longitude": None, "link": "https://www.marinetraffic.com/en/ais/details/ships/shipid:434663/mmsi:367020820/imo:7434016/vessel:AMERICAN_CHAMPION", "image": "https://i.imgur.com/woCxpkj.jpg", "name": "American Champion", "active": False, "launches": ["5eb87cdeffd86e000604b330", "5eb87cdfffd86e000604b331"], "id": "5ea6ed2d080df4000697c901"}
        result = api_client.get_landpads_data(id="id_foo")
        assert isinstance(result, dict)
        assert result["mass_kg"] == 266712


def test_simulate_check_args(api_client: SpaceXClient):
    """
    Tests error message when id and query are asserted
    Args:
        api_client (SpaceXClient): _description_
    """
    with pytest.raises(ValueError, match="Cannot take in an id argument and query argument"):
        api_client._check_args(id="abc", query={"query": {}, "options": {}})


def test_get_company_data(api_client: SpaceXClient):
    """_summary_
    Hits the SpaceX API, tests get_company_data() response

    Args:
        api_client (SpaceXClient)
    """
    data = api_client.get_company_data()

    assert isinstance(data, dict)


def test_get_ships_data_query(api_client: SpaceXClient):
    """_summary_
    Hits the SpaceX API, tests get_ships_data() response

    Args:
        api_client (SpaceXClient)
    """
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
    data = api_client.get_ships_data(shipsQuery)

    assert isinstance(data, list)
    assert len(data) == 1


def test_get_ships_data_id(api_client: SpaceXClient):
    """_summary_
    Hits the SpaceX API, tests get_ships_data() response

    Args:
        api_client (SpaceXClient)
    """
    data = api_client.get_ships_data(id="5ea6ed2d080df4000697c903")

    assert isinstance(data, dict)
    assert data['id'] == "5ea6ed2d080df4000697c903"


def test_get_landpads_data_query(api_client: SpaceXClient):
    """_summary_
    Hits the SpaceX API, tests get_landpads_data() response

    Args:
        api_client (SpaceXClient)
    """
    landpadsQuery = {
        "query": {},  # No filter, fetch all ships
        "options": {
            "limit": 1,
            "select": {
                "name": 1,
                "latitude": 1,
                "longitude": 1
            }
        }
    }

    data = api_client.get_landpads_data(landpadsQuery)

    assert isinstance(data, list)
    assert len(data) == 1


def test_get_landpads_data_id(api_client: SpaceXClient):
    """_summary_
    Hits the SpaceX API, tests get_landpads_data() response

    Args:
        api_client (SpaceXClient)
    """
    data = api_client.get_landpads_data(id="5e9e3033383ecbb9e534e7cc")

    assert isinstance(data, dict)
    assert data['id'] == "5e9e3033383ecbb9e534e7cc"
