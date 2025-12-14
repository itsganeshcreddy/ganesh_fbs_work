# 2. Create a class Product with members as pid,pname,price and quantity. Add following methods:  
#        e. Constructor (Support both parameterized and parameterless)  
#        f. Destructor   
#        g. ShowBook  
#        h. Add static member discount.  
#        i. Provide methods for applying discount on price of product.

class Product:
    discount = 10  

    def __init__(self, pid=101, pname='Mobile', price=10000, quantity=1):
        self.pid = pid
        self.pname = pname
        self.price = price
        self.quantity = quantity

    def showProduct(self):
        print("Product ID:", self.pid)
        print("Product Name:", self.pname)
        print("Price:", self.price)
        print("Quantity:", self.quantity)
        print("Discount (%):", Product.discount)
        print("---------------------")

    def applyDiscount(self):
        discount_amount = (Product.discount / 100) * self.price
        self.price = self.price - discount_amount
        print(f"Discount applied. New Price: {self.price}")

    def __del__(self):
        print("Destructor called... Object destroyed.")

p1 = Product()
p2 = Product(102, "Laptop", 50000, 1)
p1.showProduct()
p2.showProduct()

p1.applyDiscount()
p2.applyDiscount()

# show after discount
p1.showProduct()
p2.showProduct()
