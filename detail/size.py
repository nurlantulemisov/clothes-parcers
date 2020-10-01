import json


class Size:
    def __init__(self, label: str, size: str, disable: bool):
        self.label = label
        self.size = size
        self.disable = disable

    def __str__(self) -> str:
        return ("label: " + self.label +
                " size: " + self.size + " disable: "
                + str(self.disable)
                )

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)
