from selenium.webdriver.common.by import By


class FormPage:
    def __init__(self, driver):
        """
        Инициализирует класс FormPage.

        :param driver: WebDriver для управления браузером.
        """
        self.driver = driver
        self.url = "https://bonigarcia.dev/selenium-webdriver-java/data-types.html"

    def open(self) -> None:
        """
        Открывает страницу формы.

        :return: None
        """
        self.driver.get(self.url)

    def fill_form(self, form_data: dict) -> None:
        """
        Заполняет форму значениями из словаря.

        :param form_data: Словарь с именами полей и значениями.
        :return: None
        """
        for field, value in form_data.items():
            self.driver.find_element(
                By.CSS_SELECTOR, f"[name={field}]").send_keys(value)

    def submit_form(self) -> None:
        """
        Отправляет заполненную форму.

        :return: None
        """
        self.driver.find_element(
            By.CSS_SELECTOR, "button[type=submit]").click()

    def is_field_success(self, field_id: str) -> bool:
        """
        Проверяет, успешно ли заполнено поле.

        :param field_id: Идентификатор поля для проверки.
        :return: True, если поле успешно, иначе False.
        """
        return "alert-success" in self.driver.find_element(
            By.ID, field_id).get_attribute("class")

    def is_field_danger(self, field_id: str) -> bool:
        """
        Проверяет, есть ли ошибка в заполнении поля.

        :param field_id: Идентификатор поля для проверки.
        :return: True, если есть ошибка, иначе False.
        """
        return "alert-danger" in self.driver.find_element(
            By.ID, field_id).get_attribute("class")
