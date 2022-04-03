import random
import unittest
from selenium import webdriver
from selenium.webdriver.firefox.options import Log
from .objects import (
    BasePage,
    LoginPage,
    CreatePage,
    EditPage,
    SharePage,
    DiscussionPage,
    ResultsPage,
)
from .locators import GenericLocators, LoginPageLocators
from . import conf
from .utils import make_url


class TestGeneric(unittest.TestCase):
    @classmethod
    def setUp(cls):
        locs = LoginPageLocators
        options = webdriver.FirefoxOptions()
        options.headless = True
        driver = webdriver.Firefox(options=options)
        cls.page_obj = BasePage(driver)
        cls.page_obj.get(make_url("accounts/login"))
        cls.page_obj.enter_text(locs.USERNAME_INPUT, conf.USERNAME)
        cls.page_obj.enter_text(locs.PASSWORD_INPUT, conf.PASSWORD)
        cls.page_obj.click(locs.SUBMIT_BUTTON)


class CreatePage(TestGeneric):
    locs = GenericLocators

    def test_add_discussion(self):
        po = self.page_obj
        po.get(make_url("create"))
        num = random.randint(0, 500)
        title = f"The test title {num}"
        description = f"The discussion test description {num}"
        po.click(self.locs.ADD_BUTTON)
        po.enter_text(self.locs.TITLE_INPUT, title)
        po.enter_text(self.locs.DESCRIPTION_INPUT, description)
        new_title = po.get_elem_text(self.loc.DISCUSSION_TOPIC_TITLE)
        new_description = po.get_elem_text(self.loc.DISCUSSION_TOPIC_DESC)
        self.assertEqual(title, new_title)
        self.assertEqual(description, new_description)
