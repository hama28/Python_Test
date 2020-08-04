class Square:
    square_list = []

    def __init__(self,w,l):
        self.width = w
        self.len = l
        self.square_list.append((self.width, self.len))

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.width,self.width,self.width,self.width)

sq1 = Square(5,12)
sq2 = Square(7,18)
sq3 = Square(9,29)

print(Square.square_list)

sq4 = Square(29,1)

print(sq4)

print(Square.square_list)