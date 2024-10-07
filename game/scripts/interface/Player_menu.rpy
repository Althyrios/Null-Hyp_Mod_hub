init -4:

    default quick_location_1 = False
    default quick_location_2 = False
    default quick_location_3 = False
    
    default current_Player_menu_page = "database"

    default current_database_page = 0
    default current_database_filter = "info"
    default current_database_section = "personal"
    default current_database_Entry = None

    default current_mutant_ability = None

    default current_inventory_page = 0
    default current_inventory_filter = "gift"
    default current_inventory_list = []
    default current_inventory_Item = None

    default current_journal_filter = None
    default current_journal_chapter = None
    default current_journal_Quest = None
    default show_completed_Quests = False

    define location_groups = {
        "Institute": {
            "Basement": [
                "bg_danger",
                "bg_lockers"],
            "First Floor": [
                "bg_campus",
                "bg_classroom",
                "bg_entrance",
                "bg_pool",
                "bg_study"],
            "Second Floor": [
                "bg_door",
                "bg_girls_hallway",
                "bg_hallway",
                "bg_Jean",
                "bg_Kurt",
                "bg_Laura",
                "bg_Player",
                "bg_Rogue",
                "bg_Charles"],
            "Attic": [
                "bg_Ororo"]},

        "Mall": {
            "First Floor": [
                "bg_mall",
                "bg_movies"]},

        # "Town": {
        #     "Main Street": [
        #         "bg_town"]}
        }

    default current_group = "Institute"
    default current_subgroup = "Second Floor"
    
    default unlocked_locations = {
        "bg_Player": "renpy.call('travel', 'bg_Player')"}
        
    default available_locations = {}

    default marked_locations = {
        "bg_campus": [],
        "bg_classroom": [],
        "bg_danger": [],
        "bg_entrance": [],
        "bg_girls_hallway": [],
        "bg_hallway": [],
        "bg_Jean": [],
        "bg_Kurt": [],
        "bg_Laura": [],
        "bg_mall": [],
        "bg_movies": [],
        "bg_Player": [],
        "bg_pool": [],
        "bg_Rogue": [],
        "bg_lockers": [],
        "bg_study": [],
        "bg_Charles": [],
        "bg_Ororo": []}

    default current_relationships_Entry = None


# # ADDED FOR MOD SUPPORT
# init -1:
#     default companions_map_paths = get_companions_map_images()

init -1 python:

    import math

    def return_last_name(Character):
        return Character.full_name.split(" ")[-1]

    # # ADDED FOR MOD SUPPORT 
    # def get_companions_map_images():

    #     map_images = {}

    #     for companion in all_Companions:
    #         if companion not in mods_Companions:
    #             map_images[companion] = [f"images/interface/Player_menu/{companion}.webp",f"images/interface/Player_menu/{companion}_idle.webp"]
    #         else:
    #             for M in get_mod_directories():
    #                 if companion in get_mod_characters(M):
    #                     map_images[companion] = [f"mods/{M}/images/interface/Player_menu/{companion}.webp",f"images/interface/Player_menu/{companion}_idle.webp"]
        
    #     return map_images


style Player_menu is default

screen Player_menu():
    layer "interface"

    modal True

    style_prefix "Player_menu"

    on "show" action [
        Hide("say"),
        Hide("phone_screen"),
        SetVariable("current_inventory_filter", "gift"),
        SetVariable("current_journal_Quest", None),
        SetVariable("choice_disabled", True),
        Function(EventScheduler.update_conditions)]
    on "hide" action [
        SetVariable("giving_gift", False),
        SetVariable("current_inventory_Item", None),
        SetVariable("choice_disabled", False)]

    timer 0.5 repeat True action ToggleVariable("blinking")

    if not black_screen and not renpy.get_screen("say"):
        add "images/interface/main_menu/blank_background.webp" zoom interface_adjustment

        add At("images/interface/preferences/spin.webp", spinning_element) anchor (0.5, 0.5) pos (0.502, 0.502) zoom interface_adjustment

        add "images/interface/Player_menu/top.webp" zoom interface_adjustment

        for page in ["database", "skills", "inventory", "journal", "map", "relationships"]:
            button:
                idle_background At(f"images/interface/Player_menu/{page}_idle.webp", interface)
                hover_background At(f"images/interface/Player_menu/{page}.webp", interface)
                selected_idle_background At(f"images/interface/Player_menu/{page}.webp", interface)
                selected_hover_background At(f"images/interface/Player_menu/{page}.webp", interface)

                selected current_Player_menu_page == page

                action SetVariable("current_Player_menu_page", page)

                focus_mask True

        imagebutton:
            idle At("images/interface/Player_menu/preferences_idle.webp", interface)
            hover At("images/interface/Player_menu/preferences.webp", interface)

            action ShowMenu("preferences")

        imagebutton:
            idle At("images/interface/Player_menu/exit_idle.webp", interface)
            hover At("images/interface/Player_menu/exit.webp", interface)

            if not sandbox:
                action [
                    Hide("Player_menu"),
                    Return()]
            else:
                action [
                    Hide("Player_menu"),
                    Call("move_location", Player.location)]

        text "DATABASE" anchor (0.5, 0.5) pos (0.111, 0.115):
            size 28

        text "SKILLS" anchor (0.5, 0.5) pos (0.221, 0.115):
            size 28

        text "INVENTORY" anchor (0.5, 0.5) pos (0.331, 0.115):
            size 28

        text "JOURNAL" anchor (0.5, 0.5) pos (0.441, 0.115):
            size 28

        text "MAP" anchor (0.5, 0.5) pos (0.551, 0.115):
            size 28

        text "RELATIONSHIPS" anchor (0.5, 0.5) pos (0.662, 0.115):
            size 28

        text "OPTIONS" anchor (0.5, 0.5) pos (0.772, 0.115):
            size 28

        text "EXIT" anchor (0.5, 0.5) pos (0.882, 0.115):
            size 28

        if current_Player_menu_page == "database":
            use database_screen
        elif current_Player_menu_page == "skills":
            use skills_screen
        elif current_Player_menu_page == "inventory":
            use inventory_screen
        elif current_Player_menu_page == "journal":
            use journal_screen
        elif current_Player_menu_page == "map":
            use map_screen
        elif current_Player_menu_page == "relationships":
            use relationships_screen

    if black_screen or renpy.get_screen("say"):
        button xysize (1.0, 1.0):
            background None

            hover_sound None
            activate_sound None
            
            if not renpy.get_screen("choice"):
                action Return()
            else:
                action NullAction()

    use quick_menu

    if tooltips_enabled or journal_hints:
        use tooltips

