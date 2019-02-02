import asyncio
import logging
import os
from typing import Any
from typing import Dict
from typing import List

import aiohttp

from .base import Base


TOKEN = os.environ.get('GITHUB_TOKEN')

log = logging.getLogger(__name__)


class GitHub(Base):
    hints = {'github.com', 'githubusercontent.com'}

    @staticmethod
    def _headers() -> Dict[str, str]:
        h = {}
        if TOKEN:
            h['Authorization'] = f'token {TOKEN}'
        return h

    @classmethod
    async def _get(cls, owner: str, repo: str, route: str, *,
                   session: aiohttp.ClientSession) -> List[Dict[str, Any]]:
        url = f'https://api.github.com/repos/{owner}/{repo}/{route}'

        resp = await session.get(url, headers=cls._headers())
        if resp.status in {401, 403}:
            log.warning('bad GitHub auth, try setting $GITHUB_TOKEN')

        resp.raise_for_status()
        blob: List[Dict[str, Any]] = await resp.json()
        return blob

    @classmethod
    async def _get_paths(cls, owner: str, repo: str, *, path: str = '',
                         session: aiohttp.ClientSession) -> Dict[str, str]:
        files = await cls._get(owner, repo, f'contents/{path}',
                               session=session)

        futures = []
        for folder in {f['path'] for f in files if f['type'] == 'dir'}:
            if any(folder.replace(path, '').strip('/').startswith(x)
                   for x in cls._folders):
                futures.append(cls._get_paths(owner, repo, path=folder,
                                              session=session))

        filemap = {f['html_url']: f['name'].lower() for f in files
                   if f['type'] == 'file'}
        for fmap in await asyncio.gather(*futures):
            filemap.update(fmap)

        return {url: name for url, name in filemap.items()
                if any(name.startswith(x) for x in cls._filenames)}

    @classmethod
    async def find_clog(cls, url: str, *,
                        session: aiohttp.ClientSession) -> str:
        if '/tree/master/' in url:
            url, path = url.split('/tree/master/')
        else:
            path = ''

        *_, owner, repo = url.strip('/').rsplit('/', 2)
        if repo.endswith('.git'):
            repo = repo[:-4]

        files = await cls._get_paths(owner, repo, path=path, session=session)
        if not files:
            releases = await cls._get(owner, repo, 'releases', session=session)
            if not releases:
                log.error('found no GitHub releases for %s', url)
                return None

            # TODO: there doesn't seem to be a programatic way to get release
            # notes contents...
            html_url: str = releases[0]['html_url']
            return html_url

        # TODO: pick best
        return cls.get_url(list(files)[0])

        # TODO: consider fallback to commit log

    @staticmethod
    def get_url(url: str) -> str:
        return url\
            .replace('github.com', 'raw.githubusercontent.com')\
            .replace('/blob', '')
