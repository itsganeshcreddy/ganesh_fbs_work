# 1. Create a class Book with members as bid,bname,price and author.Add following methods:  
#         a. Constructor (Support both parameterized and parameterless)  
#         b. Destructor   
#         c. ShowBook 

class Book:
    def __init__(self, bid=0, bname="Not Given", price=0.0, author="Unknown"):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author

    def __del__(self):
        print("Book object destroyed")

    def showBook(self):
        print("Book ID   :", self.bid)
        print("Book Name :", self.bname)
        print("Price     :", self.price)
        print("Author    :", self.author)

b1 = Book()
b1.showBook()

print('******************************************')

b2 = Book(101, "Python Programming", 499.50, "Guido van Rossum")
b2.showBook()
