#Library Management System

A simple Library Management System built using Python, demonstrating Object-Oriented Programming (OOP) and SOLID principles. It also uses GitHub version control and a CI/CD pipeline (GitHub Actions) to reflect DevSecOps practices.

#Project Overview

This project simulates a small library environment where users can borrow books, return them, and calculate late fees. It applies key OOP and SOLID design concepts to create clean, modular, and maintainable code.

#Learning Objectives

-Implement OOP principles (Encapsulation, Inheritance, Polymorphism, Abstraction)

-Apply SOLID design principles for better software architecture

-Use GitHub for version control and project management

-Set up CI/CD pipeline with GitHub Actions for automated testing

#Project Structure

LibraryManagementSystem/
│
├── main.py                # Main program file
├── test_library.py        # Automated unit tests
├── python-app.yml         # CI/CD workflow
└── README.md              # Project documentation

#How to Run the Program

Clone the Repository

git clone https://github.com/Ayusha1216/LibraryManagementSystem.git

cd LibraryManagementSystem

Run the Application
python main.py

Run Automated Tests
pytest

#OOP Concepts Used

Concept	Implementation

Encapsulation	Book details are private (__title, __author).

Inheritance	EBook and PrintedBook inherit from Book.

Polymorphism	Subclasses override calculateLateFee().

Abstraction	User interacts with simple methods, not internal logic.

#SOLID Principles Demonstrated

Principle	Explanation

S - Single Responsibility	Each class has one responsibility (Book, Library, Payment).

O - Open/Closed	New payment methods can be added without changing existing code.

L - Liskov Substitution	Subclasses replace base classes without breaking behavior.

I - Interface Segregation	Payment interface defines only necessary methods.

D - Dependency Inversion	Library depends on abstract PaymentMethod, not concrete classes.

#DevSecOps and CI/CD Integration

The GitHub Actions workflow runs automated tests whenever code is pushed or merged.
This supports the “shift-left” approach by testing early in the development cycle.

#Workflow Tasks:

-Checkout repository

-Set up Python environment

-Install dependencies

-Run automated tests

#Version Control Practice

Sample commit messages used in GitHub:

git commit -m "Added Book class – Demonstrated Encapsulation and Abstraction"

git commit -m "Implemented Inheritance and Polymorphism – Added EBook and PrintedBook classes"

git commit -m "Applied SOLID Principles – Added PaymentMethod interface with CashPayment and CardPayment classes"

git commit -m "Completed main program – Added example run and tested book issuance"

#Conclusion

This project demonstrates how OOP and SOLID principles, combined with DevSecOps practices, create secure, maintainable, and scalable software. It provides a clear understanding of modern software engineering concepts and automation.

#Developed by:

Ayusha Gurung

Advanced Programming – Practical Assignment

Submission Deadline: 19th October 2025
