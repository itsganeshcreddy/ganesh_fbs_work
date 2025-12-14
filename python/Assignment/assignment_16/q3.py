# 3. Create a class Shirt  with members as sid,sname,type(formal etc), price and size(small,large etc).Add following methods:  
#        j. Constructor (Support both parameterized and parameterless)  
#        k. Destructor   
#        l. ShowBook  
#        m. For each size of shirt price should change by 10%. 
#           (eg. If 1000 is price then small price=1000, medium=1100,large=1200 and xlarge=1300) Use static concept.

class Shirt:
    # static dictionary for size-based price increase
    size_price = {
        "small": 0,
        "medium": 10,
        "large": 20,
        "xlarge": 30
    }

    def __init__(self, sid=1, sname="Unknown", type="Formal", price=1000, size="small"):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

        # apply size-based price change
        self.applySizePrice()

    def applySizePrice(self):
        """Increase price based on size percentage."""
        percent = Shirt.size_price.get(self.size.lower(), 0)
        increase = (percent / 100) * self.price
        self.price = self.price + increase

    def showShirt(self):
        print("Shirt ID:", self.sid)
        print("Shirt Name:", self.sname)
        print("Type:", self.type)
        print("Size:", self.size)
        print("Price:", self.price)
        print("---------------------")

    def __del__(self):
        print("Destructor called... Object destroyed.")

s1 = Shirt()  
s2 = Shirt(102, "Peter England", "Casual", 1200, "large")

s1.showShirt()
s2.showShirt()
