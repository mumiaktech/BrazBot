# Help - List all available commands
def send_help(bot, chat_id):
    help_text = """
    Available Commands:
    /start - Welcome message and introduction to BrazBot.
    /help - List all available commands and how to use BrazBot.
    /about - Learn about BrazBot and its mission.
    /coffee_types - Discover different types of coffee (Arabica, Robusta, etc.).
    /process_brew - Explore brewing techniques and processing techniques..
    /coffee_facts - Get fun and interesting coffee facts.
    /coffee_origins - Learn about where coffee is grown and its history.
    /recipes - Get simple coffee recipes to try at home.
    /terms - Get common coffee-related terms.
    /subscribe - Get updates on new content and features from BrazBot.
    /equipments - Get to know more about existing coffee equipment and their uses.

    How to use BrazBot:
    - Simply type any of the available commands listed above to get relevant information.
    - For example, you can type "/coffee_types" to learn about different coffee beans or "/recipes" for some fun coffee recipes.
    """
    bot.send_message(chat_id, help_text)
