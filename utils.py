from sys import version
from bs4 import BeautifulSoup
import pyperclip as p


def debugCheck():
    print(f'Python is running and using version {version}')


def convert_to_html(html_text) -> BeautifulSoup:
    return BeautifulSoup(html_text)


def copy_to_clipboard(text: str, copyMessage='Content has been copied to clipboard') -> None:
    p.copy(text)
    print(copyMessage)


def printHtml(content: BeautifulSoup):
    try:
        print(f'Formatted content\n{content.prettify()}')
    except Exception:
        print(
            f"Please provide a BeutifulSoup type Object: {Exception}")
