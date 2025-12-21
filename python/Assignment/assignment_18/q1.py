# 1. Create a class Complex Number with data members as real and imag and add following methods : 
    # a. Constructor 
    # b. Destructor 
    # c. Overload +,-  operator

class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __del__(self):
        print('object destroyed...') 

    def __add__(self, other):
        real = self.real + other.real
        imag = self.imag + other.imag
        return ComplexNumber(real, imag)

    def __sub__(self, other):
        real = self.real - other.real
        imag = self.imag - other.imag
        return ComplexNumber(real, imag) 

    def display(self):
        print(f'{self.real} + {self.imag}i')

c1 = ComplexNumber(4,5)            
c2 = ComplexNumber(2,3)

print('complex num 1:')
c1.display()

print('complex num 2:')
c2.display()        

print('addition:')
c3 = c1 + c2
c3.display()

print('subtraction:')
c4 = c1 - c2
c4.display()