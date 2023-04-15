class MyComplex:
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def mul(self, second):
        real = self.real * second.real - self.imaginary * second.imaginary
        imaginary = self.real * second.imaginary + self.imaginary * second.real
        print(real, "+", imaginary, "i") 
    
a = MyComplex(3, -4)
b = MyComplex(-5, 2)
a.mul(b)

print((3 * 5) - (-4 * 2))