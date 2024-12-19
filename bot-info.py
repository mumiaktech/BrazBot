import os
from dotenv import load_dotenv
import telebot
from telebot import types

# Load environment variables from the .env file
load_dotenv()

# Get the BOT_TOKEN from environment variables
BOT_TOKEN = os.getenv('BOT_TOKEN')

# Check if the BOT_TOKEN is loaded properly
if BOT_TOKEN is None:
    print("Error: BOT_TOKEN not found in environment variables or .env file.")
else:
    print(f"BOT_TOKEN: {BOT_TOKEN}")  # This line is optional, for debugging purposes

    # Initialize the bot
    bot = telebot.TeleBot(BOT_TOKEN)

    # Welcome and introduction
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Welcome to BrazBot! I’m here to share everything about coffee, including its types, brewing methods, fun facts, recipes, and more. Type /help to see all available commands.")

    # Help - List all available commands
    @bot.message_handler(commands=['help'])
    def send_help(message):
        help_text = """
        Available Commands:
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

        How to use BrazBot:
        - Simply type any of the available commands listed above to get relevant information.
        - For example, you can type "/coffee_types" to learn about different coffee beans or "/recipes" for some fun coffee recipes.
        - You can interact with BrazBot by asking questions or sharing your thoughts with the "/feedback" command.
        """
        bot.reply_to(message, help_text)

    # About - Learn about BrazBot and its mission
    @bot.message_handler(commands=['about'])
    def send_about(message):
        about_text = """
        Welcome to BrazBot, your ultimate guide to everything coffee! BrazBot is dedicated to bringing you the best of coffee culture, from its rich history to various brewing techniques, diverse coffee types, and fun, interesting facts that make coffee such a fascinating topic. Whether you're a coffee enthusiast or a casual drinker, BrazBot has something for everyone!

        Our mission is to inspire and educate coffee lovers around the world by sharing valuable insights, tips, and knowledge about all things coffee. From understanding the origins of your favorite brew to discovering new brewing methods and recipes, we aim to provide a comprehensive experience that connects you to the global coffee culture.

        **About Brazafric**:
        Brazafric is a visionary company dedicated to revolutionizing the coffee industry in Africa. We work towards promoting high-quality African coffee and fostering a deeper appreciation for coffee grown on the continent. By supporting local farmers, advocating for sustainable farming practices, and highlighting the uniqueness of African coffee beans, Brazafric strives to bring the authentic tastes of Africa to coffee lovers worldwide.

        Our mission is not just about coffee; it's about making a positive impact on communities, promoting ethical sourcing, and building a bridge between African coffee producers and the global market. Through BrazBot, we aim to share this vision and bring more awareness to the wonderful world of African coffee.
    
        Join us in exploring the fascinating world of coffee and become a part of the Brazafric movement, where coffee means more than just a drink—it's a culture, a story, and a shared experience.
    
        """
        bot.reply_to(message, about_text)

    # Coffee types - Discover different types of coffee
    @bot.message_handler(commands=['coffee_types'])
    def send_coffee_types(message):
        coffee_types_text = """
         **What is Coffee?**
        Coffee is a popular beverage made from the seeds (commonly referred to as coffee beans) of the Coffea plant. These seeds are roasted to create the characteristic flavor profile we all recognize as coffee. The flavor of coffee can vary greatly depending on the bean type, region it’s grown in, and the method of brewing. Whether you prefer a mild, smooth cup or a strong, bold shot, there's a coffee for every taste.

        **The Two Main Types of Coffee Beans:**
        1. **Arabica** - Arabica coffee beans are the most widely consumed in the world, accounting for about 60-70% of global coffee production. They are known for their smooth, mild flavor profile with a slightly acidic taste. Arabica beans are grown in higher altitudes, mainly in Latin America, and tend to have a more complex and nuanced flavor compared to other beans. Common notes include fruit, floral, and sweet flavors, often with a soft mouthfeel.
        2. **Robusta** - Robusta beans are generally stronger, more bitter, and have a higher caffeine content than Arabica. These beans are often used in espresso blends to provide a fuller body and more intense flavor. Robusta coffee has earthy, woody, and sometimes even nutty flavors. It is grown mainly in lower altitudes in Africa and Southeast Asia, and while it’s not as popular as Arabica, it’s commonly used for its strong, bold taste and crema in espresso.

        **Others commonly known:**
        3. **Liberica** - A rare and distinctive bean, Liberica has a smoky, woody flavor profile with hints of spice and a unique aroma. Grown primarily in the Philippines and parts of West Africa, Liberica beans are larger than Arabica and Robusta and have a less common shape. While not widely known, they offer an adventurous flavor for those looking for something different.
        4. **Excelsa** - Excelsa beans are typically grown in Southeast Asia, mainly the Philippines, and have a tart, fruity flavor with notes of dark fruit and wildness. Often used in blends, Excelsa contributes a complex, deep flavor, combining both fruity acidity and savory notes. The bean is often confused with Liberica due to their similar appearances, but it has a more distinct and pronounced flavor profile.

        **Other Types of Coffee Beans:**
        5. **Typica** - Typica is the base variety for many Arabica coffee beans. It originated in Ethiopia and is now grown in coffee-producing regions worldwide. Typica beans tend to have a balanced flavor profile with mild acidity and pleasant sweetness.
        6. **Caturra** - A natural mutation of the Bourbon variety, Caturra is widely grown in Brazil and Colombia. Known for its bright acidity and medium body, Caturra beans are prized for their smooth taste and adaptability to various growing conditions.
        7. **Bourbon** - Bourbon is one of the most popular Arabica varieties. It originated in the Indian Ocean island of Réunion (formerly Bourbon) and is known for its complex flavor profile, including notes of chocolate, nuts, and fruit. It's grown in regions with high altitudes and can produce a sweeter, more vibrant cup.
        8. **Gesha (Geisha)** - Gesha, also known as Geisha, is a high-quality Arabica variety famous for its unique flavor profile. Originating in Ethiopia, Gesha is highly sought after in the specialty coffee world due to its intense floral notes, jasmine-like aroma, and tea-like body. It’s one of the most expensive and prestigious coffee varieties globally.
        9. **SL28** - SL28 is a variety of Arabica coffee originating in Kenya. It is known for its bright acidity, vibrant fruit flavors, and wine-like qualities. SL28 beans are highly prized by coffee enthusiasts for their complexity and bold flavors, often including notes of blackcurrant, citrus, and tropical fruits.
        10. **Pacamara** - A hybrid of Pacas and Maragogipe, Pacamara beans are grown primarily in Central America. Known for their large size, these beans offer a rich flavor profile with a balanced acidity and sweet, fruity undertones. Pacamara is commonly used in high-end specialty coffee.
        11. **Catuai** - A hybrid of Mundo Novo and Caturra, Catuai beans are mostly grown in Brazil. They are known for their resilience to wind and rain, producing a cup with low acidity and mild flavor, often with nutty or chocolatey undertones.

        Each type of coffee bean offers a unique flavor and brewing experience, contributing to the diverse world of coffee. Whether you prefer a delicate, fruity cup of Arabica or a stronger, more robust shot of Robusta, there’s a coffee out there to suit every taste.
        """
        bot.reply_to(message, coffee_types_text)

    # Brewing methods - Explore brewing techniques
    @bot.message_handler(commands=['brewing_methods'])
    def send_brewing_methods(message):
        brewing_methods_text = """
        **Popular Coffee Brewing Methods:**

        1. **Drip Coffee** – A common method using a coffee maker.
        - Add ground coffee to a filter, pour water into the machine's reservoir, and start the brewing process. Hot water drips through the grounds, extracting coffee flavors and dripping into a pot or carafe below.

        2. **Espresso** – A concentrated form of coffee made by forcing hot water through finely ground beans.
        - Pack finely ground coffee into the portafilter, tamp it down firmly, lock it into the espresso machine, and start the brewing. The machine forces hot water through the grounds under high pressure to extract a rich and concentrated shot of coffee.

        3. **French Press** – A method that uses steeping to extract coffee flavors.
        - Boil water and pour it over coarsely ground coffee in the French press, stir gently, place the lid on, and steep for about 4 minutes. Press the plunger down slowly to separate the grounds from the brewed coffee, and serve.

        4. **Aeropress** – A brewing technique that uses pressure to make coffee similar to espresso.
        - Insert a filter into the Aeropress, add finely ground coffee, pour in hot water, stir, and steep for about 30 seconds. Then, press down the plunger to extract coffee under pressure, producing a rich, smooth cup similar to espresso.

        These methods offer various strengths and flavors, from the smooth drip coffee to the strong and concentrated espresso, giving you a variety of ways to enjoy your coffee. Try them out to find your perfect brew!
        """
        bot.reply_to(message, brewing_methods_text)

    # Coffee facts - Fun and interesting coffee facts
    @bot.message_handler(commands=['coffee_facts'])
    def send_coffee_facts(message):
        coffee_facts_text = """
        **Fun Coffee Facts:**

        1. **Coffee was originally chewed, not brewed!** – Early coffee drinkers in Ethiopia would grind the beans and mix them with fat to form a ball, which they would chew for energy.
        
        2. **The world’s most expensive coffee is made from beans eaten and excreted by civet cats.** – Known as Kopi Luwak, this coffee is produced using beans that have been consumed and excreted by civet cats, and it can sell for over $600 per pound.
        
        3. **Coffee is the second most traded commodity in the world, after oil.** – With billions of cups consumed daily, coffee holds a massive place in global trade, making it a vital economic commodity.
        
        4. **There are over 100 different types of coffee beans.** – While Arabica and Robusta dominate, there are many other lesser-known types that contribute to the wide variety of flavors in coffee.
        
        5. **Coffee can improve your physical performance.** – The caffeine in coffee acts as a stimulant, boosting your energy levels and increasing physical performance by improving endurance and strength.
        
        6. **Finland is the world’s largest coffee consumer per capita.** – Finns drink an average of 12kg of coffee per person each year, which equates to approximately 4 cups per person per day.
        
        7. **Coffee is a fruit!** – Coffee beans are actually the seeds of the coffee fruit, known as a coffee cherry. The cherries grow on coffee plants and are harvested to extract the seeds.
        
        8. **Coffee helps with weight loss.** – Caffeine can increase metabolism and help burn fat by boosting the body's ability to burn calories.
        
        9. **The first coffeehouse opened in Istanbul in 1475.** – Coffeehouses, known as "qahveh khaneh," began in the Middle East, offering a place for people to socialize and enjoy their coffee.
        
        10. **Decaf coffee isn't completely caffeine-free.** – Decaffeinated coffee still contains some caffeine, though in much smaller amounts than regular coffee, usually around 2-5 milligrams per cup.
        """
        bot.reply_to(message, coffee_facts_text)

    # Coffee origins - Learn about where coffee is grown
    @bot.message_handler(commands=['coffee_origins'])
    def send_coffee_origins(message):
        coffee_origins_text = """
        **Coffee Origins:**

        Coffee is grown in the "coffee belt," a region located between the Tropics of Cancer and Capricorn, which includes countries in South America, Africa, and Asia. This belt has the ideal climate for growing coffee, with rich soils, high altitudes, and the right balance of rainfall and sunshine. Coffee plants thrive in these regions, producing the beans that are enjoyed worldwide. Let’s explore some famous coffee-growing countries:

        1. **Ethiopia (The Birthplace of Coffee)**:
        Ethiopia is widely regarded as the birthplace of coffee, with a rich history that dates back centuries. According to legend, coffee was discovered in Ethiopia by a goat herder named Kaldi, who noticed that his goats became energetic after eating the red cherries from a particular tree. Today, Ethiopia remains a top producer of coffee, especially prized for its heirloom varieties that offer bright acidity, floral notes, and complex flavors. Ethiopian coffee is typically grown at high altitudes in regions such as Sidamo, Yirgacheffe, and Harrar. The country’s diverse coffee varieties, often processed using natural or washed methods, contribute to its unique and flavorful cups.

        2. **Brazil (The Largest Producer of Coffee)**:
        Brazil has been the world’s largest producer of coffee for over 150 years. The country’s vast coffee plantations, particularly in the regions of Minas Gerais, São Paulo, and Espírito Santo, account for about one-third of the world’s coffee supply. Brazilian coffee is known for its nutty, chocolatey flavors, with low acidity and a smooth body. The country produces both Arabica and Robusta beans, though Arabica is more common. Brazil’s coffee-growing landscape is diverse, ranging from flat plains to mountainous terrains, which allows for a wide variety of flavor profiles. The country is also known for its innovative coffee farming techniques and large-scale production, making it an essential player in the global coffee market.

        3. **Colombia (Famous for its Smooth, Mild Coffee)**:
        Colombian coffee is renowned for its smooth, balanced flavor and mild acidity. The country’s coffee-growing regions are located in the Andes Mountains, where the altitude and climate provide optimal conditions for Arabica coffee cultivation. Colombian coffee is known for its clean, crisp taste with notes of citrus, caramel, and floral undertones. The regions of Antioquia, Quindío, and Cauca are particularly famous for producing some of the highest-quality beans. Colombia’s coffee farmers use traditional and sustainable farming methods, often hand-picking the coffee cherries at their peak ripeness to ensure the highest quality. Colombian coffee has long been a favorite among coffee drinkers due to its consistency, excellent flavor, and rich cultural heritage.

        These three countries—Ethiopia, Brazil, and Colombia—are just the tip of the iceberg when it comes to coffee cultivation. Many other countries, such as Kenya, Guatemala, and Vietnam, contribute their unique beans to the coffee industry, offering coffee lovers a wide range of flavors to enjoy. The coffee belt continues to be the heart of the global coffee industry, producing some of the world’s best-loved brews.
        """
        bot.reply_to(message, coffee_origins_text)

    # Recipes - Get simple coffee recipes
    @bot.message_handler(commands=['recipes'])
    def send_recipes(message):
        recipes_text = """
        **Simple Coffee Recipes to Try at Home:**

        1. **Iced Coffee**:
        - Brew your coffee and let it cool.
        - Fill a glass with ice cubes, pour the coffee over the ice, and stir.
        - Sweeten with sugar or syrups, add milk or cream if desired, and enjoy.

        2. **Espresso Martini**:
        - Brew a shot of espresso and let it cool slightly.
        - In a shaker, combine 1 shot of espresso, 1 shot of vodka, and 1 shot of coffee liqueur (like Kahlúa).
        - Add ice, shake well, and strain into a chilled martini glass.

        3. **Mocha**:
        - Brew a shot of espresso and steam some milk.
        - In a cup, combine the espresso and a couple of tablespoons of chocolate syrup.
        - Add steamed milk, stir, and top with whipped cream for a decadent treat.

        4. **Cappuccino**:
        - Brew a shot of espresso and steam milk to create frothy foam.
        - Pour the espresso into a cup, add steamed milk, and top with a layer of foam.
        - Dust with cocoa powder or cinnamon for extra flavor.

        5. **Latte**:
        - Brew a shot of espresso and steam milk to create a creamy texture.
        - Pour the espresso into a cup and add the steamed milk.
        - For a stronger flavor, add a dash of vanilla syrup or flavored syrup of your choice.

        6. **Affogato**:
        - Brew a shot of espresso and pour it over a scoop of vanilla ice cream or gelato.
        - The hot espresso will melt the ice cream, creating a creamy, indulgent dessert.

        7. **Cold Brew**:
        - Coarsely grind coffee beans and mix them with cold water (1:4 coffee to water ratio).
        - Let it steep in the fridge for 12-24 hours.
        - Strain the coffee through a fine mesh or coffee filter, serve over ice, and enjoy.

        8. **Flat White**:
        - Brew a shot of espresso and steam milk to a velvety smooth texture.
        - Pour the espresso into a cup, then gently pour the steamed milk over it to create a silky smooth drink.
        - Unlike a latte, the milk in a flat white is less frothy and more velvety.

        9. **Irish Coffee**:
        - Brew a strong cup of coffee and add a tablespoon of brown sugar.
        - Stir until the sugar dissolves, then float a layer of Irish whiskey on top.
        - Gently spoon whipped cream on top for a creamy finish.

        10. **Turkish Coffee**:
        - In a cezve (small pot), mix very finely ground coffee, water, and sugar (optional) to taste.
        - Heat the mixture over low heat without stirring, bringing it to a boil. Remove before it overflows.
        - Pour into a small cup, allowing the grounds to settle before drinking.
        """
        bot.reply_to(message, recipes_text)

    # Tips - Brewing tips for the perfect cup of coffee
    @bot.message_handler(commands=['tips'])
    def send_tips(message):
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
        bot.reply_to(message, tips_text)

    # Quiz - Coffee knowledge quiz
    @bot.message_handler(commands=['quiz'])
    def send_quiz(message):
        # Initialize the quiz questions and answers
        questions = [
            {
                "question": "What is the world’s most expensive coffee?",
                "options": ["Kopi Luwak", "Jamaican Blue Mountain", "Black Ivory", "Sumatra"],
                "answer": "Kopi Luwak"
            },
            {
                "question": "Which country is the largest producer of coffee?",
                "options": ["Brazil", "Vietnam", "Colombia", "Ethiopia"],
                "answer": "Brazil"
            },
            {
                "question": "What type of coffee bean is the most popular?",
                "options": ["Arabica", "Robusta", "Liberica", "Excelsa"],
                "answer": "Arabica"
            },
            {
                "question": "Which coffee brewing method uses pressure to extract coffee?",
                "options": ["Espresso", "French Press", "Drip Coffee", "Aeropress"],
                "answer": "Espresso"
            },
            {
                "question": "What coffee variety is known for its smooth and mild flavor?",
                "options": ["Arabica", "Robusta", "Excelsa", "Liberica"],
                "answer": "Arabica"
            }
        ]

        # Define a function to send the quiz question and options
        def send_question(question_data, q_num):
            markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
            for option in question_data["options"]:
                markup.add(option)
            
            bot.send_message(
                message.chat.id, 
                f"Question {q_num}: {question_data['question']}", 
                reply_markup=markup
            )
            
        # Send first question
        send_question(questions[0], 1)
        
        # Wait for the user’s response and check their answer
        @bot.message_handler(func=lambda msg: True)
        def check_answer(message):
            # Get the current question index and answer
            current_question_index = 0
            user_answer = message.text
            correct_answer = questions[current_question_index]["answer"]
            
            # Check if the answer is correct or not
            if user_answer == correct_answer:
                bot.send_message(message.chat.id, "Correct! 😊")
            else:
                bot.send_message(message.chat.id, f"Wrong! The correct answer is: {correct_answer}")
            
            # Move to the next question
            current_question_index += 1
            if current_question_index < len(questions):
                send_question(questions[current_question_index], current_question_index + 1)
            else:
                bot.send_message(message.chat.id, "Quiz Completed! 🎉")

    # Feedback - Share your thoughts or ask questions
    @bot.message_handler(commands=['feedback'])
    def send_feedback(message):
        feedback_text = (
            "We’d love to hear from you! Please share your thoughts or questions about BrazBot, "
            "and we’ll get back to you as soon as we can. "
            "[Visit our website here](http://www.brazafric.com) for more information."
        )
        bot.reply_to(message, feedback_text, parse_mode='Markdown')

    # Definitions - Get common coffee-related definitions
    @bot.message_handler(commands=['definitions'])
    def send_definitions(message):
        definitions_text = """
        **Common Coffee Definitions:**

        1. **Espresso**: A concentrated coffee brewed by forcing hot water through finely ground coffee beans.
        2. **Arabica**: A type of coffee known for its mild and complex flavors.
        3. **Crema**: The golden, foamy layer on top of a well-made espresso shot.
        4. **Robusta**: A type of coffee known for its stronger and more bitter taste compared to Arabica.
        5. **Americano**: Espresso diluted with hot water to create a milder coffee drink.
        6. **Macchiato**: An espresso with a small amount of steamed milk or foam.
        7. **Cappuccino**: Espresso topped with steamed milk and milk foam.
        8. **Latte**: Espresso combined with steamed milk, topped with a small amount of foam.
        9. **Mocha**: A combination of espresso, steamed milk, and chocolate syrup.
        10. **Cold Brew**: Coffee brewed with cold water over an extended period, typically 12-24 hours.
        11. **Drip Coffee**: Coffee brewed by dripping hot water over ground coffee beans, typically using a coffee maker.
        12. **French Press**: A method of steeping coffee grounds in hot water, then pressing them with a plunger.
        13. **AeroPress**: A brewing device that uses pressure to extract coffee, similar to espresso.
        14. **Brew Ratio**: The ratio of coffee grounds to water used in brewing.
        15. **Single Origin**: Coffee sourced from one location, often highlighting unique flavors.
        16. **Blend**: Coffee made from beans sourced from different regions or varieties to create a balanced flavor.
        17. **Decaf**: Coffee made from beans that have been processed to remove most of the caffeine.
        18. **Tamping**: The process of pressing down the coffee grounds in an espresso machine to create an even surface.
        19. **Barista**: A person who prepares and serves coffee drinks, particularly espresso-based beverages.
        20. **Café au Lait**: French for "coffee with milk," typically brewed with drip coffee and steamed milk.
        21. **Iced Coffee**: Brewed coffee that is chilled and served over ice.
        22. **Nitro Coffee**: Cold brew coffee infused with nitrogen for a creamy texture and smooth finish.
        23. **Siphon Coffee**: A brewing method using a vacuum coffee maker that creates an elegant brewing process.
        24. **Percolator**: A coffee brewing device that brews coffee by cycling boiling water through coffee grounds.
        25. **Turkish Coffee**: A traditional coffee preparation where ground coffee is simmered in water and served unfiltered.
        26. **Flat White**: An espresso drink made with steamed milk and less foam than a cappuccino.
        27. **Single Shot**: A standard espresso shot made from around 7-9 grams of coffee grounds.
        28. **Double Shot**: An espresso shot made from around 14-18 grams of coffee grounds, typically the base for most drinks.
        29. **Coffee Bloom**: The initial bubbling of coffee when water is first poured over ground coffee due to the release of carbon dioxide.
        30. **Cupping**: A method of tasting coffee to evaluate its flavor and aroma, often used by roasters and coffee tasters.
        """
        bot.reply_to(message, definitions_text)

    # Subscribe - Get updates on new content and features
    @bot.message_handler(commands=['subscribe'])
    def send_subscription(message):
        subscription_text = (
            "Subscribe to get the latest updates, new coffee tips, and features from BrazBot! "
            "[Visit our website here](http://www.brazafric.com) for more information."
        )
        bot.reply_to(message, subscription_text, parse_mode='Markdown')

    # Equipment - Get to know more about existing coffee equipment
    @bot.message_handler(commands=['equipments'])
    def send_equipments(message):
        equipments_text = """
        **Coffee Equipment from Brazafric and Pinhalense:**

        1. **Coffee Roasters**: Machines designed to roast green coffee beans, enhancing their flavor and aroma.
        2. **Coffee Grinders**: Devices used to grind roasted coffee beans to the desired consistency for brewing.
        3. **Coffee Brewing Machines**: Equipment that automates the process of brewing coffee, ensuring consistency and efficiency.
        4. **Coffee Packaging Machines**: Machines that package roasted coffee into various forms, such as ground coffee or whole beans, for retail distribution.
        5. **Coffee Sorting Machines**: Equipment that sorts coffee beans based on size, weight, and quality, ensuring uniformity in the final product.
        6. **Coffee Polishing Machines**: Machines that polish roasted coffee beans to enhance their appearance and reduce static.
        7. **Coffee Decaffeination Equipment**: Specialized machines that remove caffeine from coffee beans while preserving their flavor.
        8. **Coffee Blending Equipment**: Machines that blend different coffee beans to create unique flavor profiles.
        9. **Coffee Storage Silos**: Large containers used to store green or roasted coffee beans, maintaining their quality and freshness.
        10. **Coffee Cooling Systems**: Equipment that cools roasted coffee beans rapidly to halt the roasting process and preserve flavor.
        11. **Espresso Machines**: Devices that brew espresso by forcing hot water through finely-ground coffee beans.
        12. **Drip Coffee Makers**: Machines used for brewing coffee by dripping hot water through coffee grounds in a filter.
        13. **French Press**: A method of brewing coffee by steeping grounds in hot water and pressing them with a plunger.
        14. **Aeropress**: A portable coffee brewing device that uses air pressure to push water through coffee grounds.
        15. **Cappuccino Machines**: Espresso machines equipped with a steam wand to froth milk for cappuccinos.
        16. **Coffee Capsules and Pod Machines**: Single-serve machines that brew coffee from pre-packaged pods.
        17. **Cold Brew Coffee Makers**: Specialized brewers designed to steep coffee grounds in cold water for 12-24 hours.
        18. **Siphon Coffee Makers**: Coffee makers using vacuum pressure to brew coffee, known for their unique brewing process.
        19. **Percolators**: Devices that brew coffee by continuously cycling boiling water through coffee grounds.
        20. **Moka Pots**: Small stovetop coffee makers that brew coffee by passing boiling water pressurized by steam through ground coffee.
        21. **Grind Control Machines**: Coffee grinders equipped with adjustable settings for different grind sizes based on brewing methods.
        22. **Coffee Filter Paper Machines**: Machines used to produce and package coffee filter paper for use in brewing.
        23. **Coffee Roasting Control Systems**: Automated systems that monitor and control the roasting process to ensure consistency.
        24. **Pneumatic Bean Elevators**: Systems that use air pressure to move coffee beans between different stages of production.
        25. **Turbine Coffee Roasters**: Roasting machines that use a rotating drum to evenly roast coffee beans.
        26. **Batch Coffee Roasters**: Roasters that process large batches of coffee beans at once.
        27. **Conveyor Belt Roasters**: Machines that move beans along a conveyor belt through a roasting chamber.
        28. **Coffeebean De-stoners**: Machines that remove stones and other foreign objects from coffee beans before roasting.
        29. **Cooling Trays**: Containers used to cool freshly roasted coffee beans rapidly.
        30. **Coffee Bean Elevators**: Mechanical devices used to transport coffee beans through different stages of processing.
        31. **Storage Bags and Containers**: Materials used to store coffee beans, maintaining their quality and freshness.
        32. **Grinding Hoppers**: Containers that store and feed coffee beans into grinding machines.
        33. **Coffee Moisture Analyzers**: Devices used to measure the moisture content of coffee beans, ensuring they are at optimal dryness.
        34. **Coffee Bean Sorters**: Machines that separate beans based on size, shape, and quality to ensure consistency.
        35. **Automated Coffee Brewing Systems**: Fully automated brewing systems used in coffee shops for high-volume production.
        36. **Coffee Sifters**: Devices used to sift ground coffee to achieve a consistent grind size.
        37. **Espresso Grinder Dosing Systems**: Machines that measure and dispense the right amount of coffee grounds for espresso.
        38. **Milk Frothers**: Handheld or machine-operated devices used to froth milk for drinks like lattes and cappuccinos.
        39. **Coffee Warming Stations**: Equipment used to keep brewed coffee warm in commercial settings.
        40. **Coffee Cup Sealing Machines**: Machines that seal coffee cups to prevent spills and preserve freshness in takeaway coffee.
        41. **Coffee Bean Roasting Paddles**: Tools used to stir coffee beans manually during the roasting process.
        42. **Coffee Blending Tanks**: Containers used for mixing different batches of roasted beans to achieve the desired flavor profile.
        43. **Coffee Flavor Profilers**: Devices used to analyze and rate the flavor of coffee beans.
        44. **Coffee Wet Processing Machines**: Machines used in the wet processing method, removing the coffee cherry’s outer layer.
        45. **Dry Milling Machines**: Machines used to remove the parchment layer from coffee beans after they have been dried.
        46. **Coffee Packaging Scales**: Devices used to weigh coffee beans or grounds during the packaging process.
        47. **Coffee Sealing and Labeling Machines**: Machines used for sealing coffee bags and labeling them for distribution.
        48. **Automated Coffee Dispensers**: Machines used to dispense pre-ground coffee for brewing.
        49. **Coffee Bean Degassing Chambers**: Containers that allow coffee beans to degas after roasting, releasing carbon dioxide.
        50. **Coffee Air Compressors**: Machines used to provide compressed air for pneumatic systems involved in coffee production.

        **Visit Brazafric for your coffee equipment needs!**

        To explore more equipment, innovations, and high-quality coffee machines, visit **[Brazafric](http://www.brazafric.com)**. Find the perfect tools to take your coffee experience to the next level!
        """
        bot.reply_to(message, equipments_text)

    # Start polling
    bot.infinity_polling()
