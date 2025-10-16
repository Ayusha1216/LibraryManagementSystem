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
