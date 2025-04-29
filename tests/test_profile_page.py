import allure

from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from urls import Urls


class TestProfilePage:
    @allure.title("Проверка перехода в личный кабинет авторизованного пользователя")
    def test_navigate_to_profile(self, driver, login_user_via_localStorage): # проверяет переход в личный кабинет с авторизацией
        page = MainPage(driver)
        page.click_on_button_profile_page()
        page = ProfilePage(driver)

        assert page.is_profile_info_text_correct(), 'Не удалось перейти в личный кабинет, ожидаемый текст в профиле не отобразился'

    @allure.title("Проверка перехода в раздел 'История заказов' авторизованного пользователя")
    def test_navigate_to_history_order_profile(self, driver, login_user_via_localStorage): # проверяет переход в историю заказов профиля с авторизацией
        page = MainPage(driver)
        page.click_on_button_profile_page()
        page = ProfilePage(driver)
        page.click_on_history_order_button()

        current_url = page.get_current_url(Urls.order_history_profile_url)
        assert current_url == Urls.order_history_profile_url, f"Ожидалось '{Urls.order_history_profile_url}', но получили '{current_url}'"

    @allure.title("Проверка выхода из аккаунта")
    def test_logout_user(self, driver, login_user_via_localStorage): # проверяет выход из аккаунта в личном кабинете с авторизацией
        page = MainPage(driver)
        page.click_on_button_profile_page()
        page = ProfilePage(driver)
        page.click_on_logout_button()

        assert page.is_login_button_visible(), "Кнопка входа не отображается после выхода из профиля"

