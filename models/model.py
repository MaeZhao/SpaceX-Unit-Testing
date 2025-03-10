from clients import SpaceXClient
from datetime import datetime, timedelta
import json
from abc import ABC, abstractmethod


class Model(object):

    def __init__(self, file_path: str, reload_day_schedule: float = None):
        """
        Initializes model object
        Args:
            file_path (str): file path of object
            reload_day_schedule (int) (Optional): the number of days in between 
            loading new data, defaults to 1
        """
        self.client = SpaceXClient()
        self.LATEST_FILE = file_path
        self.data = {}
        if reload_day_schedule is None:
            reload_day_schedule = float(1)
        self.load_schedule_days = reload_day_schedule
        self.load_latest_fetch()

    def get_data(self):
        """
        Gets all model data
        Returns:
            list
        """
        return self.data['data']

    @abstractmethod
    def fetch_data(self):
        """
        Fetches data from API
        """
        pass

    def load_latest_fetch(self):
        """
          Loads cached data. If cached data DNE or the number of days in between
          current request and last fetch is greater than the specified reload 
          day schedule
        """
        latest_fetch = None
        try:
            with open(self.LATEST_FILE, 'r') as f:
                data = json.load(f)
                latest_fetch = datetime.fromisoformat(
                    data['last_fetch'])
                if latest_fetch + timedelta(days=self.load_schedule_days) < datetime.now():
                    raise ValueError
                else:
                    self.data = data
        except:
            if latest_fetch is not None:
                print(
                    f"Last loaded file: {latest_fetch}. Fetching new data from database")
            else:
                print("No loaded file, fetching new data from database")
            self.fetch_data()
