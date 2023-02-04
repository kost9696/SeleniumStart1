import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from nav import homepage_navT
from nav.homepage_navT import HomepageNavT


@pytest.mark.usefixtures('setup') # обьявляем раннее написанную фикстуру в файле conftest.py с функцией setup
class TestHomePage:

    def test_nav_links(self):                            # пишем тест1 для того что бы получить фактический результат,полсе получения пишем тест2
        homepage_nav = HomepageNavT(self.driver)          # создаем переменную которая передает все что написано в HomepageNav(логика навигации) и передаем драйвер((self.driver))
        print(homepage_nav.get_nav_links_text())         # выводим переменную "homepage_nav" в которую записан весь класс "HomepageNav" с функцией "get_nav_links_text()" которая формирует и выводит список значений


    def test_nav_linkss(self):                             # пишем тест2 для того что бы сравнить фактический результат с ожидаемым
        homepage_nav = HomepageNavT(self.driver)           # создаем переменную которая передает все что написано в HomepageNav(логика навигации) и передаем драйвер((self.driver))
        actual_links = homepage_nav.get_nav_links_text()  # создаем переменную которая(как мы выяснили) передает фактический результат
        expected_links = homepage_nav.asd      # создаем переменную которая передает ожидаемый результат
        assert actual_links == expected_links, 'Validation Nav Links Text'



    def test_for_buttons(self):
        homepage_nav = HomepageNavT(self.driver)
        print(homepage_nav.get_sign_in_button())
        #expected_result=homepage_navT.SIGN_IN
        #button = homepage_navT.get_sign_in_button()
        #button.click()
        #assert actual_result == expected_result





