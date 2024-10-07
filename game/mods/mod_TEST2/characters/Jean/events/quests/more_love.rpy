init python:

    def Jean_more_love_Quest():
        name = f"{Jean.full_name}: Love"

        string = "Jean_more_love_Quest"

        Quest_type = "addon"

        chapter = 1

        description = "Fall MOOORE in love with your favorite redhaired upperclassman"

        objectives = {
            "Gain Love": ["Jean.love", 1000, None],

            "Gain Trust": ["Jean.trust", 1000, None]}

        optional_objectives = {}

        rewards = {}

        criteria = []

        return QuestClass(name, string, Quest_type, chapter, description, objectives, optional_objectives, rewards, criteria)