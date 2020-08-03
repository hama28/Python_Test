## 特殊メソッド
# すべてのクラスは、object クラスを継承している
# なので、object クラスから継承したメソッドを使える

# 例 __repr__
class Lion:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return self.name

lion = Lion("Simba")
print(lion)

# 通常は、<__main__.Lion object at 0x1011654> のような文字列の出力になるが、
# __repr__メソッドをオーバーライドしたことで、name が出力されるようになった


# 例 __add__
class AlwaysPositive:
    def __init__(self,number):
        self.n = number
    def __add__(self,other):
        return abs(self.n + other.n)

x = AlwaysPositive(-30)
y = AlwaysPositive(15)
print(x + y)

# 通常は、オブジェクト同士の足し算はできない
# __add__メソッドをオーバーライドすることで、計算できるようにしている
# 例の__add__メソッドでは、2つの数値を足して、その結果を組み込み関数 abs に渡して絶対値に変換している
# なので、式の評価結果は必ず正の値になる