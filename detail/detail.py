from typing import List
from detail.size import Size
from detail.price import Price
import json

class Detail:
    def __init__(self, name: str, link: str, thumbnail: str, color: str, sizes: List[Size], prices: List[Price]):
        self.link = link
        self.thumbnail = thumbnail
        self.color = color
        self.sizes = sizes
        self.name = name
        self.price = prices

    def __str__(self) -> str:
        return "link: " + self.link + " thumbnail: " + self.thumbnail + " color: " + self.color + " sizes: " + " \n".join([str(x) for x in self.sizes])

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
