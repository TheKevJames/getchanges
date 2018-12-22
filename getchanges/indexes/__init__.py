from typing import Set
from typing import Type

from .base import Base
from .pypi import PyPI


def get() -> Set[Type[Base]]:
    return {PyPI}


__all__ = ['get']
