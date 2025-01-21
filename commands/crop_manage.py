# Coffee Facts - Fun and interesting coffee facts
def send_crop_manage(bot, chat_id):
    crop_manage_text = """
    Coffee Crop Management
    Coffee crop management involves several key practices to ensure healthy growth and high-quality yield. Here are some important aspects of coffee crop management:

    Nutrient Management: Coffee plants require essential nutrients such as nitrogen (N), phosphorus (P), potassium (K), calcium (Ca), magnesium (Mg), sulfur (S), iron (Fe), manganese (Mn), zinc (Zn), boron (B), and copper (Cu). These nutrients are crucial for increasing crop productivity, especially since coffee is often grown in nutrient-depleted tropical soils. Proper fertilization is necessary to optimize fruit development and new branch growth.
    Pest and Disease Control: Coffee crops are susceptible to various pests and diseases, including the coffee borer and coffee rust. Farmers can manage these threats using pesticides and fungicides, or through more natural methods such as shade-grown coffee or promoting local biodiversity. Biocontrol and biopesticides, which use natural enemies of pests and diseases, are sustainable and safe options for maintaining crop health.
    Shade and Agroforestry: Historically, coffee has been grown in the shade of other trees, often in wild forest settings. Some agricultural techniques replicate these settings by planting coffee alongside trees (agroforestry) or crops that provide financial value from their fruit, leaves, or timber. These methods can help diversify income and improve soil health, carbon sequestration, and biodiversity.
    Harvesting: Coffee cherries turn red when ripe and are usually picked by hand, as widespread use of mechanical harvesters is not possible due to the mountainous terrain where coffee is often grown. A good picker can harvest 45 to 90 kilos of coffee cherries per day, which produces nine to 18 kilos of coffee beans.
    Climate Change Adaptation: Climate change poses significant risks to coffee production, including reduced yields and decreased suitable land for cultivation. Farmers need to adopt resilient agricultural practices to mitigate these risks. This includes managing soil, water, and nutrient resources effectively to address issues like drought, salinity, and biodiversity decline.
    Effective crop management practices can help coffee farmers maintain high-quality yields and adapt to the challenges posed by climate change.
    """
    bot.send_message(chat_id, crop_manage_text)
