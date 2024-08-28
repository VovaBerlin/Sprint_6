from selenium.webdriver.common.by import By


class BasePageLocators:
    TOP_ORDER_BUTTON = [By.XPATH, './/div[starts-with(@class, "Header")]/button[text()="Заказать"]']
    DOWN_ORDER_BUTTON = [By.XPATH, './/div[starts-with(@class, "Home")]/button[text()="Заказать"]']
    YANDEX_LOGO = [By.XPATH, './/img[@alt="Yandex"]']
    SCOOTER_LOGO = [By.XPATH, './/img[@alt="Scooter"]']
    COOKIE_ACCEPT_BUTTON = [By.ID, 'rcc-confirm-button']
    TEXT_UPPER_FORM = [By.XPATH, './/div[starts-with(@class, "Order")]/div[text()="Для кого самокат"]']

    @staticmethod
    def choose_faq(number_faq):
        return [By.ID, f"accordion__heading-{number_faq}"]

    @staticmethod
    def choose_faq_answer(number_answer):
        return [By.ID, f"accordion__panel-{number_answer}"]


class OrderPageLocators:
    FIRST_NAME_INPUT = [By.XPATH, './/input[starts-with(@placeholder,"* Имя")]']
    LAST_NAME_INPUT = [By.XPATH, './/input[starts-with(@placeholder,"* Фамилия")]']
    ADDRESS_INPUT = [By.XPATH, './/input[starts-with(@placeholder,"* Адрес: куда привезти заказ")]']
    METRO_INPUT = [By.XPATH, './/input[starts-with(@placeholder,"* Станция")]']
    TELEPHONE_NUMBER_INPUT = [By.XPATH, './/input[starts-with(@placeholder,"* Телефон")]']
    NEXT_BUTTON = [By.XPATH, ".//button[text()='Далее']"]

    DATE_DELIVERY = [By.XPATH, './/input[starts-with(@placeholder,"* Когда привезти самокат")]']
    DATE_RENT = [By.XPATH, ".//span[@class='Dropdown-arrow']"]
    DATE_RENT_LIST = [By.XPATH, ".//div[@class='Dropdown-option']"]
    COLOR_CHECKBOXES = [By.ID, "black"]
    COMMENT_INPUT = [By.XPATH, ".//input[starts-with(@placeholder,'Комментарий')]"]
    ORDER_BUTTON = [By.XPATH, ".//div[starts-with(@class,'Order_Buttons')]//button[text()='Заказать']"]
    ACCEPT_ORDER_BUTTON = [By.XPATH, ".//button[text()='Да']"]
    ORDER_ACCEPTED = [By.XPATH, ".//div[starts-with(@class,'Order_ModalHeader') and text()='Заказ оформлен']"]
    STATUS_BUTTON = [By.XPATH, ".//div[starts-with(@class,'Order_NextButton')]//button"]

    @staticmethod
    def choose_metro_station(station):
        return [By.XPATH, f'.//div[text()="{station}"]']

    @staticmethod
    def choose_rent_list(rent):
        return [By.XPATH, f'.//div[text()="{rent}"]']
