## is
# 前後のオブジェクトが同一のオブジェクトなら True
# 同じでないなら False を返す

class Person:
    def __init__(self):
        self.name = 'Bob'

bob = Person()
same_bob = bob
print(bob is same_bob)

another_bob = Person()
print(bob is another_bob)

# bob と another_bob は同じクラスから作成されたが、
# 別のオブジェクトなので False の評価になる


# 変数が None かどうか調べる
x = 10
if x is None:
    print("x はNone ")
else:
    print("x はNoneじゃない")

x = None
if x is None:
    print("x はNone ")
else:
    print("x はNoneじゃない")