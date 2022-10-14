from .locators import YandexDiskPageLocators
from .main_page import MainPage
from .locators import UserProfilePageLocators
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import time

class YandexPage(MainPage):
	def create_folder(self):
		self.browser.find_element(*YandexDiskPageLocators. CREATE).click()
		self.browser.find_element(*YandexDiskPageLocators. CREATE_FOLDER).click()
		name_input = self.browser.find_element(*YandexDiskPageLocators. NAME_FOLDER)
		name_input.send_keys(Keys.CONTROL + "a")
		name_input.send_keys(Keys.DELETE)
		new_name = self.browser.find_element(*YandexDiskPageLocators. NEW_NAME)
		new_name.send_keys('New_folder')
		self.browser.find_element(*YandexDiskPageLocators. SAVE_NAME).click()

	def copy_file(self):
		self.browser.find_element(*YandexDiskPageLocators.EXIT).click()
		self.browser.find_element(*YandexDiskPageLocators.FILE_DOC).click()
		name_original_file = self.browser.find_element(*YandexDiskPageLocators.ORIGINAL_NAME).text
		self.browser.find_element(*YandexDiskPageLocators.COPY_FUNCTION).click()
		self.browser.find_element(*YandexDiskPageLocators.PLACE_SAVE).click()
		self.browser.find_element(*YandexDiskPageLocators.BUTTON_COPY).click()
		open_folder = self.browser.find_element(*YandexDiskPageLocators.FOLDER)
		action = ActionChains(self.browser)
		action.double_click(open_folder).perform()
		assert self.browser.find_element(*YandexDiskPageLocators.FILE), 'The file is missing'
		name_of_copy_file = self.browser.find_element(*YandexDiskPageLocators.NAME_OF_FILE).text
		assert name_original_file == name_of_copy_file, 'Names is different'

	def user_log_out(self):
		self.browser.find_element(*UserProfilePageLocators.USER_ICON).click()
		self.browser.find_element(*UserProfilePageLocators.LOG_OUT).click()
		time.sleep(5)
