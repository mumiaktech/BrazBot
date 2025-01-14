# Definitions - Get common coffee-related definitions
def send_terms(bot, chat_id):
    terms_text = """
    Common Coffee Terms:

    1. Acidity: The pleasant tartness of a fine coffee, often referred to as brightness or liveliness that carries the high notes of flavor in a coffee.
    2. Arabica: The earliest cultivated species of coffee tree (Coffea arabica), accounting for approximately 70% of the world’s coffee production. It is known for its superior quality and rich flavor profile.
    3. Aroma: The smell that is released from freshly ground coffee (dry aroma) and from freshly brewed coffee.
    4. Balance: A tasting term applied to a coffee for which no single characteristic overwhelms the others, yet the coffee displays sufficient complexity to be interesting.
    5. Barista: An Italian term for a skilled, experienced espresso bar operator.
    6. Blend: A mixture of two or more single-origin coffees.
    7. Burr Grinder: A device that uses two revolving burrs to grind coffee beans, ensuring a more consistent grind size.
    8. Caffè Americano: An espresso-based coffee drink made by topping espresso with hot water. It originated during World War II when American soldiers in Italy diluted local espresso with hot water.
    9. Cappuccino: A hot or cold coffee beverage made of equal parts espresso, steamed milk, and foamed milk.
    10. Chemex: A manual pour-over style glass coffeemaker, invented by Peter Schlumbohm in 1941.
    11. Cold Brew: A type of coffee made by steeping coffee grounds in cold water for an extended period, resulting in a less acidic and smoother taste.
    12. Espresso: Coffee brewed by forcing hot water through finely ground darkly roasted coffee beans.
    13. Flat White: Similar to a cappuccino but with less froth and a larger volume of microfoam.
    14. Organic Certification: A process designed to show that agricultural products have been grown and/or processed using organic practices, without the use of prohibited substances.
    15. Q Grader: A professional who has been trained and certified in the sensory evaluation of green coffee, recognized worldwide in the coffee industry.
    16. Specialty Coffee: Distinguished by the quality of its raw material and representing only 1-2 percent of all coffee grown worldwide.
    17. Terroir: From the French word “terre,” meaning land, it denotes the influence of geography, geology, and climate on a coffee’s unique taste qualities.
    18. Wet-Processed/Washed Coffee: A process that removes the skin and pulp from the bean while the coffee fruit is still fresh, used for most of the world’s coffees.
    """
    bot.send_message(chat_id, terms_text)
