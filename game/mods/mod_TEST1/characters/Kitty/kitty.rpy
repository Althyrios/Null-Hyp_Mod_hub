init -1:
        
    default Kitty = create_Kitty()
    
    define Kitty_color = "#9123ad"
    define ch_Kitty = Character("[Kitty.tag]")

init -2 python:

    def create_Kitty():
        Kitty = CompanionClass("Kitty", voice = ch_Kitty)
        
        Kitty.full_name = "Kitty Pryde"
        Kitty.public_name = "Kitty"
        Kitty.call_sign = "Kitty"

        Kitty.database_type = "ally"

        Kitty.default_hair = "ponytail_hair"

        Kitty.default_body_hair = {
            "pubic": "bush",
            "anus": None,
            "armpits": None}

        Kitty.Player_petname = "pal"
        Kitty.Player_petnames.append(Player.first_name)
        Kitty.Player_petnames.append(Kitty.Player_petname)

        Kitty.body_hair = Kitty.default_body_hair
        Kitty.desired_body_hair = Kitty.default_body_hair

        Kitty.give_trait("virgin")
        Kitty.give_trait("ground_shadow")
        Kitty.give_trait("bedroom_lights_on")

        Cast.append(Kitty.tag)
        # Sprites.append(Kitty)

        all_Characters.append(Kitty)
        all_Companions.append(Kitty)
        Students.append(Kitty)

        mods_Companions.append(Kitty)

        bedrooms.append(Kitty.home)

        return Kitty

    def Kitty_faces(face):
        blush = 0

        if face == "neutral":
            brows = "neutral"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "angry1":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "angry2":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "happy"
        elif face == "appalled1":
            brows = "furrowed"
            eyes = "wide"
            mouth = "neutral"
        elif face == "appalled2":
            brows = "furrowed"
            eyes = "wide"
            mouth = "open"
        elif face == "appalled3":
            brows = "furrowed"
            eyes = "wide"
            mouth = "agape"
        elif face == "confused1":
            brows = "cocked"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "confused2":
            brows = "cocked"
            eyes = "wide"
            mouth = "neutral"
        elif face == "confused3":
            brows = "cocked"
            eyes = "wide"
            mouth = "agape"
        elif face == "devious":
            brows = "neutral"
            eyes = "squint"
            mouth = "smile"
        elif face == "furious":
            brows = "furrowed"
            eyes = "neutral"
            mouth = "frown"
        elif face == "grimace":
            brows = "furrowed"
            eyes = "closed"
            mouth = "lipbite"
        elif face == "happy":
            brows = "neutral"
            eyes = "neutral"
            mouth = "smile"
        elif face == "kiss1":
            brows = "worried"
            eyes = "closed"
            mouth = "kiss"
        elif face == "kiss2":
            brows = "neutral"
            eyes = "closed"
            mouth = "kiss"
        elif face == "manic":
            brows = "worried"
            eyes = "wide"
            mouth = "open"
            blush = 1
        elif face == "perplexed":
            brows = "cocked"
            eyes = "wide"
            mouth = "open"
        elif face == "pleased1":
            brows = "raised"
            eyes = "neutral"
            mouth = "smirk"
        elif face == "pleased2":
            brows = "raised"
            eyes = "wide"
            mouth = "smirk"
        elif face == "sad":
            brows = "worried"
            eyes = "neutral"
            mouth = "frown"
        elif face == "sexy":
            brows = "neutral"
            eyes = "sexy"
            mouth = "lipbite"
        elif face == "sly":
            brows = "neutral"
            eyes = "squint"
            mouth = "smirk"
        elif face == "smirk1":
            brows = "neutral"
            eyes = "neutral"
            mouth = "happy"
        elif face == "smirk2":
            brows = "neutral"
            eyes = "neutral"
            mouth = "smirk"
        elif face == "surprised1":
            brows = "raised"
            eyes = "neutral"
            mouth = "open"
        elif face == "surprised2":
            brows = "raised"
            eyes = "wide"
            mouth = "open"
        elif face == "surprised3":
            brows = "raised"
            eyes = "wide"
            mouth = "agape"
        elif face == "suspicious1":
            brows = "furrowed"
            eyes = "squint"
            mouth = "neutral"
        elif face == "suspicious2":
            brows = "furrowed"
            eyes = "squint"
            mouth = "frown"
        elif face == "wink":
            brows = "wink"
            eyes = "wink"
            mouth = "kiss"
        elif face == "worried1":
            brows = "worried"
            eyes = "neutral"
            mouth = "neutral"
        elif face == "worried2":
            brows = "worried"
            eyes = "wide"
            mouth = "neutral"
        elif face == "worried3":
            brows = "worried"
            eyes = "wide"
            mouth = "open"
        elif face == "worried4":
            brows = "worried"
            eyes = "wide"
            mouth = "agape"
        else:
            return "wrong", "wrong", "wrong", 0

        return brows, eyes, mouth, blush

    def Kitty_arms(pose):
        if pose == "neutral":
            left_arm = "neutral"
            right_arm = "neutral"
        elif pose == "angry":
            left_arm = "fist"
            right_arm = "fist"
        elif pose == "bra":
            left_arm = "bra"
            right_arm = "bra"
        elif pose == "come_here":
            left_arm = "fight"
            right_arm = "extended"
        elif pose == "crossed":
            left_arm = "crossed"
            right_arm = "crossed"
        elif pose == "fight":
            left_arm = "fight"
            right_arm = "fight"
        elif pose == "hips":
            left_arm = "hip"
            right_arm = "hip"
        elif pose == "plug":
            left_arm = "touch_ass"
            right_arm = "fist"
        elif pose == "sass":
            left_arm = "hip"
            right_arm = "neutral"
        elif pose == "sheepish":
            left_arm = "rub_neck"
            right_arm = "extended"
        elif pose == "shrug":
            left_arm = "extended"
            right_arm = "extended"
        elif pose == "touch_self":
            left_arm = "grope"
            right_arm = "touch_pussy"
        else:
            return "wrong", "wrong"

        return left_arm, right_arm

    def Kitty_locations():
        possible_locations = []

        possible_locations.append(Kitty.home)

        # if time_index < 3 and weather != "rain":
        #     possible_locations.append("bg_campus")

        # if weekday < 5 and time_index < 2:
        #     possible_locations.append("bg_classroom")
        #     possible_locations.append("bg_classroom")

        # if time_index < 3 and Kitty.location != "bg_lockers" and not Kitty.History.check("trained_with_Player", tracker = "daily"):
        #     possible_locations.append("bg_danger")

        # if time_index < 3:
        #     if time_index == 2:
        #         if temperature[time_index] > 22 and not weather and snow_left == 0:
        #             possible_locations.append("bg_pool")

        #         possible_locations.append("bg_mall")
        #     elif weekday > 4:
        #         if temperature[time_index] > 22 and not weather and snow_left == 0:
        #             possible_locations.append("bg_pool")

        #         possible_locations.append("bg_mall")

        # if day > 3:
        #     if (Kitty in Partners or Kitty.status["nympho"] or approval_check(Kitty, threshold = "love")) and renpy.random.random() > 0.85:
        #         if (Player.location not in bedrooms or Player.location == Player.home) and (Player.location != "bg_shower_Player" or Kitty.check_traits("has_keys_to_Players_room")):
        #             possible_locations.append(Player.location)

        #         if Kitty.check_traits("has_keys_to_Players_room"):
        #             possible_locations.append(Player.home)

        return possible_locations
    
    

label update_Kitty:
    # $ Kitty.full_name = "Kitty Pryde"
    # $ Kitty.call_sign = "Kitty Pryde"

    # $ Kitty.database_type = "ally"

    return