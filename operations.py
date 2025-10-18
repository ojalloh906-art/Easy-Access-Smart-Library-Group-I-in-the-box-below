"""
operations.py
Mini Library Management System
Author: [Tanu Jalloh]
Module: PROG211 Object-Oriented Programming 1
Note: Uses only functions, lists, dictionaries, and tuples (no OOP).
"""

# ----------------------------
# Global Data Structures
# ----------------------------

# Tuple of valid genres (immutable)
GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Mystery", "Biography")

# Dictionary to store books using ISBN as the key
# Example: {"123456": {"title": "Python Basics", "author": "John Doe", "genre": "Non-Fiction", "total_copies": 5}}
books = {}

# List of dictionaries to store library members
# Example: [{"member_id": "M001", "name": "Alice", "email": "alice@example.com", "borrowed_books": []}]
members = []


# ----------------------------
# Helper Functions
# ----------------------------

def find_member(member_id):
    """Return a member dictionary if member_id exists, else None."""
    for m in members:
        if m["member_id"] == member_id:
            return m
    return None


# ----------------------------
# CREATE OPERATIONS
# ----------------------------

def add_book(isbn, title, author, genre, total_copies):
    """
    Add a new book if ISBN is unique and genre is valid.
    Returns True if successful, False otherwise.
    """
    if isbn in books or genre not in GENRES:
        return False
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies
    }
    return True


def add_member(member_id, name, email):
    """
    Add a new member if member_id is unique.
    Returns True if successful, False otherwise.
    """
    if find_member(member_id):
        return False
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return True


# ----------------------------
# READ OPERATIONS
# ----------------------------

def search_books(query, by="title"):
    """
    Search for books by title or author (case-insensitive).
    Returns a list of matching book dictionaries.
    """
    query = query.lower()
    results = []
    for isbn, book in books.items():
        if by == "author":
            if query in book["author"].lower():
                results.append({isbn: book})
        else:
            if query in book["title"].lower():
                results.append({isbn: book})
    return results


# ----------------------------
# UPDATE OPERATIONS
# ----------------------------

def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    """
    Update book fields if ISBN exists and new genre (if any) is valid.
    Returns True if successful, False otherwise.
    """
    if isbn not in books:
        return False
    if genre and genre not in GENRES:
        return False

    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if genre:
        books[isbn]["genre"] = genre
    if total_copies is not None:
        books[isbn]["total_copies"] = total_copies
    return True


def update_member(member_id, name=None, email=None):
    """
    Update member name and/or email.
    Returns True if successful, False otherwise.
    """
    member = find_member(member_id)
    if not member:
        return False
    if name:
        member["name"] = name
    if email:
        member["email"] = email
    return True



# DELETE OPERATIONS


def delete_book(isbn):
    """
    Delete a book if it exists and no copies are borrowed.
    Returns True if successful, False otherwise.
    """
    if isbn not in books:
        return False

    borrowed_count = 0
    for m in members:
        if isbn in m["borrowed_books"]:
            borrowed_count += 1
    if borrowed_count > 0:
        return False

    del books[isbn]
    return True


def delete_member(member_id):
    """
    Delete a member if they exist and have no borrowed books.
    Returns True if successful, False otherwise.
    """
    member = find_member(member_id)
    if not member:
        return False
    if member["borrowed_books"]:
        return False

    members.remove(member)
    return True


# ----------------------------
# BORROW / RETURN OPERATIONS
# ----------------------------

def borrow_book(isbn, member_id):
    """
    Borrow a book if it exists, is available, and member has < 3 borrowed books.
    Returns True if successful, False otherwise.
    """
    if isbn not in books:
        return False

    member = find_member(member_id)
    if not member:
        return False

    book = books[isbn]
    if book["total_copies"] <= 0 or len(member["borrowed_books"]) >= 3:
        return False

    # Borrow book
    book["total_copies"] -= 1
    member["borrowed_books"].append(isbn)
    return True


def return_book(isbn, member_id):
    """
    Return a borrowed book.
    Returns True if successful, False otherwise.
    """
    if isbn not in books:
        return False

    member = find_member(member_id)
    if not member or isbn not in member["borrowed_books"]:
        return False


    books[isbn]["total_copies"] += 1
    member["borrowed_books"].remove(isbn)
    return True

