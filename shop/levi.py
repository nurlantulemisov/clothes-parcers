
"""
Levi`s parcer
"""

import collections
from typing import List
from selenium import webdriver
from item.detail import Detail
from item.size import Size
from item.price import Price
from shop.shop_interface import ShopInterface
import settings

class Levi(ShopInterface):
    """Levi`s parcer class"""
    def __init__(self, item_code: str, isset_thumbnail: bool = False):
        self.item_code = item_code
        self.isset_thumbnail = isset_thumbnail

    def find_color(self, driver: webdriver) -> str:
        clothe_color = driver.find_element_by_xpath(
            '//*[@id="pdpRootInstance"]/div/div/div[1]/div/div/div[3]/div[3]/div[2]/div/div[1]/span[2]')
        return clothe_color.get_attribute("innerHTML")

    def find_sizes(self, driver: webdriver) -> List[Size]:
        clothe_sizes = driver.find_element_by_css_selector("div.tiles-outer-grid-container")
        sizes_list = clothe_sizes.text
        return sizes_list.splitlines()

    def run(self) -> Detail:
        """Запускает задачу на сбор данных"""
        CHROME_DRIVER_PATH = 'chromedriver/chromedriver'  # путь до драйвера в проекте
        LEVIS = 'https://www.levi.com/RU/ru_RU/'  # сайт для парсинга
        # item_code = 'p/269860002'
        options = webdriver.ChromeOptions()
        options.add_argument('headless')  # для браузера
        driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH, options=options)
        driver.get(LEVIS + self.item_code)
        driver.implicitly_wait(10)
        reference = driver.current_url
        product_img_list = driver.find_element_by_class_name('image-gallery')
        thumbnail = product_img_list.find_element_by_tag_name('img').get_attribute('src')
        price = driver.find_element_by_xpath(
            '//*[@id="pdpRootInstance"]/div/div/div[1]/div/div/div[3]/div[2]/div[1]/div/span[3]')
        clothes = Detail('', reference, thumbnail, self.find_color(
            driver), self.find_sizes(driver), price)
        return clothes