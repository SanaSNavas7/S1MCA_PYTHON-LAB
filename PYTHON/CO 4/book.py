class Publisher:
    def __init__(self, name):
        self.name = name
    
    def display(self):
        print(f"Publisher: {self.name}")

class Book(Publisher):
    def __init__(self, name, title, author):
        super().__init__(name)
        self.title = title
        self.author = author
    
    def display(self):
        print(f"Book title: {self.title}, written by {self.author}")
        super().display()

class Python(Book):
    def __init__(self, name, title, author, price, no_pages):
        super().__init__(name, title, author)
        self.price = price
        self.no_pages = no_pages
    
    def display(self):
        super().display()
        print(f"Price: {self.price}, No. of pages: {self.no_pages}")

# Creating an instance of the Python class
book = Python("Publisher Name", "Python Programming", "Sana", 200, 2000)

# Display the details
book.display()
