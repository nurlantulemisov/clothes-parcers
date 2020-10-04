"""
Price Class
"""
import json


# pylint: disable=missing-function-docstring


class Price:
    """Price Class"""

    def __init__(self, price: int, disable: bool):
        self.price = price
        self.disable = disable

    def __str__(self) -> str:
        return "price: " + str(self.price) + " disable: " + str(self.disable)

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
