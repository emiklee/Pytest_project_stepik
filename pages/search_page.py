import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Search_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

    # locator
    search_input = '//input[@class="header__input header__search-input auc__input"]'
    search_button = '//button[@class="btn-reset header__button header__search-button"]'

    # Getters

    def get_search_input(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_input)))

    def get_search_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.search_button)))

    # Actions

    def input_product_name(self, product_name):
        self.get_search_input().send_keys(product_name)
        print('input product name')

    def click_search_button(self):
        self.get_search_button().click()
        print('Click search button')

    # Methods
    def search_product(self):
        self.get_current_url()
        self.input_product_name('iphone 12')
        self.click_search_button()
