## カプセル化
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

# インスタンス変数 nums は整数のリストを持っている
# nums を変更する方法は2つ
# 1) numsを直接変更する
# 2) change_dateメソッドを使う

data1 = Date()
data1.nums[0] = 100
print(data1.nums)

data2 = Date()
data2.change_date(0, 100)
print(data2.nums)

# どちらの方法でも nums の変更ができる
# しかし、nums をリスト[]からタプル()に変更した場合
# nums[0] = 100 のように直接変更するコードは正しく動作しなくなる

# 多くのプログラミング言語は、
# プライベート変数やプライベートメソッドを定義できるようにして、解決している
# プライベート変数 = オブジェクトの外から参照や操作できない属性
# パブリック変数 = クラス内のデータを直接操作できる

# Pythonにプライベート変数は無い
# 「名前付けの規約」で解決している
# 外から操作してほしくない変数やメソッドには、名前の先頭にアンダースコアを１つ付ける(自己責任で使うことはできる)
# 例
class PublicPrivateExample:
    def __init__(self):
        self.public = "safe"
        self._unsafe = "unsafe"
    def public_method(self):
        pass
    def _unsafe_method(self):
        pass

# self.public を使うのは安全
# self._unsafe を使うべきでない。もし使うなら自己責任で。
