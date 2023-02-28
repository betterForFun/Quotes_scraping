import re
from bs4 import BeautifulSoup
import requests
from pages.quote_page import quotePage

page_content = requests.get('http://quotes.toscrape.com').content
page = quotePage(page_content)

for x in page.quotes():
    print(x)

