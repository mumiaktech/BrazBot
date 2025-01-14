# Coffee origins - Learn about where coffee is grown
def send_coffee_origins(bot, chat_id):
    coffee_origins_text = """
    Coffee Origins:

    Coffee is grown in the "coffee belt," a region located between the Tropics of Cancer and Capricorn, which includes countries in South America, Africa, and Asia. This belt has the ideal climate for growing coffee, with rich soils, high altitudes, and the right balance of rainfall and sunshine. Coffee plants thrive in these regions, producing the beans that are enjoyed worldwide. Let’s explore some famous coffee-growing countries:

    1. Ethiopia (The Birthplace of Coffee):
    Ethiopia is widely regarded as the birthplace of coffee, with a rich history that dates back centuries. According to legend, coffee was discovered in Ethiopia by a goat herder named Kaldi, who noticed that his goats became energetic after eating the red cherries from a particular tree. Today, Ethiopia remains a top producer of coffee, especially prized for its heirloom varieties that offer bright acidity, floral notes, and complex flavors. Ethiopian coffee is typically grown at high altitudes in regions such as Sidamo, Yirgacheffe, and Harrar. The country’s diverse coffee varieties, often processed using natural or washed methods, contribute to its unique and flavorful cups.

    2. Brazil (The Largest Producer of Coffee):
    Brazil has been the world’s largest producer of coffee for over 150 years. The country’s vast coffee plantations, particularly in the regions of Minas Gerais, São Paulo, and Espírito Santo, account for about one-third of the world’s coffee supply. Brazilian coffee is known for its nutty, chocolatey flavors, with low acidity and a smooth body. The country produces both Arabica and Robusta beans, though Arabica is more common. Brazil’s coffee-growing landscape is diverse, ranging from flat plains to mountainous terrains, which allows for a wide variety of flavor profiles. The country is also known for its innovative coffee farming techniques and large-scale production, making it an essential player in the global coffee market.

    3. Colombia (Famous for its Smooth, Mild Coffee):
    Colombian coffee is renowned for its smooth, balanced flavor and mild acidity. The country’s coffee-growing regions are located in the Andes Mountains, where the altitude and climate provide optimal conditions for Arabica coffee cultivation. Colombian coffee is known for its clean, crisp taste with notes of citrus, caramel, and floral undertones. The regions of Antioquia, Quindío, and Cauca are particularly famous for producing some of the highest-quality beans. Colombia’s coffee farmers use traditional and sustainable farming methods, often hand-picking the coffee cherries at their peak ripeness to ensure the highest quality. Colombian coffee has long been a favorite among coffee drinkers due to its consistency, excellent flavor, and rich cultural heritage.

    These three countries—Ethiopia, Brazil, and Colombia—are just the tip of the iceberg when it comes to coffee cultivation. Many other countries, such as Kenya, Guatemala, and Vietnam, contribute their unique beans to the coffee industry, offering coffee lovers a wide range of flavors to enjoy. The coffee belt continues to be the heart of the global coffee industry, producing some of the world’s best-loved brews.
    """
    bot.send_message(chat_id, coffee_origins_text)
