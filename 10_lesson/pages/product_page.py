from selenium.webdriver.common.by import By


class ProductPage:
    """
    Класс, представляющий страницу продукта.
    """

    def __init__(self, driver):
        """
        Инициализация класса ProductPage.

        :param driver: WebDriver,
        используемый для взаимодействия с веб-страницей.
        """
        self.driver = driver

    def add_to_cart(self, product_id: str) -> None:
        """
        Добавляет продукт в корзину по его идентификатору.

        :param product_id: str - Идентификатор продукта,
        который нужно добавить в корзину.
        :return: None - Метод не возвращает значения.
        """
        self.driver.find_element(By.ID, product_id).click()

    def go_to_cart(self) -> None:
        """
        Переходит в корзину.

        :return: None - Метод не возвращает значения.
        """
        self.driver.find_element(By.CLASS_NAME, 'shopping_cart_link').click()

    def checkout(self) -> None:
        """
        Переходит к процессу оформления заказа.

        :return: None - Метод не возвращает значения.
        """
        self.driver.find_element(By.ID, 'checkout').click()
