class Book:
    all = []
    
    def __init__(self, title):
        self.title = title
        Book.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        if not isinstance(value, str):
            raise Exception("title must be a string")
        self._title = value
    
    def contracts(self):
        """Return a list of contracts related to this book."""
        return [contract for contract in Contract.all if contract.book == self]
    
    def authors(self):
        """Return a list of authors related to this book via contracts."""
        return [contract.author for contract in self.contracts()]

class Author:
    all = []
    
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise Exception("name must be a string")
        self._name = value
    
    def contracts(self):
        """Return a list of contracts related to this author."""
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        """Return a list of books related to this author via contracts."""
        return [contract.book for contract in self.contracts()]
    
    def sign_contract(self, book, date, royalties):
        """Create and return a new Contract for this author and the specified book."""
        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        """Return the sum of royalties from all contracts."""
        return sum(contract.royalties for contract in self.contracts())

class Contract:
    all = []
    
    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        Contract.all.append(self)
    
    @property
    def author(self):
        return self._author
    
    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise Exception("author must be an instance of Author")
        self._author = value
    
    @property
    def book(self):
        return self._book
    
    @book.setter
    def book(self, value):
        if not isinstance(value, Book):
            raise Exception("book must be an instance of Book")
        self._book = value
    
    @property
    def date(self):
        return self._date
    
    @date.setter
    def date(self, value):
        if not isinstance(value, str):
            raise Exception("date must be a string")
        self._date = value
    
    @property
    def royalties(self):
        return self._royalties
    
    @royalties.setter
    def royalties(self, value):
        if not isinstance(value, int):
            raise Exception("royalties must be an integer")
        self._royalties = value
    
    @classmethod
    def contracts_by_date(cls, date):
        """Return all contracts with the specified date."""
        return [contract for contract in cls.all if contract.date == date]