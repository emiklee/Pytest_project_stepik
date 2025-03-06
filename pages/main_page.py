import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Main_page(Base):
    url = 'https://www.chipdip.ru/'

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    # locator

    select_location_button = '//span[@id="geoselector_text"]'
    select_city = '//span[contains(text(), "Москва")]'

    # Getters

    def get_select_location_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_location_button)))

    def get_select_city(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_city)))

    # Actions

    def click_select_location_button(self):
        self.get_select_location_button().click()
        print('Click select location button')

    def click_select_city(self):
        self.get_select_city().click()
        print('Click select city')

    # Methods
    def get_main_page(self):
        self.driver.get(self.url)
        self.driver.maximize_window()
        self.click_select_location_button()
        self.click_select_city()
        self.assert_url('https://www.chipdip.ru/')
