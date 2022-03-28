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
        else:
            ...