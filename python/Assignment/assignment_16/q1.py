# 1. Create a class Book with members as bid,bname,price and author.Add following methods:  
#        a. Constructor (Support both parameterized and parameterless)  
#        b. Destructor   
#        c. ShowBook  
#        d. Add static variable count and also maintain count of objects created.

class Book:
    count = 0

    def __init__(self, bid=101, bname='Secret', price=499, author='Rhonda Byrne'):
        self.bid = bid
        self.bname = bname
        self.price = price
        self.author = author
        Book.count += 1  

    def showBook(self):
        print("Book ID:", self.bid)
        print("Book Name:", self.bname)
        print("Price:", self.price)
        print("Author:", self.author)
        print("---------------------")
    
    def __del__(self):
        print("Destructor called... Object destroyed.")

b1 = Book()
b2 = Book(102, "Shree Tukaram Gatha", 200, "Shree Tukobaray") 
b1.showBook()
b2.showBook()

print("Total Book objects created:", Book.count)


