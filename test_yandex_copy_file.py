import pytest
import time
from .pages.login_page import LoginPage

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class TestYandexDisk():
	def test_user_can_copy_file(self, browser):
		login_link = 'http://yandex.ru'
		page = LoginPage(browser, login_link)
		page.open()
		time.sleep(20)
		page.go_to_login_page()
		page.login_user()
		page.open_yandex_desk()
		time.sleep(15)

	#def test_autorization_user(self, browser):
		

