from selenium import webdriver
from . import config


class Booking(webdriver.Chrome):
    def __init__(self, driver_path=config.DRIVER_PATH, tear_down=False):
        self.tear_down = tear_down
        super(Booking, self).__init__(executable_path=driver_path)
        self.implicitly_wait(15)
        self.maximize_window()
    

    def __exit__(self, *args) -> None:
        if self.tear_down:
            self.quit()
    

    def land_first_page(self):
        self.get('https://www.booking.com/')
    

    def change_currency(self, currency):
        currency_btn = self.find_element_by_css_selector(
            'button[data-tooltip-text="Choose your currency"'
        )
        currency_btn.click()
        
        selected_currency = self.find_element_by_css_selector(
            f'a[data-modal-header-async-url-param*="selected_currency={currency}"]'
        )
        selected_currency.click()
