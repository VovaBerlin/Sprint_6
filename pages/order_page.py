import allure
from pages.base_page import BasePage
from locators import OrderPageLocators


class OrderPage(BasePage):
    @allure.step('Ввод фамилии.')
    def input_first_name(self, first_name):
        name_input = self.wait_and_find_element(OrderPageLocators.FIRST_NAME_INPUT)
        name_input.send_keys(first_name)

    @allure.step('Ввод имени.')
    def input_last_name(self, last_name):
        last_name_input = self.wait_and_find_element(OrderPageLocators.LAST_NAME_INPUT)
        last_name_input.send_keys(last_name)

    @allure.step('Ввод адреса.')
    def input_address(self, address):
        address_input = self.wait_and_find_element(OrderPageLocators.ADDRESS_INPUT)
        address_input.send_keys(address)

    @allure.step('Выбор станции метро.')
    def choose_metro(self, station):
        button_metro = self.wait_and_find_element(OrderPageLocators.METRO_INPUT)
        button_metro.click()
        button_station = self.wait_and_find_element(OrderPageLocators.choose_metro_station(station))
        button_station.click()

    @allure.step('Ввод номера телефона.')
    def input_telephone_number(self, telephone_number):
        telephone_input = self.wait_and_find_element(OrderPageLocators.TELEPHONE_NUMBER_INPUT)
        telephone_input.send_keys(telephone_number)

    @allure.step('Нажать на кнопку "Далее".')
    def click_on_next_button(self):
        button_next = self.wait_and_find_element(OrderPageLocators.NEXT_BUTTON)
        button_next.click()

    @allure.step('Ввод даты.')
    def input_date_delivery(self, date):
        date_input = self.wait_and_find_element(OrderPageLocators.DATE_DELIVERY)
        date_input.send_keys(date)

    @allure.step('Выбор периода аренды.')
    def choose_rent_day(self, rent):
        button_rent_list = self.wait_and_find_element(OrderPageLocators.DATE_RENT)
        button_rent_list.click()
        button_rent_day = self.wait_and_find_element(OrderPageLocators.choose_rent_list(rent))
        button_rent_day.click()

    @allure.step('Выбор чёрного цвета.')
    def color_scooter(self):
        button_color = self.wait_and_find_element(OrderPageLocators.COLOR_CHECKBOXES)
        button_color.click()

    @allure.step('Комментарий для курьера.')
    def comment_for_courier(self, comment):
        send_comment = self.wait_and_find_element(OrderPageLocators.COMMENT_INPUT)
        send_comment.send_keys(comment)

    @allure.step('Нажать на кнопку "Заказать".')
    def click_on_order_button(self):
        button_order = self.wait_and_find_element(OrderPageLocators.ORDER_BUTTON)
        button_order.click()

    @allure.step('Нажать на кнопку "Да".')
    def click_on_order_accepted(self):
        button_yes = self.wait_and_find_element(OrderPageLocators.ACCEPT_ORDER_BUTTON)
        button_yes.click()

    @allure.step('Окно с успешным оформление заказа.')
    def order_issued(self, text):
        issued = self.wait_text_and_find_element(OrderPageLocators.ORDER_ACCEPTED, text)
        return issued.text

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
