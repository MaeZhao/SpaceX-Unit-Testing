from clients import client


def fetch_paginated_data(client: client, endpoint: str, query: dict = None):
    """
      Pagination handling, fetches data in chunks.
      Args:
          endpoint (str): endpoint url
          query (dict, optional): Defaults to None.
      Returns:
          JSON or None: Returns JSON encoded response if any
    """
    if query is None:
        query = {
            'query': {},
            'options': {
                'pagination': True
            }}
    first_page = client._post_request(endpoint, query)
    data = first_page['docs']
    hasNextPage = first_page['hasNextPage']

    query['options']['page'] = 1

    while hasNextPage:
        query['options']['page'] += 1
        new_page = client._post_request(endpoint, query)
        hasNextPage = new_page['hasNextPage']
        data.extend(new_page['docs'])
    return data