screen database_screen():
    style_prefix "Player_menu"

    $ database_Entries = unlocked_database_Entries[:]

    $ database_Characters = unlocked_Characters[:]
    $ database_Characters.sort(key = return_last_name)
    $ database_Characters.insert(0, Player)

    for C in database_Characters:
        $ database_Entries.append(C)

    add "images/interface/Player_menu/database_background.webp" zoom interface_adjustment

    for filter in ["enemy", "info", "ally"]:
        imagebutton:
            idle At(f"images/interface/Player_menu/database_filter_{filter}_idle.webp", interface)
            hover At(f"images/interface/Player_menu/database_filter_{filter}.webp", interface)
            selected_idle At(f"images/interface/Player_menu/database_filter_{filter}_selected.webp", interface)
            selected_hover At(f"images/interface/Player_menu/database_filter_{filter}_selected.webp", interface)

            selected current_database_filter == filter

            if current_database_filter == filter:
                action SetVariable("current_database_filter", None)
            else:
                action [
                    SetVariable("current_database_filter", None),
                    SetVariable("current_database_page", 0),
                    SetVariable("current_database_filter", filter)]

    text "ENEMY" anchor (0.5, 0.5) pos (0.099, 0.244):
        size 35

        color "#000000"

    text "INFO" anchor (0.5, 0.5) pos (0.19, 0.244):
        size 35

        color "#000000"

    text "ALLY" anchor (0.5, 0.5) pos (0.283, 0.244):
        size 35

        color "#000000"

    text "CEREBRO DATABASE" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.065, 0.3365):
        size 35

    viewport id "database_viewport" anchor (0.5, 0.0) pos (0.18, 0.405) xysize (int(911*game_resolution), int(1114*game_resolution)):
        draggable True
        mousewheel True

        vbox:
            for D in database_Entries:
                if hasattr(D, "database_type") and D.database_type and D.database_type and (not current_database_filter or D.database_type == current_database_filter):
                    button xysize (int(911*game_resolution), int(191*game_resolution)):
                        idle_background At(f"images/interface/Player_menu/database_{D.database_type}_idle.webp", interface)
                        hover_background At(f"images/interface/Player_menu/database_{D.database_type}.webp", interface)
                        selected_idle_background At(f"images/interface/Player_menu/database_{D.database_type}.webp", interface)
                        
                        selected current_database_Entry == D

                        if D in all_Characters or D == Player:
                            text D.call_sign anchor (0.0, 0.5) pos (0.1, 0.5):
                                font "agency_fb.ttf"

                                size 36

                                color "#000000"
                        else:
                            text D.title anchor (0.0, 0.5) pos (0.1, 0.5):
                                font "agency_fb.ttf"

                                size 36

                                color "#000000"

                        action [
                            SetVariable("current_database_page", 0),
                            SetVariable("current_database_Entry", D)]

    vbar value YScrollValue("database_viewport") anchor (0.5, 0.0) pos (0.315, 0.405) xysize (int(40*game_resolution), int(1114*game_resolution)):
        base_bar At("images/interface/Player_menu/database_scrollbar.webp", interface)

        thumb At("images/interface/Player_menu/database_scrollbar_thumb.webp", interface)
        thumb_offset int(276*game_resolution/2/10)

        unscrollable "hide"

    if current_database_Entry:
        add "images/interface/Player_menu/database_profile.webp" zoom interface_adjustment

        if current_database_section in ["personal", "mutiefan"]:
            add "images/interface/Player_menu/database_profile_box.webp" zoom interface_adjustment
        
        if current_database_Entry in all_Characters or current_database_Entry == Player:
            $ Entry_name = current_database_Entry.call_sign
        else:
            $ Entry_name = current_database_Entry.title

        if blinking:
            text Entry_name.upper() + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.364, 0.247):
                size 35
        else:
            text Entry_name.upper() + "_" anchor (0.0, 0.5) pos (0.364, 0.247):
                size 35

        if current_database_Entry in all_Characters or current_database_Entry == Player:
            add "images/interface/Player_menu/database_buttons.webp" zoom interface_adjustment

            for section in ["personal", "combat", "mutiefan"]:
                imagebutton:
                    idle At(f"images/interface/Player_menu/database_{section}_idle.webp", interface)
                    hover At(f"images/interface/Player_menu/database_{section}.webp", interface)
                    selected_idle At(f"images/interface/Player_menu/database_{section}.webp", interface)

                    selected current_database_section == section

                    if current_database_section == section:
                        action NullAction()
                    else:
                        action [
                            SetVariable("current_database_section", None),
                            SetVariable("current_database_page", 0),
                            SetVariable("current_database_section", section)]

            text "PERSONAL" anchor (0.5, 0.5) pos (0.693, 0.247):
                size 35

            text "COMBAT" anchor (0.5, 0.5) pos (0.79, 0.247):
                size 35

            $ database_length = 0

            if current_database_section == "personal":
                if "stats" in current_database_Entry.database.keys():
                    $ database_length += 1

                if "description" in current_database_Entry.database.keys():
                    $ database_length += math.ceil(len(current_database_Entry.database["description"][0])/500)
                    
                if "study_materials" in current_database_Entry.database.keys():
                    $ database_length += 1

            if current_database_section == "mutiefan":
                if "wiki" in current_database_Entry.database.keys():
                    $ database_length += 1
        else:
            $ database_length = math.ceil(len(current_database_Entry.body)/700)

        if database_length > 1:
            imagebutton:
                idle At("images/interface/Player_menu/database_left_idle.webp", interface)
                hover At("images/interface/Player_menu/database_left.webp", interface)

                action SetVariable("current_database_page", (current_database_page - 1) % database_length)

            text f"{current_database_page + 1} / {database_length}" anchor (0.5, 0.5) pos (0.777, 0.875):
                size 36

            imagebutton:
                idle At("images/interface/Player_menu/database_right_idle.webp", interface)
                hover At("images/interface/Player_menu/database_right.webp", interface)

                action SetVariable("current_database_page", (current_database_page + 1) % database_length)
        
        if current_database_Entry in all_Characters or current_database_Entry == Player:
            if current_database_section == "personal":
                frame anchor (0.0, 0.0) pos (0.375, 0.345) xysize (0.543, 0.55):
                    if database_length >= 1:
                        if "stats" in current_database_Entry.database.keys() and current_database_page == 0:
                            frame anchor (0.0, 0.0) pos (0.5, 0.01) xsize 0.5:
                                text current_database_Entry.database["stats"] xalign 0.0:
                                    font "agency_fb.ttf"
                                            
                                    size 30

                                    text_align 0.0
                        elif "study_materials" in current_database_Entry.database.keys() and current_database_page == database_length - 1:
                            frame anchor (0.0, 0.0) pos (0.5, 0.01) xsize 0.5:
                                text current_database_Entry.database["study_materials"] xalign 0.0:
                                    font "agency_fb.ttf"

                                    size 30

                                    text_align 0.0
                        elif "description" in current_database_Entry.database.keys():
                            $ start = 500*(current_database_page - 1)
                            $ finish = 500*current_database_page

                            for i in range(20):
                                if start <= 1:
                                    $ start = -1
                                elif current_database_Entry.database["description"][0][start] != " " and current_database_Entry.database["description"][0][start:start + 2] != "\n":
                                    $ start += 1
                                elif current_database_Entry.database["description"][0][start + 1] == " " or current_database_Entry.database["description"][0][start:start + 2] == "\n" or current_database_Entry.database["description"][0][start - 1:start + 1] == "\n":
                                    $ start += 1

                                if finish >= len(current_database_Entry.database["description"][0]) - 1:
                                    $ finish = len(current_database_Entry.database["description"][0])
                                elif current_database_Entry.database["description"][0][finish] != " " and current_database_Entry.database["description"][0][finish - 1:finish + 1] != "\n":
                                    $ finish += 1

                            frame anchor (0.0, 0.0) pos (0.5, 0.01) xsize 0.5:
                                text current_database_Entry.database["description"][0][start + 1:finish] xalign 0.0:
                                    font "agency_fb.ttf"

                                    size 30

                                    text_align 0.0

                    if current_database_Entry == Player:
                        add f"images/interface/comics/Null.webp" anchor (0.0, 0.0) pos (0.04, 0.06) zoom 0.5
                    elif current_database_Entry in [Rogue, Laura, Jean, Ororo, Charles, Kurt, Cain]:
                        add f"images/interface/comics/{current_database_Entry.tag}.webp" anchor (0.0, 0.0) pos (0.04, 0.06) zoom 0.5
            elif current_database_section == "mutiefan":
                if "wiki" in current_database_Entry.database.keys():
                    frame anchor (0.0, 0.0) pos (0.375, 0.345) xysize (0.543, 0.57):
                        text current_database_Entry.database["wiki"] align (0.0, 0.0):
                            font "agency_fb.ttf"

                            size 36

                            text_align 0.0

                        if "comments" in current_database_Entry.database.keys():
                            frame align (0.0, 1.0) xsize 0.45:
                                vbox xsize 1.0:
                                    for comment in current_database_Entry.database["comments"]:
                                        $ comment_color = "#ffffff"
                                        
                                        $ commenter = comment.split(':')[0]

                                        for C in all_Characters:
                                            if C.call_sign == commenter:
                                                $ comment_color = eval(f"{C.tag}_color")

                                        frame xalign 0.0:
                                            background Frame("images/interface/phone/text_frame.webp", 10, 10)

                                            text comment xalign 0.0:
                                                font "agency_fb.ttf"

                                                size 26

                                                color comment_color

                                                text_align 0.0
        else:
            frame anchor (0.0, 0.0) pos (0.375, 0.345) xysize (0.543, 0.55):
                if database_length >= 1:
                    $ start = 700*current_database_page
                    $ finish = 700*(current_database_page + 1)

                    for i in range(20):
                        if start <= 1:
                            $ start = -1
                        elif current_database_Entry.body[start] != " " and current_database_Entry.body[start:start + 2] != "\n":
                            $ start += 1
                        elif current_database_Entry.body[start + 1] == " " or current_database_Entry.body[start:start + 2] == "\n" or current_database_Entry.body[start - 1:start + 1] == "\n":
                            $ start += 1

                        if finish >= len(current_database_Entry.body) - 1:
                            $ finish = len(current_database_Entry.body)
                        elif current_database_Entry.body[finish] != " " and current_database_Entry.body[finish - 1:finish + 1] != "\n":
                            $ finish += 1

                    frame anchor (0.0, 0.0) pos (0.0, 0.01) xsize 1.0:
                        text current_database_Entry.body[start + 1:finish] xalign 0.0:
                            font "agency_fb.ttf"

                            size 30

                            text_align 0.0

