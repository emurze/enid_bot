import pytest
from selenium.webdriver.chrome.webdriver import WebDriver

from helpers.driver import DriverSession

URL = 'https://www.youtube.com/@Max_Katz/videos'


@pytest.fixture
async def driver() -> WebDriver:
    async with DriverSession() as driver:
        return driver
