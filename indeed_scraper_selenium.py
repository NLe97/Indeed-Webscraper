import csv
from datetime import datetime
from msedge.selenium_tools import Edge, EdgeOptions
from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException


def get_url(position, location):
    """Generate url from position and location"""
    template = 'https://www.indeed.com/jobs?q={}&l={}'
    position = position.replace(' ', '+')
    location = location.replace(' ', '+')
    url = template.format(position, location)
    return url
