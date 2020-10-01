import json


class Price:
    def __init__(self, price: int, disable: bool):
        self.price = price
        self.disable = disable

    def __str__(self) -> str:
        return "price: " + str(self.price) + " disable: " + str(self.disable)

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
