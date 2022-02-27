#!/usr/bin/python3
import json
from typing import Any
import exceptions as e
import password as p


def encodeDictionary(dictionary: dict[str, dict[str, Any]]):
    result = "{"
    for key, value in dictionary.items():
        result += f"""\n\t{json.dumps(key)}: {json.dumps(value)},"""
    result = result[:-1]
    result += "\n}"
    return result


def signUp(username: str, password: str, confirm: str) -> None:
    # Returns True when the sign-up was successful
    # Returns False when the account was already existing
    # Raises PasswordException when the password wasn't confirmed
    if (password != confirm):
        raise e.PasswordException

    with open('data.json', 'r') as data:
        new_dict = json.load(data)

    if (username in new_dict.keys()):
        raise e.AccountException
    new_dict[username] = {"password": p.encode_password(password), "logged-in": False}

    with open('data.json', 'w') as data:
        data.write(encodeDictionary(new_dict))


def login(username: str, password: str) -> bool:
    # Returns True when the login was successful
    # False when the account was already logged in
    # Raises an AccountException when the account doesn't exist
    # Raises a PasswordException when the password is wrong
    with open('data.json', 'r') as data:
        new_dict = json.load(data)

    if (not username in new_dict.keys()):
        raise e.AccountException
    if (new_dict[username]["logged-in"]):
        return False
    if (password != p.decode_password(new_dict[username]["password"])):
        raise e.PasswordException
    new_dict[username]["logged-in"] = True

    with open('data.json', 'w') as data:
        data.write(encodeDictionary(new_dict))
    return True


def logout(username: str) -> bool:
    with open('data.json', 'r') as data:
        new_dict = json.load(data)
    try:
        if (not new_dict[username]["logged-in"]):
            return False
    except KeyError:
        raise e.AccountException
    new_dict[username]["logged-in"] = False
    with open('data.json', 'w') as data:
        data.write(encodeDictionary(new_dict))
    return True


def isLogged(user: str) -> bool:
    with open('data.json', 'r') as data:
        try:
            return json.load(data)[user]['logged-in']
        except BaseException:
            return False