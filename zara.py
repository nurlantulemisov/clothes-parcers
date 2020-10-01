from selenium import webdriver
from typing import List
from detail.size import Size
from detail.detail import Detail
from detail.price import Price
import collections
import enum


class Zara(enum.Enum):
    parcer_code = 1

    def __init__(self, item_code: str, isset_thumbnail: bool = False):
        self.item_code = item_code
        self.isset_thumbnail = isset_thumbnail

    def find_color(self, driver: webdriver) -> str:
        color_clothe = driver.find_element_by_css_selector("._colorName")
        return color_clothe.text

    def find_sizes(self, driver: webdriver) -> List[Size]:
        sizes = driver.find_elements_by_css_selector(
            '.size-list .product-size')
        obj_sizes = []
        for size in sizes:
            deque_size_types = collections.deque(
                size.get_attribute('data-name').split(' ('), 2)
            obj_size = Size(deque_size_types.popleft(), self.clean_nubmer_size(
                deque_size_types.popleft()), self.is_disable_size(size))
            obj_sizes.append(obj_size)
        return obj_sizes

    def clean_nubmer_size(self, subject: str) -> str:
        replace = subject.split(')')
        return replace[0].split(' ')[1]

    # todo убрать
    def is_disable_size(self, driver: webdriver) -> bool:
        return "disabled" in driver.get_attribute("class")

    def run(self) -> Detail:
        op = webdriver.ChromeOptions()
        op.add_argument('headless')
        driver = webdriver.Chrome('./driver/macOS/chromedriver', options=op)
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

        # todo add price and name
        clothes = Detail('', reference, thumbnail, self.find_color(
            driver), self.find_sizes(driver), [Price(1000, False)])
        driver.close()
        return clothes
