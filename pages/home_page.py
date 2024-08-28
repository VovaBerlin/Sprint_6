import allure
from data import Urls
from pages.base_page import BasePage
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import BasePageLocators as Locator


class HomePage(BasePage):
    @allure.step('Принять куки.')
    def accept_cookie(self):
        self.driver.find_element(*Locator.COOKIE_ACCEPT_BUTTON).click()

    @allure.step('Нажать на кнопку заказа вверху страницы.')
    def click_top_order_button(self):
        self.driver.find_element(*Locator.TOP_ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку заказа внизу страницы.')
    def click_on_down_order_button(self):
        self.driver.find_element(*Locator.DOWN_ORDER_BUTTON).click()

    @allure.step('Ожидание загрузки страницы с формой заказа.')
    def wait_for_load_order_page(self):
        WebDriverWait(self.driver, 3).until(expected_conditions.presence_of_element_located(Locator.TEXT_UPPER_FORM))

    @allure.step('Нажать на самокат в лого.')
    def click_on_scooter_logo(self):
        self.driver.find_element(*Locator.SCOOTER_LOGO).click()

    @allure.step('Перейти на страницу яндекса в лого.')
    def click_on_yandex_logo(self):
        self.driver.find_element(*Locator.YANDEX_LOGO).click()

    @allure.step('Переключиться на другую вкладку браузера.')
    def switch_window(self, number_window):
        self.driver.switch_to.window(self.driver.window_handles[number_window])

    @allure.step('Ожидание загрузки страницы с дзеном.')
    def wait_url_dzen(self):
        WebDriverWait(self.driver, 5).until_not(expected_conditions.url_to_be('about:blank'))

    @allure.step('Ожидание 3 секунды.')
    def wait_3_seconds(self):
        WebDriverWait(self.driver, 3)

    @allure.step('Нажать на вопрос в FAQ.')
    def click_faq(self, number_faq):
        self.driver.find_element(*Locator.choose_faq(number_faq)).click()

    @allure.step('Получить ответ на вопрос.')
    def text_faq_answer(self, number_answer):
        return self.driver.find_element(*Locator.choose_faq_answer(number_answer)).text
