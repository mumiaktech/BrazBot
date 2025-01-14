# Equipment - Get to know more about existing coffee equipment
def send_equipments(bot, chat_id):
    equipments_text = """
    Coffee Equipment from Brazafric:

    Pulping Equipment:
    1. Coffee Polishing Machines: Machines that polish roasted coffee beans to enhance their appearance and reduce static.
    2. Coffee Sorting Machines: Equipment that sorts coffee beans based on size, weight, and quality, ensuring uniformity in the final product.
    3. Coffee Decaffeination Equipment: Specialized machines that remove caffeine from coffee beans while preserving their flavor.
    4. Coffee Blending Equipment: Machines that blend different coffee beans to create unique flavor profiles.
    5. Coffee Storage Silos: Large containers used to store green or roasted coffee beans, maintaining their quality and freshness.

    Milling Equipment:
    1. Coffee Grinders: Devices used to grind roasted coffee beans to the desired consistency for brewing.
    2. Coffee Brewing Machines: Equipment that automates the process of brewing coffee, ensuring consistency and efficiency.
    3. Coffee Capsules and Pod Machines: Single-serve machines that brew coffee from pre-packaged pods.
    4. Cold Brew Coffee Makers: Specialized brewers designed to steep coffee grounds in cold water for 12-24 hours.
    5. Percolators: Devices that brew coffee by continuously cycling boiling water through coffee grounds.

    Roasting Equipment:
    1. Coffee Roasters: Machines designed to roast green coffee beans, enhancing their flavor and aroma.
    2. Coffee Cooling Systems: Equipment that cools roasted coffee beans rapidly to halt the roasting process and preserve flavor.
    3. Espresso Machines: Devices that brew espresso by forcing hot water through finely-ground coffee beans.
    4. Cappuccino Machines: Espresso machines equipped with a steam wand to froth milk for cappuccinos.
    5. Moka Pots: Small stovetop coffee makers that brew coffee by passing boiling water pressurized by steam through ground coffee.

    Visit Brazafric for your coffee equipment needs!

    To explore more equipment, innovations, and high-quality coffee machines, visit [Brazafric](http://www.brazafric.com). Find the perfect tools to take your coffee experience to the next level!
    """
    bot.send_message(chat_id, equipments_text)
