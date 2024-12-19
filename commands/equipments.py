# Equipment - Get to know more about existing coffee equipment
def send_equipments(bot, chat_id):
    equipments_text = """
    <b>Coffee Equipment from Brazafric:</b>

    <b>Pulping Equipment:</b>
    1. <b>Coffee Polishing Machines</b>: Machines that polish roasted coffee beans to enhance their appearance and reduce static.
    2. <b>Coffee Sorting Machines</b>: Equipment that sorts coffee beans based on size, weight, and quality, ensuring uniformity in the final product.
    3. <b>Coffee Decaffeination Equipment</b>: Specialized machines that remove caffeine from coffee beans while preserving their flavor.
    4. <b>Coffee Blending Equipment</b>: Machines that blend different coffee beans to create unique flavor profiles.
    5. <b>Coffee Storage Silos</b>: Large containers used to store green or roasted coffee beans, maintaining their quality and freshness.

    <b>Milling Equipment:</b>
    1. <b>Coffee Grinders</b>: Devices used to grind roasted coffee beans to the desired consistency for brewing.
    2. <b>Coffee Brewing Machines</b>: Equipment that automates the process of brewing coffee, ensuring consistency and efficiency.
    3. <b>Coffee Capsules and Pod Machines</b>: Single-serve machines that brew coffee from pre-packaged pods.
    4. <b>Cold Brew Coffee Makers</b>: Specialized brewers designed to steep coffee grounds in cold water for 12-24 hours.
    5. <b>Percolators</b>: Devices that brew coffee by continuously cycling boiling water through coffee grounds.

    <b>Roasting Equipment:</b>
    1. <b>Coffee Roasters</b>: Machines designed to roast green coffee beans, enhancing their flavor and aroma.
    2. <b>Coffee Cooling Systems</b>: Equipment that cools roasted coffee beans rapidly to halt the roasting process and preserve flavor.
    3. <b>Espresso Machines</b>: Devices that brew espresso by forcing hot water through finely-ground coffee beans.
    4. <b>Cappuccino Machines</b>: Espresso machines equipped with a steam wand to froth milk for cappuccinos.
    5. <b>Moka Pots</b>: Small stovetop coffee makers that brew coffee by passing boiling water pressurized by steam through ground coffee.

    <b>Visit Brazafric for your coffee equipment needs!</b>

    To explore more equipment, innovations, and high-quality coffee machines, visit <b>[Brazafric](http://www.brazafric.com)</b>. Find the perfect tools to take your coffee experience to the next level!
    """
    bot.send_message(chat_id, equipments_text, parse_mode='HTML')
