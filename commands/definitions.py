# Definitions - Get common coffee-related definitions
def send_definitions(bot, chat_id):
    definitions_text = """
    <b>Common Coffee Definitions:</b>

    1. <b>Espresso</b>: A concentrated coffee brewed by forcing hot water through finely ground coffee beans.
    2. <b>Arabica</b>: A type of coffee known for its mild and complex flavors.
    3. <b>Crema</b>: The golden, foamy layer on top of a well-made espresso shot.
    4. <b>Robusta</b>: A type of coffee known for its stronger and more bitter taste compared to Arabica.
    5. <b>Americano</b>: Espresso diluted with hot water to create a milder coffee drink.
    6. <b>Macchiato</b>: An espresso with a small amount of steamed milk or foam.
    7. <b>Cappuccino</b>: Espresso topped with steamed milk and milk foam.
    8. <b>Latte</b>: Espresso combined with steamed milk, topped with a small amount of foam.
    9. <b>Mocha</b>: A combination of espresso, steamed milk, and chocolate syrup.
    10. <b>Cold Brew</b>: Coffee brewed with cold water over an extended period, typically 12-24 hours.
    11. <b>Drip Coffee</b>: Coffee brewed by dripping hot water over ground coffee beans, typically using a coffee maker.
    12. <b>French Press<b>: A method of steeping coffee grounds in hot water, then pressing them with a plunger.
    13. <b>AeroPress</b>: A brewing device that uses pressure to extract coffee, similar to espresso.
    14. <b>Brew Ratio</b>: The ratio of coffee grounds to water used in brewing.
    15. <b>Single Origin</b>: Coffee sourced from one location, often highlighting unique flavors.
    16. <b>Blend</b>: Coffee made from beans sourced from different regions or varieties to create a balanced flavor.
    17. <b>Decaf</b>: Coffee made from beans that have been processed to remove most of the caffeine.
    18. <b>Tamping</b>: The process of pressing down the coffee grounds in an espresso machine to create an even surface.
    19. <b>Barista</b>: A person who prepares and serves coffee drinks, particularly espresso-based beverages.
    20. <b>Café au Lait</b>: French for "coffee with milk," typically brewed with drip coffee and steamed milk.
    21. <b>Iced Coffee</b>: Brewed coffee that is chilled and served over ice.
    22. <b>Nitro Coffee</b>: Cold brew coffee infused with nitrogen for a creamy texture and smooth finish.
    23. <b>Siphon Coffee</b>: A brewing method using a vacuum coffee maker that creates an elegant brewing process.
    24. <b>Percolator</b>: A coffee brewing device that brews coffee by cycling boiling water through coffee grounds.
    25. <b>Turkish Coffee</b>: A traditional coffee preparation where ground coffee is simmered in water and served unfiltered.
    26. <b>Flat White</b>: An espresso drink made with steamed milk and less foam than a cappuccino.
    27. <b>Single Shot</b>: A standard espresso shot made from around 7-9 grams of coffee grounds.
    28. <b>Double Shot</b>: An espresso shot made from around 14-18 grams of coffee grounds, typically the base for most drinks.
    29. <b>Coffee Bloom</b>: The initial bubbling of coffee when water is first poured over ground coffee due to the release of carbon dioxide.
    30. <b>Cupping</b>: A method of tasting coffee to evaluate its flavor and aroma, often used by roasters and coffee tasters.
    """
    bot.send_message(chat_id, definitions_text)
