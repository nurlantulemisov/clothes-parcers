from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from typing import List
import collections
from detail.size import Size
from detail.price import Price
from detail.detail import Detail
import json

def get_prices(price_elements: webdriver) -> List[Price]:
    def price_creator(price_element: webdriver) -> Price:
        return Price(''.join(list(filter(str.isdigit, price_element.text))), is_disable_price(price_element))
    return list(map(lambda price_element: price_creator(price_element), price_elements))

def find_sizes(size_elements: webdriver) -> List[Size]:
    sizes = []
    for size_element in size_elements[1:]: # костыль я пока хз как
        size_str = size_element.get_attribute('innerHTML')
        if str.isdigit(size_str):
            sizes.append(Size('', size_str, is_disable_size(size_element)))
        else:
            sizes.append(Size(size_str, '', is_disable_size(size_element)))
    return sizes

def is_disable_size(size_element: webdriver) -> bool:
    return "oos" in size_element.get_attribute("class")

def is_disable_price(price_element: webdriver) -> bool:
    return "regular" in price_element.get_attribute("class")

def run():
    op = webdriver.ChromeOptions()
    # op.headless = True
    driver = webdriver.Chrome('./driver/macOS/chromedriver', options=op)
    driver.get("https://www2.hm.com/ru_ru/search-results.html?q=0916468003")
    try:
        product = WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.products-listing')))
        name = product.find_element_by_css_selector('a.link')
        thumbnail_elem = product.find_element_by_css_selector('img')
        thumbnail = thumbnail_elem.get_attribute('src')
        prices = get_prices(product.find_elements_by_css_selector('.item-price .price'))
        reference = name.get_attribute('href')
        driver.get(reference)
        WebDriverWait(driver, 8).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.picker-list li.item .value')))
        
        clothe = Detail(
            name,
            reference,
            thumbnail,
            '',
            find_sizes(driver.find_elements_by_css_selector('.picker-list li.item .value')),
            prices
        )

    except Exception as e:
        print(e)
    driver.close()

if __name__ == "__main__":
    run()
