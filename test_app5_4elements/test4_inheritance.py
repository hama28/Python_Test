## 継承
# 継承元のクラス = 親クラス
# 継承先のクラス = 子クラス

class Shape:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def print_size(self):
        print("{} by {}".format(self.width, self.len))

my_shape = Shape(20,25)
my_shape.print_size()

# 子クラス
class Square(Shape):
    def area(self):
        return self.width * self.len

    def print_size(self):
        print("I am {} by {}".format(self.width,self.len))

a_square = Square(30,15)
a_square.print_size()

# 子クラスにメソッドや変数を定義できる
# それは親クラスに影響を与えない

print(a_square.area())

# 子クラスは親クラスのメソッドを継承している
# 子クラス内で同名のメソッドを定義することで上書きできる
# メソッドオーバーライド と言う

a_square.print_size()

# 親クラスにある print_size メソッドを、子クラスで新しく定義して
# メソッドオーバーライドをしたので、新しいメッセージが出力された