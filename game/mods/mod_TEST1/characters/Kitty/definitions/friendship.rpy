init -1:

    define Kitty_friendship_thresholds = {
        "Rogue": [0, 20, 40],
        "Laura": [0, 20, 40],
        "Jean": [0, 20, 40]}

    define Kitty_friendship_tiers = {
        "Rogue": [0, 1, 2, 3],
        "Laura": [0, 1, 2, 3],
        "Jean": [-1, 0, 1, 2]}

    
    $ Jean_friendship_thresholds["Kitty"] = [0, 20, 40]
    $ Jean_friendship_tiers["Kitty"] = [-1, 0, 1, 2]

    $ Rogue_friendship_thresholds["Kitty"] = [0, 20, 40]
    $ Rogue_friendship_tiers["Kitty"] = [0, 1, 2, 3]

    $ Laura_friendship_thresholds["Kitty"] = [0, 20, 40]
    $ Laura_friendship_tiers["Kitty"] = [0, 1, 2, 3]