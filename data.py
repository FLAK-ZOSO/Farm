#!/usr/bin/python3
import json
import text as t


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