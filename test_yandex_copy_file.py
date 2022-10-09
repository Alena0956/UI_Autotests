import pytest
import time
from .pages.login_page import LoginPage
from .pages.yandexdisk_page import YandexPage

class TestYandexDisk():
	def test_actions_user_go_from_dzen_to_disk(self, browser):
		login_link = 'http://yandex.ru'
		page = LoginPage(browser, login_link)
		page.open()
		page.go_to_login_page()
		page.login_user()
		page.open_yandex_disk()
		page_disk = YandexPage(browser,login_link)
		page_disk.create_folder()
		page_disk.copy_file()
		page_disk.user_log_out()



		
		

