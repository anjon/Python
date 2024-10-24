# Magic Methods = Dunder methods (double underscore) __init__, __str__, __eq__
#                 They are automatically called by many of python's built in functions
#                 They allow developers to define or customize the behaviour of the objects

class Book:

    def __init__(self, title, author, num_pages):
        self.title = title
        self.author = author 
        self.num_pages = num_pages

    def __str__(self):
        return f"'{self.title}' by {self.author}"

    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self, other):
        return self.num_pages < other.num_pages
    
    def __gt__(self, other):
        return self.num_pages > other.num_pages

    def __add__(self, other):
        return f"{self.num_pages + other.num_pages} pages"

    def __contains__(self, keyword):
        return keyword in self.title or keyword in self.author

    def __getitem__(self, key):
        if key == 'title':
            return self.title
        elif key == 'author':
            return self.author
        elif key == 'num_pages':
            return self.num_pages
        else:
            return f"Key '{key}' was not found"


book1 = Book('The Hobbit', 'J.R.R. Tolkien', 320)
book2 = Book("Harry Potter and the Philosopher's Stone", "J. K. Rowling", 223)
book3 = Book('The Lion, the Witch and the Wardrobe', 'C. S. Lewis', 208)
book4 = Book('The Hobbit', 'J.R.R. Tolkien', 200)

#print(book1 + book4)
#print('Lewis' in book3)
print(book3['audio'])