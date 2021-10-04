from booking.booking import Booking


with Booking() as bot:
    bot.land_first_page()
    bot.change_currency(currency='NPR')
    bot.select_place_to_go(place='Pokhara')
    bot.select_dates(check_in_date='2021-10-03', check_out_date='2021-10-05')
    bot.persons_and_room(person=5, room=3)
    bot.click_search()
    # bot.apply_filteration()
    bot.refresh()
    bot.report_results()