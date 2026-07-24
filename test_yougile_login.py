from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By

def test_yugile_login():
    


# Шаги
# Открыть страницу авторизации: https://ru.yougile.com/team/
# Ввести в поле «Email» логин: sky-best-student@yandex.ru autocomplete="email"
# Ввести в поле «Пароль» пароль: Sky_Pro1 autocomplete="current_password"
# Нажать кнопку «Войти» bg-action-default[role="button"]
# Ожидаемый результат
# Пользователь перенаправлен на главную страницу YouGile
# Отображается интерфейс рабочего пространства
# Имя пользователя placeholder="Отображаетс имя..." [Sky_Pro]


