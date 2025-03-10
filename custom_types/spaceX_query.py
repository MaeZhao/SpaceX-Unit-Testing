from dataclasses import dataclass, field
from typing import Optional


@dataclass
class SpaceXQuery:
    """
    Represents the accepted query structure for SpaceX API calls.
    Attributes:
        query (dict): any valid MongoDB find() query
        options (dict): follows the dictionary structure as documented in the SpaceX API: https://github.com/r-spacex/SpaceX-API/blob/master/docs/queries.md
    """
    query: dict = field(default_factory=dict)
    options: dict = field(default_factory=dict)


def paginateQuery(query: SpaceXQuery, paginate: bool):
    if paginate:
        query.options["pagination"] = True
    else:
        query.options["pagination"] = False
    return query
