import typing

import aiohttp


class Base:
    hints: typing.Set[str] = set()
    _filenames = {'changelog', 'changes', 'history'}
    _folders = {'change', 'doc'}

    @classmethod
    def matches(cls, url: str) -> bool:
        return any(h in url for h in cls.hints)

    @staticmethod
    async def find_clog(url: str, *, session: aiohttp.ClientSession) -> str:
        raise NotImplementedError

    @staticmethod
    def get_url(url: str) -> str:
        return url
