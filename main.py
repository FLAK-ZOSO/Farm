#!/usr/bin/python3
import account as a
import data as d
import objects as o
import sys
import text as t


# Import the Tkinter login validator v0.0.4 by FLAK-ZOSO
sys.path.insert(0, "Login-validator-0.0.4") # This is still not used


animals = {"Sheep", "Hen", "Cock"}
buildings = {"Enclosure", "Field"}
crops = {"Grain", "Carrot"}


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
    print(f"    {len(dictionary.keys())+1}) Back to menu\n")
    answer = input("> ")
    try:
        farm(user, dictionary[answer])
    except KeyError:
        main(user)


def farm(user: str, game: str) -> None:
    a.cls.main()
    dat = d.game(user, game)
    print(f"Welcome to {game}")
    print(t.information_string(dat))
    print("1) Silos")
    print("2) Enclosures")
    print("3) Fields")
    print("4) Shop")
    print("5) Back to my games\n")
    while True:
        answer = input('> ')
        if (answer == '1'):
            silos(user, game)
            return
        elif (answer == '2'):
            enclosures(user, game)
            return
        elif (answer == '3'):
            fields(user, game)
            return
        elif (answer == '4'):
            shop(user, game)
            return
        elif (answer == '5'):
            games(user)
            return


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
    ...


def fields(user: str, game: str) -> None:
    ...


def shop(user: str, game: str) -> None:
    a.cls.main()
    dat = d.shop(user, game)
    prices = d.prices()
    output, purchasables, soldables = t.shop_string(dat, prices)
    print(output)
    choice = input("> ")
    try:
        if (int(choice) <= len(purchasables.keys())): # They want to buy
            item = purchasables[choice]
            buy(user, game, item)
        elif (int(choice) > len(purchasables.keys())): # They want to sell
            item = soldables[choice]
            sell(user, game, item)
    except (KeyError, ValueError):
        farm(user, game)


def sell(user: str, game: str, item: str) -> int:
    ...


def buy(user: str, game: str, item: str) -> int:
    a.cls.main()
    # Output
    print(f"{item.upper()}")
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
                    left = left_ - quantity
                    quantity -= left_
                    enclosure[item] += left_
                    enclosure["Capacity left"] = left
            if (quantity): # Still animals without space
                print(f"There are still {quantity} {item}s without space")
                print(f"You have had your {quantity*price}$ back")
                dat["Money"] += quantity*price
                input("> ")
            dat["Shop"]["Availability"]["Buildings"][item] -= (quantity_ - quantity)
        elif (item in buildings):
            dat["Money"] -= quantity*price
            dat["Shop"]["Availability"]["Buildings"][item] -= quantity
            dat[f"{item}s"].append(o.new(item))
        dat["Shop"]["Stats"]["Bought"][item] += quantity
        d.encode_game(user, game, dat)
    shop(user, game)


if (__name__ == '__main__'):
    a.cls.main()
    print("Welcome to Farm")
    if (len(sys.argv) >= 2):
        main(sys.argv[1])
    else:
        main(a.main())