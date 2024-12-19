# Recipes - Get simple coffee recipes
def send_recipes(bot, chat_id):
    recipes_text = """
    <b>Simple Coffee Recipes to Try at Home:</b>

    1. <b>Iced Coffee</b>:
       - Brew your coffee and let it cool.
       - Fill a glass with ice cubes, pour the coffee over the ice, and stir.
       - Sweeten with sugar or syrups, add milk or cream if desired, and enjoy.

    2. <b>Espresso Martini</b>:
       - Brew a shot of espresso and let it cool slightly.
       - In a shaker, combine 1 shot of espresso, 1 shot of vodka, and 1 shot of coffee liqueur (like Kahlúa).
       - Add ice, shake well, and strain into a chilled martini glass.

    3. <b>Mocha</b>:
       - Brew a shot of espresso and steam some milk.
       - In a cup, combine the espresso and a couple of tablespoons of chocolate syrup.
       - Add steamed milk, stir, and top with whipped cream for a decadent treat.

    4. <b>Cappuccino</b>:
       - Brew a shot of espresso and steam milk to create frothy foam.
       - Pour the espresso into a cup, add steamed milk, and top with a layer of foam.
       - Dust with cocoa powder or cinnamon for extra flavor.

    5. <b>Latte</b>:
       - Brew a shot of espresso and steam milk to create a creamy texture.
       - Pour the espresso into a cup and add the steamed milk.
       - For a stronger flavor, add a dash of vanilla syrup or flavored syrup of your choice.

    6. <b>Affogato</b>:
       - Brew a shot of espresso and pour it over a scoop of vanilla ice cream or gelato.
       - The hot espresso will melt the ice cream, creating a creamy, indulgent dessert.

    7. <b>Cold Brew</b>:
       - Coarsely grind coffee beans and mix them with cold water (1:4 coffee to water ratio).
       - Let it steep in the fridge for 12-24 hours.
       - Strain the coffee through a fine mesh or coffee filter, serve over ice, and enjoy.

    8. <b>Flat White</b>:
       - Brew a shot of espresso and steam milk to a velvety smooth texture.
       - Pour the espresso into a cup, then gently pour the steamed milk over it to create a silky smooth drink.
       - Unlike a latte, the milk in a flat white is less frothy and more velvety.

    9. <b>Irish Coffee</b>:
       - Brew a strong cup of coffee and add a tablespoon of brown sugar.
       - Stir until the sugar dissolves, then float a layer of Irish whiskey on top.
       - Gently spoon whipped cream on top for a creamy finish.

    10. <b>Turkish Coffee</b>:
        - In a cezve (small pot), mix very finely ground coffee, water, and sugar (optional) to taste.
        - Heat the mixture over low heat without stirring, bringing it to a boil. Remove before it overflows.
        - Pour into a small cup, allowing the grounds to settle before drinking.
    """
    bot.send_message(chat_id, recipes_text)
