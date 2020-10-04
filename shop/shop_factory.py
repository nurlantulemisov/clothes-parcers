"""
Factory shops
"""
from shop.shop_enum import ShopEnum
from shop.zara import Zara
from shop.hm import HM
from shop.shop_interface import ShopInterface

# pylint: disable=too-few-public-methods
# pylint: disable=no-self-use


class ShopFactory:
    """
    Factory shops
    """

    def shop(self, shop_id: int, item_code: str) -> ShopInterface:
        """Get shop"""
        if shop_id == ShopEnum.ZARA.value:
            return Zara(item_code)
        return HM(item_code)
