#!/usr/bin/python3
import json
import text as t


def encode_game(user: str, game: str, data: dict) -> None:
    with open("account.json", 'r') as accounts:
        data_: dict = json.load(accounts)
    data_[user]["Games"][game] = data
    with open("account.json", 'w') as accounts:
        json.dump(data_, accounts, indent=4)


def games_list(user: str) -> list[str]:
    with open("account.json", 'r') as accounts:
        data: dict = json.load(accounts)
    return data[user]["Games"].keys()


def game(user: str, game: str) -> dict:
    with open("account.json", 'r') as accounts:
        data: dict = json.load(accounts)
    return data[user]["Games"][game]


def silos(user: str, game: str) -> dict:
    with open("account.json", 'r') as accounts:
        data: dict = json.load(accounts)
    return data[user]["Games"][game]["Silos"]


def shop(user: str, game: str) -> dict:
    with open("account.json", 'r') as accounts:
        data: dict = json.load(accounts)
    return data[user]["Games"][game]["Shop"]


def money(user: str, game: str) -> int:
    with open("account.json", 'r') as accounts:
        data: dict = json.load(accounts)
    return data[user]["Games"][game]["Money"]


def prices() -> dict:
    with open("shop.json", 'r') as prices_:
        data: dict = json.load(prices_)
    return data