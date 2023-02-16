class Shape():
    def __init__(self):
        pass
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, L, W):
        self.lenght = L
        self.width = W
    def area(self):
        print(int(self.lenght) * int(self.width))

p1 = Rectangle(int(input()), int(input()))
p1.area()