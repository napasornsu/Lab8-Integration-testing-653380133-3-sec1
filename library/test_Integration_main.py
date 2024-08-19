#Napasorn Subongkotch 653380133-3 sec1
#Test Integration test

import pytest
from main import User, Book, Borrowlist

def test_create_borrowlist(db_session):
    # Create a new user and book
    user = User(username="test_borrower", fullname="Test Borrower")
    book = Book(title="Test Book", firstauthor="Test Author", isbn="1234567890")
    
    db_session.add(user)
    db_session.add(book)
    db_session.commit()

    # Create a borrow list entry
    borrow_entry = Borrowlist(user_id=user.id, book_id=book.id)
    db_session.add(borrow_entry)
    db_session.commit()

    # Query the borrow list to see if it was created
    borrow_entry_query = db_session.query(Borrowlist).filter_by(user_id=user.id, book_id=book.id).first()
    assert borrow_entry_query is not None
    assert borrow_entry_query.user_id == user.id
    assert borrow_entry_query.book_id == book.id

def test_get_borrowlist(db_session):
    # Create a new user and book
    user = User(username="test_borrower2", fullname="Test Borrower 2")
    book = Book(title="Test Book 2", firstauthor="Test Author 2", isbn="0987654321")
    
    db_session.add(user)
    db_session.add(book)
    db_session.commit()

    # Create a borrow list entry
    borrow_entry = Borrowlist(user_id=user.id, book_id=book.id)
    db_session.add(borrow_entry)
    db_session.commit()

    # Query the borrow list for the user
    borrow_entries = db_session.query(Borrowlist).filter_by(user_id=user.id).all()
    assert len(borrow_entries) == 1
    assert borrow_entries[0].user_id == user.id
    assert borrow_entries[0].book_id == book.id
