import abc
import os

from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver

from helpers.tasks import sync_to_async


class BaseDriverFactory(abc.ABC):
    @abc.abstractmethod
    def get_webdriver(self) -> WebDriver:
        ...


class ChromeDriverFactory(BaseDriverFactory):
    host = os.getenv("STAGING_SERVER", "chrome")
    port = "4444"

    @classmethod
    def get_webdriver(cls) -> WebDriver:
        options = webdriver.ChromeOptions()
        return webdriver.Remote(
            f"http://{cls.host}:{cls.port}",
            options=options,
        )


def get_driver() -> WebDriver:
    return ChromeDriverFactory.get_webdriver()



class DriverSession:
    async def __aenter__(self) -> WebDriver:
        self.driver = await sync_to_async(get_driver)
        return self.driver

    async def __aexit__(self, *_) -> None:
        self.driver.quit()
