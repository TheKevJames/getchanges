import logging
from typing import Optional

import aiohttp

from .github import GitHub
from .readthedocs import ReadTheDocs


log = logging.getLogger(__name__)


async def find_clog(url: str, *,
                    session: aiohttp.ClientSession) -> Optional[str]:
    for host in {GitHub, ReadTheDocs}:
        if host.matches(url):
            return await host.find_clog(url, session=session)

    log.warning('could not find changelog given url %s', url)
    return None


def get_url(url: str) -> str:
    for host in {GitHub, ReadTheDocs}:
        if host.matches(url):
            return host.get_url(url)

    return url


__all__ = ['find_clog', 'get_url']
