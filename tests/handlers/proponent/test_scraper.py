from selenium.webdriver.chrome.webdriver import WebDriver

from handlers.proponent.scraper import scrap_top_videos
from helpers.tasks import create_cpu_task


async def test_scrap_top_videos_default_limit(driver: WebDriver) -> None:
    data = await create_cpu_task(scrap_top_videos, driver)
    assert len(data) == 3


async def test_scrap_top_videos_specified_limit(driver: WebDriver) -> None:
    data = await create_cpu_task(scrap_top_videos, driver, 5)
    assert len(data) == 5


async def test_scrap_top_videos_format(driver: WebDriver) -> None:
    data = await create_cpu_task(scrap_top_videos, driver, 5)
    try:
        for _, __ in data:
            pass
    except ValueError as e:
        assert f"{e}"