screen skills_screen():
    style_prefix "Player_menu"

    add "images/interface/Player_menu/skills_background.webp" zoom interface_adjustment

    if blinking:
        text "X-EVOLUTION" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.066, 0.238):
            size 35
    else:
        text "X-EVOLUTION" + "_" anchor (0.0, 0.5) pos (0.066, 0.238):
            size 35

    add "Player_portrait" anchor (0.5, 0.5) pos (0.738, 0.459) zoom 0.5

    add f"images/interface/Player_menu/skills_{Player.scholarship}.webp" zoom interface_adjustment

    if Player.scholarship == "athletic":
        text "ATHLETICS" anchor (0.5, 0.5) pos (0.89, 0.352):
            font "agency_fb.ttf"

            size 30
    elif Player.scholarship == "academic":
        text "ACADEMICS" anchor (0.5, 0.5) pos (0.89, 0.352):
            font "agency_fb.ttf"

            size 30
    elif Player.scholarship == "artistic":
        text "ARTS" anchor (0.5, 0.5) pos (0.89, 0.352):
            font "agency_fb.ttf"

            size 30

    text "LVL" anchor (0.0, 0.5) pos (0.818, 0.421):
        font "agency_fb.ttf"

        size 30

    text f"{Player.level}" anchor (1.0, 0.5) pos (0.87, 0.421):
        font "agency_fb.ttf"
        
        size 30

    text f"{Player.ability_points}" anchor (0.5, 0.5) pos (0.898, 0.421):
        font "agency_fb.ttf"
        
        size 30

    text "XP" anchor (0.0, 0.5) pos (0.818, 0.465):
        font "agency_fb.ttf"
        
        size 30

    bar value Player.XP range Player.XP_goal anchor (0.5, 0.5) pos (0.878, 0.465) xysize (int(277*game_resolution), int(24*game_resolution)):
        left_bar At("images/interface/Player_menu/skills_xp.webp", interface)
        right_bar At("images/interface/Player_menu/skills_xp_empty.webp", interface)

        thumb None
        thumb_offset 0

    text "MUTANT RANK" anchor (0.0, 0.5) pos (0.818, 0.5125):
        font "agency_fb.ttf"
        
        size 25

    text Player.mutant_rank.upper() anchor (1.0, 0.5) pos (0.921, 0.5125):
        font "agency_fb.ttf"
        
        size 25

    $ mutant_abilities = ability_names.keys()
    $ unlocked_abilities = ["nullify"]

    if "regen" in Player.mutant_abilities:
        $ unlocked_abilities.append("regen")
        $ unlocked_abilities.append("stamina_boost1")

    if "absorption" in Player.mutant_abilities:
        $ unlocked_abilities.append("absorption")

    if "stamina_boost1" in Player.mutant_abilities:
        $ unlocked_abilities.append("stamina_boost2")
        $ unlocked_abilities.append("orgasm_control")

    if "stamina_boost2" in Player.mutant_abilities:
        $ unlocked_abilities.append("stamina_boost3")

    if "orgasm_control" in Player.mutant_abilities:
        $ unlocked_abilities.append("large_loads")

    for ability in mutant_abilities:
        if ability == "nullify":
            $ x = 0.11
            $ y = 0.4
        elif ability == "regen":
            $ x = 0.149
            $ y = 0.44
        elif ability == "absorption":
            $ x = 0.188
            $ y = 0.48
        elif ability == "stamina_boost1":
            $ x = 0.11
            $ y = 0.48
        elif ability == "stamina_boost2":
            $ x = 0.11
            $ y = 0.56
        elif ability == "stamina_boost3":
            $ x = 0.11
            $ y = 0.64
        elif ability == "orgasm_control":
            $ x = 0.149
            $ y = 0.36
        elif ability == "large_loads":
            $ x = 0.188
            $ y = 0.4

        button anchor (0.5, 0.5) pos (x, y) xysize (int(209*game_resolution), int(193*game_resolution)):
            if ability in Player.mutant_abilities:
                idle_background At("images/interface/Player_menu/skills_node_purchased.webp", interface)
                hover_background At("images/interface/Player_menu/skills_node_selected.webp", interface)
                selected_idle_background At("images/interface/Player_menu/skills_node_selected.webp", interface)
            else:
                idle_background At("images/interface/Player_menu/skills_node_idle.webp", interface)
                hover_background At("images/interface/Player_menu/skills_node.webp", interface)
                selected_idle_background At("images/interface/Player_menu/skills_node.webp", interface)

            selected current_mutant_ability == ability

            if ability not in unlocked_abilities:
                add "images/interface/Player_menu/skills_locked.webp" anchor (0.5, 0.5) pos (0.48, 0.47) zoom interface_adjustment

                action NullAction()
            elif "stamina" in ability:
                add "images/interface/Player_menu/skills_stamina.webp" anchor (0.5, 0.5) pos (0.48, 0.47) zoom interface_adjustment

                action SetVariable("current_mutant_ability", ability)
            else:
                add f"images/interface/Player_menu/skills_{ability}.webp" anchor (0.5, 0.5) pos (0.48, 0.47) zoom interface_adjustment

                action SetVariable("current_mutant_ability", ability)

    if current_mutant_ability:
        add "images/interface/Player_menu/skills_box.webp" zoom interface_adjustment

        text ability_names[current_mutant_ability].upper() anchor (0.0, 0.5) pos (0.679, 0.68):
            if len(ability_names[current_mutant_ability]) > 12:
                size 24
            elif len(ability_names[current_mutant_ability]) > 8:
                size 26
            else:
                size 30

        frame anchor (0.5, 0.5) pos (0.801, 0.805) xysize (0.245, 0.202):
            text ability_descriptions[current_mutant_ability] xalign 0.5:
                font "agency_fb.ttf"
                
                size 30

                text_align 0.5

        if chapter > 1 or season > 1:
            if current_mutant_ability not in Player.mutant_abilities and current_mutant_ability in ability_costs.keys() and Player.ability_points >= ability_costs[current_mutant_ability]:
                imagebutton:
                    idle At("images/interface/Player_menu/skills_purchase.webp", interface)
                    hover At("images/interface/Player_menu/skills_purchased.webp", interface)

                    if "stamina" in current_mutant_ability:
                        action [
                            SetVariable("Player.ability_points", Player.ability_points - ability_costs[current_mutant_ability]),
                            AddToSet(Player.mutant_abilities, current_mutant_ability),
                            SetVariable("Player.max_stamina", Player.max_stamina + 1),
                            Function(Player.History.update, "bought_skill")]
                    else:
                        action [
                            SetVariable("Player.ability_points", Player.ability_points - ability_costs[current_mutant_ability]),
                            AddToSet(Player.mutant_abilities, current_mutant_ability),
                            Function(Player.History.update, "bought_skill")]

                text "AWAKEN" anchor (0.5, 0.5) pos (0.825, 0.68):
                    font "agency_fb.ttf"
                    
                    size 25
            elif current_mutant_ability not in Player.mutant_abilities:
                add "images/interface/Player_menu/skills_purchase.webp" zoom interface_adjustment

                text "AWAKEN" anchor (0.5, 0.5) pos (0.825, 0.68):
                    font "agency_fb.ttf"
                    
                    size 25
            else:
                add "images/interface/Player_menu/skills_purchased.webp" zoom interface_adjustment

                text "ACTIVE" anchor (0.5, 0.5) pos (0.825, 0.68):
                    font "agency_fb.ttf"
                    
                    size 25

        text "COST" anchor (0.0, 0.5) pos (0.8725, 0.68):
            font "agency_fb.ttf"
            
            size 24

        if current_mutant_ability not in Player.mutant_abilities and current_mutant_ability in ability_costs.keys():
            text f"{ability_costs[current_mutant_ability]}" anchor (1.0, 0.5) pos (0.902, 0.68):
                font "agency_fb.ttf"
                
                size 24
        else:
            text "0" anchor (1.0, 0.5) pos (0.902, 0.68):
                font "agency_fb.ttf"
                
                size 24

