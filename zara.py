from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from typing import List
from detail.size import Size
from detail.detail import Detail
from detail.price import Price
import collections
import json

# todo заменить название файла
def find_color(driver: webdriver) -> str:
    color_clothe = driver.find_element_by_css_selector("._colorName")
    return color_clothe.text

def find_sizes(driver: webdriver) -> List[Size]:
    sizes = driver.find_elements_by_css_selector('.size-list .product-size')
    obj_sizes = []
    for size in sizes:
        deque_size_types = collections.deque(size.get_attribute('data-name').split(' ('), 2)
        obj_size = Size(deque_size_types.popleft(), clean_nubmer_size(deque_size_types.popleft()), is_disable_size(size))
        obj_sizes.append(obj_size)
    return obj_sizes

def clean_nubmer_size(subject: str) -> str:
    replace = subject.split(')')
    return replace[0].split(' ')[1]

# todo убрать
def is_disable_size(driver: webdriver) -> bool:
    return "disabled" in driver.get_attribute("class")
    
def run():
    op = webdriver.ChromeOptions()
    op.add_argument('headless')
    driver = webdriver.Chrome('./driver/macOS/chromedriver', options=op)
    driver.get("https://www.zara.com/ru/ru/search?searchTerm=5479200800")
    driver.implicitly_wait(10)
    product_grid = driver.find_element_by_css_selector(".product-grid")
    thumbnail = product_grid.find_element_by_css_selector("img").get_attribute("src")

    detail_information = product_grid.find_element_by_css_selector('a.product-link')
    reference = detail_information.get_attribute('href')

    driver.get(reference)
    driver.implicitly_wait(10)

    #todo add price and name
    clothe = Detail('', reference, thumbnail, find_color(driver), find_sizes(driver), [Price(1000, False)])
    print(json.dumps(clothe.toJson()))
    driver.close()

if __name__ == "__main__":
    run()
