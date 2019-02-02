import asyncio
import logging
from typing import Set

import aiohttp

from ..hosts import find_clog
from ..hosts import get_url
from .base import Base


log = logging.getLogger(__name__)


class PyPI(Base):
    hints = {'pip', 'pypi', 'py', 'python'}

    @staticmethod
    async def find_url(name: str, *, session: aiohttp.ClientSession,
                       verbose: bool = False) -> Set[str]:
        candidates: Set[str] = set()
        pypi_url = f'https://pypi.org/pypi/{name}/json'

        try:
            resp = await session.get(pypi_url)
            resp.raise_for_status()
            metadata = await resp.json()

            info = metadata.get('info', {})
            # TODO: metadata.get('releases') ?
            project_urls = info.get('project_urls') or {}

            for k in {'changes', 'Changes', 'changelog', 'Changelog'}:
                if project_urls.get(k):
                    candidates.add(get_url(project_urls[k]))

            repos = {info['home_page']}
            for k in {'code', 'Code', 'source', 'Source', 'repo', 'Repo'}:
                if project_urls.get(k):
                    repos.add(project_urls[k])

            futures = [find_clog(r, session=session) for r in repos]
            candidates.update(set(await asyncio.gather(*futures)))
        except Exception as e:  # pylint: disable=broad-except
            if verbose:
                log.warning('could not find %s on PyPI', name, exc_info=e)

        return candidates
