
import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def browser(request):
	browser = webdriver.Chrome()
	browser.set_window_size(1410,1050)
	yield browser
	browser.quit()
