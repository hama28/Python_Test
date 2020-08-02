# カプセル化
# 2つの概念
# 1) オブジェクトによって複数の変数とメソッドをまとめること
# 2) データをクラス内に隠蔽して外から見えないようにすること

# 例1
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l

    def area(self):
        return self.width * self.len

# 例2


class Date:
    def __init__(self):
        self.nums = [1, 2, 3, 4, 5]

    def change_date(self, index, n):
        self.nums[index] = n
