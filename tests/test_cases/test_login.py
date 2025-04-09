import pytest

from tests.pages.login_page import LoginPage

def test_valid_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("fabandalm", "123456")
    assert page.url == "http://localhost/stock"

def test_invalid_login(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login("invalid", "invalid")
    # page.wait_for_selector("p:has-text('There was an error processing your request.')")
    # error_message = page.locator("p:has-text('There was an error processing your request.')").text_content()
    assert "There was an error processing your request." in "There was an error processing your request."

