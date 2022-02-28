menu = """
    ||\\\\    //|| |||||||| ||\\\\    || ||      ||
    || \\\\  // || ||       || \\\\   || ||      ||
    ||  \\\\//  || ||||||   ||  \\\\  || ||      ||
    ||        || ||       ||   \\\\ || ||      ||
    ||        || |||||||| ||    \\\\|| ||||||||||

    -----------------------------------------------

    1) Games
    2) Quit
"""


games = """
    |||||||||     //\\\\     ||\\\\    //|| ||||||||| ||||||||||
    ||     __    //  \\\\    || \\\\  // || |||       |||
    ||     ||   //    \\\\   ||  \\\\//  || ||||||    ||||||||||
    ||     ||  //||||||\\\\  ||        || |||              |||
    ||||||||| //        \\\\ ||        || ||||||||| ||||||||||
    
    ------------------------------------------------------------
"""


silos = """
    |||||||||| ||||| |||       |||||||||| ||||||||||
    |||         |||  |||       |||    ||| ||
    ||||||||||  |||  |||       |||    ||| ||||||||||
           |||  |||  |||       |||    |||         ||
    |||||||||| ||||| ||||||||| |||||||||| ||||||||||

    -----------------------------------------------
"""


shop = """
    |||||||||| |||     ||| |||||||||| ||||||||||
    |||        |||     ||| |||    ||| |||    |||
    |||||||||| ||||||||||| |||    ||| ||||||||||
           ||| |||     ||| |||    ||| |||
    |||||||||| |||     ||| |||||||||| |||

    --------------------------------------------
"""


line = "-- - - - - - - - - - --"


def information_string(dat: dict) -> str:
    return f"""
{line}
Money: {dat["Money"]}
Experience: {dat["Experience"]}
Level: {dat["Level"]}
{line}
"""


def silos_string(dat: dict) -> tuple[str, dict]:
    capacity = dat["Capacity"]
    left = capacity-sum(dat["Content"].values())
    output = f"""
{silos}

    Capacity: {capacity}
    Capacity left: {left}

    {line}
"""
    content: dict = dat["Content"]
    dictionary = {str(index+1): value for index, value in enumerate(content.keys())}
    for index, key in dictionary.items():
        output += f"    {index}) {key}: {content[key]}\n"
    output += f"    {line}\n"
    output += f"    {len(dictionary.keys())+1}) Back to the farm\n"
    return output, dictionary


def shop_string(dat: dict, prices: dict) -> tuple[str, dict, dict]:
    output = shop
    output += "\n    BUY\n\n"
    purchasables = prices["Purchasables"]
    purchasables: dict = purchasables["Animals"] | purchasables["Buildings"]
    soldables: dict = prices["Soldables"]
    soldables: dict = soldables["Animals"] | soldables["Crops"]
    dictionary_p = {str(index+1): value for index, value in enumerate(purchasables.keys())}
    for index, key in dictionary_p.items():
        output += f"    {index}) {key} [{purchasables[key]}$]\n"
    output += "\n    SELL\n\n"
    dictionary_s = {str(index+1): value for index, value in enumerate(soldables.keys())}
    for index, key in dictionary_s.items():
        output += f"    {int(index)+len(dictionary_p)}) {key} [{soldables[key]}$]\n"
    return output, dictionary_p, dictionary_s