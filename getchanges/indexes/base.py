from typing import Set

import aiohttp


class Base:
    hints: Set[str] = set()

    @staticmethod
    async def find_url(name: str, *, session: aiohttp.ClientSession,
                       verbose: bool = False) -> Set[str]:
        raise NotImplementedError
