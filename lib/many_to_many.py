class Author:
    all = []
    def __init__(self,name):
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.author == self]

    def books(self):
        return [contract.book for contract in self.contracts()]

    def sign_contract(self,book,date,royalties):
        return Contract(self,book, date, royalties)

    def total_royalties(self):
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [contract for contract in Contract.all if contract.book == self]

    def authors(self):
        return [contract.author for contract in self.contracts()]
class Contract:
    all = []
    def __init__(self,author,book,date,royalties):
        if isinstance(author,Author):
            if isinstance(book,Book):
                if isinstance(date, str):
                    if isinstance(royalties, (int, float)):
                        self.author = author
                        self.book = book
                        self.date = date
                        self.royalties = royalties
                        Contract.all.append(self)
                    else:
                        raise Exception("Royalties must be a number.")
                else:
                    raise Exception("Date must be a string in 'MM/DD/YYYY' format.")
            else:
                raise Exception("Book must be an instance of Book.")
        else:
            raise Exception("Author must be an instance of Author.")

    @classmethod
    def contracts_by_date(cls,date):
        return [contract for contract in cls.all if contract.date == date]
