TO TEST: python3 -m pytest

TO RUN:
- pip3 install -r requirements.txt
- See code __init__.py in root folder that lists out useful calls 

Documentation:
- see /documentation/ for html documentation generated via pydoc

Notable code:
- /utils/data_fetching.py addresses scalability of large requests by processing data via pagination
- /tests/ contains test codes covering core functionality (see modules in clients folder)
- /model/model addresses scalability of efficient data processing through fetching data on an predefined schedule. Contains code that caches data into the root folder. Method load_latest_fetch() checks the recorded time of the last fetch call, and compares it with the specified/defaulted data update schedule. If the (current time - last recorded time) surpasses the indicated update schedule, fetches fresh data from api. 
- Flexible coding is exercised via custom parent classes like /clients/client.py and models/model.py
- Flexible coding is exercised in /clients/ folder and /custom_types/ folder. Methods in /clients/spacex_client.py allow users query data whenever possible. The /custom_types/ folder contains a dataclass called SpaceXQuery that outlines the general query structure for post requests with the Space X API. The custom defined dataclass can help users figure out how to write a custom query for the API. 
- Resilience is exercised via try/except in /clients/client.py. Requests contain timeout constraints, and raises timeout exceptions as well as Request Exception failure.ss