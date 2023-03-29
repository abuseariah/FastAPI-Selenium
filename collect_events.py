from typing import Iterator, Dict
import datetime as dt

from scrapper import events_of_the_day


def date_range(start_date: dt.date, end_date: dt.date) -> Iterator[dt.date]:
    for n in range(int((end_date - start_date).days)):
        yield start_date + dt.timedelta(n)


def create_event_dict() -> Dict:
    events = dict()
    start_date = dt.date(2020, 1, 1)
    end_date = dt.date(2021, 1, 1)

    for date in date_range(start_date, end_date):
        month = date.strftime("%B").lower()
        if month not in events:
            events[month] = dict()
        events[month][date.day] = events_of_the_day(month, date.day)
    return events

def create_event_dict_single_month(month:int) -> Dict:
    events = dict()
    start_date = dt.date(2020, month, 1)
    end_date = dt.date(2020, month+1, 1)

    for date in date_range(start_date, end_date):
        month = date.strftime("%B").lower()
        if month not in events:
            events[month] = dict()
        events[month][date.day] = events_of_the_day(month, date.day)
    return events


def certen_date(date: dt.date) -> Dict:
    events = dict()
    month = date.strftime("%B").lower()
    events[month] = dict()
    events[month][date.day] = events_of_the_day(month, date.day)
    return events
