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
    ||     __    //  \\\\    || \\\\  // || ||        ||
    ||     ||   //    \\\\   ||  \\\\//  || ||||||    ||||||||||
    ||     ||  //||||||\\\\  ||        || ||                ||
    ||||||||| //        \\\\ ||        || ||||||||| ||||||||||
    
    ------------------------------------------------------------
"""


silos = """
    |||||||||| |||| ||        |||||||||| ||||||||||
    ||          ||  ||        ||      || ||
    ||||||||||  ||  ||        ||      || ||||||||||
            ||  ||  ||        ||      ||         ||
    |||||||||| |||| ||||||||| |||||||||| ||||||||||
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


def silos_string(dat: dict) -> str:
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