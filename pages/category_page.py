import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Category_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

    # locator
    select_category = '//a[contains(text(), "Дисплеи и тачскрины для Apple")]'

    # Getters

    def get_select_category(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_category)))

    # Actions

    def click_select_category(self):
        self.get_select_category().click()
        print('Click select category')

    # Methods
    def choose_category(self):
        self.get_current_url()
        self.click_select_category()
