#!/usr/bin/python3
import account as a
import data as d
from datetime import datetime
import objects as o
import sys
import text as t


animals = {"Sheep", "Hen"}
buildings = {"Enclosure", "Field"}
crops = {"Grain", "Carrot"}
animal_products = {"Egg", "Eggs", "Wool"}


def main(user: str) -> None:
    while (True):
        a.cls.main()
        print(t.menu)
        print(f"\n  {user}, welcome to the menu, make your choice.")
        choice = input("> ")
        if (choice == '1'):
            games(user)
        elif (choice == '2'):
            quit()


def games(user: str) -> None:
    a.cls.main()
    print(t.games)
    for index, value in enumerate(g_l := d.games_list(user)):
        print(f"    {index+1}) {value}")
    dictionary = {str(index+1): value for index, value in enumerate(g_l)}
    print(f"    {len(dictionary)+1}) New Game")
    print(f"    {len(dictionary)+2}) Back to menu\n")
    answer = input("> ")
    try:
        farm(user, dictionary[answer])
    except KeyError:
        if (answer == str(len(dictionary)+1)):
            new_game(user)
        else:
            main(user)


def new_game(user: str) -> None:
    a.cls.main()
    dat = d.user_(user)
    print(t.new_game)
    input("> ")
    a.cls.main()
    choice = input("Farm name: ")
    while (choice.isspace() or not choice):
        choice = input("Farm name: ")
    dat["Games"][choice] = o.new_game
    d.encode_user(user, dat)


def farm(user: str, game: str) -> None:
    a.cls.main()
    dat = d.game(user, game)
    print(f"Welcome to {game}")
    print(t.information_string(dat))
    print("1) Silos")
    print("2) Enclosures")
    print("3) Fields")
    print("4) Shop")
    print("5) Refresh")
    print("6) Back to my games\n")
    answers = {
        '1': silos, '2': enclosures, '3': fields, 
        '4': shop, '5': refresh
    }
    while True:
        answer = input('> ')
        try:
            answers[answer](user, game)
        except KeyError:
            if (answer == '6'):
                games(user)
            continue
        break


def refresh(user: str, game: str) -> None:
    a.cls.main()
    print("Refreshing all... [    ]", end='\r')
    print("Checking delays... [-   ]", end='\r')
    delays = d.times()
    dat = d.game(user, game)
    print("Refreshing enclosures... [--  ]", end='\r')
    enclosures_: list[dict] = dat["Enclosures"]
    for enclosure in enclosures_:
        for product, products in enclosure["Content"].items():
            for index, i in enumerate(products):
                if (i == "[DONE]"):
                    continue
                delta = (datetime.now() - datetime.fromisoformat(i)).total_seconds()
                if (delta >= delays[product]):
                    products[index] = "[DONE]"
    print("Refreshing fields... [--- ]          ", end='\r')
    fields_: list[dict[str, list]] = dat["Fields"]
    for field in fields_:
        for product, products in field.items():
            for index, i in enumerate (products):
                if (i == "[DONE]"):
                    continue
                delta = (datetime.now() - datetime.fromisoformat(i)).total_seconds()
                if (delta >= delays[product]):
                    products[index] = "[DONE]"
    print("Saving data... [----]      ", end='\r')
    d.encode_game(user, game, dat)
    farm(user, game)


def silos(user: str, game: str) -> None:
    a.cls.main()
    dat = d.silos(user, game)
    output, dictionary = t.silos_string(dat)
    print(output)
    choice = input("> ")
    try:
        good = dictionary[choice]
    except KeyError:
        farm(user, game)
        return
    # d.information(good)


def enclosures(user: str, game: str) -> None:
    a.cls.main()
    dat = d.game(user, game)
    print(t.enclosures_string(dat["Enclosures"]))
    choice = input("\n> ")
    try:
        dat["Enclosures"][int(choice)-1]
    except (KeyError, ValueError):
        farm(user, game)
        return
    enclosure(user, game, int(choice)-1)


