# Subscribe - Get updates on new content and features
def send_subscription(bot, chat_id):
    subscription_text = (
        "Subscribe to get the latest updates, new coffee tips, and features from BrazBot! "
        "[Visit our website here](http://www.brazafric.com) for more information."
    )
    bot.send_message(chat_id,  subscription_text, parse_mode='Markdown')
