# Brewing Methods - Explore brewing techniques
def send_process_brew(bot, chat_id):
    process_brew_text = """
    Coffee Processing Techniques and Brewing Methods
    
    Coffee Processing Techniques:
    
    These techniques focus on removing the coffee bean from the cherry and preparing it for roasting. The main types include:

    a. Natural (Dry) Process: The entire cherry is dried in the sun, and the bean is extracted later. This method results in a heavy-bodied coffee with complex flavors.

    b. Washed (Wet) Process: The cherry is removed from the bean before drying, and the bean is washed to remove the mucilage. This leads to a cleaner, brighter taste.
    
    c.Semi-Washed (Pulped Natural, Honey Process): The cherry is partially removed, and the bean is dried with some mucilage still attached. This method offers a balance between the natural and washed processes, with sweeter and more nuanced flavors.

    
    Coffee Brewing Methods:
    
    These methods involve preparing the roasted and ground coffee for consumption. They include:

    1. Pour-Over: Water is poured over coffee grounds in a filter, allowing for precise control over brewing variables and extraction.

    2. French Press: Coffee grounds are steeped in hot water, and then a plunger is used to separate the grounds from the liquid, resulting in a full-bodied cup.

    3. Espresso: High-pressure water is forced through finely ground coffee, producing a concentrated shot of coffee with a rich crema.

    4. Cold Brew: Coffee grounds are steeped in cold water for an extended period, resulting in a smooth, less acidic coffee.

    5. Drip Coffee: Hot water passes through coffee grounds in a filter, collecting the brewed coffee in a pot below, offering convenience and simplicity.
    """
    bot.send_message(chat_id, process_brew_text)
