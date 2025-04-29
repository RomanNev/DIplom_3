import allure

from pages.forgot_password_page import ForgotPasswordPage
from pages.login_page import LoginPage
from urls import Urls
from data import Data

class TestPasswordRecovery:

    @allure.title("Проверка перехода на страницу восстановления пароля")
    def test_navigate_to_password_recovery_page(self, driver):
        page = LoginPage(driver)
        page.open()
        page.click_on_forgot_password()
        page = ForgotPasswordPage(driver) # переход на страницу восстановления
        current_url = page.get_current_url()

        assert current_url == Urls.forgot_password_url, f"Ожидалось '{Urls.forgot_password_url}', но получили '{current_url}'"

    @allure.title("Проверка ввода email и отправки формы восстановления пароля")
    def test_submit_email_for_password_recovery(self, driver):
        page = ForgotPasswordPage(driver)
        page.open()
        page.fill_form_recovery_email(Data.EMAIL_FOR_RECOVERY)
        page.click_on_button_recovery()

        current_url = page.get_current_url(Urls.reset_password_url)

        assert current_url == Urls.reset_password_url, f"Ожидалось '{Urls.reset_password_url}', но получили '{current_url}'"

    @allure.title("Проверка подсветки поля пароля при переключении видимости")
    def test_toggle_password_visibility_and_highlight_input(self, driver):
        page = ForgotPasswordPage(driver)
        page.open()
        page.click_on_button_recovery()
        page.fill_form_recovery_password(Data.PASSWORD_FOR_RECOVERY)
        page.click_icon_show_password()

        assert page.is_password_input_active(), "Поле пароля не подсвечено после клика по кнопке показать/скрыть"



