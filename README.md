# telegram PlaneTrip_bot
<p>Telegram bot that searches for cheap flights using Tequila API. The bot applies text recognition using regular expressions.
You need to set the API token of the bot, as well as the ID of the Telegram account in the environment variables:</p>

>_SECRET_TOKEN_ — bot API token
>
>_USER_ID_ — ID Telegram of User, from which messages will be received (messages from other accounts are ignored)
>
>_API_KEY_ - secret key for Tequila API connection


<h2>How does it work</h2>

The bot searches for air tickets in a given direction up to specified maximum price. The bot offers the user some input templates, according to which the following parameters will be then recognized: 
<ul>
  <li>oneway or round flight
   <li> departure and arrival cities 
   <li> max changes allowed
   <li> allowed date interval during which the user is considering the trip (note that these are <b>not departure and arrival dates</b>)  
   <li> min and max days of stay/trip if round
     <li> max price allowed
 </ul>

Example of input template:

>Type a desired destination in the following mode: 
><p><b>round direct Milan to Mykonos </b></p>
><p>or <b>oneway 1 change Berlin to London </b></p>
><p>or <b>round direct Milan to anywhere </b></p>

<br>
<p>After successful request, the bot will return to the user with an offer to complete his booking on Kiwi website, message example:</p>


>Hey! I found something interesting for you!

>Oneway flight from Milan (MXP) to Mykonos (JMK) with departure on 2022-04-09 at a great price 44 EUR.
>Hurry up and <a href="https://www.kiwi.com/deep?from=MXP&to=JMK&flightsId=07f015d04a930000d924071f_0%7C15d007f04a9a0000ca8d6697_0&price=44.0&passengers=1&affilid=katyaaltflightsearcher&lang=en&currency=EUR&booking_token=D_afXviyyywjnD8uSF8oRl4D4BQF9m1xVl8fpfklzvtQ80xgcIjMb9rux8mMkr6HkUAINW45XoS5Jlxws5bqcfR3AnCbN3tKcIZmtCsBXGV1ZOAHk15bMaZcw4MvjmbsBXFlc7fU50zTpk3sR0-EaTZtJiP-DzVb6JDVKVpjFsjsvHBfNP2RverLW7vea8EwCqCTGTLKERjG4lTUIeLriFkpX9erzTvoKQNI0Jgekp2xhJdGsT7qp0uHHecZvJEdfSNOTmqWIYUwKFpNz3DfGgdWKShflNQskF70PjGankM938-LYqSLR7VHYMrHdXhsgQLbKpfKP6slF0hdeLyUkWuNRaSGbIIt-3jCWRJEa9QgOmYgr7H_gaFkJ94gP322c1tfWvmiFHJDYFo2Q-NJTJ62s1gfgllKJiCv5dLe9xc-n3fS0q-JyR9XPE2k04QbVTFIQHAC8o-uqtJtaHlK-pA==">>complete your booking here🥝</a> Don't like it? Start new /search_destination!

>Your PlaneTrip bot
<br>

<p align="center">
  <img src="QR-code/planetrip_qr.jpg" width="250" title="hover text">
</p>


_**In the near future the bot will be able to create a database for the user's wishlist, check directions from the wishlist on its own and notify the user when the price falls to allowed level.**_

