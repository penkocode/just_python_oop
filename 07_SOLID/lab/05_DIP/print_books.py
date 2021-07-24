# Dependency Inversion - SOLI*D

from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class BaseFormatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class MobileFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:20]


class DesktopFormatter(BaseFormatter):
    def format(self, book: Book) -> str:
        return book.content[:100]


class Printer:
    def get_book(self, book: Book, formatter: BaseFormatter):
        print("Print....")
        return formatter.format(book)


printer = Printer()
book = Book('Hello there,this is only a test of the Dependency Inversion')
formatter_for_mobile = MobileFormatter()
formatter_for_desktop = DesktopFormatter()
print(printer.get_book(book, formatter_for_mobile))
print(printer.get_book(book, formatter_for_desktop))