def enclosure(user: str, game: str, n: int) -> None:
    a.cls.main()
    dat = d.game(user, game)
    my_enclosure: dict[str, int | dict[str, list[str]]] = dat["Enclosures"][n]
    output = t.enclosure
    symbols = d.symbols()
    items: list[str] = []
    formatted = []
    for key, value in my_enclosure.items():
        if (key in symbols.keys()):
            for i in range(value):
                items.append(key.removesuffix('s'))
                formatted.append(symbols[key])
    for i in range(6):
        try:
            formatted[i]
        except IndexError:
            formatted.append(' ')
    print(output.format(*formatted))
    for index, value in enumerate(items):
        print(f"{index+1}) {value}")
    print(f"\n{len(items)+1}) See content")
    choice = input("\n> ")
    try:
        animal: str = items[int(choice)-1]
    except (KeyError, ValueError, IndexError):
        if (choice == str(len(items)+1)):
            a.cls.main()
            print(output.format(*formatted))
            times = d.times()
            for key, value in my_enclosure["Content"].items():
                print(key.upper())
                if (not len(value)):
                    print("...\n")
                    continue
                for value_ in value:
                    if (value_ == "[DONE]"):
                        print(f"-> {symbols[key]}") # Error raised here while debugging
                    else:
                        delta = (datetime.now() - datetime.fromisoformat(value_)).total_seconds()
                        print(f"-> {times[key] - int(delta)}s")
            print(f"\n1) Collect all\n2) Refresh\n3) Back to enclosure")
            choice = input("\n> ")
            if (choice == '1'):
                for animal in animals:
                    collect_animal(user, game, n, animal)
            elif (choice == '2'):
                refresh(user, game)
            elif (choice == '3'):
                enclosure(user, game, n)
        enclosures(user, game)
        return
    a.cls.main()
    print(animal.upper())
    print("1) Collect product")
    print("2) Produce product")
    print("3) Sell animal")
    choice = input("\n> ")
    if (choice == '1'):
        collect_animal(user, game, n, animal)
    elif (choice == '2'):
        produce_animal(user, game, n, animal)
    elif (choice == '3'):
        sell(user, game, animal)
    input("> ")


def fields(user: str, game: str) -> None:
    a.cls.main()
    dat = d.game(user, game)
    print(t.fields_string(dat["Fields"]))
    choice = input("\n> ")
    try:
        dat["Fields"][int(choice)-1]
    except (KeyError, IndexError, ValueError):
        farm(user, game)
        return
    field(user, game, int(choice)-1)



def field(user: str, game: str, n: int) -> None:
    a.cls.main()
    dat = d.game(user, game)
    # The capacity of a field is set by default to 4 and can't be incremented
    my_field: dict[str, list[str]] = dat["Fields"][n]
    output = t.field
    symbols = d.symbols()
    items: list[str] = []
    formatted = []
    for key, value in my_field.items():
        if (key in symbols.keys()):
            for i in range(len(value)):
                items.append(key.removesuffix('s'))
                formatted.append(symbols[key])
    for i in range(4):
        try:
            formatted[i]
        except IndexError:
            formatted.append(' ')
    print(output.format(*formatted))
    global crops
    crops_ = list(crops)
    for index, value in enumerate(crops_):
        print(f"{index+1}) {value}")
    print(f"\n{len(crops_)+1}) See content")
    answer = input("> ")
    try:
        crop = crops_[int(answer)-1]
        a.cls.main()
        print(crop.upper())
        print("1) Collect product")
        print("2) Produce product")
        print("3) Sell crop")
        choice = input("\n> ")
        if (choice == '1'):
            collect_crop(user, game, n, crop)
        elif (choice == '2'):
            produce_crop(user, game, n, crop)
        elif (choice == '3'):
            sell(user, game, crop)
    except (KeyError, IndexError):
        if (answer == str(len(crops_)+1)):
            a.cls.main()
            times = d.times()
            for key, value in my_field.items():
                print(key.upper())
                if (not len(value)):
                    print("...\n")
                    continue
                for value_ in value:
                    if (value_ == "[DONE]"):
                        print(f"-> {symbols[key]}")
                    else:
                        delta = (datetime.now() - datetime.fromisoformat(value_)).total_seconds()
                        print(f"-> {times[key] - int(delta)}s")
            print(f"\n1) Collect all\n2) Refresh\n3) Back to fields")
            choice = input("\n> ")
            if (choice == '1'):
                for crop in crops:
                    collect_crop(user, game, n, crop)
            elif (choice == '2'):
                refresh(user, game)
            elif (choice == '3'):
                fields(user, game)
    except ValueError:
        return
    input("\n> ")


