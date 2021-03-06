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


def points_level() -> list[list[int]]:
    with open("points-level.json", 'r') as level_:
        data: list[list[int, int]] = json.load(level_)
    return data


def community_shop() -> dict[str, dict[str, list[dict[str, str | int]]]]:
    with open("community_shop.json", 'r') as shop_:
        data: dict = json.load(shop_)
    return data


def encode_community_shop(data: dict[str, dict[str, list[dict[str, str | int]]]]) -> None:
    with open("community_shop.json", 'w') as shop_:
        json.dump(data, shop_, indent=4)