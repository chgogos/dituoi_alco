# Λίστα βιβλίων
books = [
    {"title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925},
    {"title": "1984", "author": "George Orwell", "year": 1949},
    {"title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960},
    {"title": "Pride and Prejudice", "author": "Jane Austen", "year": 1813},
    {"title": "Brave New World", "author": "Aldous Huxley", "year": 1932},
]

# Ταξινόμηση κατά τίτλο (αλφαβητικά)
sorted_by_title = sorted(books, key=lambda book: book["title"])

print("Ταξινόμηση κατά τίτλο:")
for book in sorted_by_title:
    print(book)

# Ταξινόμηση κατά έτος έκδοσης (αύξουσα σειρά)
sorted_by_year = sorted(books, key=lambda book: book["year"])

print("\nΤαξινόμηση κατά έτος έκδοσης:")
for book in sorted_by_year:
    print(book)

# Ταξινόμηση κατά έτος έκδοσης (φθίνουσα σειρά)
sorted_by_year_desc = sorted(books, key=lambda book: book["year"], reverse=True)

print("\nΤαξινόμηση κατά έτος έκδοσης (φθίνουσα σειρά):")
for book in sorted_by_year_desc:
    print(book)
