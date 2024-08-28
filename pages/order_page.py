import allure
from pages.base_page import BasePage
from locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('Ввод фамилии.')
    def input_first_name(self, first_name):
        self.driver.find_element(*OrderPageLocators.FIRST_NAME_INPUT).send_keys(first_name)

    @allure.step('Ввод имени.')
    def input_last_name(self, last_name):
        self.driver.find_element(*OrderPageLocators.LAST_NAME_INPUT).send_keys(last_name)

    @allure.step('Ввод адреса.')
    def input_address(self, address):
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)

    @allure.step('Выбор станции метро.')
    def choose_metro(self, station):
        self.driver.find_element(*OrderPageLocators.METRO_INPUT).click()
        self.driver.find_element(*OrderPageLocators.choose_metro_station(station)).click()

    @allure.step('Ввод номера телефона.')
    def input_telephone_number(self, telephone_number):
        self.driver.find_element(*OrderPageLocators.TELEPHONE_NUMBER_INPUT).send_keys(telephone_number)

    @allure.step('Нажать на кнопку "Далее".')
    def click_on_next_button(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    @allure.step('Ввод даты.')
    def input_date_delivery(self, date):
        self.driver.find_element(*OrderPageLocators.DATE_DELIVERY).send_keys(date)

    @allure.step('Выбор периода аренды.')
    def choose_rent_day(self, rent):
        self.driver.find_element(*OrderPageLocators.DATE_RENT).click()
        self.driver.find_element(*OrderPageLocators.choose_rent_list(rent)).click()

    @allure.step('Выбор чёрного цвета.')
    def color_scooter(self):
        self.driver.find_element(*OrderPageLocators.COLOR_CHECKBOXES).click()

    @allure.step('Комментарий для курьера.')
    def comment_for_courier(self, comment):
        self.driver.find_element(*OrderPageLocators.COMMENT_INPUT).send_keys(comment)

    @allure.step('Нажать на кнопку "Заказать".')
    def click_on_order_button(self):
        self.driver.find_element(*OrderPageLocators.ORDER_BUTTON).click()

    @allure.step('Нажать на кнопку "Да".')
    def click_on_order_accepted(self):
        self.driver.find_element(*OrderPageLocators.ACCEPT_ORDER_BUTTON).click()

    @allure.step('Окно с успешным оформление заказа.')
    def order_issued(self):
        return self.driver.find_element(*OrderPageLocators.ORDER_ACCEPTED).text

    @allure.step('Заполнить данные на форме "Для кого самокат".')
    def user_form_order(self, data):
        self.input_first_name(data["first_name"])
        self.input_last_name(data["last_name"])
        self.input_address(data["address"])
        self.choose_metro(data["station"])
        self.input_telephone_number(data["telephone_number"])

    @allure.step('Заполнить данные на форме "Про аренду".')
    def rent_form_order(self, data):
        self.input_date_delivery(data["date"])
        self.choose_rent_day(data["rental_period"])
        self.color_scooter()
        self.comment_for_courier(data["comment"])
