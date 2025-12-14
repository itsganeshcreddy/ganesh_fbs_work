# 2. Create a class Product with members as pid,pname,price and quantity . Add following methods:  
#          d. Constructor (Support both parameterized and parameterless)  
#          e. Destructor   
#          f. ShowBook 

class Product:
    def __init__(self, pid=111, pname='smartphone', price=25000.00, quantity=2):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def showBook(self):
        data = (f'PRODUCT ID:{self.pid}\nPRODUCT NAME:{self.pname}\nPRICE:{self.price}\nQUANTITY:{self.quantity}')
        return data


p1 = Product()
print(p1.showBook())

print('*******************************************')

p2 = Product(101, 'Mobile', 15000, 3)
print(p2.showBook())
