#!/usr/bin/python3
import cleanscreen as cls
import getpass
import json
import password as p


def main() -> str:
    print("\nChoose your option:")
    print("\t1) Sign Up")
    print("\t2) Sign In\n")
    while (True):
        choice = input("> ")
        if (choice == '1'):
            user = sign_up()
            if (not user):
                quit()
            return user
        elif (choice == '2'):
            user = sign_in()
            if (not user):
                quit()
            return user
        else:
            print(f"Option {choice} wasn't recognized")
            continue


def sign_up() -> str:
    cls.main()
    with open("account.json", 'r') as accounts:
        data: dict = json.load(accounts)
    username = input("Username: ")
    if (username in data.keys()):
        print("The account already exists")
        return ''
    password = getpass.getpass("Password: ")
    confirm = getpass.getpass("Confirm Password: ")
    if (confirm != password):
        print("The confirmed password doesn't match")
        return ''
    initialize(data, username, password)
    with open("account.json", 'w') as accounts:
        json.dump(data, accounts, indent=4)
    return username


def sign_in() -> str:
    cls.main()
    with open("account.json", 'r') as accounts:
        data: dict = json.load(accounts)
    username = input("Username: ")
    if (username not in data.keys()):
        print("The account doesn't exist")
        return ''
    password = getpass.getpass("Password: ")
    if (p.decode_password(data[username]["Password"]) == password):
        return username
    print("The password doesn't match")


def initialize(data: dict, username: str, password: str) -> None:
    # No need for return, dicts are passed by reference by default
    data[username] = {
        "Password": f"{p.encode_password(password)}",
        "Games": {}
    }