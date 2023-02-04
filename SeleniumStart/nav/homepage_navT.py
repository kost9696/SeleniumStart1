from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from selenium_base.base_functions import SeleniumBase
import time


class HomepageNavT(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.nav_links: str = '#top-nav'
        self.EXPECTED_R = 'Регистрация'
        self.sign_in_button: str = '#topnav-menu>li'
        self.SIGN_IN = ' '
        self.search_field: str = '.header-search js-app-search-suggest'


    def get_nav_links(self) -> List[WebElement]:
            return self.are_visiable('css', self.nav_links, 'Header Navigation links')

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = [link.text for link in nav_links]
        return "\n".join(nav_links_text)



    def get_sign_in_button(self) -> WebElement:
        return self.is_present('css', self.sign_in_button, 'SIGN IN')

    def get_button_text(self):
        button = self.get_sign_in_button()
        return button


    def get_search_field(self) -> WebElement:
        return self.is_visiable('class', self.search_field, "POISK")

    def test_search_field(self):
        s_f = self.get_search_field
        s_f.clear()
        s_f.send_keys(str'All Baby')









