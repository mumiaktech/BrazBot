# Coffee Facts - Fun and interesting coffee facts
def send_pest(bot, chat_id):
    pest_text = """
    Common Coffee Diseases
    
    Coffee Leaf Rust (CLR) (Hemileia vastatrix)
        Symptoms: Yellow-orange powdery spots on the underside of leaves; leaves may drop prematurely.
        Identification: Look for circular lesions with orange spore masses, especially during humid conditions.
        
    Coffee Berry Disease (CBD) (Colletotrichum kahawae)
        Symptoms: Dark, sunken lesions on berries that expand and cause fruit rot.
        Identification: Typically seen during the wet season; berries shrivel and blacken.

    Root Rot (Fusarium spp., Pythium spp., Rhizoctonia spp.)
        Symptoms: Wilting, stunted growth, yellowing leaves, and root decay.
        Identification: Check roots for mushy, brown tissues and ensure soil drainage is adequate.

    Black Rot (Ceratocystis fimbriata)
        Symptoms: Black discoloration of stems, leaves, and berries.
        Identification: Look for cankers on branches and wilting of affected areas.

    Coffee Wilt Disease (Gibberella xylarioides)
        Symptoms: Sudden wilting, dieback, and dark streaks inside the stem.
        Identification: Cut open stems to check for vascular discoloration.
    
    Common Coffee Pests
    
    Coffee Berry Borer (Hypothenemus hampei)
        Symptoms: Small holes in coffee berries; beans may be damaged or hollowed out.
        Identification: Inspect berries for entry holes and frass (sawdust-like material).
        
    Coffee Leaf Miner (Leucoptera coffeella)    
        Symptoms: White trails or blotches on leaves caused by larval feeding.
        Identification: Look for larvae or pupae within leaf mines.

    Green Scales (Coccus viridis)
        Symptoms: Sticky honeydew on leaves and stems, sooty mold growth, and plant weakening.
        Identification: Check for small, green, oval-shaped insects clustered on stems and leaves.
    
    White Stem Borer (Xylotrechus quadripes)
        Symptoms: Yellowing leaves, premature leaf drop, and boreholes in stems.
        Identification: Examine stems for entry/exit holes and frass.

    Aphids (Toxoptera aurantii, Aphis gossypii)
        Symptoms: Curling or yellowing leaves, sticky honeydew, and presence of ants.
        Identification: Look for small, soft-bodied insects in clusters on young shoots and leaves.

    General Tips for Identification
    Observation: Regularly inspect leaves, stems, and berries for unusual discoloration, holes, or deformities.
    Magnification: Use a hand lens to identify small pests or fungal spores.
    Environmental Factors: Note the climate and season, as some pests and diseases thrive in specific conditions (e.g., humidity for rust).
    Sampling: Collect affected plant parts for closer examination or lab testing if needed.
    """
    bot.send_message(chat_id, pest_text)
