import pytest
from tests.pages.home_page import HomePage
from tests.pages.login_page import login_page

#assumption is user already landed on home page
def test_add_product(page):
    home_page = HomePage(page)
    home_page.click_addproduct()
    home_page.add_productname("Product1")
    home_page.add_quantity("5")
    home_page.add_price("100")
    home_page.select_supplier("Gotham Supplies")
    home_page.select_category("Books")
    home_page.add_barcode("121212")
    home_page.click_addnewproduct()
    home_page.verify_productadded()







