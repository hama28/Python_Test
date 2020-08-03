## コンポジション
# 「has-a関係」を表す
# 例
# 犬とその飼い主の関係
# 「犬は1人の飼い主を持つ」と表現する

class Dog:
    def __init__(self,name,breed,owner):
        self.name = name
        self.breed = breed
        self.owner = owner

class Person:
    def __init__(self,name):
        self.name = name

mick = Person("Mick Jagger")
stan = Dog("Stanley", "Bulldog", mick)
print(stan.owner.name)

# print(stan.owner) を実行すると、Pythonから、オブジェクトだと返ってくる
# print(stan.owner.name) を実行することで、オブジェクト内の要素を出力できる