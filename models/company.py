from clients import SpaceXClient
from datetime import datetime, timedelta
import json
from .model import Model


class Company(Model):

    def __init__(self, reload_day_schedule: int = None):
        super().__init__("company.json", reload_day_schedule)

    def fetch_data(self):
        with open(self.LATEST_FILE, 'w') as f:
            new_data = {}
            new_data['data'] = self.client.get_company_data()
            new_data['last_fetch'] = datetime.now().isoformat()
            self.data = new_data
            json.dump(new_data, f)

    def get_location(self):
        """
        Gets location of company
        Returns:
           list
        """
        return self.data['data']['headquarters']

    def get_employees(self):
        """
        Gets the number of employees

        Returns:
            list
        """
        return self.data['data']['employees']

    def get_valuation(self):
        """
        Gets the valuation
        Returns:
            list
        """
        return self.data['data']['valuation']
