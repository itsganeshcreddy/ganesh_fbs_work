# 2. Create a class Distance with data members as km,m and cm and add following methods : 
    # a. Constructor 
    # b. Destructor 
    # c. Overload +,-  operator

class Distance:
    def __init__(self, km, m, cm):
        self.km = km
        self.m = m
        self.cm = cm

    def __del__(self):
        print('Object destroyed...')

    def __add__(self, other):
        km = self.km + other.km
        m = self.m + other.m
        cm = self.cm + other.cm
        return Distance(km, m, cm)

    def __sub__(self, other):
        km = self.km - other.km
        m = self.m - other.m
        cm = self.cm - other.cm
        return Distance(km, m, cm)

    def display(self):
        print(f'{self.km} km {self.m} m {self.cm} cm')

d1 = Distance(2, 500, 40)
d2 = Distance(1, 200, 30)

print('distance 1:')
d1.display()

print('distance 2:')
d2.display()

print('addition:')
d3 = d1 + d2
d3.display()

print('subtraction:')
d4 = d1 - d2
d4.display()

