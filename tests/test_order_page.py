import pytest
import allure
from data import *
from locators import *
from pages.order_page import OrderPage
from pages.home_page import HomePage


class TestOrderPage:
    @allure.title('Успешное оформление заказа.')
    @allure.description('Проверка, что при корректном заполнении форм заказа, заказ успешно оформится')
    @pytest.mark.parametrize('data', ["data_1", "data_2"])
    def test_order_page_create_order_successful(self, driver, data):
        order_page = OrderPage(driver)
        order_page.open_page(Urls.ORDER_PAGE)
        home_page = HomePage(driver)
        home_page.accept_cookie()
        order_page.user_form_order(Data.data[data])
        order_page.click_on_next_button()
        order_page.rent_form_order(Data.data[data])
        order_page.click_on_order_button()
        order_page.click_on_order_accepted()

        assert Order.ORDER_SUCCESSFUL in order_page.order_issued(Order.ORDER_SUCCESSFUL)
