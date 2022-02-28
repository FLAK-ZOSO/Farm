#!/usr/bin/python3


def new(item: str) -> (dict | list):
    if (item.lower() in ["enclosure", "enclosures"]):
        return {
            "Capacity": 0, "Capacity left": 6, 
            "Sheeps": 0, "Hens": 0, "Cocks": 0, 
            "Content": {
                "Eggs": [], "Fertilized eggs": [],"Wool": []
            }
        }
    if (item.lower() in ["field", "fields"]):
        return {"Grain": [], "Carrots": []}