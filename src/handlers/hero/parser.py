from aiohttp import ClientResponse
from bs4 import BeautifulSoup


def parse_signatures(response: str, parent_dir: str) -> list[str]:
    html = BeautifulSoup(response, 'lxml')
    child_div = ".counter__block__number__value"
    numbers_html = html.select(f"{parent_dir} {child_div}")
    numbers = [num.text for num in numbers_html]
    return numbers


def parse_collected_signatures(response: str):
    return parse_signatures(response, ".counter__block--collected")


def parse_left_signatures(response: str):
    return parse_signatures(response, ".counter__block--left")
