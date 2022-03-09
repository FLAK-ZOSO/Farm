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


new_game = """
    |||\\\\\\    ||| |||||||||| \\\\\\                  ///           ||||||||||||     ///\\\\\\     |||\\\\    ///||| ||||||||||
    ||| \\\\\\   ||| |||         \\\\\\                ///            |||             ///  \\\\\\    ||| \\\\  /// ||| |||
    |||  \\\\\\  ||| ||||||       \\\\\\    ///\\\\\\    ///   |||||||   |||      ___   ///    \\\\\\   |||  \\\\///  ||| ||||||
    |||   \\\\\\ ||| |||           \\\\\\  ///  \\\\\\  ///              |||      |||  ///||||||\\\\\\  |||         ||| |||
    |||    \\\\\\||| ||||||||||     \\\\\\///    \\\\\\///               |||||||||||| ///        \\\\\\ |||         ||| ||||||||||

    ------------------------------------------------------------------------------------------------------------------------------
"""


enclosures = """
    |||||||||||||||||||||||||||||||||||||||    |||||||||||||||||||||||||||||||||||||||
    |||         |||         |||         |||    |||         |||         |||         |||
    |||         |||         |||         |||    |||         |||         |||         |||
    |||         |||         |||         |||    |||         |||         |||         |||
    |||         |||         |||         |||    |||         |||         |||         |||
    |||||||||||||||||||||||||||||||||||||||    |||||||||||||||||||||||||||||||||||||||
    |||         |||         |||         |||    |||         |||         |||         |||
    |||         |||         |||         |||    |||         |||         |||         |||
    |||         |||         |||         |||    |||         |||         |||         |||
    |||         |||         |||         |||    |||         |||         |||         |||
    |||||||||||||||||||||||||||||||||||||||    |||||||||||||||||||||||||||||||||||||||
    
    ----------------------------------------------------------------------------------\n
"""


enclosure = """
    |||||||||  |||||||||  |||||||||
    ||| {} |||  ||| {} |||  ||| {} |||
    |||||||||  |||||||||  |||||||||
    
    |||||||||  |||||||||  |||||||||
    ||| {} |||  ||| {} |||  ||| {} |||
    |||||||||  |||||||||  |||||||||
"""

fields = """
    |||||||||||||||||||||||||||    |||||||||||||||||||||||||||
    |||         |||         |||    |||         |||         |||
    |||         |||         |||    |||         |||         |||
    |||         |||         |||    |||         |||         |||
    |||         |||         |||    |||         |||         |||
    |||||||||||||||||||||||||||    |||||||||||||||||||||||||||
    |||         |||         |||    |||         |||         |||
    |||         |||         |||    |||         |||         |||
    |||         |||         |||    |||         |||         |||
    |||         |||         |||    |||         |||         |||
    |||||||||||||||||||||||||||    |||||||||||||||||||||||||||
    
    |||||||||||  |||||  ||||||||||  |||        ||||||\\
    |||           |||   |||         |||        |||  \\|||\\
    |||||||       |||   |||||||     |||        |||    \\|||
    |||           |||   |||         |||        |||      |||
    |||          |||||  ||||||||||  |||||||||| |||||||||||| S
    
    ---------------------------------------------------------\n
"""


field = """
    |||||||||||||||||||||||||||    |||||||||||||||||||||||||||
    |||         |||         |||    |||         |||         |||
    |||         |||         |||    |||         |||         |||
    |||    {}    |||    {}    |||    |||    {}    |||    {}    |||
    |||         |||         |||    |||         |||         |||
    |||         |||         |||    |||         |||         |||
    |||||||||||||||||||||||||||    |||||||||||||||||||||||||||
    
    ----------------------------------------------------------\n
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


def enclosures_string(dat: dict) -> str:
    output = enclosures
    for i in range(1, len(dat)+1):
        if (i%10 == 1):
            suffix = 'st'
        elif (i%10 == 2):
            suffix = 'nd'
        else:
            suffix = 'th'
        output += f"    {i}) {i}{suffix} enclosure\n"
    output += f"    {line}\n"
    output += f"    {len(dat)+1}) Back to the farm\n"
    return output


def fields_string(dat: dict) -> str:
    output = fields
    for i in range(1, len(dat)+1):
        if (i%10 == 1):
            suffix = 'st'
        elif (i%10 == 2):
            suffix = 'nd'
        else:
            suffix = 'th'
        output += f"    {i}) {i}{suffix} field\n"
    output += f"    {line}\n"
    output += f"    {len(dat)+1}) Back to the farm\n"
    return output


def shop_string(dat: dict, prices: dict) -> tuple[str, dict, dict]:
    output = shop
    output += "\n    BUY\n\n"
    purchasables = prices["Purchasables"]
    purchasables: dict = purchasables["Animals"] | purchasables["Buildings"]
    soldables: dict = prices["Soldables"]
    soldables: dict = soldables["Animals"] | soldables["Crops"] | soldables["Animal products"]
    dictionary_p = {str(index+1): value for index, value in enumerate(purchasables.keys())}
    for index, key in dictionary_p.items():
        output += f"    {index}) {key} [{purchasables[key]}$]\n"
    output += "\n    SELL\n\n"
    dictionary_s = {str(index+1): value for index, value in enumerate(soldables.keys())}
    for index, key in dictionary_s.items():
        output += f"    {int(index)+len(dictionary_p)}) {key} [{soldables[key]}$]\n"
    return output, dictionary_p, dictionary_s