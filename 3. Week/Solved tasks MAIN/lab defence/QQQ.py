class Parent1():
    word1 = ""
    def __init__(self, color1, number1):
        self.color1 = color1
        self.number1 = number1
    def INFOparent1(self):
        print("Color 1 - " + self.color1 + " Number 1 - " + self.number1)
    def SETword1(self):
        self.word1 = input()
    def GETword1(self):
        return self.word1
class Parent2():
    word2 = ""
    def __init__(self, color2, number2):
        self.color2 = color2
        self.number2 = number2
    def INFOparent2(self):
        print("Color 2 - " + self.color2 + " Number 2 - " + self.number2)
    def SETword2(self):
        self.word2 = input()
    def GETword2(self):
        return self.word2

class BabyBoy(Parent1, Parent2):
    def __init__(self, color1, number1, color2, number2):
        Parent1.__init__(self, color1, number1,)
        Parent2.__init__(self, color2, number2)
        self.color3 = self.color1 + self.color2
        self.number3 = self.number1 + self.number2
    def INFObaby(self):
        print("Color 3 - " + self.color3 + " Number 3 - " + str(self.number3))
    def PRINTword3(self):
        print("Word3 - " + Parent1.GETword1(self) + Parent2.GETword2(self))


p1 = BabyBoy("Black", 25, "White", 25)
p1.SETword1()
p1.SETword2()
p1.PRINTword3()
p1.INFObaby()