def collect_crop(user: str, game: str, n: int, crop: str) -> None:
    ...


def produce_crop(user: str, game: str, n: int, crop: str) -> None:
    a.cls.main()
    field_: dict[str, list] = d.fields(user, game)[n]
    plural = f"{crop}s" if (crop.lower() in ["carrot"]) else crop
    if (sum([len(value) for value in field_.values()]) >= 4):
        print(f"Your field is already busy")
        input("> ")
        return
    field_[plural].append(datetime.now().isoformat())
    print(f"Your {crop} is growing")
    dat = d.game(user, game)
    dat["Fields"][n] = field_
    d.encode_game(user, game, dat)
    input("> ")


def produce_animal(user: str, game: str, n: int, animal: str) -> None:
    a.cls.main()
    enclosure_: dict = d.enclosures(user, game)[n]
    product = d.animal_product()[animal]
    content: dict[str, list[str]] = enclosure_["Content"]
    plural = f"{product}s" if (product.lower() in ["egg"]) else product
    if (len(content[plural]) >= enclosure_[f"{animal}s"]):
        print(f"Your {animal} is already busy")
        input("> ")
        return
    content[plural].append(datetime.now().isoformat())
    print(f"Your {animal} is producing {product}")
    dat = d.game(user, game)
    dat["Enclosures"][n]["Content"] = content
    d.encode_game(user, game, dat)
    input("> ")


def collect_animal(user: str, game: str, n: int, animal: str) -> None:
    a.cls.main()
    enclosure_: dict = d.enclosures(user, game)[n]
    animal_product = d.animal_product()
    product = animal_product[animal]
    silo: dict[str, str | dict[str, int]] = d.silos(user, game)
    content: dict[str, list[str]] = enclosure_["Content"]
    plural = f"{product}s" if (product.lower() in ["egg"]) else product
    if (content[plural]): # The list of the products isn't empty
        if ("[DONE]" in content[plural]): # The error for sheeps came from here, since we don't have "Wools"
            if (silo["Capacity"] - sum(silo["Content"].values()) > 0):
                content[plural].remove("[DONE]")
                try:
                    silo["Content"][plural] += 1
                except KeyError:
                    silo["Content"][plural] = 1
            else:
                print(f"No space in the silos for your {product}")
                input("> ")
                silos(user, game)
                return
        else:
            print(f"No {product} is ready")
    else:
        print(f"No {product} is being produced")
    dat = d.game(user, game)
    dat["Silos"] = silo
    dat["Enclosures"][n]["Content"] = content
    d.encode_game(user, game, dat)
    input("> ")


def shop(user: str, game: str) -> None:
    a.cls.main()
    dat = d.shop(user, game)
    prices = d.prices()
    output, purchasables, soldables = t.shop_string(dat, prices)
    print(output)
    choice = input("> ")
    try:
        lenght = len(purchasables.keys())
        if (int(choice) <= lenght): # They want to buy
            item = purchasables[choice]
            buy(user, game, item)
        elif (int(choice) > lenght): # They want to sell
            item = soldables[str(int(choice)-lenght)]
            sell(user, game, item)
    except (KeyError, ValueError):
        farm(user, game)


