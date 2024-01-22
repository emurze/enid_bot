import logging

from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By

from handlers.proponent.constants import URL

lg = logging.getLogger(__name__)


def scrap_top_videos(driver: WebDriver, limit: int = 3) -> list[tuple]:
    lg.info('HERE')

    driver.get(URL)

    links_elems = driver.find_elements(
        By.CSS_SELECTOR,
        f'#content ytd-rich-grid-media #dismissible '
        f'#thumbnail ytd-thumbnail #thumbnail',
    )
    titles_elems = driver.find_elements(
        By.CSS_SELECTOR,
        '#content ytd-rich-grid-media #dismissible #details #video-title',
    )

    lg.info('HERE')

    data = [
        (title.text, link.get_attribute('href'))
        for link, title in zip(links_elems[:limit], titles_elems[:limit])
    ]
    return data
