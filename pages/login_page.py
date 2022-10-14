from .locators import LoginPageLocators
from .locators import MainPageLocators
from .main_page import MainPage

class LoginPage(MainPage):
	def go_to_login_page(self):
		self.browser.find_element(*LoginPageLocators. LOGIN_LINK).click()

	def login_user(self):
		self.browser.find_element(*LoginPageLocators. BUTTON_EMAIL_ADDRESS).click()
		email_address = self.browser.find_element(*LoginPageLocators. EMAIL_ADDRESS)
		email_address.send_keys('testUIsimbirSoft')
		self.browser.find_element(*LoginPageLocators. BUTTON_SIGN_IN).click()
		password_field = self.browser.find_element(*LoginPageLocators. PASSWORD_FIELD)
		password_field.send_keys('testUIsimbirsoft12454')
		self.browser.find_element(*LoginPageLocators. BUTTON_SIGN_IN).click()

	def open_yandex_disk(self):
		self.browser.find_element(*MainPageLocators. SEARCH).click()
		self.browser.switch_to.frame(self.browser.find_element_by_css_selector('.dzen-search-arrow-common__frame'))
		self.browser.find_element(*MainPageLocators. OTHER_SERVICES).click()
		self.browser.switch_to.window(self.browser.window_handles[1])
		self.browser.find_element(*MainPageLocators.ICON_DISK).click()



	