screen inventory_screen():
    style_prefix "Player_menu"

    $ current_inventory_list = []
    
    for Item_string in Player.inventory.keys():
        if current_inventory_filter == "gift" and not isinstance(Player.inventory[Item_string], list):
            $ current_inventory_list.append(Item_string)
        elif isinstance(Player.inventory[Item_string], list):
            for I in Player.inventory[Item_string]:
                if current_inventory_filter in I.filter_type:
                    if Item_string not in current_inventory_list:
                        if I.Owner == Player and current_inventory_filter == "key":
                            $ current_inventory_list.append(Item_string)
                        elif I.Owner != Player and current_inventory_filter == "gift":
                            $ current_inventory_list.append(Item_string)

    add "images/interface/Player_menu/inventory_background.webp" zoom interface_adjustment

    if math.floor(len(current_inventory_list)/15) > 0:
        imagebutton:
            idle At("images/interface/Player_menu/inventory_left_idle.webp", interface)
            hover At("images/interface/Player_menu/inventory_left.webp", interface)

            action SetVariable("current_inventory_page", (current_inventory_page - 1) % math.ceil(len(current_inventory_list)/15))

    if math.floor(len(current_inventory_list)/15) > 0:
        imagebutton:
            idle At("images/interface/Player_menu/inventory_right_idle.webp", interface)
            hover At("images/interface/Player_menu/inventory_right.webp", interface)

            action SetVariable("current_inventory_page", (current_inventory_page + 1) % math.ceil(len(current_inventory_list)/15))

    if current_inventory_page < 9:
        if blinking:
            text "TAB{alpha=0.0}_{/alpha}" + f"0{current_inventory_page + 1}" anchor (0.5, 0.5) pos (0.086, 0.808):
                size 35
        else:
            text f"TAB_0{current_inventory_page + 1}" anchor (0.5, 0.5) pos (0.086, 0.808):
                size 35
    else:
        if blinking:
            text "TAB{alpha=0.0}_{/alpha}" + f"{current_inventory_page + 1}" anchor (0.5, 0.5) pos (0.086, 0.808):
                size 35
        else:
            text f"TAB_{current_inventory_page + 1}" anchor (0.5, 0.5) pos (0.086, 0.808):
                size 35

    grid 5 3 anchor (0.0, 0.0) pos (0.147, 0.4) xysize (0.495, 0.524):
        xspacing 13
        yspacing 16

        for i in range(15*current_inventory_page, min(15*(current_inventory_page + 1), len(current_inventory_list))):
            $ Item_string = current_inventory_list[i]
            
            if isinstance(Player.inventory[Item_string], list):
                $ Item = None

                for I in Player.inventory[Item_string]:
                    if current_inventory_filter == "key":
                        if I.Owner == Player:
                            $ Item = I
                    elif current_inventory_filter == "gift":
                        if giving_gift and I.Owner == focused_Character:
                            $ Item = I

                            break
                        else:
                            $ Item = I

                if giving_gift and Item.Owner == Player:
                    continue

                $ I_string = Item_string

                if "Player_" in I_string:
                    $ I_string = I_string.replace("Player_", "")

                for C in all_Characters:
                    if C.tag + "_" in I_string:
                        $ I_string = I_string.replace(C.tag + "_", "")
                    
                button xysize (int(355*game_resolution), int(355*game_resolution)):
                    if current_inventory_Item == Item_string:
                        background At("images/interface/Player_menu/inventory_selector.webp", interface)
                    else:
                        background None

                    hover_sound None

                    if "piercing" in Item_string:
                        add "images/interface/items/piercings.webp" anchor (0.5, 0.5) pos (0.5, 0.4) zoom 0.2
                    else:
                        # add f"images/interface/items/{I_string}.webp" anchor (0.5, 0.5) pos (0.5, 0.4) zoom 0.2
                        # ADDED FOR MOD SUPPORT
                        add item_paths[I_string] anchor (0.5, 0.5) pos (0.5, 0.4) zoom 0.2

                    text f"x{len(Player.inventory[Item_string])}" anchor (0.5, 1.0) pos (0.5, 1.0):
                        size 32

                    if giving_gift:
                        if Item.filter_type != "key_gifts" or Item.Owner == focused_Character:
                            action [
                                SetVariable("current_inventory_Item", Item_string),
                                Show("confirm_gift_screen", Character = focused_Character, Item = Item)]
                        else:
                            action SetVariable("current_inventory_Item", Item_string)
                    else:
                        action SetVariable("current_inventory_Item", Item_string)
            else:
                $ Clothing = Player.inventory[Item_string]
                
                button xysize (int(355*game_resolution), int(355*game_resolution)):
                    if current_inventory_Item == Clothing:
                        background At("images/interface/Player_menu/inventory_selector.webp", interface)
                    else:
                        background None

                    hover_sound None

                    if Clothing.shop_type == "clothing":
                        add "images/interface/items/mutant_couture.webp" anchor (0.5, 0.5) pos (0.5, 0.4) zoom 0.2
                    elif Clothing.shop_type == "lingerie":
                        add "images/interface/items/xtreme_intimates.webp" anchor (0.5, 0.5) pos (0.5, 0.4) zoom 0.2

                    add At(f"images/interface/icons/{Clothing.Owner.tag}.webp", humhum_icon) anchor (0.5, 0.5) pos (0.93, 0.89)

                    if giving_gift and focused_Character == Clothing.Owner:
                        action [
                            SetVariable("current_inventory_Item", Clothing),
                            Show("confirm_gift_screen", Character = focused_Character, Item = Clothing)]
                    else:
                        action SetVariable("current_inventory_Item", Clothing)

    for filter in ["gift", "key"]:
        imagebutton:
            idle At(f"images/interface/Player_menu/inventory_{filter}_idle.webp", interface)
            hover At(f"images/interface/Player_menu/inventory_{filter}.webp", interface) 
            selected_idle At(f"images/interface/Player_menu/inventory_{filter}.webp", interface)

            selected current_inventory_filter == filter

            action [
                SetVariable("current_inventory_Item", None),
                SetVariable("current_inventory_filter", filter)]

    text "GIFT" anchor (0.5, 0.5) pos (0.51, 0.335):
        size 35

    text "KEY" anchor (0.5, 0.5) pos (0.602, 0.335):
        size 35

    text "ITEM NAME" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.674, 0.3365):
        size 35

    if isinstance(current_inventory_Item, str):
        text f"{Player.inventory[current_inventory_Item][0].name.upper()}" anchor (1.0, 0.5) pos (0.93, 0.3365):
            if len(Player.inventory[current_inventory_Item][0].name) > 20:
                size 25
            elif len(Player.inventory[current_inventory_Item][0].name) > 15:
                size 30
            else:
                size 35

        text f"{Player.inventory[current_inventory_Item][0].description}" anchor (0.5, 0.5) pos (0.8, 0.608) xysize (0.25, 0.44):
            size 40

        if Item.filter_type == "key_gifts" and Item.Owner == Player:
            vbox anchor (0.5, 0.5) pos (0.8, 0.78):
                text "ACTIVE?" anchor (0.5, 0.5) pos (0.47, 0.5):
                    size 40

                button xysize (int(321*game_resolution), int(190*game_resolution)):
                    idle_background At("images/interface/preferences/off.webp", interface) 
                    hover_background At("images/interface/preferences/off.webp", interface) 
                    selected_idle_background At("images/interface/preferences/on.webp", interface) 
                    selected_hover_background At("images/interface/preferences/on.webp", interface)

                    hover_sound None
                    
                    selected Player.inventory[current_inventory_Item][0].active

                    text "OFF" anchor (0.5, 0.5) pos (0.22, 0.461):
                        size 35

                    text "ON" anchor (0.5, 0.5) pos (0.7, 0.461):
                        size 35

                    action ToggleField(Player.inventory[current_inventory_Item][0], "active")
    elif current_inventory_Item:
        text f"{current_inventory_Item.name.upper()}" anchor (1.0, 0.5) pos (0.93, 0.3365):
            if len(current_inventory_Item.name) > 20:
                size 25
            elif len(current_inventory_Item.name) > 15:
                size 30
            else:
                size 35

    text "CASH" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.674, 0.907):
        size 45

    text f"$ {Player.cash}" anchor (1.0, 0.5) pos (0.93, 0.907):
        size 45

screen confirm_gift_screen(Character, Item):
    modal True

    style_prefix "confirm"

    frame anchor (0.5, 0.5) pos (0.5, 0.5):
        vbox:
            spacing 25

            text f"Give {Character.name} the {Item.name}?":
                size 40
                
            hbox:
                spacing 100

                textbutton _("Yes"): 
                    text_size 36

                    if "piercing" in Item.string:
                        action [
                            Hide("confirm_gift_screen"),
                            Call("give_Character_piercing", Character, Item, from_current = True)]
                    elif hasattr(Item, "available_states"):
                        action [
                            Hide("confirm_gift_screen"),
                            Call("give_Character_Clothing", Character, Item, from_current = True)]
                    else:
                        action [
                            Hide("confirm_gift_screen"),
                            Call("give_Character_gift", Character, Item, from_current = True)]

                textbutton _("No"): 
                    text_size 36

                    action Hide("confirm_gift_screen")

