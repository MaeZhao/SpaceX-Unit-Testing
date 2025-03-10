import pytest
from unittest.mock import patch
from clients import Client
from utils import fetch_paginated_data
import json
import requests


@pytest.fixture
def api_client():
    return Client("https://api.spacexdata.com/v4")


def test_simulate_fetch_success(api_client: Client):
    """
    Does not hit API, tests successful fetch
    Args:
        api_client (Client): _description_
    """
    with patch('clients.Client._get_request') as mock:
        mock.return_value.ok = True
        mock.return_value = {'last_ais_update': None, 'legacy_id': 'AMERICANSPIRIT', 'model': None, 'type': 'Cargo', 'roles': ['Support Ship'], 'imo': None, 'mmsi': None, 'abs': None, 'class': None, 'mass_kg': None, 'mass_lbs': None, 'year_built': None,
                             'home_port': 'Port of Los Angeles', 'status': None, 'speed_kn': None, 'course_deg': None, 'latitude': None, 'longitude': None, 'link': None, 'image': None, 'name': 'American Spirit', 'active': False, 'launches': ['5eb87ce1ffd86e000604b334'], 'id': '5ea6ed2d080df4000697c903'}
        result = api_client._fetch_data(
            "https://api.spacexdata.com/v4/ships/", id="5ea6ed2d080df4000697c903")
        assert isinstance(result, dict)
        assert result['name'] == "American Spirit"
        assert result['id'] == "5ea6ed2d080df4000697c903"


def test_simulate_timeout(api_client: Client):
    """
    Does not hit API, test error message when timeout occurs
    Args:
        api_client (Client): _description_
    """
    with patch('clients.Client._get_request') as mock:
        mock.side_effect = requests.exceptions.Timeout
        with pytest.raises(TimeoutError, match="Request timed out. Try again later."):
            api_client._fetch_data(endpoint="foo_url", id="123")


def test_simulate_request_exception(api_client: Client):
    """
    Does not hit API, test error message when Request Exception
    Args:
        api_client (Client): _description_
    """
    with patch('clients.Client._get_request') as mock:
        mock.side_effect = requests.exceptions.RequestException
        with pytest.raises(requests.exceptions.RequestException, match="API request failed: "):
            api_client._fetch_data(endpoint="foo_url", id="123")


def test_simulate_fetch_data(api_client: Client):
    """_summary_
    Does not hit API. Tests  _fetch_data() response
    Args:
        api_client (Client)
    """
    with patch('utils.fetch_paginated_data') as mock, \
            patch('clients.Client._post_request') as end_mock:
        end_mock.return_value.ok = True
        mock.return_value.ok = True
        end_mock.return_value = {"hasNextPage": False, "docs": [{'last_ais_update': None, 'legacy_id': 'AMERICANSPIRIT', 'model': None, 'type': 'Cargo', 'roles': ['Support Ship'], 'imo': None, 'mmsi': None, 'abs': None, 'class': None, 'mass_kg': None, 'mass_lbs': None, 'year_built': None,
                                 'home_port': 'Port of Los Angeles', 'status': None, 'speed_kn': None, 'course_deg': None, 'latitude': None, 'longitude': None, 'link': None, 'image': None, 'name': 'American Spirit', 'active': False, 'launches': ['5eb87ce1ffd86e000604b334'], 'id': '5ea6ed2d080df4000697c903'}]}
        result = api_client._fetch_data("foo_url")
        assert isinstance(result, list)
        assert result[0]['name'] == "American Spirit"
        assert result[0]['id'] == "5ea6ed2d080df4000697c903"


def test_get_request(api_client: Client):
    """_summary_
    Tests get_request
    Args:
        api_client (Client)
    """
    data = api_client._get_request("https://api.spacexdata.com/v4/company")
    assert isinstance(data, dict)
    assert 'name' in data
    assert 'founder' in data
    assert 'founded' in data
    assert data['name'] == "SpaceX"
    assert data['founder'] == "Elon Musk"
    assert data['founded'] == 2002


def test_post_request(api_client: Client):
    """_summary_
    Tests post_request
    Args:
        api_client (Client)
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
    data = api_client._post_request(
        "https://api.spacexdata.com/v4/ships/query", shipsQuery)
    assert isinstance(data, dict)
    assert 'docs' in data
    assert data['docs'] is not None
    assert len(data['docs']) == 1
