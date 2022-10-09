
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser(request):
	browser = webdriver.Chrome()
	browser.set_window_size(1410,1050)
	print("\nstart browser for test..")
	yield browser
	print("\nquit browser..")
	browser.quit()
