# Sprint_6
Проект содержит автотесты на базе pytest и selenium для сервиса Yandex Scooter

Установить зависимости
pip install -r requirements.txt.

Для запуска тестов использовать следующую команду
pytest -v

Для запуска тестов с формированием отчёта allure использовать следующую команду
pytest -v --alluredir=allure-results

Для просмотра отчёта allure выполнить команду:
allure serve allure-results
