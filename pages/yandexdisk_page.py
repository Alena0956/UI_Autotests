from .locators import YandexDiskPageLocators
from .main_page import MainPage
from .locators import UserProfilePageLocators
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver import ActionChains

class YandexPage(MainPage):
	def create_folder(self):
		create_button = self.browser.find_element(*YandexDiskPageLocators. CREATE).click()
		create_folder = self.browser.find_element(*YandexDiskPageLocators. CREATE_FOLDER).click()
		name_input = self.browser.find_element(*YandexDiskPageLocators. NAME_FOLDER)
		name_input.send_keys(Keys.CONTROL + "a")
		name_input.send_keys(Keys.DELETE)
		new_name = self.browser.find_element(*YandexDiskPageLocators. NEW_NAME)
		new_name.send_keys('New_folder')
		save_name = self.browser.find_element(*YandexDiskPageLocators. SAVE_NAME).click()

	def copy_file(self):
		exit = self.browser.find_element(*YandexDiskPageLocators.EXIT).click()
		file_doc = self.browser.find_element(*YandexDiskPageLocators.FILE_DOC).click()
		name_original_file = self.browser.find_element(*YandexDiskPageLocators.ORIGINAL_NAME).text
		copy_function = self.browser.find_element(*YandexDiskPageLocators.COPY_FUNCTION).click()
		pace_save = self.browser.find_element(*YandexDiskPageLocators.PLACE_SAVE).click()
		click_button_copy = self.browser.find_element(*YandexDiskPageLocators.BUTTON_COPY).click()
		open_folder = self.browser.find_element(*YandexDiskPageLocators.FOLDER)
		action = ActionChains(self.browser)
		action.double_click(open_folder).perform()
		assert self.browser.find_element(*YandexDiskPageLocators.FILE), 'The file is missing'
		name_of_copy_file = self.browser.find_element(*YandexDiskPageLocators.NAME_OF_FILE).text
		assert name_original_file == name_of_copy_file, 'Names is different'

	def user_log_out(self):
		user_icon = self.browser.find_element(*UserProfilePageLocators.USER_ICON).click()
		log_out = self.browser.find_element(*UserProfilePageLocators.LOG_OUT).click()
		time.sleep(5)
