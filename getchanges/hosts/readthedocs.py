import html.parser
import logging
from typing import List
from typing import Set
from typing import Tuple

import aiohttp
import yarl

from .base import Base


log = logging.getLogger(__name__)


# <li class="toctree-l1">
#   <a class="reference internal" href="path/to/changes.html">Changelog</a>
# </li>
class Parser(html.parser.HTMLParser):
    def __init__(self, filenames: Set[str]) -> None:
        super().__init__()
        self._filenames = filenames
        self.candidates: List[str] = []
        self.in_li = False
        self.last_href: str

    def error(self, message: str) -> None:
        log.error('got parsing error: %s', message)

    def handle_starttag(self, tag: str, attrs: List[Tuple[str, str]]) -> None:
        if tag == 'li' and ('class', 'toctree-l1') in attrs:
            self.in_li = True
            return

        if self.in_li and tag == 'a':
            self.last_href = [v for k, v in attrs if k == 'href'][0]

    def handle_endtag(self, tag: str) -> None:
        if self.in_li and tag == 'li':
            self.in_li = False

    def handle_data(self, data: str) -> None:
        if not self.in_li:
            return

        if any(data.lower().startswith(x) for x in self._filenames):
            self.candidates.append(self.last_href)


class ReadTheDocs(Base):
    hints = {'readthedocs.io', 'rtfd.io'}

    @classmethod
    async def find_clog(cls, url: str, *,
                        session: aiohttp.ClientSession) -> str:
        resp = await session.get(url)
        resp.raise_for_status()
        body = await resp.text()

        parser = Parser(cls._filenames)
        parser.feed(body)

        # TODO: pick best
        base_url = resp.url
        for candidate in parser.candidates:
            return cls.get_url(str(base_url.join(yarl.URL(candidate))))

        raise Exception(f'no candidate found for {url}')

    @staticmethod
    def get_url(url: str) -> str:
        return url\
            .replace('/latest/', '/latest/_sources/')\
            .replace('.html', '.rst.txt')
