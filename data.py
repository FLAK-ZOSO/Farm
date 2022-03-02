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


def silos(user: str, game: str) -> dict:
    return game(user, game)["Silos"]


def shop(user: str, game: str) -> dict:
    return game(user, game)["Shop"]


def money(user: str, game: str) -> int:
    return game(user, game)["Money"]


def prices() -> dict:
    with open("shop.json", 'r') as prices_:
        data: dict = json.load(prices_)
    return data