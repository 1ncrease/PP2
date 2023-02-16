class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, L):
        Shape.__init__(self)
        self.lenght = L
    def area(self):
        print(int(self.lenght) * int(self.lenght))

Square = Square(int(input()))
Square.area()