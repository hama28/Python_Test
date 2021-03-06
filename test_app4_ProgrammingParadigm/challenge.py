import math


class Apple:
    def __init__(self, w, c, p, o):
        self.weight = w
        self.color = c
        self.price = p
        self.origin = o
        print("Appleオブジェクトを作成したよ！")


ringo1 = Apple(200, "apple red", 100, "青森")
print("産地は" + ringo1.origin + "です。")


class Circle:
    def __init__(self, r):
        self.radius = r
        print("Circleオブジェクトを作成したよ！")

    def area(self):
        return self.radius * self.radius * math.pi


en1 = Circle(12)
print("面積は" + str(en1.area()) + "だよ。")


class Triangle:
    def __init__(self, b, h):
        self.base = b
        self.height = h
        print("Triangleオブジェクトを作成したよ！")

    def area(self):
        return self.base * self.height / 2


sankaku1 = Triangle(6, 4)
print(sankaku1.area())
