import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC
from conftest import *
from pages.login_page import Login_page
from pages.select_product_page import Select_produt_page
from pages.category_page import Category_page
from pages.search_page import Search_page
from pages.main_page import Main_page
from pages.cart_page import Cart_page
from pages.filter_page import Filter_page
from pages.finish_order_page import Finish_order_page
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


def test_buy_product(set_up):
    options = webdriver.ChromeOptions()
    service = Service(executable_path=ChromeDriverManager().install())
    options.add_experimental_option("detach", True)
    options.page_load_strategy = 'eager'
    driver = webdriver.Chrome(options=options, service=service)

    mp = Main_page(driver)  # Get main page and select my city.
    mp.get_main_page()

    login = Login_page(driver)
    login.authorization()  # Authorization.

    sp = Search_page(driver)  # Search product.
    sp.search_product()

    sc = Category_page(driver)  # Select category.
    sc.choose_category()

    fp = Filter_page(driver)    # Filter
    fp.filter_items()

    sp = Select_produt_page(driver)  # Select and add to cart
    sp.select_product()
    driver.refresh()

    cp = Cart_page(driver)  # Cart check
    cp.cart_product()

    fp = Finish_order_page(driver)  # Finish order
    fp.finish_order()
