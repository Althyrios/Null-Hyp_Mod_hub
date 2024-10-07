init python:

    def default_Kitty_Outfits():
        Outfits = []
        
        Outfits.append(OutfitClass("Casual 1", flags = ["public", "day"]))

        # Outfits[-1].Clothes.update({
        #     "bra": None, "underwear": None,
        #     "pants": None, "footwear": None,
        #     "top": None,
        #     "gloves": None})

        Outfits.append(OutfitClass("Casual 2", flags = ["public", "day"]))

        # Outfits[-1].Clothes.update({
        #     "bra": None, "underwear": None, "hose":None,
        #     "pants": None, "footwear": None,
        #     "top": None,
        #     "neck": None, "gloves": None, "sleeves": None,
        #     "jacket": None})

        Outfits.append(OutfitClass("Winter (Indoor)", flags = ["public"]))

        # Outfits[-1].Clothes.update({
        #     "bra": None, "underwear": None, "hose": None,
        #     "footwear": None,
        #     "dress": None,
        #     "gloves": None})

        Outfits.append(OutfitClass("Winter (Outdoor)", flags = ["public", "winter"]))

        # Outfits[-1].Clothes.update({
        #     "bra": None, "underwear": None, "hose": None,
        #     "footwear": None,
        #     "dress": None,
        #     "gloves": None,
        #     "jacket": None})

        Outfits.append(OutfitClass("Exercise", flags = ["exercise"]))

        # Outfits[-1].Clothes.update({
        #     "hair": None,
        #     "bra": None, "underwear": None, "hose": None, "socks": None, 
        #     "footwear": None,
        #     "gloves": None})

        Outfits.append(OutfitClass("Hero (Chapter I)", flags = ["hero"]))

        # Outfits[-1].Clothes.update({
        #     "face_inner_accessory": None,
        #     "bra": None, "underwear": None,
        #     "bodysuit": None,
        #     "footwear": None,
        #     "gloves": None, "belt": None,
        #     "jacket": None})

        Outfits.append(OutfitClass("Swimsuit (One-Piece)", flags = ["swim"]))

        # Outfits[-1].Clothes.update({
        #     "bodysuit": None})

        Clothes = {
            "bra": None, "underwear": None}

        # if check_if_Clothes_in_Wardrobe(Kitty, Clothes):
        #     Outfits.append(OutfitClass("Swimsuit (Bikini)", flags = ["swim"]))

        #     Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Datenight 1", flags = ["date"]))

        # Outfits[-1].Clothes.update({
        #     "bra": None, "underwear": None, "hose": None, 
        #     "skirt": None, "footwear": None,
        #     "top": None,
        #     "neck": None, "gloves": None})
        
        Outfits.append(OutfitClass("Datenight 2", flags = ["date"]))

        # Outfits[-1].Clothes.update({
        #     "underwear": None, "hose": None,
        #     "footwear": None,
        #     "dress": None,
        #     "neck": None, "gloves": None, "sleeves": None,
        #     "jacket": None})

        # Clothes = {
        #     "underwear": None,
        #     "footwear": None,
        #     "dress": None,
        #     "gloves": None}

        # if check_if_Clothes_in_Wardrobe(Kitty, Clothes):
        #     Outfits.append(OutfitClass("Formal", flags = []))

        #     Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Pajamas", flags = ["sleep"]))

        # Outfits[-1].Clothes.update({
        #     "bra": None, "underwear": None})

        # Clothes = {
        #     "bra": None, "underwear": None, "hose": None, "socks": None}

        # if check_if_Clothes_in_Wardrobe(Kitty, Clothes):
        #     Outfits.append(OutfitClass("Lingerie 1", flags = ["sex"]))

        #     Outfits[-1].Clothes.update(Clothes)

        # Clothes = {
        #     "underwear": None,
        #     "dress": None}

        # if check_if_Clothes_in_Wardrobe(Kitty, Clothes):
        #     Outfits.append(OutfitClass("Lingerie 2", flags = ["sex"]))

        #     Outfits[-1].Clothes.update(Clothes)

        Outfits.append(OutfitClass("Nude"))

        Outfits[-1].Clothes.update({})
                
        return Outfits