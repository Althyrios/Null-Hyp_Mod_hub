
# Create your mod :

Add a new folder inside the `mods` folder.
Give it the name you want but it needs to have "mod_" before.

Example :
If you want to create the mod TEST you folder needs to be named "mod_TEST"

________________________________________________________________________________________________________________________

# How to add a new quest and events to an existing character :

Inside the `mod_TEST/characters/existing_character/events` folder (if one of the element of this path doesn't exist create it) create a file `registry.rpy`

ATTENTION : existing_character is of course the name of the character in the base game characters

registry.rpy template :

```
init python:

    def all_mod_TEST_existing_character_Events():
        Events = []

        return Events

    def all_mod_TEST_existing_character_Quests():
        Quests = []

        return Quests
```

## How to add a new quest to an existing character :

Create the folder `quests` and create the file of your quest `example_name.rpy` and refer to existing quests in the base game to write yours.

Then add your quest inside Quests = [] in registry.rpy

Do not forget to tag your quest as "addon" in Quest_type


## How to add a new event to an existing character :

Inside the folder event create the file of your event `event_name.rpy` and refer to existing events in the base game to write yours/

Then add your event inside Events = [] in registry.rpy
________________________________________________________________________________________________________________________

# Add a general event or quest :

Inside the `mod_TEST/events` folder (if one of the element of this path doesn't exist create it) create a file `registry.rpy`

registry.rpy template :

```
init python:

    def all_mod_TEST_Events():
        Events = []

        return Events

    def all_mod_TEST_Quests():
        Quests = []

        return Quests
```

## Add a general quest :

Create the folder `quests` and create the file of your quest `example_name.rpy` and refer to existing quests in the base game to write yours.

Then add your quest inside Quests = [] in registry.rpy

Do not forget to tag your quest as "addon" in Quest_type


## How to add a general event :

Inside the folder event create the file of your event `event_name.rpy` and refer to existing events in the base game to write yours.

Then add your event inside Events = [] in registry.rpy

________________________________________________________________________________________________________________________

# Add a new Item :

Inside the `mod_TEST/inventory` folder (if one of the element of this path doesn't exist create it) create a file `registry.rpy`

registry.rpy template :

```
init python:

    def all_mod_TEST_Items():
        Items = [
        ]

        return Items

init:
    default item_mod_TEST_paths = {
        
    }

```

Then inside `mod_TEST/inventory/items` add your item `item_name.rpy` and refer to existing items in the base game to write yours.
Once done add the `item_name(None)` inside `Items = []` in registry.rpy
Also add `"item_name" : "mods/mod_TEST/images/interface/items/item_name.webp"` to `item_mod_TEST_paths` in registry.rpy.
This will  get the item registered in the image path list for the inventory display.

You can create a “gift reaction” when the girls receive the new item you've made :
For every girl create a new folder inside `mods/mod_TEST/characters/character_name/inventory/items/item_name.rpy`
Refer the base game scripts to create the reactions. The labels must exist but can be left empty.
You can also create some special reaction with a file `mods/mod_TEST/characters/character_name/inventory/registry.rpy` if your item is a special item for this girl.

I you do that you MUST also add the gift threshold for each character in a new file `mods/mod_TEST/characters/character_name/definitions/gifts.rpy` :
```
init python:
    # Nouveaux éléments à ajouter
    Character_mod_TEST_gift_thresholds = {
        "item_name": [value, value]
    }
    
    Character_mod_TEST_gift_bonuses = {
        "item_name": [value, value]
    }
    
    Character_gift_thresholds.update(Character_mod_TEST2_gift_thresholds)
    Character_gift_bonuses.update(Character_mod_TEST2_gift_bonuses)
```

If you don't create a reaction, the characters will automatically refuse your gift.


________________________________________________________________________________________________________________________
