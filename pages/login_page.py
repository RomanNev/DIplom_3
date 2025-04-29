import allure

from pages.base_page import BasePage
from urls import Urls
from locators.login_page_locators import LoginPageLocators

class LoginPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.url = Urls.login_page_url
        self.locators = LoginPageLocators()

    @allure.step("Клик по кнопке 'Восстановить пароль'")
    def click_on_forgot_password(self):
        self.click_on_element(self.locators.FORGOT_PASSWORD_BUTTON)

