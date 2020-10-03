"""
Size class
"""
import json

# pylint: disable=missing-function-docstring


class Size:
    """Size class"""

    def __init__(self, label: str, size: str, disable: bool):
        self.label = label
        self.size = size
        self.disable = disable

    def __str__(self) -> str:
        return ("label: " + self.label +
                " size: " + self.size + " disable: "
                + str(self.disable)
                )

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__)
