init python:

    def Rogue_mod_test():
        label = "Rogue_mod_test"

        conditions = [
            "chapter == 1 and season == 4",

            "Player.destination == 'bg_girls_hallway'",

            "not Party",

            "renpy.random.random() > 0.9",

            "Rogue.is_in_normal_mood()"]

        traveling = True

        priority = 1

        markers = {
            "bg_danger": [
                "chapter == 1 and season == 4",

                "Player.location != 'bg_girls_hallway'",

                "not Party",

                "renpy.random.random() > 0.9",

                "Rogue.is_in_normal_mood()"]}

        return EventClass(label, conditions, traveling = traveling, priority = priority, markers = markers)


label Rogue_mod_test:
    $ ongoing_Event = True

    call remove_Characters(location = "bg_girls_hallway")
    call set_the_scene(location = "bg_girls_hallway")

    "Walking through the hall you stop in front of [Rogue.name]'s room. It's a TRAP!!!!" 

    menu:
        extend ""
        "Go see what she's up to":
            pass
        "Let her do her thing":
            $ EventScheduler.Events["Rogue_mod_test"].reset()

            $ ongoing_Event = False

            return

    call knock_on_door(times = 2)

    ch_Player "Hello There !"
    
    call set_the_scene(location = Rogue.home)

    call add_Characters(Rogue)

    ch_Rogue "GENERAL KENOBI!"
    ch_Rogue "You are a bold one"

    call move_location("bg_girls_hallway")

    $ ongoing_Event = False

    return