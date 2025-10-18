"""
demo.py
Demonstration script for the Mini Library Management System
Author: [Tanu Jalloh]
Module: PROG211  Object-Oriented Programming 1
"""

from operations import (
    GENRES, books, members,
    add_book, add_member,
    search_books, update_book, update_member,
    delete_book, delete_member,
    borrow_book, return_book
)

def print_state():
    """Display current library state."""
    print("\n===== CURRENT LIBRARY STATE =====")
    print("Books:")
    for isbn, data in books.items():
        print(f"  {isbn}: {data}")
    print("\nMembers:")
    for m in members:
        print(f"  {m}")
    print("=================================\n")


def main():
    print("===== MINI LIBRARY MANAGEMENT SYSTEM DEMO =====\n")

    # 1. Initialize genres
    print(f"Available Genres: {GENRES}\n")

    # 2. Add sample books
    print(">>> Adding books...")
    add_book("B001", "Python Basics", "Tanu Jalloh", "Non-Fiction", 5)
    add_book("B002", "Space Odyssey", "Binta Jalloh", "Sci-Fi", 3)
    add_book("B003", "Mystery of the Nile", "Salamata Jalloh", "Mystery", 4)
    add_book("B004", "The Life of Elon Musk", "huliematu Jalloh", "Biography", 2)
    add_book("B005", "Love in Africa", "Jamie Jalloh", "Fiction", 6)
    print_state()

    # 3. Add sample members
    print(">>> Adding members...")
    add_member("M001", "Amadu Jalloh", "alice@example.com")
    add_member("M002", "Joshua Yiaffa", "bob@example.com")
    add_member("M003", "Ayisha BOckarie", "charlie@example.com")
    print_state()

    # 4. Search books by title
    print(">>> Searching books by title containing 'Python':")
    results = search_books("Python")
    print(results, "\n")

    # 5. Update a book and a member
    print(">>> Updating 'B003' and 'M002'...")
    update_book("B003", title="Mystery of the Nile - Revised", total_copies=5)
    update_member("M002", name="Bob J. Johnson")
    print_state()

    # 6. Borrow books
    print(">>> Borrowing books...")
    borrow_book("B001", "M001")
    borrow_book("B002", "M001")
    borrow_book("B003", "M002")
    borrow_book("B004", "M003")
    print_state()

    # 7. Return a book
    print(">>> Returning book 'B001' for M001...")
    return_book("B001", "M001")
    print_state()

    # 8. Attempt to delete a borrowed book
    print(">>> Trying to delete 'B003' (borrowed by M002)...")
    result = delete_book("B003")
    print("Delete successful?" , result)
    print_state()

    # 9. Return and delete again
    print(">>> Returning 'B003' and deleting...")
    return_book("B003", "M002")
    delete_book("B003")
    print_state()

    # 10. Delete a member with no borrowed books
    print(">>> Deleting member 'M003'...")
    delete_member("M003")
    print_state()

    print("===== DEMO COMPLETE =====")


if __name__ == "__main__":
    main()