import pytest
import allure
from data import *
from pages.home_page import *


class TestFAQ:
    @allure.title('Проверка раскрытия ответа при нажатии на вопрос FAQ.')
    @allure.description('Нажатие на вопрос приводит к раскрытию ответа в соответствии с ТЗ.')
    @pytest.mark.parametrize(
        "number_faq,number_answer,answer",
        [
            (0, 0, FAQ.answer_1),
            (1, 1, FAQ.answer_2),
            (2, 2, FAQ.answer_3),
            (3, 3, FAQ.answer_4),
            (4, 4, FAQ.answer_5),
            (5, 5, FAQ.answer_6),
            (6, 6, FAQ.answer_7),
            (7, 7, FAQ.answer_8),
        ]
    )
    def test_click_on_question_faq_show_correct_answer(self, driver, number_faq, number_answer, answer):
        home_page = HomePage(driver)
        home_page.open_page(Urls.MAIN_PAGE)
        home_page.accept_cookie()
        home_page.click_faq(number_faq)
        answ = home_page.text_faq_answer(number_answer, answer)

        assert answ == answer, "Ответ не совпадает с ожидаемым значением теста."
