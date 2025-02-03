from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        """
        Инициализирует класс LoginPage.

        :param driver: WebDriver, используемый для управления браузером.
        """
        self.driver = driver

    def enter_username(self, username: str) -> None:
        """
        Вводит имя пользователя в поле ввода.

        :param username: str - имя пользователя, которое будет введено.
        :return: None - Метод не возвращает значения.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="user-name"]').send_keys(username)

    def enter_password(self, password: str) -> None:
        """
        Вводит пароль в поле ввода.

        :param password: str - пароль, который будет введен.
        :return: None - Метод не возвращает значения.
        """
        self.driver.find_element(
            By.CSS_SELECTOR, '[name="password"]').send_keys(password)

    def click_login_button(self) -> None:
        """
        Нажимает на кнопку входа.

        :return: None - Метод не возвращает значения.
        """
        self.driver.find_element(By.ID, 'login-button').click()