screen journal_screen():
    style_prefix "Player_menu"

    add "images/interface/Player_menu/journal_background.webp" zoom interface_adjustment

    for filter in ["main", "side", "addon"]:
        imagebutton:
            idle At(f"images/interface/Player_menu/journal_{filter}_idle.webp", interface)
            hover At(f"images/interface/Player_menu/journal_{filter}.webp", interface)
            selected_idle At(f"images/interface/Player_menu/journal_{filter}_selected.webp", interface)
            selected_hover At(f"images/interface/Player_menu/journal_{filter}_selected.webp", interface)

            selected current_journal_filter == filter

            if current_journal_filter == filter:
                action SetVariable("current_journal_filter", None)
            else:
                action [
                    SetVariable("current_journal_Quest", None),
                    SetVariable("current_journal_filter", filter)]

    text "MAIN" anchor (0.5, 0.5) pos (0.096, 0.244):
        size 35

        color "#000000"

    text "SIDE" anchor (0.5, 0.5) pos (0.19, 0.244):
        size 35

        color "#000000"

    text "ADD-ON" anchor (0.5, 0.5) pos (0.283, 0.244):
        size 35

        color "#000000"

    for c in range(1, chapter + 1):
        imagebutton:
            idle At(f"images/interface/Player_menu/journal_chapter{c}_idle.webp", interface)
            hover At(f"images/interface/Player_menu/journal_chapter{c}.webp", interface)
            selected_idle At(f"images/interface/Player_menu/journal_chapter{c}.webp", interface)

            selected current_journal_chapter == c

            if current_journal_chapter == c:
                action SetVariable("current_journal_chapter", None)
            else:
                action [
                    SetVariable("current_journal_Quest", None),
                    SetVariable("current_journal_chapter", c)]

    text "CHAPTER I" anchor (0.5, 0.5) pos (0.395, 0.242):
        size 35

    text "QUEST LIST" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.065, 0.3365):
        size 35

    imagebutton:
        idle At("images/interface/Player_menu/journal_checkbox_off.webp", interface)
        hover At("images/interface/Player_menu/journal_checkbox_on.webp", interface)
        selected_idle At("images/interface/Player_menu/journal_checkbox_on.webp", interface)

        selected not show_completed_Quests

        action ToggleVariable("show_completed_Quests")

    text "Hide Completed" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.25, 0.3365):
        font "agency_fb.ttf"

        size 25

    viewport id "journal_viewport" anchor (0.5, 0.0) pos (0.18, 0.405) xysize (int(911*game_resolution), int(1114*game_resolution)):
        draggable True
        mousewheel True

        $ list_of_Quests = []

        for Q in reversed(QuestPool.Quests.values()):
            if not Q.fully_completed:
                $ list_of_Quests.append(Q)

        for Q in reversed(QuestPool.Quests.values()):
            if Q.fully_completed:
                $ list_of_Quests.append(Q)

        vbox:
            for Q in list_of_Quests:
                if Q.unlocked and (not current_journal_filter or Q.Quest_type == current_journal_filter) and (not current_journal_chapter or Q.chapter == current_journal_chapter):
                    if show_completed_Quests or not Q.fully_completed:
                        button xysize (int(911*game_resolution), int(191*game_resolution)):
                            idle_background At(f"images/interface/Player_menu/journal_button_{Q.Quest_type}_idle.webp", interface)
                            hover_background At(f"images/interface/Player_menu/journal_button_{Q.Quest_type}.webp", interface)
                            selected_idle_background At(f"images/interface/Player_menu/journal_button_{Q.Quest_type}.webp", interface)
                            
                            selected current_journal_Quest == Q

                            text Q.name anchor (0.0, 0.5) pos (0.1, 0.5):
                                font "agency_fb.ttf"

                                if len(Q.name) > 20:
                                    size 32
                                else:
                                    size 36

                                color "#000000"

                            if Q.fully_completed:
                                add "images/interface/Player_menu/journal_clear.webp" anchor (0.5, 0.5) pos (0.51, 0.47) zoom interface_adjustment
                            elif Q.completed:
                                add "images/interface/Player_menu/journal_partial.webp" anchor (0.5, 0.5) pos (0.51, 0.47) zoom interface_adjustment

                            action SetVariable("current_journal_Quest", Q)

    vbar value YScrollValue("journal_viewport") anchor (0.5, 0.0) pos (0.315, 0.405) xysize (int(40*game_resolution), int(1114*game_resolution)):
        base_bar At("images/interface/Player_menu/journal_scrollbar.webp", interface)

        thumb At("images/interface/Player_menu/journal_scrollbar_thumb.webp", interface)
        thumb_offset int(276*game_resolution/2/10)

        unscrollable "hide"

    if current_journal_Quest:
        add "images/interface/Player_menu/journal_quest_box.webp" zoom interface_adjustment

        if current_journal_Quest.fully_completed:
            add "images/interface/Player_menu/journal_complete.webp" zoom interface_adjustment
        elif current_journal_Quest.completed:
            add "images/interface/Player_menu/journal_cleared.webp" zoom interface_adjustment
        else:
            add "images/interface/Player_menu/journal_pending.webp" zoom interface_adjustment

        if blinking:
            text "SUMMARY" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.364, 0.3365):
                size 35
        else:
            text "SUMMARY" + "_" anchor (0.0, 0.5) pos (0.364, 0.3365):
                size 35

        text current_journal_Quest.description anchor (0.5, 0.5) pos (0.635, 0.3365):
            if len(current_journal_Quest.description) >= 30:
                size 28
            elif len(current_journal_Quest.description) >= 25:
                size 32
            else:
                size 36

        text "OBJECTIVES" anchor (0.0, 0.0) pos (0.364, 0.4):
            size 35

        vbox anchor (0.5, 0.0) pos (0.635, 0.42):
            spacing 5

            for objective in current_journal_Quest.objectives.keys():
                $ display_objective = renpy.substitute(objective)

                if current_journal_Quest.objectives[objective][1]:
                    $ progress = eval(current_journal_Quest.objectives[objective][0])
                    $ target = current_journal_Quest.objectives[objective][1]

                    if current_journal_Quest.completed or progress > target:
                        $ progress = target

                    if progress == target:
                        textbutton "{s}[display_objective]: [progress]/[target]{/s}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            background None
                            
                            text_font "agency_fb.ttf"

                            text_size 32

                            action NullAction()

                            ## can eventually delete the length check
                            if journal_hints and len(current_journal_Quest.objectives[objective]) > 2 and current_journal_Quest.objectives[objective][2]:
                                tooltip current_journal_Quest.objectives[objective][2]
                    else:
                        textbutton "[display_objective]: [progress]/[target]" anchor (0.5, 0.5) pos (0.5, 0.5):
                            background None
                            
                            text_font "agency_fb.ttf"

                            text_size 32

                            action NullAction()

                            if journal_hints and len(current_journal_Quest.objectives[objective]) > 2 and current_journal_Quest.objectives[objective][2]:
                                tooltip current_journal_Quest.objectives[objective][2]
                else:
                    if eval(current_journal_Quest.objectives[objective][0]):
                        textbutton "{s}[display_objective]{/s}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            background None
                            
                            text_font "agency_fb.ttf"

                            text_size 32

                            action NullAction()

                            if journal_hints and len(current_journal_Quest.objectives[objective]) > 2 and current_journal_Quest.objectives[objective][2]:
                                tooltip current_journal_Quest.objectives[objective][2]
                    else:
                        textbutton "[display_objective]" anchor (0.5, 0.5) pos (0.5, 0.5):
                            background None
                            
                            text_font "agency_fb.ttf"

                            text_size 32

                            action NullAction()

                            if journal_hints and len(current_journal_Quest.objectives[objective]) > 2 and current_journal_Quest.objectives[objective][2]:
                                tooltip current_journal_Quest.objectives[objective][2]

            for optional_objective in current_journal_Quest.optional_objectives.keys():
                if current_journal_Quest.optional_objectives[optional_objective][1]:
                    $ progress = eval(current_journal_Quest.optional_objectives[optional_objective][0])
                    $ target = current_journal_Quest.optional_objectives[optional_objective][1]

                    $ optional_objective = renpy.substitute(optional_objective)

                    if current_journal_Quest.fully_completed or progress > target:
                        $ progress = target

                    if progress == target:
                        textbutton "{s}{i}Optional - [optional_objective]: [progress]/[target]{/i}{/s}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            background None
                            
                            text_font "agency_fb.ttf"

                            text_size 32

                            action NullAction()

                            if journal_hints and len(current_journal_Quest.optional_objectives[optional_objective]) > 2 and current_journal_Quest.optional_objectives[optional_objective][2]:
                                tooltip current_journal_Quest.optional_objectives[optional_objective][2]
                    else:
                        textbutton "{i}Optional - [optional_objective]: [progress]/[target]{/i}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            background None
                            
                            text_font "agency_fb.ttf"

                            text_size 32

                            action NullAction()

                            if journal_hints and len(current_journal_Quest.optional_objectives[optional_objective]) > 2 and current_journal_Quest.optional_objectives[optional_objective][2]:
                                tooltip current_journal_Quest.optional_objectives[optional_objective][2]
                else:
                    if eval(current_journal_Quest.optional_objectives[optional_objective][0]):
                        $ optional_objective = renpy.substitute(optional_objective)

                        textbutton "{s}{i}Optional - [optional_objective]{/i}{/s}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            background None
                            
                            text_font "agency_fb.ttf"

                            text_size 32

                            action NullAction()

                            if journal_hints and len(current_journal_Quest.optional_objectives[optional_objective]) > 2 and current_journal_Quest.optional_objectives[optional_objective][2]:
                                tooltip current_journal_Quest.optional_objectives[optional_objective][2]
                    else:
                        $ optional_objective = renpy.substitute(optional_objective)

                        textbutton "{i}Optional - [optional_objective]{/i}" anchor (0.5, 0.5) pos (0.5, 0.5):
                            background None

                            text_font "agency_fb.ttf"

                            text_size 32

                            action NullAction()

                            if journal_hints and len(current_journal_Quest.optional_objectives[optional_objective]) > 2 and current_journal_Quest.optional_objectives[optional_objective][2]:
                                tooltip current_journal_Quest.optional_objectives[optional_objective][2]

        if current_journal_Quest.rewards:
            hbox anchor (0.0, 0.5) pos (0.436, 0.885) xysize (0.41, int(248*game_resolution)):
                spacing 0

                for reward_type in current_journal_Quest.rewards.keys():
                    for reward in current_journal_Quest.rewards[reward_type]:
                        fixed xysize (int(249*game_resolution), int(249*game_resolution)):
                            add f"images/interface/Player_menu/journal_{reward_type}.webp" zoom interface_adjustment

                            text reward.upper() anchor (0.5, 0.5) pos (0.5, 0.81):
                                size 20

