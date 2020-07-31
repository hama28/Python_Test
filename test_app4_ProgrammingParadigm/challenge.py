class Apple:
    def __init__(self, w, c, p, o):
        self.weight = w
        self.color = c
        self.price = p
        self.origin = o
        print("Appleオブジェクトを作成したよ！")

ringo1 = Apple(200,"apple red",100,"青森")
print("産地は" + ringo1.origin + "です。")


import math

class Circle:
    def __init__(self, r):
        self.radius = r
        print("Circleオブジェクトを作成したよ！")
    def area(self):
        return self.radius * self.radius * math.pi

en1 = Circle(12)
print("面積は" + str(en1.area()) + "だよ。")
