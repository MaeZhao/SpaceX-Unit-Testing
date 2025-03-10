from .client import Client
from custom_types import SpaceXQuery, paginateQuery
from dataclasses import asdict


class SpaceXClient(Client):
    def __init__(self):
        super().__init__("https://api.spacexdata.com/v4")

    def _check_args(self, id: str = None, query: SpaceXQuery = None):
        if id is not None:
            if query is not None:
                raise ValueError(
                    "Cannot take in an id argument and query argument")
        else:
            return

    def _set_args(self, id: str = None, query: SpaceXQuery = None) -> SpaceXQuery | None:
        """
        Sets the SpaceXClient get arguments to the proper values

        Args:
            id (str, optional): Defaults to None.
            query (SpaceXQuery, optional): Dictionary following SpaceXQuery structure. Defaults to None.
        Returns:
            SpaceXQuery | None
        """
        self._check_args(id, query)
        if query is SpaceXQuery:
            query = asdict(query)
        return query

    def get_company_data(self):
        """
        Gets general SpaceX company data

        Returns:
            JSON or None: Returns JSON encoded response if any
        """
        endpoint = f"{self.API_URL}/company"
        return self._get_request(endpoint)

    def get_ships_data(self, query: SpaceXQuery = None, id: str = None):
        """
        Gets ship data. If query not provided, will return all data.

        Args:
            query (SpaceXQuery, optional): Dictionary following SpaceXQuery structure. Defaults to None.
            id (str, optional): id particular item, cannot have simultaneously with query

        Returns:
            JSON or None: Returns JSON encoded response if any
        """
        endpoint = f"{self.API_URL}/ships"
        query = self._set_args(id, query)
        return self._fetch_data(endpoint, id, query)

    def get_landpads_data(self, query: SpaceXQuery = None, id: str = None):
        """
        Gets landing pads data. If query not provided, will return all data.
        Args:
            query (SpaceXQuery, optional): Dictionary following SpaceXQuery structure. Defaults to None.
            id (str, optional): id particular item, cannot have simultaneously with query

        Returns:
            JSON or None: Returns JSON encoded response if any
        """
        endpoint = f"{self.API_URL}/landpads"
        query = self._set_args(id, query)

        return self._fetch_data(endpoint, id, query)
