import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from base.base_class import Base


class Finish_order_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

    # locator

    select_delivery_address = '//*[@id="tochka_group"]/label[1]/span/span/span[1]'
    select_order_pay = '//*[@id="payment_tab_2"]'
    select_finish_button = '//button[@class="button button_red button_big"]'

    # Getters

    def get_select_delivery_address(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_delivery_address)))

    def get_select_order_pay(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_order_pay)))

    def get_select_finish_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_finish_button)))

    # Actions

    def click_select_delivery_address(self):
        self.get_select_delivery_address().click()
        print('Click select delivery address')

    def click_select_order_pay(self):
        self.get_select_order_pay().click()
        print('Click select order pay')

    def click_select_finish_button(self):
        self.get_select_finish_button().click()
        print('Click select finish button')

    # Methods
    def finish_order(self):
        self.get_current_url()
        self.click_select_delivery_address()
        self.click_select_order_pay()
        # self.click_select_finish_button()
        self.get_screenshot()

