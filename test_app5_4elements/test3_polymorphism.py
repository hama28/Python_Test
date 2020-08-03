## ポリモーフィズム
# 「同じインターフェイスでありながらデータ型に合わせて異なる動作をする機能」をプログラミングで提供すること
# インターフェイスとは、関数やメソッドのこと

# 例
print("Hello World")
print(200)
print(300.14)

# print 関数は、文字列、整数、浮動小数点数のどれでも同じ使い方で動作する
# print_string、print_int、print_float といったデータ型専用の関数を用意しなくてよい

# 例
print(type("Hello World"))
print(type(200))
print(type(300.14))

# 組み込み関数の type はデータ型を返す


## ダック・タイピング
# 例
# ポリモーフィズムなしでの様々な形状を描画する場合
shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    if isinstance(a_shape, Triangle):
        a_shape.draw_triangle()
    if isinstance(a_shape, Square):
        a_shape.draw_square()
    if isinstance(a_shape, Circle):
        a_shape.draw_circle()

# ポリモーフィズムを実装して描画する場合
shapes = [tr1, sq1, cr1]
for a_shape in shapes:
    a_shape.draw()

# ダック・タイピングでは、あるオブジェクト(obj)が期待する属性(.draw())を持っていて、
# 期待する動作をしてくれるなら、そのオブジェクトが何クラスのインスタンスかは気にしない
# このような、実行してみて期待通りの動作をするならそれで良い、という考え方が
# ダック・タイピングというプログラミングの作法です
# 「それがアヒルのように歩き、アヒルのように鳴くのなら、それはアヒルだ」という比喩から名付けられた
