"""
tests.py
Unit tests for Mini Library Management System
Author: [Tanu Jalloh]
Module: PROG211 Object-Oriented Programming 1
"""

from operations import (
    GENRES, books, members,
    add_book, add_member,
    update_book, update_member,
    delete_book, delete_member,
    borrow_book, return_book
)

# Clear all global data before testing
books.clear()
members.clear()

print("===== RUNNING LIBRARY SYSTEM TESTS =====")

# ⿡ Test: Add a book
assert add_book("B001", "Python Basics", "John Doe", "Non-Fiction", 5) == True, "Failed to add valid book"
assert add_book("B001", "Duplicate", "Someone", "Fiction", 3) == False, " Duplicate ISBN should fail"
assert add_book("B002", "Unknown Genre", "John", "Romance", 2) == False, " Invalid genre should fail"
print(" add_book() passed")

# ⿢ Test: Add a member
assert add_member("M001", "Alice", "alice@example.com") == True, " Failed to add member"
assert add_member("M001", "Duplicate", "dup@example.com") == False, "Duplicate member ID should fail"
print(" add_member() passed")

# ⿣ Test: Update book & member
assert update_book("B001", title="Python for Beginners") == True, " Book update failed"
assert update_book("B999", title="Invalid") == False, "Nonexistent book update should fail"
assert update_member("M001", email="alice_new@example.com") == True, " Member update failed"
print(" update_book() & update_member() passed")

# ⿤ Test: Borrow and return
add_book("B003", "Data Science 101", "Jane Doe", "Non-Fiction", 1)
add_member("M002", "Bob", "bob@example.com")

assert borrow_book("B003", "M002") == True, " Borrow should work when available"
assert borrow_book("B003", "M002") == False, " Cannot borrow if no copies left"
assert return_book("B003", "M002") == True, " Return should work"
assert return_book("B003", "M002") == False, " Cannot return a non-borrowed book"
print("borrow_book() & return_book() passed")

# ⿥ Test: Delete operations
assert delete_book("B003") == True, " Should delete returned book"
assert delete_member("M001") == True, " Should delete member with no borrowed books"
print("delete_book() & delete_member() passed")

print("\n ALL TESTS PASSED SUCCESSFULLY")
