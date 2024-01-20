import pytest

from helpers.web import make_text_from_url

URL = "https://nadezhdin2024.ru/"


@pytest.fixture
async def response() -> str:
    return await make_text_from_url(URL)
