from bs4 import BeautifulSoup


def parse_top_videos(text: str, limit: int = 5):
    html = BeautifulSoup(text, 'lxml')
    images = html.select("#primary", limit=limit)

    print(images)
