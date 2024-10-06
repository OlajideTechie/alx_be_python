class Book:
    def __init__(self, title, author):
        """Initialize a book with a title and an author."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Check out the book, marking it as unavailable."""
        if self._is_checked_out:
            return f'The book "{self.title}" is already checked out.'
        self._is_checked_out = True
        return f'You have checked out "{self.title}".'

    def return_book(self):
        """Return the book, making it available again."""
        if not self._is_checked_out:
            return f'The book "{self.title}" is not checked out.'
        self._is_checked_out = False
        return f'You have returned "{self.title}".'

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []  # Private list to store books

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)
        return f'Book "{book.title}" by {book.author} has been added to the library.'

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return f'The book "{title}" is not available in the library.'

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return f'The book "{title}" is not available in the library.'

    def list_available_books(self):
        """List all available books in the library."""
        available_books = [book.title for book in self._books if book.is_available()]
        if available_books:
            return "Available books: " + ", ".join(available_books)
        return "No available books."


