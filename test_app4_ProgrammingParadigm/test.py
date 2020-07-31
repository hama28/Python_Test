## プログラミングパラダイム
# それぞれの大きな違いは、状態(ステート)の持ち方
# 状態(ステート) ＝ 変数の値

## 手続き型プログラミング
# 途中途中で状態(ステート)を変えながら、欲しい答えに近付いていく
# 「まずこれして、次にあれやって」といったかんじ
x = 2
y = 4
z = 8
xyz = x + y + z
print(xyz)

pop = []
jpop = []

def collect_songs():
    song = "曲名を入力してください："
    ask = "p か j のどちらかを入力してください(qで終了)："

    while True:
        genre = input(ask)
        if genre == "q":
            break
        if genre == "p":
            p = input(song)
            pop.append(p)
        elif genre == "j":
            j = input(song)
            jpop.append(j)
        else:
            print("不正な値です。")
    
    print("pop songs: ", pop)
    print("jpop songs: ", jpop)

collect_songs()


## 関数型プログラミング
# 関数外のデータに依存しない
# なので、副作用がない

# 副作用を起こす関数の例
a = 0
def increment():
    global a
    a += 1

# 副作用のない関数の例
def increment(a):
    return a + 1


## オブジェクト指向プログラミング
# オブジェクトに状態(ステート)を持たせる
# クラスを定義し、インスタンス(≒オブジェクト)を作成する
# 個々のインスタンス(≒オブジェクト)は、クラスで定義した属性(特徴)を持つ
# 属性(特徴)の値はインスタンス(≒オブジェクト)によって異なる

# クラスとは
# ヘッダーとスイートを持つ複合文のこと
# 複合文は1つ以上の「節」で構成される
# 「節」は1行のヘッダーと1行以上のスイートで構成される
# 例
# class [クラス名]:     <-- ヘッダー
#    [スイート]         <-- スイート
# クラス名は大文字で始まるキャメルケースで書くのが慣習(例 -> LikeThis)
# スイート部分は、単純文、またはメソッド(複合文)を書く
# メソッドはすべて小文字で、アンダースコアでつなげる

# メソッドとは
# 関数と同じような構文で定義するが、2つ違いがある
# 1) クラスのスイート部分に定義する
# 2) 引数を少なくとも1つ定義する必要がある
#        1つ目の必須な引数には self という名前を使うのが慣習
#           オブジェクトにPythonが自動的に渡してくれる
# self 変数
# インスタンス変数の定義に使う
# インスタンス変数とは、そのオブジェクトに属する変数のこと
# 例
# slef.[変数名] = [値]
# 基本的に、インスタンス変数は __init__ という特別なメソッドの中で定義する
# init = initialize = 初期化
# 二重のアンダースコアで囲まれたメソッドは、特殊メソッドと呼ばれる

# 例
class Orange:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        print("Created!")
# orange オブジェクトを作成すると、__init__が実行され、
# 2つのインスタンス変数、weightとcolorが作成される

# オブジェクトの作り方
# 関数を呼び出すのと同じ構文で作る
# 例
# [クラス名]([引数])

# オブジェクトを作ってみる
mikan1 = Orange(10,"dark orange")
print(mikan1)

# 1) Orangeクラスの定義
# 2) Orange(10,"dark orange")でOrangeクラスをインスタンス化
# 3) Orangeオブジェクトの出力
#        Pythonはそれが Orangeクラスのオブジェクトであることと、
#        コンピュータのメモリー上の位置を表示する

# インスタンス変数の値の取得
# 例
# [オブジェクト名].[インスタンス変数名]
print(mikan1.weight)
print(mikan1.color)

# インスタンス変数の値の変更
# [オブジェクト名].[インスタンス変数名] = [新しい値]
mikan1.weight = 100
mikan1.color = "light orange"
print(mikan1.weight)
print(mikan1.color)

# 複数のオブジェクトの作成
mikan1 = Orange(7,"light orange")
mikan2 = Orange(11,"dark orange")
mikan3 = Orange(13,"yellow")

# 属性の追加
class Apple:
    def __init__(self, w, c):
        self.weight = w
        self.color = c
        self.mold = 0
        print("Appleオブジェクトを作成したよ！")
    # 腐る性質のメソッドを追加
    def rot(self, days, temp):
        self.mold = days * temp

ringo1 = Apple(200,"red")
print(ringo1.mold)
ringo1.rot(10,37)
print(ringo1.mold)

# 例2
class Rectangle:
    def __init__(self, w, l):
        self.width = w
        self.len = l
        print("Rectangleオブジェクトを作成したよ！")
    def area(self):
        return self.width * self.len
    def change_size(self, w ,l):
        self.width = w
        self.len = l

rectangle = Rectangle(10,20)
print(rectangle.area())
rectangle.change_size(15,25)
print(rectangle.area())

# 1) Rectangleクラスの定義
# 2) widthとlenの2つのインスタンス変数がある
# 3) areaメソッドは、2つのインスタンス変数を掛け算して返す
# 4) chage_sizeメソッドは、引数に渡された値を、2つのインスタンス変数に代入して変更する

## オブジェクト指向プログラミングの利点
# コードの再利用が促進され、開発の時間が短縮される
# 解決したい問題を分割して扱うことが推奨されるので、保守しやすいコードになる

## オブジェクト指向プログラミングの欠点
# プログラムを書く前の設計に、より多くの労力をかける必要がある
