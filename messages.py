class Messages:
    def __init__(self):
        self.greeting = '<b> Hi! I am PlaneTrip bot ✈️ </b>\n\nI will help you to plan your exciting trip - just ' \
                        'type direction, the date interval when you plan a trip and the maximum price you\'d like ' \
                        'to spend. HINT! You can even choose ' \
                        '"anywhere" to discover random destinations   \n\n-' \
                        'Let\'s start! Press this command to /search_destination'
        self.ask_destination = 'Great! Type desired destination in the following mode: \n\n<b>round direct Milan to ' \
                               'Mykonos </b>\n or \n<b>oneway 1 change Berlin to London </b>\n or \n<b>round ' \
                               'direct Milan to anywhere' \
                               ' </b>'
        self.ask_round_date_interval = 'Type desired date interval where you plan your Trip, min and max amount  ' \
                                       'of nights of stay in the chosen city like this:' \
                                       ' \n\n<b>20/05/2022-08/06/2022 min 3 max 5 days</b> \n\n or simply for current year\n\n<b>20/05-08/06 min 7 max 12</b>'
        self.ask_oneway_date_interval = 'Type a desired date interval where you plan a Trip in the following mode:' \
                                        ' \n\n<b>20/05/2022-08/06/2022</b>\n\n or simply for current year\n\n<b>20/05-08/06 </b>'

        self.ask_price = f'Type max price allowed for the whole trip ... EUR/GBP/USD, for example:' \
                         f'\n\n<b>50 euro</b> or <b>65 usd</b>'
        self.unsuccessful_result = 'There is no interesting flight for you at this moment, ' \
                                   'try another /search_destination or check this trip a little bit later 🥝'
        self.denied = 'Sorry, Access Denied'
