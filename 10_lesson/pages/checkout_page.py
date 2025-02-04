from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        """
        Инициализирует объект CheckoutPage.

        :param driver: WebDriver,
        используемый для взаимодействия с веб-страницей.
        """
        self.driver = driver

    def enter_first_name(self, first_name: str) -> None:
        """
        Вводит имя в поле "Имя".

        :param first_name: str - Имя, которое нужно ввести в поле.
        :return: None - Метод не возвращает значения.
        """
        first_name_field = self.driver.find_element(
            By.CSS_SELECTOR, '[name="firstName"]')
        first_name_field.clear()
        first_name_field.send_keys(first_name)

    def enter_last_name(self, last_name: str) -> None:
        """
        Вводит фамилию в поле "Фамилия".

        :param last_name: str - Фамилия, которую нужно ввести в поле.
        :return: None - Метод не возвращает значения.
        """
        last_name_field = self.driver.find_element(
            By.CSS_SELECTOR, '[name="lastName"]')
        last_name_field.clear()
        last_name_field.send_keys(last_name)

    def enter_postal_code(self, postal_code: str) -> None:
        """
        Вводит почтовый индекс в поле "Почтовый код".

        :param postal_code: str - Почтовый код, который нужно ввести в поле.
        :return: None - Метод не возвращает значения.
        """
        postal_code_field = self.driver.find_element(
            By.CSS_SELECTOR, '[name="postalCode"]')
        postal_code_field.clear()
        postal_code_field.send_keys(postal_code)

    def continue_checkout(self) -> None:
        """
        Нажимает кнопку "Продолжить" для перехода
        к следующему шагу оформления заказа.

        :return: None - Метод не возвращает значения.
        """
        self.driver.find_element(By.ID, 'continue').click()

    def get_total(self) -> str:
        """
        Получает общую сумму из элемента на странице.

        :return: str - Текстовое представление общей суммы.
        """
        return self.driver.find_element(
            By.CSS_SELECTOR, "div.summary_total_label").text
