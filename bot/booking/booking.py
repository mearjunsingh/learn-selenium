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
    

    def select_place_to_go(self, place):
        search_field = self.find_element_by_id('ss')
        search_field.clear()
        search_field.send_keys(place)

        first_result = self.find_element_by_css_selector(
            'li[data-i="0"]'
        )
        first_result.click()

    
    def select_dates(self, check_in_date, check_out_date):
        check_in_element = self.find_element_by_css_selector(
            f'td[data-date="{check_in_date}"]'
        )
        check_in_element.click()

        check_out_element = self.find_element_by_css_selector(
            f'td[data-date="{check_out_date}"]'
        )
        check_out_element.click()
    

    def persons_and_room(self, person, room):
        selection_element = self.find_element_by_id('xp__guests__toggle')
        selection_element.click()

        while True:
            decrease_adults_element = self.find_element_by_css_selector('button[aria-label="Decrease number of Adults"]')
            decrease_adults_element.click()

            adults_value_element = self.find_element_by_id('group_adults')
            adults_value = adults_value_element.get_attribute('value') 
            if int(adults_value) == 1:
                break

        increase_adult_button_element = self.find_element_by_css_selector('button[aria-label="Increase number of Adults"]')

        for _ in range(person - 1):
                increase_adult_button_element.click()
        
        while True:
            decrease_rooms_element = self.find_element_by_css_selector('button[aria-label="Decrease number of Rooms"]')
            decrease_rooms_element.click()

            rooms_value_element = self.find_element_by_id('no_rooms')
            rooms_value = rooms_value_element.get_attribute('value') 
            if int(rooms_value) == 1:
                break

        increase_room_button_element = self.find_element_by_css_selector('button[aria-label="Increase number of Rooms"]')

        for _ in range(room - 1):
                increase_room_button_element.click()


    def click_search(self):
        search_button = self.find_element_by_css_selector(
            'button[type="submit"]'
        )
        search_button.click()