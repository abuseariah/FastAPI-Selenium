import requests as rq
import bs4 as bs4
from typing import List


def generate_url(month: str, day: int) -> str:
    url = f"https://www.onthisday.com/day/{month}/{day}"
    return url


def get_page(url: str) -> bs4.BeautifulSoup:
    page = rq.get(url)
    soup = bs4.BeautifulSoup(page.content, "html.parser")
    return soup


def events_of_the_day(mouth: str, day: int) -> List[str]:
    url = generate_url(mouth, day)
    page = get_page(url)
    raw_events = page.findAll(class_="event")
    events=[event.text for event in raw_events]
    return events

