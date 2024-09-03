import allure
from data import Urls
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import BasePageLocators as Locator


class HomePage(BasePage):
    @allure.step('Принять куки.')
    def accept_cookie(self):
        button_cookie = self.wait_and_find_element(Locator.COOKIE_ACCEPT_BUTTON)
        button_cookie.click()

    @allure.step('Нажать на кнопку заказа вверху страницы.')
    def click_top_order_button(self):
        button_order = self.wait_and_find_element(Locator.TOP_ORDER_BUTTON)
        button_order.click()

    @allure.step('Нажать на кнопку заказа внизу страницы.')
    def click_on_down_order_button(self):
        button_order_down = self.wait_and_find_element(Locator.DOWN_ORDER_BUTTON)
        button_order_down.click()

    @allure.step('Нажать на самокат в лого.')
    def click_on_scooter_logo(self):
        button_logo_sc = self.wait_and_find_element(Locator.SCOOTER_LOGO)
        button_logo_sc.click()

    @allure.step('Перейти на страницу яндекса в лого.')
    def click_on_yandex_logo(self):
        button_logo_ya = self.wait_and_find_element(Locator.YANDEX_LOGO)
        button_logo_ya.click()

    @allure.step('Переключиться на другую вкладку браузера.')
    def switch_window(self, number_window):
        self.driver.switch_to.window(self.driver.window_handles[number_window])

    @allure.step('Ожидание загрузки страницы с дзеном.')
    def wait_url_dzen(self):
        WebDriverWait(self.driver, 5).until_not(expected_conditions.url_to_be('about:blank'))

    @allure.step('Нажать на вопрос в FAQ.')
    def click_faq(self, number_faq):
        button_faq = self.wait_and_find_element(Locator.choose_faq(number_faq))
        button_faq.click()

    @allure.step('Получить ответ на вопрос.')
    def text_faq_answer(self, number_answer, answer):
        get_answer = self.wait_text_and_find_element(Locator.choose_faq_answer(number_answer), answer)
        return get_answer.text

