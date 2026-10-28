class Book:
    def __init__(self, title, author, price, copies):
        self.title = title
        self.author = author
        self.price = price
        self.copies = copies

    def calculate_stock_value(self):
        return self.price * self.copies

    def check_stock(self):
        if self.copies > 0:
            return "In Stock"
        else:
            return "Out of Stock"

book1 = Book("Python Basics", "John Simiyu", 1200, 5)
book2 = Book("Database Systems", "Mary Mueni", 2500, 0)

for book in [book1, book2]:
    print(f"Title: {book.title}")
    print(f"Author: {book.author}")
    print(f"Price: {book.price}")
    print(f"Copies Available: {book.copies}")
    print(f"Stock Value: {book.calculate_stock_value()}")
    print(f"Status: {book.check_stock()}")
    print("-" * 30)
