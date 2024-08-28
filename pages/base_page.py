import allure
from data import Urls


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Открыть страницу по адресу.')
    def open_page(self, url):
        self.driver.get(url)

    @allure.step('Получить текущий URL.')
    def current_url(self):
        return self.driver.current_url
