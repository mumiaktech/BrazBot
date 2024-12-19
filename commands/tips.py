# Tips - Brewing tips for the perfect cup of coffee
def send_tips(bot, chat_id):
    tips_text = """
    **Tips for Brewing the Perfect Cup of Coffee:**

    1. Use fresh, high-quality beans.
    2. Grind your coffee just before brewing.
    3. Use the right water temperature (195-205°F).
    4. Adjust the grind size according to your brewing method.
    5. Measure your coffee and water for consistency.
    6. Use filtered water to avoid impurities.
    7. Keep your equipment clean to avoid old coffee residues.
    8. Brew at the right time—don’t over-brew or under-brew.
    9. Store your coffee beans in an airtight container in a cool, dark place.
    10. Experiment with different brewing methods to find your perfect cup.
    """
    bot.send_message(chat_id, tips_text)
