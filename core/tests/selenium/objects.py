from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from . import conf
from .utils import make_url


class BasePage:
    def __init__(self, driver, headless=True):
        self.driver = driver

    def get(self, url: str):
        self.driver.get(url)

    def get_elem(self, xp: str):
        return WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xp))
        )

    def click(self, xp):
        elem = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.XPATH, xp))
        )
        elem.click()

    def enter_text(self, xp: str, text: str):
        elem = self.get_elem(xp)
        elem.send_keys(text)

    def get_elem_text(self, xp: str):
        elem = self.get_elem(xp)
        return elem.text

    def get_elem_attr(self, xp: str, attr: str = "innerHTML"):
        elem = self.get_elem(xp)
        return elem.get_attribute(attr)


class LoginPage(BasePage):
    def __init__(self):
        super().__init__()
        self.driver.get(make_url("accounts/login"))


class CreatePage(BasePage):
    def __init__(self, pk: str = ""):
        super().__init__()
        self.driver.get(make_url(f"create/{pk}"))


class EditPage(BasePage):
    def __init__(self, pk: str = ""):
        super().__init__()
        self.driver.get(make_url(f"edit/{pk}"))


class SharePage(BasePage):
    def __init__(self, pk: str = ""):
        super().__init__()
        self.driver.get(make_url(f"share/{pk}"))


class DiscussionPage(BasePage):
    def __init__(self, pk: str = ""):
        super().__init__()
        self.driver.get(make_url(f"discussion/{pk}"))


class ResultsPage(BasePage):
    def __init__(self, pk: str = ""):
        super().__init__()
        self.driver.get(make_url(f"create/{pk}"))
