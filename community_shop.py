#!/usr/bin/python3
import asyncio
import data
import text


class Market:
    def __init__(self):
        self.data = data.community_shop()
        asyncio.run(self._update())

    def __str__(self) -> str:
        return text.community_shop_string(data.community_shop(), '')
    
    async def _update(self) -> None:
        while (True):
            await asyncio.sleep(1)
            if (self.data != data.community_shop()):
                data.encode_community_shop(self.data)


class MarketForUser:
    def __init__(self, market: Market, user: str, game: str) -> None:
        self.market = market
        self.user = user
        self.game = game

    def __str__(self) -> str:
        return text.community_shop_string(self.market.data, self.game)

    def __call__(self) -> None:
        self.mainloop()

    def __del__(self) -> None:
        ...

    def choice() -> bool:
        print("1) Take me to my market")
        print("2) Take me to the common market")
        answer = input("> ")
        while (answer not in {'1', '2'}):
            answer = input("> ")
        return answer == '2' # 2 => True, 1 => False

    def mainloop(self) -> None:
        if (self.choice()):
            while True:
                print(self, '\n')
                # Do what is needed
        else:
            ...


class SalesStall:
    def __init__(self, market: Market, user: str, game: str):
        self.user = user
        self.game = game
        self.market = market

    def __call__(self) -> None:
        self.mainloop()
    
    def mainloop(self) -> None:
        while True:
            print(self, '\n')
            # Do what is needed


def main(user: str, game: str) -> None:
    m = Market()
    mfu = MarketForUser(m, user, game)
    ss = SalesStall(m, user, game)