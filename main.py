#!/usr/bin/python3
import account as a
import data as d
import sys
import text as t


# Import the Tkinter login validator v0.0.4 by FLAK-ZOSO
sys.path.insert(0, "Login-validator-0.0.4") # This is still not used


def main(user: str) -> None:
    while (True):
        a.cls.main()
        print(t.menu)
        print(f"\n{user}, welcome to the menu, make your choice.\n")
        choice = input("> ")
        if (choice == '1'):
            games(user)
        elif (choice == '2'):
            quit()


def games(user: str) -> None:
    a.cls.main()
    print(t.games)
    for index, value in enumerate(g_l := d.games_list(user)):
        print(f"{index+1}) {value}")
    dictionary = {str(index+1): value for index, value in enumerate(g_l)}
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
    print("4) Back to my games\n")
    while True:
        answer = input('> ')
        if (answer == '1'):
            silos(user, game)
            break
        elif (answer == '2'):
            enclosures(user, game)
            break
        elif (answer == '3'):
            fields(user, game)
            break
        elif (answer == '4'):
            games(user)
            break


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
    sell(user, game, "Silos", good)
    


def enclosures(user: str, game: str) -> None:
    ...


def fields(user: str, game: str) -> None:
    ...


def sell(user: str, game: str, container: str, good: str) -> int:
    ...


if (__name__ == '__main__'):
    a.cls.main()
    print("Welcome to Farm")
    if (len(sys.argv) >= 2):
        main(sys.argv[1])
    else:
        main(a.main())