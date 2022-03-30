class Messages:
    def __init__(self):
        self.greeting = '<b> Hi! I am PlaneTrip bot ✈️ </b>\n\nI will help you to plan your best trip. ' \
                        'Here are my general commands:\n\n- /search_destination a new Trip to list\n\n' \
                        'Let\'s start creating your Trip list of all desired destinations'
        self.ask_destination = 'Type a desired destination in the following mode: \n\n<b>round direct Milan to ' \
                               'Mykonos </b>\n or \n<b>oneway 1 change Berlin to London </b>\n or \n<b>round ' \
                               'direct Milan to anywhere' \
                               ' </b>'
        self.ask_round_date_interval = 'Type a desired date, min and max amount days in the following mode:' \
                                       ' \n\n<b>24/03 - 08/07 min 7 max 12 days</b>'
        self.ask_oneway_date_interval = 'Type a desired date in the following mode: \n\n<b>24/03 - 08/07</b>'

        self.ask_price = f'Price up to .. EUR/GBP/USD'
        self.unsuccessful_result = 'There is no interesting flight for you at this moment, ' \
                                   'try another /search_destination or check this trip a little bit later 🥝'
        self.denied = 'Sorry, Access Denied'