screen map_screen():
    style_prefix "Player_menu"

    $ available_groups = []
    $ available_subgroups = []

    for possible_group in location_groups.keys():
        if possible_group in ["Institute"] or time_index < 3:
            if type(location_groups[possible_group]) is dict:
                for possible_subgroup in location_groups[possible_group].keys():
                    for possible_location in location_groups[possible_group][possible_subgroup]:
                        $ available_groups.append(possible_group)
                        $ available_subgroups.append(possible_subgroup)
            else:        
                for possible_location in location_groups[possible_group]:
                    $ available_groups.append(possible_group)

    add "images/interface/Player_menu/map_background.webp" zoom interface_adjustment

    for location_group in location_groups.keys():
        if location_group in available_groups:
            imagebutton:
                idle At(f"images/interface/Player_menu/map_selection_{location_group}_idle.webp", interface)
                hover At(f"images/interface/Player_menu/map_selection_{location_group}.webp", interface)
                selected_idle At(f"images/interface/Player_menu/map_selection_{location_group}.webp", interface)

                selected location_group == current_group

                action [
                    SetVariable("current_group", location_group),
                    SetVariable("current_subgroup", "First Floor")]

            if location_group == "Institute":
                text "INSTITUTE" anchor (0.5, 0.5) pos (0.107, 0.251):
                    size 36
            elif location_group == "Mall":
                text "MALL" anchor (0.5, 0.5) pos (0.107, 0.331):
                    size 36

    if type(location_groups[current_group]) is dict:
        for location_subgroup in location_groups[current_group].keys():
            if location_subgroup in available_subgroups:
                imagebutton:
                    idle At(f"images/interface/Player_menu/map_floor_{location_subgroup.replace(' ', '_')}_idle.webp", interface)
                    hover At(f"images/interface/Player_menu/map_floor_{location_subgroup.replace(' ', '_')}.webp", interface)
                    selected_idle At(f"images/interface/Player_menu/map_floor_{location_subgroup.replace(' ', '_')}.webp", interface)

                    action SetVariable("current_subgroup", location_subgroup)

    text "FLOORS" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.065, 0.444):
        size 35

    if sandbox:
        imagebutton:
            idle At("images/interface/Player_menu/map_quikloc1_idle.webp", interface)
            hover At("images/interface/Player_menu/map_quikloc1.webp", interface)
            selected_idle At("images/interface/Player_menu/map_quikloc1.webp", interface)

            selected quick_location_1 is None

            if quick_location_2 is None:
                action [
                    SetVariable("quick_location_2", False),
                    SetVariable("quick_location_1", None)]
            elif quick_location_3 is None:
                action [
                    SetVariable("quick_location_3", False),
                    SetVariable("quick_location_1", None)]
            else:
                if quick_location_1 is None:
                    action SetVariable("quick_location_1", False)
                else:
                    action SetVariable("quick_location_1", None)

        imagebutton:
            idle At("images/interface/Player_menu/map_quikloc2_idle.webp", interface)
            hover At("images/interface/Player_menu/map_quikloc2.webp", interface)
            selected_idle At("images/interface/Player_menu/map_quikloc2.webp", interface)

            selected quick_location_2 is None

            if quick_location_1 is None:
                action [
                    SetVariable("quick_location_1", False),
                    SetVariable("quick_location_2", None)]
            elif quick_location_3 is None:
                action [
                    SetVariable("quick_location_3", False),
                    SetVariable("quick_location_2", None)]
            else:
                if quick_location_2 is None:
                    action SetVariable("quick_location_2", False)
                else:
                    action SetVariable("quick_location_2", None)

        imagebutton:
            idle At("images/interface/Player_menu/map_quikloc3_idle.webp", interface)
            hover At("images/interface/Player_menu/map_quikloc3.webp", interface)
            selected_idle At("images/interface/Player_menu/map_quikloc3.webp", interface)

            selected quick_location_3 is None

            if quick_location_1 is None:
                action [
                    SetVariable("quick_location_1", False),
                    SetVariable("quick_location_3", None)]
            elif quick_location_2 is None:
                action [
                    SetVariable("quick_location_2", False),
                    SetVariable("quick_location_3", None)]
            else:
                if quick_location_3 is None:
                    action SetVariable("quick_location_3", False)
                else:
                    action SetVariable("quick_location_3", None)

        text "1" anchor (0.5, 0.5) pos (0.073, 0.892):
            size 36

        text "2" anchor (0.5, 0.5) pos (0.107, 0.892):
            size 36

        text "3" anchor (0.5, 0.5) pos (0.14, 0.892):
            size 36

    text "QUICK TRAVEL" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.065, 0.801):
        size 30

    $ map_to_show = None

    if current_group == "Institute":
        if current_subgroup == "Basement":
            $ map_to_show = "basement"
        elif current_subgroup == "First Floor":
            $ map_to_show = "first_floor"
        elif current_subgroup == "Second Floor":
            $ map_to_show = "second_floor"
        elif current_subgroup == "Attic":
            $ map_to_show = "attic"
            
        add f"images/interface/Player_menu/map_institute_{map_to_show}.webp" zoom interface_adjustment
    elif current_group == "Mall":
        if current_subgroup == "First Floor":
            $ map_to_show = "mall"
            
        add "images/interface/Player_menu/map_mall.webp" zoom interface_adjustment
        
    if map_to_show:
        if current_subgroup:
            for possible_location in location_groups[current_group][current_subgroup]:
                if possible_location in marked_locations.keys():
                    $ Characters_present = []
                    $ map_tooltip = ""

                    for C in all_Characters:
                        if possible_location in [C.location, C.location.replace("_shower_", "_")]:
                            $ Characters_present.append(C)

                            if map_tooltip:
                                $ map_tooltip += f", {C.name}"
                            else:
                                $ map_tooltip += f"{C.name}"
                        elif C.location == "nearby" and Player.location == possible_location:
                            $ Characters_present.append(C)

                            if map_tooltip:
                                $ map_tooltip += f", {C.name}"
                            else:
                                $ map_tooltip += f"{C.name}"

                    button:
                        selected Player.location == possible_location

                        if possible_location in available_locations.keys():
                            if quick_location_1 is None:
                                action SetVariable("quick_location_1", available_locations[possible_location])
                            elif quick_location_2 is None:
                                action SetVariable("quick_location_2", available_locations[possible_location])
                            elif quick_location_3 is None:
                                action SetVariable("quick_location_3", available_locations[possible_location])
                            elif Player.location != possible_location:
                                action Function(exec, available_locations[possible_location])
                            else:
                                action NullAction()
                        else:
                            hover_sound None

                            action NullAction()

                        if possible_location not in bedrooms:
                            background None

                            if possible_location in ["bg_girls_hallway", "bg_hallway"]:
                                text map_names[possible_location] anchor (0.5, 0.5) pos (0.8, 0.5):
                                    size 36

                                    if possible_location in available_locations.keys():
                                        color "#000000" 
                                        hover_color "#aa4b14" 
                                        selected_color "#aa4b14"
                                    else:
                                        color "#bfbfbf"

                                    vertical True
                            elif possible_location in ["bg_mall"]:
                                text map_names[possible_location] anchor (0.5, 0.5) pos (0.65, 0.5):
                                    size 36

                                    if possible_location in available_locations.keys():
                                        color "#000000" 
                                        hover_color "#aa4b14" 
                                        selected_color "#aa4b14"
                                    else:
                                        color "#bfbfbf"

                                    vertical True
                            else:
                                text map_names[possible_location]:
                                    size 36

                                    if possible_location in available_locations.keys():
                                        color "#000000" 
                                        hover_color "#aa4b14" 
                                        selected_color "#aa4b14"
                                    else:
                                        color "#bfbfbf"
                        elif possible_location == Player.home:
                            idle_background At(f"images/interface/Player_menu/Player_{Player.background_color}_idle.webp", interface)
                            hover_background At(f"images/interface/Player_menu/Player_{Player.background_color}.webp", interface)
                            selected_idle_background At(f"images/interface/Player_menu/Player_{Player.background_color}.webp", interface)
                        elif possible_location not in [Charles.home, Kurt.home]:
                            if possible_location in available_locations.keys():
                                
                                if renpy.loadable(f"images/interface/Player_menu/{possible_location[3:]}_idle.webp"):
                                    idle_background At(f"images/interface/Player_menu/{possible_location[3:]}_idle.webp", interface)
                                    hover_background At(f"images/interface/Player_menu/{possible_location[3:]}.webp", interface)
                                    selected_idle_background At(f"images/interface/Player_menu/{possible_location[3:]}.webp", interface)

                            else:
                                background None
                        else:
                            background None

                            text map_names[possible_location]:
                                size 36

                                if possible_location in available_locations.keys():
                                    color "#000000" 
                                    hover_color "#aa4b14" 
                                    selected_color "#aa4b14"
                                else:
                                    color "#bfbfbf"

                        if possible_location == "bg_campus":
                            pos (0.445, 0.89) xysize (0.49, 0.11)
                        elif possible_location == Charles.home:
                            pos (0.445, 0.503) xysize (0.1, 0.135)
                        elif possible_location == "bg_classroom":
                            pos (0.628, 0.408) xysize (0.12, 0.166)
                        elif possible_location == "bg_danger":
                            pos (0.2615, 0.408) xysize (0.125, 0.169)
                        elif possible_location == "bg_entrance":
                            pos (0.445, 0.7965) xysize (0.01, 0.01)
                        elif possible_location == "bg_girls_hallway":
                            pos (0.259, 0.578) xysize (0.0274, 0.51)
                        elif possible_location == "bg_hallway":
                            pos (0.626, 0.578) xysize (0.0274, 0.51)
                        elif possible_location == Kurt.home:
                            pos (0.590, 0.604) xysize (0.05, 0.05)
                        elif possible_location == "bg_lockers":
                            pos (0.336, 0.534) xysize (0.118, 0.075)
                        elif possible_location == "bg_mall":
                            pos (0.346, 0.5765) xysize (0.038, 0.533)
                        elif possible_location == "bg_movies":
                            pos (0.485, 0.477) xysize (0.074, 0.2)
                        elif possible_location == "bg_pool":
                            pos (0.445, 0.352) xysize (0.243, 0.157)
                        elif possible_location == "bg_study":
                            pos (0.628, 0.739) xysize (0.12, 0.183)
                        else:
                            focus_mask True

                        if map_icons:
                            if possible_location in ["bg_girls_hallway", "bg_hallway"]:
                                vbox anchor (0.5, 1.0) pos (0.7, 0.96) xysize (1.0, 1.0):
                                    spacing 10

                                    $ marked = False

                                    if marked_locations[possible_location]:
                                        add At("images/interface/Player_menu/event_alert.webp", phone_icon)

                                        $ marked = True

                                    if Player.location == possible_location:
                                        add At(f"images/interface/icons/Player_{Player.background_color}.webp", map_icon) align (0.5, 0.5)

                                        $ marked = True

                                    for C in Characters_present:
                                        if marked:
                                            imagebutton align (0.5, 0.5):
                                                idle At(f"images/interface/Player_menu/plus.webp", phone_icon) 
                                                hover At(f"images/interface/Player_menu/plus.webp", phone_icon) 

                                                tooltip map_tooltip

                                                if tooltips_enabled:
                                                    action NullAction()
                                                else:
                                                    action None

                                            break
                                        else:
                                            add At(f"images/interface/icons/{C.tag}.webp", map_icon) align (0.5, 0.5)

                                        $ marked = True
                            elif possible_location in ["bg_mall"]:
                                vbox anchor (0.5, 1.0) pos (0.57, 0.8) xysize (1.0, 1.0):
                                    spacing 10

                                    $ marked = False

                                    if marked_locations[possible_location]:
                                        add At("images/interface/Player_menu/event_alert.webp", phone_icon)

                                        $ marked = True

                                    if Player.location == possible_location:
                                        add At(f"images/interface/icons/Player_{Player.background_color}.webp", map_icon) align (0.5, 0.5)

                                        $ marked = True

                                    for C in Characters_present:
                                        if marked:
                                            imagebutton align (0.5, 0.5):
                                                idle At(f"images/interface/Player_menu/plus.webp", phone_icon) 
                                                hover At(f"images/interface/Player_menu/plus.webp", phone_icon) 

                                                tooltip map_tooltip

                                                if tooltips_enabled:
                                                    action NullAction()
                                                else:
                                                    action None

                                            break
                                        else:
                                            add At(f"images/interface/icons/{C.tag}.webp", map_icon) align (0.5, 0.5)

                                        $ marked = True
                            elif possible_location not in [Player.home, Rogue.home, Laura.home, Jean.home]:
                                hbox xysize (1.0, 1.0):
                                    if possible_location in ["bg_campus", Charles.home]:
                                        spacing 10

                                        anchor (0.5, 1.0) pos (0.5, 1.1)
                                    elif possible_location in ["bg_lockers"]:
                                        spacing 10

                                        anchor (0.5, 1.0) pos (0.5, 1.3)
                                    else:
                                        spacing 10

                                        anchor (0.5, 1.0) pos (0.5, 0.9)

                                    $ marked = False

                                    if marked_locations[possible_location]:
                                        add At("images/interface/Player_menu/event_alert.webp", phone_icon)

                                        $ marked = True

                                    if possible_location == "bg_study" and time_index < 3 and Charles.check_traits("has_jobs"):
                                        add At("images/interface/Player_menu/work.webp", phone_icon)

                                        $ marked = True

                                    if Player.location == possible_location:
                                        add At(f"images/interface/icons/Player_{Player.background_color}.webp", map_icon) align (0.5, 0.5)

                                        $ marked = True

                                    for C in Characters_present:
                                        if marked:
                                            imagebutton align (0.5, 0.5):
                                                idle At(f"images/interface/Player_menu/plus.webp", phone_icon) 
                                                hover At(f"images/interface/Player_menu/plus.webp", phone_icon) 

                                                tooltip map_tooltip

                                                if tooltips_enabled:
                                                    action NullAction()
                                                else:
                                                    action None

                                            break
                                        else:
                                            add At(f"images/interface/icons/{C.tag}.webp", map_icon) align (0.5, 0.5)

                                        $ marked = True

                    if map_icons:
                        if possible_location in [Player.home, Rogue.home, Laura.home, Jean.home]:
                            hbox xysize (1.0, 1.0):
                                if possible_location == Player.home:
                                    spacing 5

                                    anchor (0.5, 0.5) pos (0.5, 0.5) offset (318, -21)
                                elif possible_location == Rogue.home:
                                    spacing 5

                                    anchor (0.5, 0.5) pos (0.5, 0.5) offset (-387, -88)
                                elif possible_location == Laura.home:
                                    spacing 5

                                    anchor (0.5, 0.5) pos (0.5, 0.5) offset (-531, 114)
                                elif possible_location == Jean.home:
                                    spacing 5

                                    anchor (0.5, 0.5) pos (0.5, 0.5) offset (-531, -157)

                                $ marked = False

                                if marked_locations[possible_location]:
                                    add At("images/interface/Player_menu/event_alert.webp", phone_icon)

                                    $ marked = True

                                if Player.location == possible_location:
                                    add At(f"images/interface/icons/Player_{Player.background_color}.webp", map_icon)

                                    $ marked = True

                                for C in Characters_present:
                                    if marked:
                                        imagebutton:
                                            idle At(f"images/interface/Player_menu/plus.webp", phone_icon) 
                                            hover At(f"images/interface/Player_menu/plus.webp", phone_icon) 

                                            tooltip map_tooltip

                                            if tooltips_enabled:
                                                action NullAction()
                                            else:
                                                action None

                                        break
                                    else:
                                        add At(f"images/interface/icons/{C.tag}.webp", map_icon)

                                    $ marked = True
    if blinking:
        text "X-TRACKER" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.733, 0.237):
            size 35
    else:
        text "X-TRACKER" + "_" anchor (0.0, 0.5) pos (0.733, 0.237):
            size 35

    vpgrid anchor (0.5, 0.0) pos (0.828, 0.294) xysize (0.19, 0.63):
        cols 1

        spacing 10

        draggable True
        mousewheel True

        xfill True

        for possible_group in location_groups.keys():
            for possible_subgroup in location_groups[possible_group].keys():
                for possible_location in location_groups[possible_group][possible_subgroup]:
                    if possible_location in marked_locations.keys():
                        if marked_locations[possible_location] or possible_location in [Player.location, Player.location.replace("_shower_", "_")] or get_Present(location = possible_location, include_Party = False)[0] or get_Present(location = possible_location.replace("bg_", "bg_shower_"), include_Party = False)[0] or (possible_location == "bg_study" and time_index < 3 and Charles.check_traits("has_jobs")):
                            button xalign 0.0 xsize 1.0:
                                background None

                                selected Player.location == possible_location

                                text location_names[possible_location] xanchor 0.0 xpos -0.035:
                                    size 36

                                    text_align 0.0

                                    if possible_location in available_locations.keys():
                                        hover_color "#ffa903" 
                                        selected_color "#ffa903"

                                if possible_location in available_locations.keys():
                                    if quick_location_1 is None:
                                        action SetVariable("quick_location_1", available_locations[possible_location])
                                    elif quick_location_2 is None:
                                        action SetVariable("quick_location_2", available_locations[possible_location])
                                    elif quick_location_3 is None:
                                        action SetVariable("quick_location_3", available_locations[possible_location])
                                    elif Player.location != possible_location:
                                        action Function(exec, available_locations[possible_location])
                                    else:
                                        action NullAction()
                                else:
                                    hover_sound None

                                    action NullAction()

                            fixed xysize(1.0, int(88*game_resolution)):
                                hbox xalign 0.0:
                                    spacing 5

                                    if marked_locations[possible_location]:
                                        add At("images/interface/Player_menu/event_alert.webp", phone_icon)

                                    if possible_location == "bg_study" and time_index < 3 and Charles.check_traits("has_jobs"):
                                        add At("images/interface/Player_menu/work.webp", phone_icon)

                                    if possible_location in [Player.location, Player.location.replace("_shower_", "_")]:
                                        add At(f"images/interface/icons/Player_{Player.background_color}.webp", map_icon)

                                    for C in all_Characters:
                                        if possible_location in [C.location, C.location.replace("_shower_", "_")]:
                                            add At(f"images/interface/icons/{C.tag}.webp", map_icon)

