"""
Detail class
"""

from typing import List
import json
from item.size import Size
from item.price import Price


# pylint: disable=missing-function-docstring
# pylint: disable=too-many-arguments

class Detail:
    """Detail class"""
    def __init__(
        self,
        name: str,
        link: str,
        thumbnail: str,
        color: str,
        sizes: List[Size],
        prices: List[Price]
    ):
        self.link = link
        self.thumbnail = thumbnail
        self.color = color
        self.sizes = sizes
        self.name = name
        self.price = prices

    def __str__(self) -> str:
        return ("link: " + self.link + " thumbnail: " +
                self.thumbnail + " color: " + self.color + " sizes: " +
                " \n".join([str(x) for x in self.sizes])
                )

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
