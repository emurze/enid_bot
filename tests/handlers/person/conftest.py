import pytest

from helpers.web import make_request

URL = "https://nadezhdin2024.ru/"


@pytest.fixture
async def response() -> str:
    return await make_request(URL)
