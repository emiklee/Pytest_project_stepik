import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Cart_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

    # locator

    product_title = '//a[@class="link name"]'
    product_price = '//span[@id="sum_9001586552"]'
    total_price = '//*[@id="ordering_bar"]/div/div[2]/div/span/span[1]'
    continue_button = '//button[@class="button button_red button_big button_w100 not-print"]'

    # Getters

    def get_product_title(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_title)))

    def get_product_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.product_price)))

    def get_total_price(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.total_price)))

    def get_continue_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.continue_button)))

    # Actions

    def read_product_name(self):
        result_name = self.get_product_title().text.strip()
        print(f'Product name - {result_name}')

    def read_product_price(self):
        result_price = self.get_product_price().text.replace(' ', '')
        return result_price

    def read_total_price(self, price):
        print(f'Product price - {self.read_product_price()}p')
        result_total_price = self.get_total_price().text.replace(' ', '')
        print(f'Total price - {result_total_price}p')
        assert result_total_price == price
        print(f'The price match')

    def click_continue_button(self):
        self.get_continue_button().click()
        print('Click continue_button ')

    # Methods
    def cart_product(self):
        self.get_current_url()
        self.read_product_name()
        self.read_product_price()
        self.read_total_price(self.read_product_price())
        self.click_continue_button()
