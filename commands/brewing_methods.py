# Brewing Methods - Explore brewing techniques
def send_brewing_methods(bot, chat_id):
    brewing_methods_text = """
    <b>Popular Coffee Brewing Methods:<b>

    1. <b>Drip Coffee/b> – A common method using a coffee maker.
    - Add ground coffee to a filter, pour water into the machine's reservoir, and start the brewing process. Hot water drips through the grounds, extracting coffee flavors and dripping into a pot or carafe below.

    2. <b>Espresso</b> – A concentrated form of coffee made by forcing hot water through finely ground beans.
    - Pack finely ground coffee into the portafilter, tamp it down firmly, lock it into the espresso machine, and start the brewing. The machine forces hot water through the grounds under high pressure to extract a rich and concentrated shot of coffee.

    3. <b>French Press</b> – A method that uses steeping to extract coffee flavors.
    - Boil water and pour it over coarsely ground coffee in the French press, stir gently, place the lid on, and steep for about 4 minutes. Press the plunger down slowly to separate the grounds from the brewed coffee, and serve.

    4. <b>Aeropress</b> – A brewing technique that uses pressure to make coffee similar to espresso.
    - Insert a filter into the Aeropress, add finely ground coffee, pour in hot water, stir, and steep for about 30 seconds. Then, press down the plunger to extract coffee under pressure, producing a rich, smooth cup similar to espresso.

    These methods offer various strengths and flavors, from the smooth drip coffee to the strong and concentrated espresso, giving you a variety of ways to enjoy your coffee. Try them out to find your perfect brew!
    """
    bot.send_message(chat_id, brewing_methods_text)
