"""
Interface for shop's parcers
"""

import abc
from item.detail import Detail

# pylint: disable=too-few-public-methods
# pylint: disable=missing-function-docstring


class ShopInterface:
    """Shop parcers"""

    @abc.abstractmethod
    def run(self) -> Detail:
        pass
