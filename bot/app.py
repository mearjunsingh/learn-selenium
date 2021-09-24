from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='NPR')
    bot.select_place_to_go(place='Kathmandu')
    bot.select_dates(check_in_date='2021-09-25', check_out_date='2021-09-30')