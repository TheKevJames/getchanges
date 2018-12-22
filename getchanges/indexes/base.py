from typing import Set

import aiohttp


class Base:
    hints: Set[str] = set()

    @staticmethod
    async def find_url(name: str, *,
                       session: aiohttp.ClientSession) -> Set[str]:
        raise NotImplementedError
