from typing import Optional
from typing import Set

import aiohttp


class Base:
    hints: Set[str] = set()
    _filenames = {'changelog', 'changes', 'history', 'release'}
    _folders = {'change', 'doc', 'release'}

    @classmethod
    def matches(cls, url: str) -> bool:
        return any(h in url for h in cls.hints)

    @staticmethod
    async def find_clog(url: str, *,
                        session: aiohttp.ClientSession) -> Optional[str]:
        raise NotImplementedError

    @staticmethod
    def get_url(url: str) -> str:
        return url
