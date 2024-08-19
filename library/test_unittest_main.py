#Napasorn Subongkotch 653380133-3 sec1
#Test Unittest
import pytest
from main import User, Book

def test_add_user(db_session):
    # Create a new user instance
    new_user = User(username="test_newuser1", fullname="Test User 1")
    db_session.add(new_user)
    db_session.commit()

    # Query the test_newuser1 to see if it is there
    user = db_session.query(User).filter_by(username="test_newuser1").first()
    assert user is not None
    assert user.username == "test_newuser1"

def test_delete_user(db_session):
    # Add a user, then remove this new user from the db
    user = User(username="test_newuser2", fullname="Test User 2")
    db_session.add(user)
    db_session.commit()

    # Delete the test_newuser2
    db_session.delete(user)
    db_session.commit()

    # Query the test_newuser2 to check if it is removed from the db
    deleted_user = db_session.query(User).filter_by(username="test_newuser2").first()
    assert deleted_user is None

def test_add_book(db_session):
    # Create a new book instance
    new_book = Book(title="Test Book", firstauthor="Test Author", isbn="1234567890")
    db_session.add(new_book)
    db_session.commit()

    # Query the book to see if it is there
    book = db_session.query(Book).filter_by(isbn="1234567890").first()
    assert book is not None
    assert book.title == "Test Book"
    assert book.firstauthor == "Test Author"

def test_delete_book(db_session):
    # Add a book, then remove this new book from the db
    book = Book(title="Test Book", firstauthor="Test Author", isbn="0987654321")
    db_session.add(book)
    db_session.commit()

    # Delete the test book
    db_session.delete(book)
    db_session.commit()

    # Query the book to check if it is removed from the db
    deleted_book = db_session.query(Book).filter_by(isbn="0987654321").first()
    assert deleted_book is None

