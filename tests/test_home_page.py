import allure
import pytest
from data import Urls
from pages.home_page import HomePage


class TestHomePage:

    @allure.title('Нажатие на кнопку "Заказать" в header.')
    @allure.description('Проверка, что при нажатии на кнопку "Заказать" в верху страницы,'
                        'осуществляется переход на страницу с оформлением заказа.')
    def test_click_on_top_order_button_open_order_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_page(Urls.MAIN_PAGE)
        home_page.accept_cookie()
        home_page.click_top_order_button()
        assert home_page.current_url() == Urls.ORDER_PAGE

    @allure.title('Нажатие на кнопку "Заказать" в блоке "Как это работает".')
    @allure.description('Проверка, что при нажатии на кнопку "Заказать" в блоке "Как это работает",'
                        'осуществляется переход на страницу с оформлением заказа.')
    def test_click_on_down_order_button_open_order_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_page(Urls.MAIN_PAGE)
        home_page.accept_cookie()
        home_page.click_on_down_order_button()
        assert home_page.current_url() == Urls.ORDER_PAGE

    @allure.title('При нажатии на текст "Яндекс", открывается страница "Дзен".')
    @allure.description('Проверка что, при нажатии на текст "Яндекс" в лого, осуществляется'
                        'редирект на страницу Яндекс Дзен.')
    def test_click_on_scooter_logo_open_home_page(self, driver):
        home_page = HomePage(driver)
        home_page.open_page(Urls.MAIN_PAGE)
        home_page.accept_cookie()
        home_page.click_on_down_order_button()
        home_page.click_on_scooter_logo()
        assert home_page.current_url() == Urls.MAIN_PAGE

    @allure.title('При нажатии на текст "Яндекс", открывается страница "Дзен".')
    @allure.description('Проверка что, при нажатии на текст "Яндекс" в лого, осуществляется'
                        'редирект на страницу Яндекс Дзен.')
    def test_click_on_yandex_logo_open_dzen_page_with_redirection(self, driver):
        home_page = HomePage(driver)
        home_page.open_page(Urls.MAIN_PAGE)
        home_page.accept_cookie()
        home_page.click_on_yandex_logo()
        home_page.switch_window(1)
        home_page.wait_url_dzen()
        assert Urls.DZEN_PAGE in home_page.current_url()
