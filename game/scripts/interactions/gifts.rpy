label give_Character_gift(Character, Item):
    hide screen Player_menu

    $ temp_Character_picker_disabled = Character_picker_disabled

    $ Character_picker_disabled = True

    if Item.Owner and Item.Owner != Character:
        "Pretty sure you bought that with someone else in mind."

        show screen interactions_screen(Character)
        
        return

    if ("piercing" in Item.string or "plug" in Item.string or "vibrator" in Item.string) and Item.string in Character.inventory.keys():
        "She already owns this."

        show screen interactions_screen(Character)

        return

    if "plant" in Item.string:
        $ Item_string = "plant"
    else:
        $ Item_string = Item.string

    $ can_give_item = False

    # ADDED FOR MOD SUPPORT
    $ thresholds_key = f"{Character.tag}_gift_thresholds"
    if Item.string in eval(thresholds_key):

        if (Item.shop_type in ["sex"] and approval_check(Character, threshold = eval(f"{Character.tag}_gift_thresholds[Item.string]"), extra_condition = "sexy_gifts")) or approval_check(Character, threshold = eval(f"{Character.tag}_gift_thresholds[Item.string]")):
            if Item.filter_type == "key_gifts":
                $ I_string = Item.Owner.tag + "_" + Item.string
            else:
                $ I_string = Item.string
            
            if I_string not in Character.inventory.keys():
                call expression f"{Character.tag}_{Item_string}_gift_accept" from _call_expression_239

                if _return:
                    call change_Character_stat(Character, "love", eval(f"{Character.tag}_gift_bonuses[Item.string]")[0]) from _call_change_Character_stat_4
                    call change_Character_stat(Character, "trust", eval(f"{Character.tag}_gift_bonuses[Item.string]")[1]) from _call_change_Character_stat_5

                    $ _return = True
            else:
                $ _return = True

            if _return:
                $ Item.Owner = Character

                if I_string in Character.inventory.keys():
                    $ Character.inventory[I_string].append(Item)
                else:
                    $ Character.inventory[I_string] = [Item]

                if I_string in Player.inventory.keys():
                    if len(Player.inventory[I_string]) > 1:
                        $ Player.inventory[I_string].remove(Item)
                    else:
                        $ del Player.inventory[I_string]

                ## can delete eventually
                if Item.shop_type in ["clothing", "lingerie"] or Item.filter_type == "key_gifts":
                    if Item.string in Player.inventory.keys():
                        if len(Player.inventory[Item.string]) > 1:
                            $ Player.inventory[Item.string].remove(Item)
                        else:
                            $ del Player.inventory[Item.string]
                    
                $ Player.History.update("gave_gift")
                $ Player.History.update(f"gave_{Item_string}")
                
                $ Character.History.update(f"given_{Item_string}")

                if Item_string == "remote_vibrator" and "Player_remote_vibrator" not in Player.inventory.keys():
                    $ Player_remote_vibrator = remote_vibrator(Player)
                    $ Player_remote_vibrator.name = "remote vibrator controller"
                    $ Player_remote_vibrator.filter_type = "key_gifts"

                    $ Player.inventory["Player_remote_vibrator"] = [Player_remote_vibrator]
            else:
                $ Character.History.update(f"said_no_to_{Item_string}")
        else:
            if Character.History.check(f"said_no_to_{Item_string}", tracker = "recent") >= 2:
                call change_Character_stat(Character, "love", -small_stat) from _call_change_Character_stat_979
                call change_Character_stat(Character, "trust", -small_stat) from _call_change_Character_stat_980

                call expression f"{Character.tag}_rejected_gift_twice" from _call_expression_241
            elif Character.History.check(f"said_no_to_{Item_string}", tracker = "recent") == 1:
                call change_Character_stat(Character, "love", -tiny_stat) from _call_change_Character_stat_981

                call expression f"{Character.tag}_rejected_gift_once" from _call_expression_242
            else:
                call expression f"{Character.tag}_{Item_string}_gift_reject" from _call_expression_243

            $ Character.History.update(f"said_no_to_{Item_string}")
            
    else:
        $ ch_tag = f"ch_{Character.tag}"
        $ renpy.say(eval(ch_tag), f"No thanks, I don't need {Item.name}.")
    $ Character_picker_disabled = temp_Character_picker_disabled

    if Character.location == Player.location:
        show screen interactions_screen(Character)
    else:
        call move_location(Player.location) from _call_move_location_69

    return