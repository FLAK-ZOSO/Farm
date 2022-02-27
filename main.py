#!/usr/bin/python3
import account as a
import json
import sys


# Import the Tkinter login validator v0.0.4 by FLAK-ZOSO
sys.path.insert(0, "Login-validator-0.0.4") # This is still not used


def main(user: str) -> None:
    ...


if (__name__ == '__main__'):
    print("Welcome to Farm")
    if (len(sys.argv) >= 2):
        main(sys.argv[1])
    else:
        main(a.main())