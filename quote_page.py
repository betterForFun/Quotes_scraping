from bs4 import BeautifulSoup
from locators.quote_page_locators import quotePageLocator
from parsers.quote import quoteParser

class quotePage:
    def __init__(self, page):
        self.soup = BeautifulSoup(page, 'html.parser')

    def quotes(self):
        locator = quotePageLocator.QUOTE
        quote_tag = self.soup.select(locator)
        return [quoteParser(e) for e in quote_tag]




