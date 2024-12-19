# Coffee types - Discover different types of coffee
def send_coffee_types(bot, chat_id):
    coffee_types_text = """
    <b>What is Coffee?</b>
    Coffee is a popular beverage made from the seeds (commonly referred to as coffee beans) of the Coffea plant. These seeds are roasted to create the characteristic flavor profile we all recognize as coffee. The flavor of coffee can vary greatly depending on the bean type, region it’s grown in, and the method of brewing. Whether you prefer a mild, smooth cup or a strong, bold shot, there's a coffee for every taste.

    <b>The Two Main Types of Coffee Beans:</b>
    1. <b>Arabica</b>:
       Arabica coffee beans are the most widely consumed in the world, accounting for about 60-70% of global coffee production. They are known for their smooth, mild flavor profile with a slightly acidic taste. Arabica beans are grown in higher altitudes, mainly in Latin America, and tend to have a more complex and nuanced flavor compared to other beans. Common notes include fruit, floral, and sweet flavors, often with a soft mouthfeel.

    2. <b>Robusta</b>:
       Robusta beans are generally stronger, more bitter, and have a higher caffeine content than Arabica. These beans are often used in espresso blends to provide a fuller body and more intense flavor. Robusta coffee has earthy, woody, and sometimes even nutty flavors. It is grown mainly in lower altitudes in Africa and Southeast Asia, and while it’s not as popular as Arabica, it’s commonly used for its strong, bold taste and crema in espresso.

    <b>Other Types of Coffee Beans:</b>
    3. <b>Liberica</b>:
       A rare and distinctive bean, Liberica has a smoky, woody flavor profile with hints of spice and a unique aroma. Grown primarily in the Philippines and parts of West Africa, Liberica beans are larger than Arabica and Robusta and have a less common shape. While not widely known, they offer an adventurous flavor for those looking for something different.

    4. <b>Excelsa</b>:
       Excelsa beans are typically grown in Southeast Asia, mainly the Philippines, and have a tart, fruity flavor with notes of dark fruit and wildness. Often used in blends, Excelsa contributes a complex, deep flavor, combining both fruity acidity and savory notes. The bean is often confused with Liberica due to their similar appearances, but it has a more distinct and pronounced flavor profile.

    Each type of coffee bean offers a unique flavor and brewing experience, contributing to the diverse world of coffee. Whether you prefer a delicate, fruity cup of Arabica or a stronger, more robust shot of Robusta, there’s a coffee out there to suit every taste.
    """
    bot.send_message(chat_id, coffee_types_text)
