"""
Zara parcer
"""

import collections
from typing import List
from selenium import webdriver
from item.detail import Detail
from item.size import Size
from item.price import Price
import settings


class Zara:
    """Zara parcer class"""

    def __init__(self, item_code: str, isset_thumbnail: bool = False):
        self.item_code = item_code
        self.isset_thumbnail = isset_thumbnail

    @staticmethod
    def find_color(driver: webdriver) -> str:
        # pylint: disable=missing-function-docstring
        color_clothe = driver.find_element_by_css_selector("._colorName")
        return color_clothe.text

    def find_sizes(self, driver: webdriver) -> List[Size]:
        # pylint: disable=missing-function-docstring
        sizes = driver.find_elements_by_css_selector(
            '.size-list .product-size')
        obj_sizes = []
        for size in sizes:
            deque_size_types = collections.deque(
                size.get_attribute('data-name').split(' ('), 2)
            obj_size = Size(
                deque_size_types.popleft(),
                self.clean_nubmer_size(
                    deque_size_types.popleft()),
                "disabled" in size.get_attribute("class"))
            obj_sizes.append(obj_size)
        return obj_sizes

    @staticmethod
    def clean_nubmer_size(subject: str) -> str:
        # pylint: disable=missing-function-docstring
        replace = subject.split(')')
        return replace[0].split(' ')[1]

    def run(self) -> Detail:
        """Запускает задачу на сбор данных"""
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome(
            settings.DRIVER_PATH,
            options=options)
        driver.get("https://www.zara.com/ru/ru/search?searchTerm=" +
                   self.item_code)  # 5479200800
        driver.implicitly_wait(10)
        product_grid = driver.find_element_by_css_selector(".product-list")
        thumbnail = product_grid.find_element_by_css_selector(
            "img").get_attribute("src")

        detail_information = product_grid.find_element_by_css_selector('a')
        reference = detail_information.get_attribute('href')

        driver.get(reference)
        driver.implicitly_wait(10)

        # todo add price and name #pylint: disable=W0511
        clothes = Detail('', reference, thumbnail, self.find_color(
            driver), self.find_sizes(driver), [Price(1000, False)])
        driver.close()
        return clothes
