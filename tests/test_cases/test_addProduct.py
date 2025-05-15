import pytest
from tests.pages.login_page import LoginPage
from tests.pages.home_page import HomePage

def test_add_product(page):
    login_page = LoginPage(page)
    login_page.goto()
    login_page.login_fill_username("fabandalm")
    login_page.login_fill_password("123456")
    login_page.login_click_signin()
    assert page.url == "http://localhost/stock"

# def test_invalid_login(page):
#     login_page = LoginPage(page)
#     login_page.goto()
#     login_page.login("invalid", "invalid")
#     # page.wait_for_selector("p:has-text('There was an error processing your request.')")
#     # error_message = page.locator("p:has-text('There was an error processing your request.')").text_content()
#     assert "There was an error processing your request." in "There was an error processing your request."