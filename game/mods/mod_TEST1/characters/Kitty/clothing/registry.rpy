init:

    default all_Kitty_Clothes_strings = []

init python:

    def all_Kitty_Clothes():
        global all_Kitty_Clothes_strings
        
        Clothes = [
            Kitty_ponytail_hair()
        ]

        all_Kitty_Clothes_strings = []

        for C in Clothes:
            all_Kitty_Clothes_strings.append(C.string)

        return Clothes

    def Kitty_shopping_list():
        Clothes = [
            
        ]

        return Clothes