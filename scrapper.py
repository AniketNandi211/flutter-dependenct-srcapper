from bs4 import BeautifulSoup
import requests


def parseLink(url: str) -> BeautifulSoup:
    print(f"making request to {url}")
    response = requests.get(url)
    return BeautifulSoup(response.text, features="html.parser")


def findElement(element: BeautifulSoup, selector: str):
    return element.select(selector)[0]


def findElements(element: BeautifulSoup, selector: str):
    return element.select(selector)
