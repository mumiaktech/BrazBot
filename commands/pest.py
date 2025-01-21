# Coffee Facts - Fun and interesting coffee facts
def send_pests(bot, chat_id):
    pests_text = """
    Common Coffee Diseases:
    Coffee Leaf Rust (CLR) (Hemileia vastatrix)  
    Coffee Berry Disease (CBD) (Colletotrichum kahawae)
    Root Rot (Fusarium spp., Pythium spp., Rhizoctonia spp.)
    Black Rot (Ceratocystis fimbriata)
    Coffee Wilt Disease (Gibberella xylarioides)
    
    Common Coffee Pests:
    Coffee Berry Borer (Hypothenemus hampei)
    Coffee Leaf Miner (Leucoptera coffeella)    
    Green Scales (Coccus viridis)
    White Stem Borer (Xylotrechus quadripes)
    Aphids (Toxoptera aurantii, Aphis gossypii)

    General Tips for Identification:
    Observation: Regularly inspect leaves, stems, and berries for unusual discoloration, holes, or deformities.
    Magnification: Use a hand lens to identify small pests or fungal spores.
    Environmental Factors: Note the climate and season, as some pests and diseases thrive in specific conditions (e.g., humidity for rust).
    Sampling: Collect affected plant parts for closer examination or lab testing if needed.
    """
    bot.send_message(chat_id, pests_text)
