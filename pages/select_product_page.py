import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Select_produt_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

    # locator
    product_title = '//*[@id="item9001586552"]/div[2]/div[4]/a'
    product_price = '//span[@id="price_9001586552"]'
    add_cart_button = '//button[@data-id="qty_9001586552"]'
    select_cart_button = '//span[@id="topbox_cart_qty"]'

    # Getters

    def get_product_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_title)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_add_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.add_cart_button)))

    def get_select_cart_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_cart_button)))

    # Actions

    def read_product_name(self):
        result_name = self.get_product_title().text.strip()
        print(f'Product name - {result_name}')

    def read_product_price(self):
        result_price = self.get_product_price().text.replace(' ', '')
        print(f'Product price - {result_price}p')

    def click_add_cart_button(self):
        self.get_add_cart_button().click()
        print('Click select add cart button')

    def click_select_cart_button(self):
        self.get_select_cart_button().click()
        print('Click select cart button')

    # Methods
    def select_product(self):
        self.get_current_url()
        self.read_product_name()
        self.read_product_price()
        self.click_add_cart_button()
        self.click_select_cart_button()
