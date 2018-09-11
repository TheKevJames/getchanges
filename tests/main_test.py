import aiohttp
import pytest

import getchanges


@pytest.mark.asyncio
async def test_alabaster():
    # PyPI info -> RtD:/ -> ./changelog.html
    async with aiohttp.ClientSession() as s:
        clog = await getchanges.retrieve('alabaster', source='pypi', session=s)

    assert clog


@pytest.mark.skip(reason='TODO: fallback to searching description')
@pytest.mark.asyncio
async def test_appenlight_client():
    # PyPI description -> GitHub:/ -> ./CHANGELOG
    async with aiohttp.ClientSession() as s:
        clog = await getchanges.retrieve('appenlight-client', source='pypi',
                                         session=s)

    assert clog


@pytest.mark.skip(reason='TODO: bitbucket support')
@pytest.mark.asyncio
async def test_alemic():
    # PyPI info -> BitBucket:/ -> (./changes) -> ./docs/changelog.rst
    async with aiohttp.ClientSession() as s:
        clog = await getchanges.retrieve('alembic', source='pypi', session=s)

    assert clog


@pytest.mark.skip(reason='TODO: ./docs/{source,src,build} support')
@pytest.mark.asyncio
async def test_boto():
    # PyPI info -> GitHub:/ -> ./docs/source/changelog.rst
    async with aiohttp.ClientSession() as s:
        clog = await getchanges.retrieve('boto', source='pypi', session=s)

    assert clog


@pytest.mark.asyncio
async def test_coveralls():
    # PyPI project_urls -> GitHub:/CHANGELOG.md
    async with aiohttp.ClientSession() as s:
        clog = await getchanges.retrieve('coveralls', source='pypi', session=s)

    assert clog


@pytest.mark.skip(reason='TODO: grab index in docs folder')
@pytest.mark.asyncio
async def test_django():
    # PyPI info -> GitHub:/ -> ./docs/releases/index.rst
    async with aiohttp.ClientSession() as s:
        clog = await getchanges.retrieve('django', source='pypi', session=s)

    assert clog


@pytest.mark.skip(reason='TODO: GitLab support')
@pytest.mark.asyncio
async def test_flake8():
    # PyPI info -> GitLab:/ -> ./docs/source/release-notes/index.rst
    async with aiohttp.ClientSession() as s:
        clog = await getchanges.retrieve('flake8', source='pypi', session=s)

    assert clog


@pytest.mark.asyncio
async def test_gcloud_rest():
    # PyPI info -> GitHub:/ -> GitHub Releases
    async with aiohttp.ClientSession() as s:
        clog = await getchanges.retrieve('gcloud-rest', source='pypi',
                                         session=s)

    assert clog


@pytest.mark.skip(reason='TODO: determine best changelog')
@pytest.mark.asyncio
async def test_gitpython():
    # PyPI description -> GitHub:/ -> ./CHANGES vs ./docs/source/changes.rst
    async with aiohttp.ClientSession() as s:
        clog = await getchanges.retrieve('gitpython', source='pypi', session=s)

    assert clog.raw.count('\n') > 5


@pytest.mark.asyncio
async def test_hypothesis():
    # PyPI info -> GitHub:/hypothesis-python -> ./docs/CHANGELOG.rst
    async with aiohttp.ClientSession() as s:
        clog = await getchanges.retrieve('hypothesis', source='pypi',
                                         session=s)

    assert clog


@pytest.mark.skip(reason='TODO: git commit log support')
@pytest.mark.asyncio
async def test_mccabe():
    # PyPI info -> GitHub:/
    async with aiohttp.ClientSession() as s:
        clog = await getchanges.retrieve('mccabe', source='pypi', session=s)

    assert clog


@pytest.mark.asyncio
async def test_pytest():
    # PyPI info -> GitHub:/ -> ./CHANGELOG.rst
    async with aiohttp.ClientSession() as s:
        clog = await getchanges.retrieve('pytest', source='pypi', session=s)

    assert clog
