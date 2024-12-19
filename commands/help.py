# Help - List all available commands
def send_help(bot, chat_id):
    help_text = """
    <b>Available Commands:</b>
    /start - Welcome message and introduction to BrazBot.
    /help - List all available commands and how to use BrazBot.
    /about - Learn about BrazBot and its mission.
    /coffee_types - Discover different types of coffee (Arabica, Robusta, etc.).
    /brewing_methods - Explore brewing techniques like drip, espresso, or French press.
    /coffee_facts - Get fun and interesting coffee facts.
    /coffee_origins - Learn about where coffee is grown and its history.
    /recipes - Get simple coffee recipes to try at home.
    /tips - Brewing tips for the perfect cup of coffee.
    /quiz - Take a fun coffee knowledge quiz.
    /feedback - Share your thoughts or ask questions about BrazBot.
    /definitions - Get common coffee-related definitions.
    /subscribe - Get updates on new content and features from BrazBot.
    /equipments - Get to know more about existing coffee equipment and their uses.

    <b>How to use BrazBot:</b>
    - Simply type any of the available commands listed above to get relevant information.
    - For example, you can type "/coffee_types" to learn about different coffee beans or "/recipes" for some fun coffee recipes.
    - You can interact with BrazBot by asking questions or sharing your thoughts with the "/feedback" command.
    """
    bot.send_message(chat_id, help_text)
