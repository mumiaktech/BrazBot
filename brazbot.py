import os
import sys
import telebot
from telebot import types
from dotenv import load_dotenv

# Load environment variables from the .env file
load_dotenv()

try:
    # Get the BOT_TOKEN from environment variables using os.getenv
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    
    # Validate if BOT_TOKEN is set
    if not BOT_TOKEN:
        raise ValueError("Error: BOT_TOKEN environment variable is not set. Please configure it.")
    
    # Initialize the bot
    bot = telebot.TeleBot(BOT_TOKEN)
    
    # Print the BOT_TOKEN safely (masking part of it)
    print(f"BOT_TOKEN successfully loaded: {BOT_TOKEN[:5]}***{BOT_TOKEN[-3:]}")

    # Function to display the main menu
    def show_main_menu(chat_id):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("ℹ️ About", "🔍 Definitions")
        markup.add("🌍 Coffee Origins", "☕ Coffee Types")
        markup.add("📖 Brewing Methods", "🍳 Recipes")
        markup.add("⚙️ Equipment", "📚 Coffee Facts")
        markup.add("📬 Subscribe", "📢 Feedback")
        markup.add("💡 Tips", "🆘 Help")
        bot.send_message(chat_id, "Choose an option from the menu to continue: ", reply_markup=markup)

    # Command handler to start the bot and show the menu
    @bot.message_handler(commands=['start', 'menu'])
    def send_start(message):
        bot.send_message(message.chat.id, "Welcome to BrazBot! ☕")
        show_main_menu(message.chat.id)

    # Command handlers for menu options
    @bot.message_handler(func=lambda message: message.text == "☕ Coffee Types")
    def handle_coffee_types(message):
        from commands.coffee_types import send_coffee_types
        send_coffee_types(bot, message.chat.id)
        show_main_menu(message.chat.id)

    @bot.message_handler(func=lambda message: message.text == "📖 Brewing Methods")
    def handle_brewing_methods(message):
        from commands.brewing_methods import send_brewing_methods
        send_brewing_methods(bot, message.chat.id)
        show_main_menu(message.chat.id)

    @bot.message_handler(func=lambda message: message.text == "📚 Coffee Facts")
    def handle_coffee_facts(message):
        from commands.coffee_facts import send_coffee_facts
        send_coffee_facts(bot, message.chat.id)
        show_main_menu(message.chat.id)

    @bot.message_handler(func=lambda message: message.text == "🌍 Coffee Origins")
    def handle_coffee_origins(message):
        from commands.coffee_origins import send_coffee_origins
        send_coffee_origins(bot, message.chat.id)
        show_main_menu(message.chat.id)

    @bot.message_handler(func=lambda message: message.text == "🍳 Recipes")
    def handle_recipes(message):
        from commands.recipes import send_recipes
        send_recipes(bot, message.chat.id)
        show_main_menu(message.chat.id)

    @bot.message_handler(func=lambda message: message.text == "📬 Subscribe")
    def handle_subscribe(message):
        from commands.subscribe import send_subscription
        send_subscription(bot, message.chat.id)
        show_main_menu(message.chat.id)

    @bot.message_handler(func=lambda message: message.text == "ℹ️ About")
    def handle_about(message):
        from commands.about import send_about
        send_about(bot, message.chat.id)
        show_main_menu(message.chat.id)

    @bot.message_handler(func=lambda message: message.text == "🔍 Definitions")
    def handle_definitions(message):
        from commands.definitions import send_definitions
        send_definitions(bot, message.chat.id)
        show_main_menu(message.chat.id)

    @bot.message_handler(func=lambda message: message.text == "⚙️ Equipment")
    def handle_equipment(message):
        from commands.equipments import send_equipments
        send_equipments(bot, message.chat.id)
        show_main_menu(message.chat.id)

    @bot.message_handler(func=lambda message: message.text == "📢 Feedback")
    def handle_feedback(message):
        from commands.feedback import send_feedback
        send_feedback(bot, message.chat.id)
        show_main_menu(message.chat.id)

    @bot.message_handler(func=lambda message: message.text == "🆘 Help")
    def handle_help(message):
        from commands.help import send_help
        send_help(bot, message.chat.id)
        show_main_menu(message.chat.id)

    @bot.message_handler(func=lambda message: message.text == "💡 Tips")
    def handle_tips(message):
        from commands.tips import send_tips
        send_tips(bot, message.chat.id)
        show_main_menu(message.chat.id)

    # Keep the bot running
    print("✅ BrazBot is running...")
    bot.infinity_polling()

except ValueError as ve:
    print(f"[ValueError] {ve}")
    sys.exit(1)

except Exception as e:
    print(f"[Error] An unexpected error occurred: {e}")
    sys.exit(1)
