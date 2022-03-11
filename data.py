#!/usr/bin/python3
import json


def encode_game(user: str, game: str, data: dict) -> None:
    with open("account.json", 'r') as accounts:
        data_: dict = json.load(accounts)
    data_[user]["Games"][game] = data
    with open("account.json", 'w') as accounts:
        json.dump(data_, accounts, indent=4)


def encode_user(user: str, data: dict) -> None:
    with open("account.json", 'r') as accounts:
        data_: dict = json.load(accounts)
    data_[user] = data
    with open("account.json", 'w') as accounts:
        json.dump(data_, accounts, indent=4)


def user_(user: str) -> dict:
    with open("account.json", 'r') as accounts:
        data: dict = json.load(accounts)
    return data[user]


def games_list(user: str) -> list[str]:
    return games(user).keys()


def games(user: str) -> dict:
    return user_(user)["Games"]


def game(user: str, game: str) -> dict:
    return games(user)[game]


def silos(user: str, game_: str) -> dict:
    return game(user, game_)["Silos"]


def enclosures(user: str, game_: str) -> list[dict]:
    return game(user, game_)["Enclosures"]


def fields(user: str, game_: str) -> list[dict]:
    return game(user, game_)["Fields"]


def shop(user: str, game_: str) -> dict:
    return game(user, game_)["Shop"]


def money(user: str, game_: str) -> int:
    return game(user, game_)["Money"]


def prices() -> dict:
    with open("shop.json", 'r') as prices_:
        data: dict = json.load(prices_)
    return data


def times() -> dict[str, int]:
    with open("time.json", 'r') as times_:
        data: dict[str, int] = json.load(times_)
    return data


def symbols() -> dict[str, str]:
    with open("symbols.json", 'r') as symbols_:
        data: dict[str, str] = json.load(symbols_)
    return data


def animal_product() -> dict[str, str]:
    with open("animal-product.json", 'r') as products_:
        data: dict[str, str] = json.load(products_)
    return data