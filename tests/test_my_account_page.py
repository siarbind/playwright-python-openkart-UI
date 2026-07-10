from playwright.sync_api import Page,expect
import pytest

from page.my_account_page import MyAccountPage


def test_my_account_page(page:Page):
    page.goto("http://localhost/opencart/upload/")
    register = MyAccountPage(page)
    page_title= register.get_page_title()
    print("title:",page_title)
    assert page_title == "Your Store"
    register.go_to_register_page()