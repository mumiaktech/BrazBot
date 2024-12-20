import os
import sys
import threading
import telebot
from telebot import types
from dotenv import load_dotenv
from http.server import HTTPServer, BaseHTTPRequestHandler

# Load environment variables from the .env file
load_dotenv()

# Reconfigure stdout to handle UTF-8
sys.stdout.reconfigure(encoding='utf-8')

try:
    # Get the BOT_TOKEN from environment variables
    BOT_TOKEN = os.getenv("BOT_TOKEN")
    
    if not BOT_TOKEN:
        raise ValueError("Error: BOT_TOKEN environment variable is not set. Please configure it.")
    
    # Initialize the bot
    bot = telebot.TeleBot(BOT_TOKEN)
    print(f"BOT_TOKEN successfully loaded: {BOT_TOKEN[:5]}***{BOT_TOKEN[-3:]}")
    
    # Define the main menu function
    def show_main_menu(chat_id):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add("ℹ️ About", "🔍 Definitions")
        markup.add("🌍 Coffee Origins", "☕ Coffee Types")
        markup.add("📖 Brewing Methods", "🍳 Recipes")
        markup.add("⚙️ Equipment", "📚 Coffee Facts")
        markup.add("📬 Subscribe", "📢 Feedback")
        markup.add("💡 Tips", "🆘 Help")
        bot.send_message(chat_id, "Choose an option from the menu to continue: ", reply_markup=markup)

    # Bot command handlers
    @bot.message_handler(commands=['start', 'menu'])
    def send_start(message):
        bot.send_message(message.chat.id, "Welcome to BrazBot! ☕")
        show_main_menu(message.chat.id)

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

    # Run the bot in a separate thread
    def run_bot():
        print("✅ BrazBot is running...")
        bot.infinity_polling()

    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

    # Simple HTTP server to keep the service running on Render
    class HealthCheckHandler(BaseHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.end_headers()
            self.wfile.write(b"Health check: BrazBot is running")

    PORT = int(os.getenv("PORT", 8080))
    httpd = HTTPServer(("", PORT), HealthCheckHandler)
    print(f"HTTP server running on port {PORT}")
    httpd.serve_forever()

except ValueError as ve:
    print(f"[ValueError] {ve}")
    sys.exit(1)

except Exception as e:
    print(f"[Error] An unexpected error occurred: {e}")
    sys.exit(1)