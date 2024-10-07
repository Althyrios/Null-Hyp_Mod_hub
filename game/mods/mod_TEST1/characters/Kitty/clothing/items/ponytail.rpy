init -1 python:
    
    def Kitty_ponytail_hair():
        name = "ponytail_hair"
        short_name = "hair"
        string = "ponytail"
        
        Clothing_type = "hair"

        shop_type = "salon"
        chapter = 0
        season = 0

        thresholds = {
            "accept": [0, 0],
            "wear_in_private": [0, 0],
            "wear_in_public": [0, 0]}
        
        price = 0
        
        shame = [0, 0]
        
        available_states = {
            "standing": [0],
            "doggy": [0],
            "hands_and_knees": [0],
            "masturbation": [0],
            "missionary": [0]}
        undressed_states = {
            "standing": 0,
            "doggy": 0,
            "hands_and_knees": 0,
            "masturbation": 0,
            "missionary": 0}
        
        covers = {
            "standing": {},
            "doggy": {},
            "hands_and_knees": {},
            "masturbation": {},
            "missionary": {}}
        hides = {
            "standing": {},
            "doggy": {},
            "hands_and_knees": {},
            "masturbation": {},
            "missionary": {}}

        blocked_by = {}
        obscured_by = {}
        covered_by = {}

        traits = []
        
        return ClothingClass(
            Kitty, 
            name, short_name, string, Clothing_type, 
            shop_type, chapter, season,
            thresholds,
            price = int(price*work_unit*min(max(renpy.random.gauss(1.0, 0.15), 0.85), 1.15)), shame = shame, 
            available_states = available_states, undressed_states = undressed_states,
            covers = covers, hides = hides, 
            blocked_by = blocked_by, obscured_by = obscured_by, covered_by = covered_by,
            traits = traits)


label Kitty_ponytail_hair_shopping_accept:

    return

label Kitty_ponytail_hair_shopping_reject:

    return

label Kitty_ponytail_hair_gift_accept:

    return

label Kitty_ponytail_hair_gift_reject:

    return

label Kitty_ponytail_hair_change_private_before:

    return

label Kitty_ponytail_hair_change_private_after:

    return

label Kitty_ponytail_hair_change_public_before:

    return

label Kitty_ponytail_hair_change_public_after:

    return