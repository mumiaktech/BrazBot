# Coffee Facts - Fun and interesting coffee facts
def send_coffee_facts(bot, chat_id):
    coffee_facts_text = """
    <b>Fun Coffee Facts:<b>

    1. <b>Coffee was originally chewed, not brewed!</b> – Early coffee drinkers in Ethiopia would grind the beans and mix them with fat to form a ball, which they would chew for energy.
    
    2. <b>The world’s most expensive coffee is made from beans eaten and excreted by civet cats.</b> – Known as Kopi Luwak, this coffee is produced using beans that have been consumed and excreted by civet cats, and it can sell for over $600 per pound.
    
    3. <b>Coffee is the second most traded commodity in the world, after oil.</b> – With billions of cups consumed daily, coffee holds a massive place in global trade, making it a vital economic commodity.
    
    4. <b>There are over 100 different types of coffee beans.</b> – While Arabica and Robusta dominate, there are many other lesser-known types that contribute to the wide variety of flavors in coffee.
    
    5. <b>Coffee can improve your physical performance.</b> – The caffeine in coffee acts as a stimulant, boosting your energy levels and increasing physical performance by improving endurance and strength.
    
    6. <b>Finland is the world’s largest coffee consumer per capita.</b> – Finns drink an average of 12kg of coffee per person each year, which equates to approximately 4 cups per person per day.
    
    7. <b>Coffee is a fruit!</b> – Coffee beans are actually the seeds of the coffee fruit, known as a coffee cherry. The cherries grow on coffee plants and are harvested to extract the seeds.
    
    8. <b>Coffee helps with weight loss.</b> – Caffeine can increase metabolism and help burn fat by boosting the body's ability to burn calories.
    
    9. <b>The first coffeehouse opened in Istanbul in 1475.</b> – Coffeehouses, known as "qahveh khaneh," began in the Middle East, offering a place for people to socialize and enjoy their coffee.
    
    10. <b>Decaf coffee isn't completely caffeine-free.</b> – Decaffeinated coffee still contains some caffeine, though in much smaller amounts than regular coffee, usually around 2-5 milligrams per cup.
    """
    bot.send_message(chat_id, coffee_facts_text)
