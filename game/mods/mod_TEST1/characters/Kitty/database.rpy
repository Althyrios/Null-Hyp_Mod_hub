label update_Kitty_database:
    $ Kitty.database["stats"] = [
        "Name: Kitty Pryde\nCodename: Shadowcat\nAge: 18\nDoB: \nHeight: \"\nHair: Brown\nEyes: Brown\nPowers: "]

    $ Kitty.database["description"] = [
        ""]

    $ Kitty.database["study_materials"] = [
        "RECOMMENDED STUDY MATERIALS\n\n- "]

    $ Kitty.database["wiki"] = [
    "\n\n"]

    $ Kitty.database["comments"] = [
        f"{Kitty.call_sign}: ",
        f"{Kitty.call_sign}: ",
        f"{Kitty.call_sign}: "]

    $ Kitty.database["quirks"] = {}

    if Kitty.check_traits("customizable_quirks") or (Kitty.History.check("submissiveness_encouraged") + Kitty.History.check("submissiveness_discouraged") >= 2):
        $ Kitty.database["quirks"].update({
            "Quirk 1 - Submissiveness": ""})
    
    if Kitty.check_traits("customizable_quirks") or (Kitty.History.check("masochism_encouraged") + Kitty.History.check("masochism_discouraged") >= 2):
        $ Kitty.database["quirks"].update({
            "Quirk 2 - Masochism": ""})


    return