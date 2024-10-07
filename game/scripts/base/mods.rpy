init -1:
    default mod_directories = get_mod_directories()
    # default mod_map_icons = get_mod_map_icon()

init -2 python:

    import os

    def get_mod_directories():
        all_files = renpy.list_files(common=False)

        elements = [f for f in all_files if f.startswith("mods/mod_")]

        mod_files = set()

        for element in elements:
            parts = element.split('/') # Split string
            if len(parts) > 1:
                mod_files.add(parts[1])

        mod_directories = list(mod_files)

        return mod_directories
    
    def get_mod_characters(mod_directory):
        all_files = renpy.list_files(common=False)

        elements = [f for f in all_files if f.startswith(f"mods/{mod_directory}/characters")]

        characters = set()

        for element in elements:
            parts = element.split('/') # Split string
            if len(parts) > 3 and ".rpy" not in parts[3]:
                characters.add(parts[3])

        mod_characters = list(characters)

        return mod_characters

    def random_bullshit_go():
        # testlist = []

        # for M in mod_directories:
        #     mod_characters = get_mod_characters(M)

        #     mod_tags = []
        #     for name in mod_characters:
        #         mod_tags.append(eval(f"{name}.tag"))

        #     for C in mod_tags:
        #         # testlist.append(f"all_{M}_{C}_Quests()")
        #         # function_name = f"all_{M}_{C}_Quests"
        #         function_name = f"all_{M}_{C}_Events"
        #         if function_name in globals() and callable(globals()[function_name]):
        #             testlist.append(function_name)

        #     return testlist

        mod_directories = get_mod_directories()

        all_files = renpy.list_files(common=False)

        image_names = []

        for M in mod_directories:
            mod_images = [f for f in all_files if f.startswith(f"mods/{M}/images/interface/Player_menu/")]

            mod_images = [f for f in mod_images if not f.endswith("_idle.webp")]

            image_names.extend(mod_images)

        return image_names

    def is_modded_item(item):
        for M in mod_directories:
            function_name = f"all_{M}_Items"
            if function_name in globals() and callable(globals()[function_name]):
                mod_items = eval(f"{function_name}()")
                if item in mod_items:
                    return True
                
        return False

    def get_mod_of_item(item):
        for M in mod_directories:
            function_name = f"all_{M}_Items"
            if function_name in globals() and callable(globals()[function_name]):
                mod_items = eval(f"{function_name}()")
                if item in mod_items:
                    return M
        return None

    def get_mod_map_icon():

        mod_directories = get_mod_directories()

        all_files = renpy.list_files(common=False)

        image_names = []

        for M in mod_directories:
            mod_images = [f for f in all_files if f.startswith(f"mods/{M}/images/interface/Player_menu/")]

            mod_images = [f for f in mod_images if not f.endswith("_idle.webp")]

            image_names.extend(mod_images)

        return image_names

    def get_mod_item_image():

        all_files = renpy.list_files(common=False)

        for M in mod_directories:
            image_names = [f for f in all_files if f.startswith(f"mods/{M}/images/interface/items/")]

        return image_names

label mods:

    "Here is the list of folders in the 'mods' directory: [mod_directories]"

    # $ c_mT1 = get_mod_characters("mod_TEST1")
    $ c_mT2 = get_mod_characters("mod_TEST2")

    # "Here are all characters in mod_TEST1: [c_mT1]"
    # "Here are all characters in mod_TEST2: [c_mT2]"

    # $ q1 = all_Jean_Quests()
    # $ q2 = all_mod_TEST2_Jean_Quests()

    # "[q1]"
    # "[q2]"

    # $ testTAG = eval(f"{'Jean'}.tag")
    # $ testTAG_list = eval(f"{c_mT2[0]}.tag")

    # "[Jean.tag] - [testTAG] - [testTAG_list]"

    $ test = random_bullshit_go()
    "[test]"

    return