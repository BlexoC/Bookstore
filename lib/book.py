class Book:
    def __init__(self, title: str, page_count):
        self.title = title
        self.page_count = page_count

    @property
    def page_count(self):
        return self._page_count

    @page_count.setter
    def page_count(self, value):
        if not isinstance(value, int):
            print("page_count must be an integer")
        self._page_count = value

    def turn_page(self):
        self.page_count += 1
        print("Flipping the page...wow, you read fast!")