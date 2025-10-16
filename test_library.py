from main import Book, EBook, PrintedBook

def test_calculateLateFee_book():
    book = Book("Test", "Author", "B001", 5)
    assert book.calculateLateFee(3) == 15

def test_calculateLateFee_ebook():
    ebook = EBook("EBook", "Author", "E001", 5)
    assert ebook.calculateLateFee(3) == 1.5

def test_calculateLateFee_printedbook():
    printed = PrintedBook("PrintedBook", "Author", "P001", 5)
    assert printed.calculateLateFee(3) == 6
