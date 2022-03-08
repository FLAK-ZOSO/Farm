#!/usr/bin/python3


new_game = {
    "Money": 10000,
    "Experience": 0,
    "Level": 0,
    "Silos": {
        "Capacity": 150,
        "Content": {
            "Grain": 10,
            "Carrots": 0
        }
    },
    "Enclosures": [
        {
            "Capacity": 6,
            "Capacity left": 6,
            "Sheeps": 0,
            "Hens": 0,
            "Content": {
                "Eggs": [],
                "Wool": []
            }
        }
    ],
    "Fields": [
        {
            "Grain": [],
            "Carrots": []
        },
        {
            "Grain": [],
            "Carrots": []
        }
    ],
    "Shop": {
        "Stats": {
            "Sold": {
                "Grain": 0,
                "Carrots": 0,
                "Sheep": 0
            },
            "Bought": {
                "Sheep": 0,
                "Hen": 0,
                "Field": 0,
                "Enclosure": 0
            }
        },
        "Availability": {
            "Animals": {
                "Sheep": 2,
                "Hen": 2
            },
            "Buildings": {
                "Field": 1,
                "Enclosure": 1
            }
        }
    }
}


def new(item: str) -> (dict | list):
    if (item.lower() in ["enclosure", "enclosures"]):
        return {
            "Capacity": 6, "Capacity left": 6, 
            "Sheeps": 0, "Hens": 0,
            "Content": {
                "Eggs": [], "Wool": []
            }
        }
    if (item.lower() in ["field", "fields"]):
        return {"Grain": [], "Carrots": []}