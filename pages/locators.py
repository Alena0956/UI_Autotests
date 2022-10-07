from selenium.webdriver.common.by import By

class LoginPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, '.dzen-header-desktop__rightItems-3y .dzen-header-desktop__profileMenu-3q')
	BUTTON_EMAIL_ADDRESS = (By.CSS_SELECTOR, '.AuthLoginInputToggle-type [data-type =login]')
	EMAIL_ADDRESS = (By.CSS_SELECTOR, '#passp-field-login')
	BUTTON_SIGN_IN = (By.CSS_SELECTOR, '.passp-button.passp-sign-in-button')
	PASSWORD_FIELD = (By.CSS_SELECTOR, '#passp-field-passwd')

class MainPageLocators():
	SEARCH = (By.CSS_SELECTOR, '.arrow__input.mini-suggest__input')
	OTHER_SERVICES = (By.CSS_SELECTOR, '.desktop-services__icon.desktop-services__icon_more')
