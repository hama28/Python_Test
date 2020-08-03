# Shapeクラスの定義
class Shape:
    def __init__(self):
        pass
    def what_am_i(self):
        return "I am a shape"

class Rectangle(Shape):
    def __init__(self,w,l):
        self.width = w
        self.len = l
    def calculate_perimeter(self):
        return self.width * self.len

class Square(Shape):
    def __init__(self,w,l):
        self.width = w
        self.len = l
    def calculate_perimeter(self):
        return self.width * self.len
    def change_size(self,w,l):
        self.width = self.width - w
        self.len = self.len - l


rect1 = Rectangle(12,23)
squa1 = Square(21,17)

print(rect1.calculate_perimeter())
print(squa1.calculate_perimeter())

# change_sizeメソッドの追加と定義
squa1.change_size(4,5)
print(squa1.calculate_perimeter())


# Shapeクラスを定義して、Rectangleクラスの親クラスに
rect2 = Rectangle(7,9)
print(rect2.what_am_i())


# コンポジションさせよう
class Horse:
    def __init__(self,n,o,r):
        self.name = n
        self.owner = o
        self.rider = r

class Rider:
    def __init__(self,n):
        self.name = n

hito = Rider("TakeYutaka")
uma = Horse("OguriCap","oguri",hito)
print(uma.rider.name)