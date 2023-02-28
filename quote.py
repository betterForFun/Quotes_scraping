from locators.quote_locators import quoteLocator

class quoteParser:
    def __init__(self, parent):
        self.parent = parent
        self.check = 0

    def __repr__(self):
        return f'{self.content()} by {self.author()}'

    def content(self):
        locator = quoteLocator.CONTENT
        return self.parent.select_one(locator).string

    def author(self):
        locator = quoteLocator.AUTHOR
        return self.parent.select_one(locator).string

    def tags(self):
        locator = quoteLocator.TAGS
        return [x.string for x in self.parent.select_one(locator)]
