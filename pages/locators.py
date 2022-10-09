from selenium.webdriver.common.by import By

class LoginPageLocators():
	LOGIN_LINK = (By.CSS_SELECTOR, '.dzen-header-desktop__rightItems-3y .dzen-header-desktop__profileMenu-3q')
	BUTTON_EMAIL_ADDRESS = (By.CSS_SELECTOR, '.AuthLoginInputToggle-type [data-type =login]')
	EMAIL_ADDRESS = (By.CSS_SELECTOR, '#passp-field-login')
	BUTTON_SIGN_IN = (By.CSS_SELECTOR, '.passp-button.passp-sign-in-button')
	PASSWORD_FIELD = (By.CSS_SELECTOR, '#passp-field-passwd')

class MainPageLocators():
	SEARCH = (By.CSS_SELECTOR, 'iframe.dzen-search-arrow-common__frame')
	OTHER_SERVICES = (By.CSS_SELECTOR, '.desktop-services__icon.desktop-services__icon_more')
	ICON_DISK = (By.CSS_SELECTOR, '#services-big-item-disk-title')

class YandexDiskPageLocators():
	CREATE = (By.CSS_SELECTOR, '.Button2.Button2_view_raised.Button2_size_m.Button2_width_max')
	CREATE_FOLDER = (By.CSS_SELECTOR, '.file-icon.file-icon_size_m.file-icon_dir_plus.create-resource-button__icon')
	NAME_FOLDER = (By.CSS_SELECTOR, '.Textinput.Textinput_view_default.Textinput_size_m input')
	NEW_NAME = (By.CSS_SELECTOR, '.rename-dialog__rename-form input')
	SAVE_NAME = (By.CSS_SELECTOR, '.Button2.Button2_view_action.Button2_size_m.confirmation-dialog__button.confirmation-dialog__button_submit')
	EXIT = (By.CSS_SELECTOR, '.Button2.Button2_view_clear-inverse.Button2_size_m.resources-action-bar__close')
	FILE_DOC = (By.CSS_SELECTOR, 'div .listing-item.listing-item_theme_tile.listing-item_size_m.listing-item_type_file.js-prevent-deselect:nth-child(8)')
	ORIGINAL_NAME = (By.CSS_SELECTOR, '.listing-item__title.listing-item__title_overflow_clamp [title="Файл для копирования.docx"]')
	COPY_FUNCTION = (By.CSS_SELECTOR, '[class="Button2 Button2_view_clear-inverse Button2_size_m groupable-buttons__visible-button groupable-buttons__visible-button_name_copy "]')
	PLACE_SAVE = (By.CSS_SELECTOR, '.b-tree__name:nth-child(3)')
	BUTTON_COPY = (By.CSS_SELECTOR, '.Button2.Button2_view_action.Button2_size_m.confirmation-dialog__button.confirmation-dialog__button_submit')
	FOLDER = (By.CSS_SELECTOR, '.listing-item__fields:nth-child(2)')
	FILE = (By.CSS_SELECTOR, '.listing-item__icon.listing-item__icon_type_preview')
	NAME_OF_FILE = (By.CSS_SELECTOR, '.listing-item__title.listing-item__title_overflow_clamp .clamped-text')

class UserProfilePageLocators():
	USER_ICON = (By.CSS_SELECTOR, '.PSHeader-User.PSHeader-User_noUserName.promozavr-anchor-user')
	LOG_OUT = (By.CSS_SELECTOR, '.menu__item.menu__item_type_link.legouser__menu-item.legouser__menu-item_action_exit')