screen relationships_screen():
    style_prefix "Player_menu"

    add "images/interface/Player_menu/relationships_background.webp" zoom interface_adjustment

    text "RELATIONSHIPS" + "{alpha=0.0}_{/alpha}" anchor (0.0, 0.5) pos (0.065, 0.3365):
        size 35

    viewport id "relationships_viewport" anchor (0.5, 0.0) pos (0.18, 0.405) xysize (int(911*game_resolution), int(1114*game_resolution)):
        draggable True
        mousewheel True

        vbox:
            for C in active_Companions:
                button xysize (int(911*game_resolution), int(191*game_resolution)):
                    idle_background At(f"images/interface/Player_menu/relationships_button_idle.webp", interface)
                    hover_background At(f"images/interface/Player_menu/relationships_button.webp", interface)
                    selected_idle_background At(f"images/interface/Player_menu/relationships_button.webp", interface)
                    
                    selected current_relationships_Entry == C

                    if C.full_name == "???":
                        text C.name anchor (0.0, 0.5) pos (0.1, 0.5):
                            font "agency_fb.ttf"

                            size 36

                            color "#000000"
                    else:
                        text C.full_name anchor (0.0, 0.5) pos (0.1, 0.5):
                            font "agency_fb.ttf"

                            size 36

                            color "#000000"

                    action SetVariable("current_relationships_Entry", C)

    vbar value YScrollValue("relationships_viewport") anchor (0.5, 0.0) pos (0.315, 0.405) xysize (int(40*game_resolution), int(1114*game_resolution)):
        base_bar At("images/interface/Player_menu/relationships_scrollbar.webp", interface)

        thumb At("images/interface/Player_menu/relationships_scrollbar_thumb.webp", interface)
        thumb_offset int(276*game_resolution/2/10)

        unscrollable "hide"

    if current_relationships_Entry:
        add "images/interface/Player_menu/relationships_info.webp" zoom interface_adjustment

        add f"images/interface/photos/{current_relationships_Entry.tag}.webp" anchor (0.5, 0.5) pos (0.421, 0.48) zoom 0.5

        add "images/interface/Player_menu/relationships_love.webp" zoom interface_adjustment

        text f"{current_relationships_Entry.love}" anchor (0.5, 0.5) pos (0.435, 0.567):
            font "agency_fb.ttf"

            size 30

            color "#000000"

        add "images/interface/Player_menu/relationships_trust.webp" zoom interface_adjustment

        text f"{current_relationships_Entry.trust}" anchor (0.5, 0.5) pos (0.435, 0.608):
            font "agency_fb.ttf"

            size 30

            color "#000000"

        text "PUBLIC NAME" anchor (0.0, 0.5) pos (0.495, 0.343):
            font "agency_fb.ttf"

            size 28

        text current_relationships_Entry.public_name anchor (1.0, 0.5) pos (0.713, 0.343):
            font "agency_fb.ttf"

            size 28

        text "RELATIONSHIP STATUS" anchor (0.0, 0.5) pos (0.495, 0.398):
            font "agency_fb.ttf"

            size 28

        if current_relationships_Entry not in Partners:
            text "Single" anchor (1.0, 0.5) pos (0.713, 0.398):
                font "agency_fb.ttf"

                size 28
        elif current_relationships_Entry.check_traits("polyamorous"):
            text "Polyamorous" anchor (1.0, 0.5) pos (0.713, 0.398):
                font "agency_fb.ttf"

                size 28
        else:
            text "In a relationship" anchor (1.0, 0.5) pos (0.713, 0.398):
                font "agency_fb.ttf"

                size 28

        text "HER PETNAME" anchor (0.0, 0.5) pos (0.495, 0.454):
            font "agency_fb.ttf"

            size 28

        text current_relationships_Entry.petname anchor (1.0, 0.5) pos (0.713, 0.454):
            font "agency_fb.ttf"

            size 28

        text "MY PETNAME" anchor (0.0, 0.5) pos (0.495, 0.512):
            font "agency_fb.ttf"

            size 28

        text current_relationships_Entry.Player_petname anchor (1.0, 0.5) pos (0.713, 0.512):
            font "agency_fb.ttf"

            size 28

        text "MOOD" anchor (0.5, 0.5) pos (0.829, 0.335):
            font "agency_fb.ttf"

            size 28

        if current_relationships_Entry.is_in_normal_mood():
            add "images/interface/Player_menu/relationships_happy.webp" zoom interface_adjustment

        if current_relationships_Entry.get_status() == "mad":
            add "images/interface/Player_menu/relationships_mad.webp" zoom interface_adjustment

        if current_relationships_Entry.status["horny"] or current_relationships_Entry.status["nympho"]:
            add "images/interface/Player_menu/relationships_horny.webp" zoom interface_adjustment

        for s, status in enumerate(["heartbroken"]):
            if current_relationships_Entry.status[status]:
                add f"images/interface/Player_menu/relationships_{status}.webp" zoom interface_adjustment

        text "FRIENDSHIPS" anchor (0.5, 0.5) pos (0.829, 0.447):
            font "agency_fb.ttf"

            size 22

        text "Best Friends" anchor (0.5, 0.5) pos (0.771, 0.488):
            font "agency_fb.ttf"

            size 20

        text "Good Friends" anchor (0.5, 0.5) pos (0.834, 0.488):
            font "agency_fb.ttf"

            size 20

        text "Friends" anchor (0.5, 0.5) pos (0.896, 0.488):
            font "agency_fb.ttf"

            size 22

        text "Acquaintances" anchor (0.5, 0.5) pos (0.771, 0.517):
            font "agency_fb.ttf"

            size 16

        text "Rivals" anchor (0.5, 0.5) pos (0.834, 0.517):
            font "agency_fb.ttf"

            size 22

        text "Enemies" anchor (0.5, 0.5) pos (0.896, 0.517):
            font "agency_fb.ttf"

            size 22

        viewport id "relationships_friendship_viewport" anchor (0.0, 0.5) pos (0.515, 0.595) xysize (0.385, int(195*game_resolution)):
            draggable True
            mousewheel True

            hbox:
                spacing 20

                for C in eval(f"{current_relationships_Entry.tag}_friendship_thresholds.keys()"):
                    if C != current_relationships_Entry.tag and eval(C) in active_Companions:
                        $ friendship = eval(f"current_relationships_Entry.get_friendship({C})")

                        fixed xysize (int(135*game_resolution), int(195*game_resolution)):
                            add f"images/interface/photos/{C}.webp" align (0.5, 0.5) zoom 0.13

                            add f"images/interface/Player_menu/relationships_{friendship}.webp" align (0.5, 0.5) zoom interface_adjustment

        for q, quirk in enumerate(current_relationships_Entry.database["quirks"].keys()):
            if " 2 - " in quirk and q == 0:
                $ q = 1

            text quirk anchor (0.0, 0.5) pos (0.37 + 0.288*q, 0.684):
                font "agency_fb.ttf"

                size 30

            frame anchor (0.5, 0.0) pos (0.503 + 0.288*q, 0.724) xsize 0.275:
                text current_relationships_Entry.database["quirks"][quirk] xalign 0.0:
                    font "agency_fb.ttf"
                            
                    size 28

                    text_align 0.0