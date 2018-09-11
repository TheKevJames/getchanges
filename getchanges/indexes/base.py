import typing

import aiohttp


class Base:
    hints: typing.Set[str] = set()

    @staticmethod
    async def find_url(name: str, *,
                       session: aiohttp.ClientSession) -> typing.Set[str]:
        raise NotImplementedError
