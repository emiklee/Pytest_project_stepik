import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from base.base_class import Base


class Login_page(Base):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.action = ActionChains(self.driver)

    # locator
    select_enter_button = '//*[@id="logonlink"]/span'
    user_name = '//input[@name="login"]'
    password = '//input[@class="input input_password"]'
    select_login_button = '//button[@class="button button_big button_w100"]'

    # Getters
    def get_select_enter_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_enter_button)))

    def get_user_name(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.user_name)))

    def get_password(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.password)))

    def get_select_login_button(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.select_login_button)))

    # Actions

    def click_select_enter_button(self):
        self.action.move_to_element(self.get_select_enter_button()).pause(0.9).click().perform()
        print('Click select enter button ')

    def input_user_name(self, user_name):
        self.get_user_name().send_keys(user_name)
        print('input user name')

    def input_password(self, password):
        self.get_password().send_keys(password)
        print('input password')

    def click_select_login_button(self):
        self.get_select_login_button().click()
        print('Click select login button')

    # Methods
    def authorization(self):
        self.get_current_url()
        self.click_select_enter_button()
        self.input_user_name('user_agent')
        self.input_password('Qwerty2025')
        self.click_select_login_button()
