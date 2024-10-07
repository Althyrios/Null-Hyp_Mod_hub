init:
    default item_paths = get_all_item_images()

init python:

    def get_all_item_images():
        item_images = {}

        all_files = renpy.list_files()

        for file in all_files:
            if file.startswith("images/interface/items/") and file.endswith(('.png', '.jpg', '.webp')):
                item_name = file.split('/')[-1].split('.')[0]
                item_images[item_name] = file

        for M in get_mod_directories():
            mod_var_name = f"item_{M}_paths"

            if mod_var_name in globals():
                mod_items = globals()[mod_var_name]
                for item_name, item_path in mod_items.items():
                    item_images[item_name] = item_path

        return item_images

    def all_Items():
        Items = [
            barbell_labia_piercings(None),
            barbell_nipple_piercings(None),
            belly_piercing(None),
            box_of_chocolates(None),
            candle(None),
            # coffee(None),
            combat_manual(None),
            designer_purse(None),
            dildo(None),
            # flowers(None),
            # flowery_perfume(None),
            # fruity_perfume(None),
            heart_anal_plug(None),
            horror_novel(None),
            # journal(None),
            mystery_novel(None),
            plant1(None),
            plant2(None),
            plant3(None),
            remote_vibrator(None),
            ring_labia_piercings(None),
            ring_nipple_piercings(None),
            round_anal_plug(None),
            # spicy_perfume(None),
            steamy_romance_novel(None),
            # tea(None),
            teddy_bear(None),
            vibrator(None),
            # watercolors(None),
            wholesome_romance_novel(None)
        ]

        return Items

    def register_Items():
        global shop_inventory
        global unrestricted_shop_inventory

        Items = all_Items()

        for I in Items:
            if I.string not in shop_inventory[I.shop_type].keys():
                unlocked = True

                for criterion in I.criteria:
                    if not eval(criterion):
                        unlocked = False

                if unlocked:
                    shop_inventory[I.shop_type][I.string] = I
                    unrestricted_shop_inventory[I.shop_type][I.string] = I

        # ADDED FOR MOD SUPPORT
        for M in mod_directories:
            function_name = f"all_{M}_Items"
            if function_name in globals() and callable(globals()[function_name]):
                Items =  eval(f"all_{M}_Items()")

                for I in Items:
                    if I.string not in shop_inventory[I.shop_type].keys():
                        unlocked = True

                        for criterion in I.criteria:
                            if not eval(criterion):
                                unlocked = False

                        if unlocked:
                            shop_inventory[I.shop_type][I.string] = I
                            unrestricted_shop_inventory[I.shop_type][I.string] = I

        for C in all_Companions:
            Items = eval(f"{C.tag}_special_Items()")

            for I in Items:
                already_bought = False

                Item_string = I.Owner.tag + "_" + I.string

                if Item_string in Player.inventory.keys():
                    already_bought = True

                ## can delete this eventually
                if I.string in Player.inventory.keys():
                    if isinstance(Player.inventory[I.string], list):
                        for other_I in Player.inventory[I.string]:
                            if other_I.Owner == C:
                                already_bought = True
                    elif Player.inventory[I.string].Owner == C:
                        already_bought = True

                ## can delete third condition eventually
                if already_bought or Item_string in C.inventory.keys() or I.string in C.inventory.keys():
                    continue

                ## can delete second condition eventually
                if Item_string not in shop_inventory[I.shop_type].keys() and I.string not in shop_inventory[I.shop_type].keys():
                    unlocked = True

                    for criterion in I.criteria:
                        if not eval(criterion):
                            unlocked = False

                    if unlocked:
                        shop_inventory[I.shop_type][Item_string] = I
                        unrestricted_shop_inventory[I.shop_type][Item_string] = I
        



        return