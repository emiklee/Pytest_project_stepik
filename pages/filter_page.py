import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Filter_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

    # locator
    filter_to_model_product = '//a[contains(text(), "для iPhone 12")]'
    filter_to_mark_amperin = '//span[contains(text(), "Amperin")]'
    filter_to_mark_foxconn = '//span[contains(text(), "Foxconn")]'
    filter_to_mark_no_trademark = '//span[contains(text(), "No trademark")]'
    select_price_button = '//div[@id="filter_prices"]'
    filter_set_min_price = '//input[@id="input_prices_min"]'
    filter_set_max_price = '//input[@id="input_prices_max"]'
    select_show_button = '//button[@id="formsubmitterbtn"]'

    # Getters

    def get_filter_to_model_product(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_to_model_product)))

    def get_filter_to_mark_amperin(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_to_mark_amperin)))

    def get_filter_to_mark_foxconn(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_to_mark_foxconn)))

    def get_filter_to_mark_no_trademark(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_to_mark_no_trademark)))

    def get_select_price_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_price_button)))

    def get_filter_set_min_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_set_min_price)))

    def get_filter_set_max_price(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.filter_set_max_price)))

    def get_select_show_button(self):
        return WebDriverWait(self.driver, 30).until(
            EC.element_to_be_clickable((By.XPATH, self.select_show_button)))

    # Actions

    def click_filter_to_model_product(self):
        self.get_filter_to_model_product().click()
        print('Click filter to model product')

    def click_filter_to_mark_amperin(self):
        self.get_filter_to_mark_amperin().click()
        print('Click filter to mark amperin')

    def click_filter_to_mark_foxconn(self):
        self.get_filter_to_mark_foxconn().click()
        print('Click filter to mark foxconn')

    def click_filter_to_mark_no_trademark(self):
        self.get_filter_to_mark_no_trademark().click()
        print('Click filter to no_trademark')

    def click_select_price_button(self):
        self.get_select_price_button().click()
        print('Click price_button')

    def input_filter_set_min_price(self, min_price):
        self.get_filter_set_min_price().send_keys(min_price)
        print('Input filter set min price')

    def input_filter_set_max_price(self, max_price):
        self.get_filter_set_max_price().send_keys(max_price)
        print('Input filter set max price')

    def click_select_show_button(self):
        self.get_select_show_button().click()
        print('Click show button')

    # Methods
    def filter_items(self):
        self.get_current_url()
        self.click_filter_to_model_product()
        # self.driver.execute_script("window.scrollTo(0, 300);")
        self.click_filter_to_mark_amperin()
        self.click_filter_to_mark_foxconn()
        self.click_filter_to_mark_no_trademark()
        # self.driver.execute_script("window.scrollTo(0, 900);")
        self.click_select_price_button()
        self.input_filter_set_min_price('3000')
        self.input_filter_set_max_price('10000')
        self.click_select_show_button()
