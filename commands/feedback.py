# Feedback - Share your thoughts or ask questions
def send_feedback(bot, chat_id):
    feedback_text = (
        "We’d love to hear from you! Please share your thoughts or questions about BrazBot, "
        "and we’ll get back to you as soon as we can. "
        "[Visit our website here](http://www.brazafric.com) for more information."
    )
    bot.send_message(chat_id, feedback_text, parse_mode='Markdown')
