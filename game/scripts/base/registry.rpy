init python:

    def register_Characters():
        global shop_inventory
        global unrestricted_shop_inventory

        test = eval(f"PlayerClass('John', 'Doe', voice = ch_Player)")

        for attribute in test.__dict__.keys():
            if attribute not in Player.__dict__.keys():
                setattr(Player, attribute, test.__dict__[attribute])

        del test

        ## can delete eventually
        Player.animations = {
            "blink": {
                "start": 0.0,
                "delay": 3.5}}

        for part in ["breath", "head", "hair", "tongue", "left_arm", "right_arm", "left_leg", "right_leg", "orgasming", "vibrator", "dildo_pussy", "dildo_ass", "remote_vibrator"]:
            if part == "breath":
                times = [1.5, 1.25, 1.75]
                bounds = [-0.5, 0.5]
            else:
                times = [0.0, 2.0]
                bounds = [0.0, 0.0]

            Player.animations.update({
                part: {
                    "start": 0.0,
                    "times": times,
                    "bounds": bounds}})

        for part in Player.animations.keys():
            Player.animations[part]["start"] = 0.0

        if "active" not in Player.skin_tint.keys():
            Player.skin_tint.update({"active": None})
            Player.hair_tint.update({"active": None})

        for C in all_Characters:
            if C in all_Companions:
                test = eval(f"CompanionClass('{C.tag}', voice = ch_{C.tag}, love = 0, trust = 0)")
            elif C in all_NPCs:
                test = eval(f"NPCClass('{C.tag}', voice = ch_{C.tag})")
            else:
                continue

            for attribute in test.__dict__.keys():
                if attribute not in C.__dict__.keys():
                    setattr(C, attribute, test.__dict__[attribute])

            del test

            ## can delete eventually
            C.animations = {
                "blink": {
                    "start": 0.0,
                    "delay": 3.5}}

            for part in ["breath", "head", "hair", "tongue", "left_arm", "right_arm", "left_leg", "right_leg", "orgasming", "vibrator", "dildo_pussy", "dildo_ass", "remote_vibrator"]:
                if part == "breath":
                    times = [1.5, 1.25, 1.75]
                    bounds = [-0.5, 0.5]
                else:
                    times = [0.0, 2.0]
                    bounds = [0.0, 0.0]

                C.animations.update({
                    part: {
                        "start": 0.0,
                        "times": times,
                        "bounds": bounds}})

            for part in C.animations.keys():
                C.animations[part]["start"] = 0.0

            if C in all_Companions:
                if "active" not in C.body_hair_tint.keys():
                    C.body_hair_tint.update({"active": None})
                    C.tan_tint.update({"active": None})

            if C in all_Companions or C == Kurt:
                if game_started:
                    if C.location == Player.location and C.Outfit.name != "null":
                        set_default_Outfits(C, change = False)
                    else:
                        set_default_Outfits(C, change = True)
                else:
                    set_default_Outfits(C, change = True)

                Clothing_list = eval(f"all_{C.tag}_Clothes()")

                temp_Clothing_list = list(C.Wardrobe.Clothes.keys())

                for I in temp_Clothing_list:
                    found = False

                    for I_A in Clothing_list:
                        if I == I_A.name:
                            found = True

                            break

                    if not found:
                        del C.Wardrobe.Clothes[I]

                for I in Clothing_list:
                    hair = "hair" in I.name or "bun" in I.name or "ponytail" in I.name or "mohawk" in I.name

                    if I.name in C.Wardrobe.Clothes.keys() or hair:
                        if not hair:
                            if C.Wardrobe.Clothes[I.name].selected_state in C.Wardrobe.Clothes[I.name].available_states["standing"]:
                                I.selected_state = C.Wardrobe.Clothes[I.name].selected_state
                            else:
                                I.selected_state = I.available_states["standing"][0]

                        if I.name in C.Wardrobe.Clothes.keys():
                            
                            ## can delete second condition eventually
                            if hasattr(C.Wardrobe.Clothes[I.name], "tint"):
                                I.tint = copy.copy(C.Wardrobe.Clothes[I.name].tint)
                            else:
                                I.tint = {
                                    "active": None,
                                    "multiply": [1.0, 1.0, 1.0],
                                    "screen": [0.0, 0.0, 0.0]}
                            
                        C.Wardrobe.Clothes[I.name] = I.copy()

                        for O in C.Wardrobe.Outfits.values():
                            if I.string == O.Clothes[I.Clothing_type].string:
                                if not hair:
                                    if O.Clothes[I.Clothing_type].selected_state in O.Clothes[I.Clothing_type].available_states["standing"]:
                                        I.selected_state = O.Clothes[I.Clothing_type].selected_state
                                    else:
                                        I.selected_state = I.available_states["standing"][0]
                                    
                                ## can delete second condition eventually
                                if hasattr(O.Clothes[I.Clothing_type], "tint"):
                                    I.tint = copy.copy(O.Clothes[I.Clothing_type].tint)
                                else:
                                    I.tint = {
                                        "active": None,
                                        "multiply": [1.0, 1.0, 1.0],
                                        "screen": [0.0, 0.0, 0.0]}

                                O.Clothes[I.Clothing_type] = I.copy()

                        if C.Clothes[I.Clothing_type].name == I.name:
                            if not hair:
                                if C.Clothes[I.Clothing_type].selected_state in C.Clothes[I.Clothing_type].available_states["standing"]:
                                    I.selected_state = C.Clothes[I.Clothing_type].selected_state
                                else:
                                    I.selected_state = I.available_states["standing"][0]

                            ## can delete second condition eventually
                            if hasattr(C.Clothes[I.Clothing_type], "tint"):
                                I.tint = copy.copy(C.Clothes[I.Clothing_type].tint)
                            else:
                                I.tint = {
                                    "active": None,
                                    "multiply": [1.0, 1.0, 1.0],
                                    "screen": [0.0, 0.0, 0.0]}

                            C.Clothes[I.Clothing_type] = I.copy()

            if C in all_Companions:
                for I in eval(f"{C.tag}_shopping_list()"):
                    Item_string = I.Owner.tag + "_" + I.string

                    if I.name not in C.Wardrobe.Clothes.keys() and Item_string not in Player.inventory:
                        if (chapter > I.chapter) or (chapter == I.chapter and season >= I.season):
                            shop_inventory[I.shop_type][Item_string] = I.copy()

                        unrestricted_shop_inventory[I.shop_type][Item_string] = I.copy()

        return

    def register_Events():
        global EventScheduler

        Event_list = []
        Event_label_list = []

        for C in Cast:
            for E in eval(f"all_{C}_Events()"):
                Event_list.append(E)
                Event_label_list.append(E.label)

        for E in all_Events():
            Event_list.append(E)
            Event_label_list.append(E.label)

        
        # ADDED FOR MOD SUPPORT
        for M in mod_directories:
            # Events for existing characters
            mod_characters = get_mod_characters(M)

            mod_tags = []
            for name in mod_characters:
                mod_tags.append(eval(f"{name}.tag"))

            for C in mod_tags:
                function_name = f"all_{M}_{C}_Events"
                if function_name in globals() and callable(globals()[function_name]):
                    for E in eval(f"all_{M}_{C}_Events()"):
                        Event_list.append(E)
                        Event_label_list.append(E.label)

            # Events quests
            function_name = f"all_{M}_Events"
            if function_name in globals() and callable(globals()[function_name]):
                    for E in eval(f"all_{M}_Events()"):
                        Event_list.append(E)
                        Event_label_list.append(E.label)


        for E in Event_list:
            EventScheduler.add(E)

        temp = list(EventScheduler.Events.keys())

        for E in temp:
            if E in EventScheduler.Events.keys() and E not in Event_label_list:
                del EventScheduler.Events[E]

        return

    def register_Quests():
        global QuestPool
        
        Quests = []

        for C in Cast:
            for Q in eval(f"all_{C}_Quests()"):
                Quests.append(Q)

        for Q in all_Quests():
            Quests.append(Q)

        # ADDED FOR MOD SUPPORT
        for M in mod_directories:
            # Quests for existing characters
            mod_characters = get_mod_characters(M)

            mod_tags = []
            for name in mod_characters:
                mod_tags.append(eval(f"{name}.tag"))

            for C in mod_tags:
                function_name = f"all_{M}_{C}_Quests"
                if function_name in globals() and callable(globals()[function_name]):
                    for Q in eval(f"all_{M}_{C}_Quests()"):
                        Quests.append(Q)

            # General quests
            function_name = f"all_{M}_Quests"
            if function_name in globals() and callable(globals()[function_name]):
                    for Q in eval(f"all_{M}_Quests()"):
                        Quests.append(Q)
            

        Quest_strings = list(QuestPool.Quests.keys())

        for Q_string in Quest_strings:
            absent = True

            for Q in Quests:
                if Q_string == Q.string:
                    absent = False

                    break

            if absent:
                del QuestPool.Quests[Q_string]

        for Q in Quests:
            QuestPool.add(Q)

        return