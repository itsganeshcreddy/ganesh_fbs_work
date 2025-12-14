# 3. Create a class Shirt  with members as sid,sname,type(formal etc), price and size(small,large etc).Add following methods:  
#      g. Constructor (Support both parameterized and parameterless)  
#      h. Destructor  
#      i.ShowBook  

class Shirt:
    def __init__(self, sid=101, sname='T-shirt', type='Casual', price=500, size='Medium'):
        self.sid = sid
        self.sname = sname
        self.type = type
        self.price = price
        self.size = size

    def __del__(self):
        print("Shirt object destroyed")


    def showBook(self):
        data = (f'SHIRT ID:{self.sid}\nSHIRT NAME:{self.sname}\nTYPE:{self.type}\nPRICE:{self.price}\nSIZE:{self.size}')
        return data

s1 = Shirt()
print(s1.showBook())

print('*************************************')

s2 = Shirt(301, 'Cotton Shirt', 'Formal', 1200, 'Large')
print(s2.showBook())
