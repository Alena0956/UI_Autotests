from .locators import LoginPageLocators
from .locators import MainPageLocators
from .main_page import MainPage
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

class LoginPage(MainPage):
	def go_to_login_page(self):
		link = self.browser.find_element(*LoginPageLocators. LOGIN_LINK)
		time.sleep(5)
		link.click()

	def login_user(self):
		button_email = self.browser.find_element(*LoginPageLocators. BUTTON_EMAIL_ADDRESS)
		button_email.click()
		#time.sleep(10)
		email_address = self.browser.find_element(*LoginPageLocators. EMAIL_ADDRESS)
		email_address.send_keys('testUIsimbirSoft')
		button = self.browser.find_element(*LoginPageLocators. BUTTON_SIGN_IN)
		button.click()
		password_field = self.browser.find_element(*LoginPageLocators. PASSWORD_FIELD)
		password_field.send_keys('testUIsimbirsoft12454')
		button = self.browser.find_element(*LoginPageLocators. BUTTON_SIGN_IN)
		button.click()

	def open_yandex_desk(self):
		#time.sleep(30)
		search = self.browser.find_element(*MainPageLocators. SEARCH)
		search.send_keys('https://disk.yandex.ru/')
		other_app = self.browser.find_element(*MainPageLocators. OTHER_SERVICES)
		other_app.click()

