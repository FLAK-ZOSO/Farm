#!/usr/bin/python3
import asyncio
import data
import os
import text


class Market:
    def __init__(self) -> None:
        self.data = data.community_shop()
        asyncio.run(self.__update())

    def __str__(self) -> str:
        return text.community_shop_string(data.community_shop(), '')

    def __len__(self) -> int:
        return len(self.data)
    
    async def __update(self) -> None:
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

    def __choice(self) -> bool:
        os.system('cls')
        print(self)
        print("1) Go to offers")
        print("2) Go to requests")
        answer = input("> ")
        while (answer not in {'1', '2'}):
            answer = input("> ")
        return answer == '1' # 1 => True, 2 => False        

    def __mainloop(self) -> None:
        while True:
            os.system()
            print(self, '\n')
            if (self.__choice()):
                Offers(self, self.user, self.game)()


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

    def __choice(self) -> bool:
        os.system('cls')
        print(self)
        print("1) Go to market")
        print("2) Go to requests")
        answer = input("> ")
        while (answer not in {'1', '2'}):
            answer = input("> ")
        return answer == '1' # 1 => True, 2 => False

    def __mainloop(self) -> None:
        while True:
            os.system('cls')
            print(self, '\n')
            if (self.__choice()):
                Requests(self.user, self.game)()


class Requests:
    def __init__(self, user: str, game: str) -> None:
        self.user = user
        self.game = game
        self.content = data.community_shop()[game]["Requests"]


def main(user: str, game: str) -> None:
    m = Market()
    mfu = MarketForUser(m, user, game)
    mfu()