init python:

    def mod_TEST1_init():
        label = "mod_TEST1_init"

        conditions = [
            "chapter == 1 and season == 4",

            "Player.destination == 'bg_girls_hallway'",

            "not Party",

            "renpy.random.random() > 0"]

        traveling = True

        priority = 1

        markers = {
            "bg_danger": [
                "chapter == 1 and season == 4",

                "Player.location != 'bg_girls_hallway'",

                "not Party",

                "renpy.random.random() > 0"]}

        return EventClass(label, conditions, traveling = traveling, priority = priority, markers = markers)

label mod_TEST1_init:
    "Congrats, you unlocked Kitty !"

    call set_the_scene(location = "bg_girls_hallway")
    call add_Characters(Kitty)

    ch_Kitty "Hey pal"
    
    $ unlocked_Characters.append(Kitty)
    $ Kitty.History.update("met")

    call send_Characters(Kitty, "hold")

    # call hide_Character(Kitty, send_Offscreen = True)

    call update_Kitty_database

    $ location_groups["Institute"]["Second Floor"].append("bg_Kitty")
    $ marked_locations["bg_Kitty"] = []
    $ unlocked_locations.update({Kitty.home: "renpy.call('travel', Kitty)"})

    $ active_Companions.append(Kitty)

    $ register_Items()

    return
