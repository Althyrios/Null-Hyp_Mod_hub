init python:

    def Rogue_wagh_Quest():
        name = f"{Rogue.name}: 40K"

        string = "Rogue_wagh_Quest"

        Quest_type = "addon"

        chapter = 1

        description = "Oh no, Rogue will be playing orcs for your next Warhammer40K game!"

        objectives = {
            "Gain Trust": ["Rogue.trust", 10000, None]}

        optional_objectives = {}

        rewards = {}

        criteria = []

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)