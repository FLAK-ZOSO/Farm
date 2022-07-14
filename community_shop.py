#!/usr/bin/python3
import asyncio
import data
import os
import text


class Constants:
    animals = {"Sheeps", "Hens"}
    crops = {"Grain", "Carrots"}
    animal_products = {"Eggs", "Wool"}
    elements = animals | crops | animal_products


class Market:
    def __init__(self) -> None:
        self.data = data.community_shop()

    def __str__(self) -> str:
        return text.community_shop_string(data.community_shop(), '')

    def __len__(self) -> int:
        return len(self.data)
    
    async def _update(self) -> None:
        while (True):
            if (self.data != data.community_shop()):
                data.encode_community_shop(self.data)
            await asyncio.sleep(1)


class MarketForUser:
    def __init__(self, market: Market, user: str, game: str) -> None:
        self.market = market
        self.user = user
        self.game = game

    def __str__(self) -> str:
        return text.community_shop_string(self.market.data, self.game)

    def __call__(self) -> None:
        self.__mainloop()

    def __choice() -> bool:
        os.system('cls')
        print("1) Take me to my market")
        print("2) Take me to the common market")
        answer = input("> ")
        while (answer not in {'1', '2'}):
            answer = input("> ")
        return answer == '2' # 2 => True, 1 => False

    def __mainloop(self) -> None:
        if (self.__choice()):
            while True:
                os.system('cls')
                print(self, '\n')
        else:
            SalesStall(self.market, self.user, self.game)()


class SalesStall:
    def __init__(self, market: Market, user: str, game: str) -> None:
        self.user = user
        self.game = game
        self.market = market
        self.content = self.market.data[self.game]
    
    def __str__(self) -> str:
        return f"""
        Welcome to your sales stall!

        You have {data.money(self.user, self.game)}$
        You currently have {len(self.content["Offers"])} offers
        You currently have {len(self.content["Requests"])} requests
    """

    def __call__(self) -> None:
        self.__mainloop()

    def __choice(self) -> int:
        os.system('cls')
        print(self, '\n')
        print("1) Go to offers")
        print("2) Go to requests")
        print("3) Go back")
        answer = input("> ")
        while (answer not in {'1', '2', '3'}):
            answer = input("> ")
        if (answer == '3'):
            return 2
        return 1 if answer == '1' else 0  

    def __mainloop(self) -> None:
        while True:
            os.system()
            print(self, '\n')
            if (choice := self.__choice()):
                if (choice == 2):
                    break
                Offers(self, self.user, self.game)()
            else:
                Requests(self, self.user, self.game)()


class Offers:
    def __init__(self, sales_stall: SalesStall, user: str, game: str) -> None:
        self.user = user
        self.game = game
        self.sales_stall = sales_stall
        self.list = self.sales_stall.content["Offers"]

    def __str__(self) -> str:
        output = f"Your offers: "
        for x, i in enumerate(self.list):
            output += f'{x+1}) {i["Quantity"]} {i["Item"]} for {i["Price"]}$ each'
        return output

    def __call__(self) -> None:
        self.__mainloop()

    def __choice(self) -> int:
        os.system('cls')
        print(self, '\n')
        print("1) Make an offer")
        print("2) Delete an offer")
        print("3) Go back")
        answer = input("> ")
        while (answer not in {'1', '2', '3'}):
            answer = input("> ")
        if (answer == '3'):
            return 2
        return 1 if answer == '1' else 0

    def __delete_offer(self) -> None:
        os.system('cls')
        print(self, '\n')
        print("Which offer do you want to delete?")
        answer = input("> ")
        while (True):
            while (not answer or answer.isspace()):
                answer = input("> ")
            try:
                choice = int(choice)-1 # choice is now the index of the offer to delete
            except ValueError:
                continue
            if (choice <= len(self.list) and choice >= 0):
                break
        self.list.pop(choice)
        print("Offer deleted")
        input("> ")
        # Don't need to encode it back since it's already been encoded by the market

    def __make_offer(self) -> None:
        os.system('cls')
        print("What do you want to offer? (Use plural where possible)")
        item = input("> ")
        while (item.capitalize() not in Constants.elements):
            item = input("> ")
        print(f"How many {item} do you want to offer?")
        while (True):
            try:
                quantity = int(input("> "))
                if (quantity <= 0):
                    continue
                break
            except ValueError:
                continue
        print(f"How much do you want to earn for each {item.lower().removesuffix('s')}?")
        price = input("> ")
        self.list.append({"Item": item, "Quantity": quantity, "Price": price})
        Offer(self.list[-1])()

    def __mainloop(self) -> None:
        while True:
            os.system('cls')
            print(self, '\n')
            if (choice := self.__choice()):
                if (choice == 2):
                    break
                self.__delete_offer()
            else:
                self.__make_offer()


class Requests:
    def __init__(self, sales_stall: SalesStall, user: str, game: str) -> None:
        self.user = user
        self.game = game
        self.sales_stall = sales_stall
        self.list = self.sales_stall.content["Requests"]

    def __str__(self) -> str:
        output = f"Your requests: "
        for x, i in enumerate(self.list):
            output += f"{x+1}) {i['Quantity']} {i['Item']} up to {i['Price']}$ for each"
        return output

    def __call__(self) -> None:
        self.__mainloop()

    def __choice(self) -> int:
        os.system('cls')
        print(self, '\n')
        print("1) Make a request")
        print("2) Delete a request")
        print("3) Go back")
        answer = input("> ")
        while (answer not in {'1', '2', '3'}):
            answer = input("> ")
        if (answer == '3'):
            return 2
        return 1 if answer == '1' else 0

    def __delete_request(self) -> None:
        os.system('cls')
        print(self, '\n')
        print("Which request do you want to delete?")
        answer = input("> ")
        while (True):
            while (not answer or answer.isspace()):
                answer = input("> ")
            try:
                choice = int(choice)-1 # choice is now the index of the request to delete
            except ValueError:
                continue
            if (choice <= len(self.list) and choice >= 0):
                break
        self.list.pop(choice)
        print("Request deleted")
        input("> ")
        # Don't need to encode it since it's already been encoded by the market

    def __make_request(self) -> None:
        os.system('cls')
        print("What do you want to offer? (Use plural where possible)")
        item = input("> ")
        while (item.capitalize() not in Constants.elements):
            item = input("> ")
        print(f"How many {item} do you want to offer?")
        while (True):
            try:
                quantity = int(input("> "))
                if (quantity <= 0):
                    continue
                break
            except ValueError:
                continue
        print(f"How much would you pay for each {item.lower().removesuffix('s')}?")
        price = input("> ")
        self.list.append({"Item": item, "Quantity": quantity, "Price": price})
        Offer(self.list[-1])()

    def __mainloop(self) -> None:
        while True:
            os.system('cls')
            print(self, '\n')
            if (choice := self.__choice()):
                if (choice == 2):
                    break
                self.__delete_request()
            else:
                self.__make_request()


class Offer: 
    # Quite useless, it's only used to make the code inline when printing the offer
    def __init__(self, dictionary: dict) -> None:
        self.dictionary = dictionary

    def __str__(self) -> str:
        return f"{self.dictionary['Quantity']} {self.dictionary['Item']} for {self.dictionary['Price']}$ each"

    def __call__(self) -> None:
        print(self)


def main(user: str, game: str) -> None:
    asyncio.run(main_(user, game))


async def main_(user: str, game: str) -> None:
    m = Market()
    await m._update()
    MarketForUser(m, user, game)()