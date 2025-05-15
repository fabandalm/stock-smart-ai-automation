from playwright.sync_api import Page

class HomePage:
    def __init__(self, page: Page):
        self.page = page
        self.supplier_link = page.get_by_role("link", name="Suppliers")
        self.category_link = page.get_by_role("link", name="Categories")
        self.addProduct_button = page.get_by_role("button", name="Add Product")
        self.productname_input = page.locator("#name")
        self.quantity_input = page.locator("#quantity")
        self.price_input = page.locator("#price")
        self.supplier_input = page.locator("#supplier")
        self.category_input = page.locator("#category")
        self.barcode_input = page.locator("#barCode")
        self.producttable = page.locator("table.w-full")

        self.logout_link = page.get_by_role("link", name="Logout")

    def goto(self):
        self.page.goto("http://localhost")

    def click_addproduct(self):
        self.addProduct_button.click()
        self.page.wait_for_timeout(1000)

    def add_productname(self, productname: str):
        self.productname_input.fill(productname)
        self.page.wait_for_timeout(1000)

    def add_quantity(self, quantity_num: str):
        self.quantity_input.fill(quantity_num)
        self.page.wait_for_timeout(1000)

    def add_price(self, price_num: str):
        self.price_input.fill(price_num)
        self.page.wait_for_timeout(1000)

    def select_supplier(self, suppliername: str):
        self.supplier_input.select_option("#supplier", label=suppliername)
        self.page.wait_for_timeout(1000)

    def select_category(self, bookname: str):
        self.category_input.select_option("#category", label=bookname)
        self.page.wait_for_timeout(1000)

    def add_barcode(self, barcode: str):
        self.barcode_input.fill(barcode)
        self.page.wait_for_timeout(1000)

    def click_addnewproduct(self):
        self.addProduct_button.click()
        self.page.wait_for_timeout(1000)

    def verify_productadded(self):
        assert self.page.locator("table.w-full >> text=Test 1").count() > 0, "Product not found"
        self.page.wait_for_timeout(1000)