def sell(user: str, game: str, item: str) -> int:
    a.cls.main()
    dat = d.game(user, game)
    # Availability
    if (item in animals):
        items = [enclosure[f"{item}s"] for enclosure in dat["Enclosures"]]
        availability = sum(items)
        price = d.prices()["Soldables"]["Animals"][item]
    elif (item in crops):
        availability = dat["Silos"]["Content"][item]
        price = d.prices()["Soldables"]["Crops"][item]
    elif (item in animal_products):
        plural = f"{item}s" if (item.lower() in ("egg",)) else item
        availability = dat["Silos"]["Content"][plural]
        price = d.prices()["Soldables"]["Animal products"][plural]
    print(item.upper())
    print(f"Availability: {availability}")
    print(f"Price: {price}$\n")
    while (True):
        quantity = input("Quantity -> ")
        try:
            quantity = int(quantity)
        except ValueError:
            continue
        break
    quantity: int = min([quantity, availability])
    total = price*quantity
    print(f"\nQuantity: {quantity}\nTotal price: {total}")
    print(f"\nConfirm? (y/n)")
    if (input("> ").lower() == 'y'):
        try:
            dat["Shop"]["Stats"]["Sold"][item] += quantity
        except KeyError:
            dat["Shop"]["Stats"]["Sold"][item] = quantity
        if (item in animals):
            for enclosure in dat["Enclosures"]:
                if (quantity): # Animals you need to sell them all
                    if (enclosure[f"{item}s"] >= quantity):
                        anim = enclosure[f"{item}s"]
                        enclosure[f"{item}s"] -= quantity
                        enclosure["Capacity left"] += (anim - quantity)
                        quantity = 0
                        break
                    quantity -= enclosure[f"{item}s"]
                    enclosure["Capacity left"] += enclosure[f"{item}s"]
                    enclosure[f"{item}s"] = 0
        elif (item in crops or item in animal_products):
            dat["Silos"]["Content"][item] -= quantity
        dat["Money"] += total
    d.encode_game(user, game, dat)
    shop(user, game)


def buy(user: str, game: str, item: str) -> int:
    a.cls.main()
    # Output
    print(item.upper())
    # Availability
    shop_ = d.shop(user, game)
    shop_: dict[str, dict] = shop_["Availability"]
    for category in shop_.values():
        if (item in category.keys()):
            shop_: dict = category
            break
    availability = shop_[item]
    # Price
    prices_ = d.prices()
    prices_: dict[str, dict] = prices_["Purchasables"]
    for category in prices_.values():
        if (item in category.keys()):
            prices_: dict[str, int] = category
            break
    price: int = prices_[item]
    print(f"Availability: {availability}")
    print(f"Price: {price}$\n")
    while (True):
        quantity = input("Quantity -> ")
        try:
            quantity = int(quantity)
        except ValueError:
            continue
        else:
            break
    quantity: int = min([quantity, availability])
    total = price*quantity
    print(f"\nQuantity: {quantity}\nTotal price: {total}")
    print(f"\nConfirm? (y/n)")
    answer = input("> ")
    if (answer.lower() == 'y'):
        money = d.money(user, game)
        if (total > money):
            print(f"{money} aren't enough, you need {total}")
            quantity = money//price
            total = total*price
            print(f"Do you want to buy {quantity} {item}s for {total}? (y/n)")
            if (input("> ").lower() != 'y'):
                shop(user, game)
        dat = d.game(user, game)
        dat["Money"] -= total
        if (item in animals):
            quantity_ = quantity
            for enclosure in dat["Enclosures"]:
                left_ = enclosure["Capacity left"]
                if (left_): # Space left for the new animal
                    if (quantity > left_): # Not enough space in this enclosure
                        quantity -= left_
                        enclosure[f"{item}s"] += left_
                        enclosure["Capacity left"] = 0
                    else:
                        enclosure[f"{item}s"] += quantity
                        enclosure["Capacity left"] -= quantity
                        quantity = 0
                        break
            if (quantity > 0): # Still animals without space
                print(f"There are still {quantity} {item}s without space")
                print(f"You have had your {quantity*price}$ back")
                dat["Money"] += quantity*price
                input("> ")
            dat["Shop"]["Availability"]["Animals"][item] -= (quantity_ - quantity)
        elif (item in buildings):
            dat["Money"] -= quantity*price
            dat["Shop"]["Availability"]["Buildings"][item] -= quantity
            for _ in range(quantity):
                dat[f"{item}s"].append(o.new(item))
        dat["Shop"]["Stats"]["Bought"][item] += quantity
        d.encode_game(user, game, dat)
        input("> ")
    shop(user, game)


if (__name__ == '__main__'):
    a.cls.main()
    print("Welcome to Farm")
    if (len(sys.argv) >= 2):
        main(sys.argv[1])
    else:
        main(a.main())