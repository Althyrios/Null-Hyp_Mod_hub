init python:

    def Random_mod_story():
        label = "Random_mod_story"

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

label Random_mod_story:
    "Congrats, you triggered a random mod story event."

    return