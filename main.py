from abc import ABC, abstractmethod

# Base class Encapsulation and Abstraction
class Book:
    def __init__(self, title, author, isbn, dailyLateFee):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__dailyLateFee = dailyLateFee

    def get_title(self):
        return self.__title

    def calculateLateFee(self, daysLate):
        return daysLate * self.__dailyLateFee
        
# Inheritance and Polymorphism
class EBook(Book):
    def calculateLateFee(self, daysLate):
        return daysLate * 0.5 * 1

class PrintedBook(Book):
    def calculateLateFee(self, daysLate):
        return daysLate * 2
        
# Interface Segregation and Dependency Inversion
class PaymentMethod(ABC):
    @abstractmethod
    def processPayment(self, amount):
        pass

class CashPayment(PaymentMethod):
    def processPayment(self, amount):
        print(f"Paid Rs.{amount} in cash.")

class CardPayment(PaymentMethod):
    def processPayment(self, amount):
        print(f"Paid Rs.{amount} by card.")
        
# Library class Single Responsibility and Dependency Injection
class Library:
    def __init__(self, payment_method: PaymentMethod):
        self.books = []
        self.payment_method = payment_method

    def addBook(self, book: Book):
        self.books.append(book)

    def issueBook(self, book_title, daysLate):
        for book in self.books:
            if book.get_title() == book_title:
                fee = book.calculateLateFee(daysLate)
                print(f"{book_title} returned late. Late fee: Rs.{fee}")
                self.payment_method.processPayment(fee)
                return
        print("Book not found.")
        
if _name_ == "_main_":
    payment = CardPayment()
    library = Library(payment)

    ebook = EBook("Python Basics", "John Doe", "E001", 5)
    printed = PrintedBook("Advanced OOP", "Jane Smith", "P002", 5)
    library.addBook(ebook)
    library.addBook(printed)

    library.issueBook("Python Basics", 3)
    library.issueBook("Advanced OOP", 3)
