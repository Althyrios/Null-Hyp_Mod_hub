init python:

    def something_stupid():
        name = "Something stupid"

        string = "something_stupid"

        Quest_type = "addon"

        chapter = 1

        description = "Do something very stupid"

        objectives = {
            "Attend class this week": [f"Player.History.check('attended_class', tracker = 'weekly')", 50, None]}

        optional_objectives = {}

        rewards = {}

        criteria = []

        resets = True

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria, resets = resets)