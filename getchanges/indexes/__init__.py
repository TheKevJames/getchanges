import typing

from .base import Base
from .pypi import PyPI


def get() -> typing.Set[typing.Type[Base]]:
    return {PyPI}


__all__ = ['get']
