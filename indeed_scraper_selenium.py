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

def get_record(card):
    """Extract job data from single card"""
    job_title = card.find_element_by_class_name('jobtitle').text
    company = card.find_element_by_class_name('company').text
    location = card.find_element_by_class_name('location').text
    post_date = card.find_element_by_class_name('date').text
    extract_date = datetime.today().strftime('%Y-%m-%d')
    summary = card.find_element_by_class_name('summary').text
    job_url = card.find_element_by_class_name('jobtitle').get_attribute('href')
    return job_title, company, location, post_date, extract_date, summary, job_url